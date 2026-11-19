"""Authored RAM verifies reader boundaries, not a commercial game's behavior."""
import importlib.util
from pathlib import Path
import struct

import pytest


SPEC = importlib.util.spec_from_file_location(
    "dune_ui_reader", Path(__file__).resolve().parents[1] / "scripts/experiments/dune_ui_reader.py")
reader = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reader)
BASE = reader.DS * 16
TEXT_SEGMENT, TEXT_TABLE = 0x3000, 0x0040


def put_word(ram, offset, value):
    struct.pack_into("<H", ram, BASE + offset, value)


def put_label(ram, text_id, payload, *, offset=0x0400, phrase=False):
    segment, table = (0x4000, 0x0030) if phrase else (TEXT_SEGMENT, TEXT_TABLE)
    index = (text_id - 1) & 0x07FF if phrase else text_id - 1
    struct.pack_into("<H", ram, segment * 16 + table + index * 2, offset)
    start = segment * 16 + offset
    ram[start:start + len(payload) + 1] = payload + b"\xff"


def authored_ram(*, conversation=False):
    ram = bytearray(reader.RAM_BYTES)
    put_word(ram, 0x2184, 12)
    for index in range(12):
        offset = 0x2186 + index * 14
        if 7 <= index <= 11:
            row = index - 7
            bounds, callback = (92, 159 + row * 8, 228, 167 + row * 8), reader.ROW_CALLBACKS[row]
        else:
            bounds, callback = (index * 8, 10, index * 8 + 6, 16), 0x1000 + index
        struct.pack_into("<4H2B2H", ram, BASE + offset, *bounds, 0x80, 0, 1, callback)
    menu = 0x2608 if conversation else 0x2598
    put_word(ram, 0x2840, 0x2824)
    put_word(ram, 0x2824, menu)
    put_word(ram, menu, 0x00FF)
    for index, text_id in enumerate((1, 2)):
        put_word(ram, menu + 2 + 4 * index, text_id)
        put_word(ram, menu + 4 + 4 * index, 0x1111 + index)
    ram[BASE + 0xFED5] = 0xFF
    ram[BASE + 0xFED8] = 2
    put_word(ram, 0x4303, TEXT_TABLE)
    put_word(ram, 0x4305, TEXT_SEGMENT)
    put_word(ram, 0x4307, 0x0030)
    put_word(ram, 0x4309, 0x4000)
    put_label(ram, 1, b"Authored alpha")
    put_label(ram, 2, b"Authored beta", offset=0x0440)
    put_label(ram, 0x94, b"Authored next page", offset=0x0480)
    put_label(ram, 0x6E, b"Authored speaker", offset=0x04C0)
    return ram


def put_speech(ram, payload, *, box=0x2884):
    put_word(ram, 0x42F5, box)
    ram[BASE + 0xA1F7:BASE + 0xA387] = bytes(reader.TEXT_WINDOW_BYTES)
    start = BASE + 0xA1F7
    ram[start:start + len(payload) + 1] = payload + b"\xff"


def test_reader_preserves_input_and_binds_rows_to_records():
    ram = authored_ram()
    before = bytes(ram)
    result = reader.describe(ram)
    assert bytes(ram) == before
    assert [row["label"]["ascii"] for row in result["menu"]["rows"]] == ["Authored alpha", "Authored beta"]
    assert [row["record_offset"] for row in result["menu"]["rows"]] == [0x21E8, 0x21F6]
    assert result["text_buffer_candidate"]["buffer_status"] == "zero_filled"
    assert "subject_name_candidate" not in result["conversation_witness"]


@pytest.mark.parametrize("ram", [b"", bytes(reader.RAM_BYTES - 1), bytes(reader.RAM_BYTES + 1), "not bytes"])
def test_snapshot_extent_and_type_are_explicit(ram):
    with pytest.raises(reader.SnapshotError, match="640 KiB"):
        reader.describe(ram)


@pytest.mark.parametrize("ds", [-1, 0, 0xFFFF, True])
def test_other_segment_bindings_are_not_silently_reused(ds):
    with pytest.raises(reader.SnapshotError, match="16F3"):
        reader.describe(authored_ram(), ds=ds)


@pytest.mark.parametrize("offset,value", [(0x2184, 0), (0x2184, 65), (0x2840, 0xFFFF),
                                          (0x2824, 0xFFFF), (0x4303, 0xFFFF), (0x4305, 0xA000)])
def test_counts_and_pointer_bounds_fail_closed(offset, value):
    ram = authored_ram()
    put_word(ram, offset, value)
    with pytest.raises(reader.SnapshotError):
        reader.describe(ram)


def test_menu_signed_skip_and_underflow():
    ram = authored_ram()
    ram[BASE + 0x2599] = 8
    ram[BASE + 0x25A2:BASE + 0x25AA] = ram[BASE + 0x259A:BASE + 0x25A2]
    result = reader.describe(ram)
    assert result["menu"]["page_skip"] == 8
    assert result["menu"]["rows"][0]["entry_offset"] == 0x25A2
    put_word(ram, 0x2824, 2)
    ram[BASE + 3] = 0x80
    with pytest.raises(reader.SnapshotError, match="wrap"):
        reader.describe(ram)


@pytest.mark.parametrize("field,value", [(0xFED8, 6), (0xFED5, 5)])
def test_menu_row_limits(field, value):
    ram = authored_ram()
    ram[BASE + field] = value
    with pytest.raises(reader.SnapshotError, match="five-row"):
        reader.describe(ram)


def test_active_geometry_and_row_callback_are_required():
    ram = authored_ram()
    put_word(ram, 0x21E8 + 4, 321)
    with pytest.raises(reader.SnapshotError, match="geometry"):
        reader.describe(ram)
    ram = authored_ram()
    put_word(ram, 0x21E8 + 12, 0x1234)
    with pytest.raises(reader.SnapshotError, match="callback"):
        reader.describe(ram)


@pytest.mark.parametrize("mode,handler", [(0, 0), (1, 0xCE6B), (0x80, 0xCE65), (0x81, 0xCE65)])
def test_paging_row_is_generated_instead_of_reading_a_normal_entry(mode, handler):
    ram = authored_ram()
    ram[BASE + 0xFED5] = 1
    ram[BASE + 0xFED4] = mode
    put_word(ram, 0x259E, 0)  # A normal entry would be invalid here.
    row = reader.describe(ram)["menu"]["rows"][1]
    assert row["source"] == "generated_paging_row"
    assert row["handler"] == handler
    assert row["label"]["ascii"] == "Authored next page"


def test_text_read_cannot_cross_segment_or_scan_past_its_budget():
    ram = authored_ram()
    struct.pack_into("<H", ram, TEXT_SEGMENT * 16 + TEXT_TABLE, 0xFFFE)
    start = TEXT_SEGMENT * 16 + 0xFFFE
    ram[start:start + 3] = b"AA\xff"  # Terminator exists, but in the next segment.
    with pytest.raises(reader.SnapshotError, match="terminator"):
        reader.describe(ram)
    ram = authored_ram()
    start = TEXT_SEGMENT * 16 + 0x0400
    ram[start:start + reader.MAX_LABEL_BYTES + 1] = b"A" * reader.MAX_LABEL_BYTES + b"\xff"
    with pytest.raises(reader.SnapshotError, match="terminator"):
        reader.describe(ram)


def test_labels_escape_controls_and_keep_phrase_expansion_unqualified():
    ram = authored_ram()
    put_label(ram, 1, b"Alpha\rBeta\x01\x80")
    label = reader.describe(ram)["menu"]["rows"][0]["label"]
    assert label["ascii"] == "Alpha\nBeta\\x01\\x80"
    assert label["ascii_only"] is False
    assert label["unexpanded_control_bytes"] == [1, 0x80]
    put_word(ram, 0x259A, 0x0801)
    put_label(ram, 0x0801, b"Authored phrase\xe0", phrase=True)
    label = reader.describe(ram)["menu"]["rows"][0]["label"]
    assert label["table_slot"] == 0x4307
    assert label["lookup_kind"] == "phrase_candidate"
    assert label["ascii"].endswith("\\xe0")


def test_compact_line_remains_candidate_and_disappears_after_box_closes():
    ram = authored_ram(conversation=True)
    put_speech(ram, b"An entirely authored line.")
    result = reader.describe(ram)
    view = reader.compact(result)
    assert view["subject_name_candidate"] == "Authored speaker"
    assert view["dialogue"]["line_candidate"] == "An entirely authored line."
    assert view["dialogue"]["rendered_currentness"] == "unqualified"
    put_word(ram, 0x42F5, 0)
    closed = reader.describe(ram)
    assert closed["text_buffer_candidate"]["ascii_projection"] == "An entirely authored line."
    assert reader.compact(closed)["dialogue"]["line_candidate"] is None
    assert reader.compact(closed)["dialogue"]["status"] == "conversation_box_inactive"
    assert reader.compact(closed)["dialogue"]["other_presentations"] == "map/status presentation unqualified"


def test_compact_withholds_controlled_or_unterminated_text():
    ram = authored_ram()
    put_speech(ram, b"Unexpanded\x81text")
    result = reader.describe(ram)
    assert result["text_buffer_candidate"]["ascii_projection"] == "Unexpanded\\x81text"
    assert reader.compact(result)["dialogue"]["status"] == "unexpanded_controls"
    ram[BASE + 0xA1F7:BASE + 0xA387] = b"A" * reader.TEXT_WINDOW_BYTES
    assert reader.compact(reader.describe(ram))["dialogue"]["status"] == "incomplete_or_empty_buffer"


def test_admission_excludes_highlight_but_retains_guard_and_route_changes():
    ram = authored_ram()
    baseline = reader.describe(ram)["menu_admission_sha256"]
    put_word(ram, 0x259A, 0x8001)
    assert reader.describe(ram)["menu_admission_sha256"] == baseline
    put_word(ram, 0x259A, 0x4001)
    assert reader.describe(ram)["menu_admission_sha256"] != baseline
    ram = authored_ram()
    put_word(ram, 0x2186 + 12, 0x5678)  # A non-row target also invalidates the digest.
    assert reader.describe(ram)["menu_admission_sha256"] != baseline


def test_dialogue_context_invalidates_admission_but_text_has_separate_witness():
    ram = authored_ram(conversation=True)
    put_speech(ram, b"Authored first line")
    before = reader.describe(ram)
    put_speech(ram, b"Authored next line")
    changed_text = reader.describe(ram)
    assert changed_text["menu_admission_sha256"] == before["menu_admission_sha256"]
    assert changed_text["dialogue_witness_sha256"] != before["dialogue_witness_sha256"]
    put_word(ram, 0x4315, 1)
    assert reader.describe(ram)["menu_admission_sha256"] != changed_text["menu_admission_sha256"]
    stable = reader.describe(ram)["dialogue_witness_sha256"]
    ram[BASE + 0xA386] = 7  # Stale tail after the first terminator is irrelevant.
    put_word(ram, 0x42F5, 0x288C)  # Layout alone is not dialogue progress.
    assert reader.describe(ram)["dialogue_witness_sha256"] == stable


def test_opaque_dialogue_fields_do_not_claim_story_semantics():
    ram = authored_ram(conversation=True)
    for offset, value in ((0x4311, 0x1234), (0x4315, 3), (0x42F9, 0x4567),
                          (0x000E, 0x0055), (0x0014, 0x00AA)):
        put_word(ram, offset, value)
    ram[BASE + 0x4319] = 0x80
    witness = reader.describe(ram)["conversation_witness"]
    assert {key: witness[key] for key in ("dialogue_record_4311", "dialogue_selector_4315",
                                        "dialogue_mask_4319", "subject_record_42f9",
                                        "entry_bitset_000e", "entry_bitset_0014")} == {
        "dialogue_record_4311": 0x1234, "dialogue_selector_4315": 3,
        "dialogue_mask_4319": 0x80, "subject_record_42f9": 0x4567,
        "entry_bitset_000e": 0x0055, "entry_bitset_0014": 0x00AA}
    assert "story_complete" not in witness and "input_ready" not in witness


def authored_map():
    ram = authored_ram()
    ram[BASE + 0x4247] = 1
    put_word(ram, 0x0006, 0x0180)
    put_word(ram, 0x114E, 0x0100)
    put_word(ram, 0x4258, 0x011C)
    for pointer, first_id, second_part in ((0x0100, 1, 2), (0x011C, 2, 3)):
        ram[BASE + pointer] = first_id
        ram[BASE + pointer + 1] = second_part
    put_label(ram, 14, b"Authored suffix", offset=0x0500)
    put_label(ram, 15, b"Other suffix", offset=0x0540)
    struct.pack_into("<3H", ram, BASE + 0xA107, 0x0100, 100, 0x0100 | 70)
    struct.pack_into("<3H", ram, BASE + 0xA10D, 0x011C, 120, 0x0100 | 80)
    return ram


def test_map_points_bind_screen_context_and_site_names_without_claiming_arrival():
    ram = authored_map()
    site = reader.describe(ram)["site_witness"]
    assert site["site_location_context"] is True
    assert site["current_record_114e"] == 0x0100
    assert site["selected_record_4258"] == 0x011C
    assert [point["screen_xy"] for point in site["rendered_map_points"]] == [[100, 70], [120, 80]]
    assert [point["site"]["name_candidate"] for point in site["rendered_map_points"]] == [
        "Authored alpha Authored suffix", "Authored beta-Other suffix"]
    assert "arrival" not in site
    ram[BASE + 0x4247] = 0
    assert reader.describe(ram)["site_witness"]["rendered_map_points"] == []


def test_map_points_exclude_other_modes_and_do_not_dereference_direction_selectors():
    ram = authored_map()
    put_word(ram, 0xA10D + 4, 0x0200 | 80)
    put_word(ram, 0x4258, 0xFFF1)
    site = reader.describe(ram)["site_witness"]
    assert len(site["rendered_map_points"]) == 1
    assert site["selected_name_candidate"]["name_candidate"] is None
    assert site["selected_name_candidate"]["qualification"] == "unrecognized_or_direction_pointer"


def test_site_selection_and_map_mode_invalidate_admission():
    ram = authored_map()
    baseline = reader.describe(ram)["menu_admission_sha256"]
    put_word(ram, 0x4258, 0x0100)
    assert reader.describe(ram)["menu_admission_sha256"] != baseline
    ram = authored_map()
    put_word(ram, 0x114E, 0x011C)
    assert reader.describe(ram)["menu_admission_sha256"] != baseline
    ram = authored_map()
    ram[BASE + 0x4247] = 0
    assert reader.describe(ram)["menu_admission_sha256"] != baseline


def test_map_point_list_is_bounded_before_text_buffer():
    ram = authored_map()
    for index in range(reader.MAX_MAP_POINTS):
        struct.pack_into("<3H", ram, BASE + 0xA107 + 6 * index, 0x0100, 100, 0x0100 | 70)
    with pytest.raises(reader.SnapshotError, match="terminator before the text buffer"):
        reader.describe(ram)


@pytest.mark.parametrize("pointer,x,y", [(0x0101, 100, 70), (0x0100, 320, 70), (0x0100, 100, 200)])
def test_invalid_map_point_geometry_or_site_binding_is_refused(pointer, x, y):
    ram = authored_map()
    struct.pack_into("<3H", ram, BASE + 0xA107, pointer, x, 0x0100 | y)
    with pytest.raises(reader.SnapshotError):
        reader.describe(ram)
