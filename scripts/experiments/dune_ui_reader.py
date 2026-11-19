"""Bounded, read-only UI witnesses for one observed Dune DOS edition.

``describe(ram, ds=DS)`` consumes a coherent frozen 640 KiB conventional-RAM
image starting at linear address zero. It has no emulator, filesystem, network,
input, restore or disassembler dependency, and changes neither RAM nor state.

Entry conditions belong to the caller: verify SOURCE_SHA256/SOURCE_SIZE against
the actual executable and selected resources, CS=0824/DS=16F3 in real-mode,
16-bit, unpaged execution, and capture all bytes at one confirmed stopped
boundary. These bindings came from the supplied English RIP edition. This is
not an edition detector or a portable Dune adapter. A successful parse does not
verify those conditions, input ownership, readiness or rendered consistency.

CA45 selects loaded text through DS:4303/4307. Labels may be read without OCR;
phrase dictionary/control expansion is deliberately not implemented. The
A1F7 buffer and 42F5 box descriptor are candidate dialogue evidence, not proof
of a currently displayed line or a committed story effect. Buffer contents can
survive their presentation. In particular, a newer native frame ID alone does
not prove that captured pixels agree with logical state after a restore.

The admission digest covers only the reported menu/control context, excluding
hover highlighting. It is not a complete game-state token or a live-input grant.
The separate dialogue digest can detect unchanged measured dialogue witnesses;
a change does not establish story progress. ``compact(describe(ram))`` produces
a small inspection packet, with candidate text still explicitly unqualified.
Keep original RAM, decoded commercial text and captures outside the repository;
public tests use authored synthetic bytes only.
"""
from __future__ import annotations

import hashlib
import json
import struct


SOURCE_SHA256 = "32439602abe95e0ff778653ad58052bfed56a73e103b92f079455daa2ee886e7"
SOURCE_SIZE = 74757
CS, DS = 0x0824, 0x16F3
RAM_BYTES, SEGMENT_BYTES = 0xA0000, 0x10000
MAX_CONTROLS, MAX_LABEL_BYTES, TEXT_WINDOW_BYTES = 64, 1024, 400
MAX_MAP_POINTS, MAX_SITE_RECORDS = 40, 128
ROW_CALLBACKS = (0xCE85, 0xCE80, 0xCE7B, 0xCE76, 0xCE71)


class SnapshotError(ValueError):
    """The supplied snapshot does not satisfy the bounded observed schema."""


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _ascii(payload: bytes) -> str:
    """Retain unexpanded controls visibly; do not silently join their text."""
    return "".join("\n" if value == 13 else chr(value) if 32 <= value <= 126
                   else f"\\x{value:02x}" for value in payload)


def _controls_in(payload: bytes) -> list[int]:
    return sorted({value for value in payload if value != 13 and not 32 <= value <= 126})


def describe(ram: bytes, *, ds: int = DS) -> dict:
    """Return bounded observations; raise SnapshotError on unsupported layout.

    ``bytes`` and ``bytearray`` are accepted, with a private immutable copy for
    the latter. The exact RAM extent and observed DS are deliberate scope
    checks. Rebinding another load mapping needs separate qualification.
    """
    if not isinstance(ram, (bytes, bytearray)) or len(ram) != RAM_BYTES:
        raise SnapshotError("Expected exactly 640 KiB of conventional RAM from linear zero")
    if type(ds) is not int or ds != DS:
        raise SnapshotError("The observed data-segment binding must remain 16F3")
    ram = bytes(ram)

    def data(address: int, count: int) -> bytes:
        if count < 0 or not 0 <= address <= RAM_BYTES - count:
            raise SnapshotError(f"Snapshot does not cover {address:05X}+{count}")
        return ram[address:address + count]

    def segmented(segment: int, offset: int, count: int) -> bytes:
        if not 0 <= offset <= SEGMENT_BYTES - count:
            raise SnapshotError("Read would wrap its 16-bit segment")
        return data(segment * 16 + offset, count)

    def byte(offset: int) -> int:
        return segmented(ds, offset, 1)[0]

    def word(offset: int) -> int:
        return struct.unpack("<H", segmented(ds, offset, 2))[0]

    def far(offset: int) -> dict:
        return {"offset": word(offset), "segment": word(offset + 2)}

    def text_lookup(text_id: int) -> dict:
        if not 1 <= text_id <= 0x3FFF:
            raise SnapshotError("Text id is outside the observed metadata range")
        index = text_id - 1
        slot = 0x4307 if index & 0x0800 else 0x4303
        if slot == 0x4307:
            index &= 0x07FF
        table = far(slot)
        table_entry = table["offset"] + index * 2
        pointer = struct.unpack("<H", segmented(table["segment"], table_entry, 2))[0]
        start = table["segment"] * 16 + pointer
        limit = min(MAX_LABEL_BYTES, SEGMENT_BYTES - pointer, RAM_BYTES - start)
        if limit <= 0:
            raise SnapshotError("Text pointer is outside captured conventional RAM")
        block = segmented(table["segment"], pointer, limit)
        terminator = block.find(b"\xff")
        if terminator < 0:
            raise SnapshotError("Text has no FF terminator in the bounded window")
        payload = block[:terminator]
        controls = _controls_in(payload)
        return {"text_id": text_id, "table_slot": slot, "table": table,
                "string_offset": pointer, "ascii": _ascii(payload),
                "ascii_only": not controls, "unexpanded_control_bytes": controls,
                "lookup_kind": "phrase_candidate" if slot == 0x4307 else "normal_label",
                "bytes_sha256": _sha(payload)}

    # D326 dispatches 14-byte control records; CE85..CE71 select command rows.
    count = word(0x2184)
    if not 1 <= count <= MAX_CONTROLS:
        raise SnapshotError("Control table count outside bounded schema")
    controls = []
    for index in range(count):
        offset = 0x2186 + index * 14
        x0, y0, x1, y1, flags0, flags1, value, callback = struct.unpack(
            "<4H2B2H", segmented(ds, offset, 14))
        active = bool(flags0 & 0x80)
        if active and not (0 <= x0 < x1 <= 320 and 0 <= y0 < y1 <= 200):
            raise SnapshotError("Active control has unsupported 320-by-200 geometry")
        controls.append({"record_offset": offset, "bounds": [x0, y0, x1, y1],
                         "flags": [flags0, flags1], "active": active,
                         "value": value, "callback": callback})
    by_offset = {control["record_offset"]: control for control in controls}

    # CE96 resolves menu entries. CECC renders metadata&3FFF; bit4000 rejects
    # the action while bit8000 only changes highlighting.
    stack_slot = word(0x2840)
    menu = word(stack_slot)
    segmented(ds, menu, 2)
    skip = struct.unpack("<b", segmented(ds, menu + 1, 1))[0]
    first = menu + 2 + skip
    special_row, mode = byte(0xFED5), byte(0xFED4)
    count_visible = byte(0xFED8)
    if count_visible > 5:
        raise SnapshotError("Visible row count exceeds the five-row renderer")
    if special_row != 0xFF and special_row >= 5:
        raise SnapshotError("Paging row is outside the five-row renderer")
    segmented(ds, first, 4 * count_visible)
    rows = []
    for index in range(count_visible):
        entry = first + 4 * index
        if index == special_row:
            metadata = 0x0094
            handler = 0xCE65 if mode & 0x80 else 0xCE6B if mode else 0
            source = "generated_paging_row"
        else:
            metadata, handler = word(entry), word(entry + 2)
            source = "menu_record"
        label_id = metadata & 0x3FFF
        if not label_id:
            raise SnapshotError("Visible menu row has no label id")
        record_offset = 0x21E8 + 14 * index
        control = by_offset.get(record_offset)
        if control is None or control["callback"] != ROW_CALLBACKS[index]:
            raise SnapshotError("Expected command rectangle/callback absent")
        rows.append({"row": index, "source": source, "entry_offset": entry,
                     "record_offset": record_offset, "metadata": metadata,
                     "handler": handler, "disabled_by_metadata": bool(metadata & 0x4000),
                     "highlighted": bool(metadata & 0x8000),
                     "active_rectangle": control["active"], "bounds": control["bounds"],
                     "callback": control["callback"], "label": text_lookup(label_id)})

    # 9583 / A7AE assemble text into A1F7 before 96E3 renders it. 9875 clears
    # the active box descriptor, but need not clear the retained text buffer.
    buffer = segmented(ds, 0xA1F7, TEXT_WINDOW_BYTES)
    end = next((i for i, value in enumerate(buffer) if value >= 0xF0), None)
    empty = not any(buffer)
    payload = b"" if empty else buffer if end is None else buffer[:end]
    box_descriptor = word(0x42F5)
    speech = {"buffer_offset": 0xA1F7, "window_bytes": TEXT_WINDOW_BYTES,
              "terminator_offset": end, "terminator": None if end is None else buffer[end],
              "ascii_projection": _ascii(payload),
              "nonprintable_bytes": _controls_in(payload),
              "window_sha256": _sha(buffer),
              "buffer_status": "zero_filled" if empty else "terminated_candidate" if end is not None
                               else "unterminated_candidate",
              "text_box_word_42f5": box_descriptor,
              "remaining_text_pointer": far(0x430D),
              "context": {"box_descriptor": box_descriptor,
                          "box_descriptor_nonzero": box_descriptor != 0,
                          "menu_is_conversation": menu == 0x2608,
                          "rendered_currentness": "unqualified"},
              "freshness": "Candidate buffer; qualify against a current visible line or text-display boundary"}

    # 9E91 writes subject; 9EBD initializes selector=subject*8. 9F3F consumes
    # record/selector/mask on the conversation action. Their story meaning is
    # deliberately opaque, including the two bitsets updated upon entry.
    location = {"word_0004": word(4), "word_0006": word(6)}
    subject = word(0x431B)
    conversation = {
        "menu_is_2608": menu == 0x2608,
        "subject_selector_431b": subject,
        "dialogue_record_4311": word(0x4311),
        "dialogue_selector_4315": word(0x4315),
        "dialogue_mask_4319": byte(0x4319),
        "subject_record_42f9": word(0x42F9),
        "entry_bitset_000e": word(0x000E),
        "entry_bitset_0014": word(0x0014),
    }
    # 9D32 checks2608 as conversation context. Subject0 alone is insufficient:
    # that value also exists outside a conversation in the observed baseline.
    if menu == 0x2608 and subject < 0x17:
        conversation["subject_name_candidate"] = text_lookup(subject + 0x6E)

    def site_name(pointer: int) -> dict | None:
        if pointer == 0:
            return None
        # 6B6E walks 1C-byte site records from0100. A negative 4258 value
        # can instead represent a desert direction; do not dereference it.
        if not (0x0100 <= pointer < 0x0100 + MAX_SITE_RECORDS * 0x1C
                and (pointer - 0x0100) % 0x1C == 0) or word(pointer) == 0xFFFF:
            return {"record_offset": pointer, "name_candidate": None,
                    "qualification": "unrecognized_or_direction_pointer"}
        # 7046 renders the two name components and chooses its separator.
        first_id, second_part = byte(pointer), byte(pointer + 1)
        if first_id == 0:
            return {"record_offset": pointer, "name_candidate": None,
                    "qualification": "unnamed_record"}
        first_name, second_name = text_lookup(first_id), text_lookup(second_part + 0x0C)
        separator = "-" if second_part >= 3 else " "
        return {"record_offset": pointer,
                "name_candidate": first_name["ascii"] + separator + second_name["ascii"],
                "name_ascii_only": first_name["ascii_only"] and second_name["ascii_only"],
                "name_text_ids": [first_id, second_part + 0x0C],
                "type_byte_0008": byte(pointer + 8),
                "world_words": [word(pointer + 2), word(pointer + 4)],
                "qualification": "name_from_loaded_resource; location_and_arrival_require_context"}

    ui_mode = byte(0x4247)
    site = {"current_record_114e": word(0x114E), "selected_record_4258": word(0x4258),
            "site_location_context": (word(6) & 0xFF) == 0x80,
            "map_mode_4247": ui_mode, "map_points_context_active": ui_mode != 0,
            "current_name_candidate": site_name(word(0x114E)),
            "selected_name_candidate": site_name(word(0x4258)),
            "rendered_map_points": [],
            "scope": "Record identities and map selection are not arrival or travel completion"}
    if ui_mode != 0:
        # 6B6E produces six-byte screen entries atA107; 6C0D filters mode and
        # finds the nearest Manhattan point. 4D9F accepts distances below9.
        # A1F7 starts the text buffer, imposing this independent read bound.
        for index in range(MAX_MAP_POINTS):
            offset = 0xA107 + 6 * index
            pointer = word(offset)
            if pointer == 0:
                break
            x, packed = word(offset + 2), word(offset + 4)
            if packed >> 8 != ui_mode:
                continue
            y = packed & 0xFF
            if not (0 <= x < 320 and 0 <= y < 200):
                raise SnapshotError("Map point is outside the observed screen geometry")
            name = site_name(pointer)
            if name is None or name["name_candidate"] is None:
                raise SnapshotError("Map point does not identify a bounded named site record")
            site["rendered_map_points"].append({"entry_offset": offset,
                                                "site_record": pointer, "screen_xy": [x, y],
                                                "mode": packed >> 8, "site": name})
        else:
            raise SnapshotError("Map point table has no terminator before the text buffer")

    result = {"schema": "dune-frozen-ui-witness-1", "data_segment": ds,
              "location_key": location, "subject_selector_431b": subject,
              "ui_mode_4247": ui_mode,
              "menu": {"stack_slot": stack_slot, "menu_offset": menu,
                       "page_skip": skip, "paging_mode": mode, "special_row": special_row,
                       "visible_rows": count_visible, "rows": rows},
              "controls": controls, "text_buffer_candidate": speech,
              "conversation_witness": conversation, "site_witness": site}
    semantic_key = {"location": location, "menu": menu, "menu_stack_slot": stack_slot,
                    "page_skip": skip, "paging_mode": mode, "special_row": special_row,
                    "ui_mode": ui_mode,
                    "site": {key: site[key] for key in
                             ("current_record_114e", "selected_record_4258")},
                    "subject": subject,
                    "rows": [{"label": row["label"]["ascii"], "handler": row["handler"],
                              "disabled": row["disabled_by_metadata"], "active": row["active_rectangle"],
                              "bounds": row["bounds"], "record_offset": row["record_offset"],
                              "callback": row["callback"]} for row in rows],
                    "controls": [{key: control[key] for key in
                                  ("record_offset", "bounds", "active", "value", "callback")}
                                 for control in controls],
                    "map_points": [{key: point[key] for key in ("site_record", "screen_xy", "mode")}
                                   for point in site["rendered_map_points"]]}
    if menu == 0x2608:
        semantic_key["dialogue"] = {key: conversation[key] for key in
                                   ("dialogue_record_4311", "dialogue_selector_4315",
                                    "dialogue_mask_4319", "subject_record_42f9")}
    result["menu_admission_sha256"] = _sha(
        json.dumps(semantic_key, sort_keys=True, separators=(",", ":")).encode())
    # Ignore unused trailing buffer bytes and layout-only descriptor changes.
    # Repeated equal witnesses are useful to bound a continuation macro; the
    # digest is not a claim that different witnesses advanced the story.
    dialogue_key = {"menu": menu, "subject": subject,
                    "fields": {key: conversation[key] for key in
                               ("dialogue_record_4311", "dialogue_selector_4315",
                                "dialogue_mask_4319", "subject_record_42f9")},
                    "box_present": box_descriptor != 0,
                    "remaining_pointer": speech["remaining_text_pointer"],
                    "text_sha256": _sha(payload), "terminator": speech["terminator"]}
    result["dialogue_witness_sha256"] = _sha(
        json.dumps(dialogue_key, sort_keys=True, separators=(",", ":")).encode())
    return result


def compact(observation: dict) -> dict:
    """Project a describe() result for inspection, without narrating as current.

    An inactive conversation box, missing terminator or unexpanded controls
    withhold text from ``line_candidate``. Other map/status renderers can use
    the same buffer without that box; their presentation remains unqualified.
    Even a returned candidate still needs external visible/text-display
    qualification. Dispatch bits are narrower than live
    input readiness, ownership, effect success or a complete action guard.
    """
    speech = observation["text_buffer_candidate"]
    context = speech["context"]
    if not context["box_descriptor_nonzero"]:
        status = "conversation_box_inactive"
    elif speech["terminator"] is None or not speech["ascii_projection"]:
        status = "incomplete_or_empty_buffer"
    elif speech["nonprintable_bytes"]:
        status = "unexpanded_controls"
    else:
        status = "candidate_line"
    name = observation["conversation_witness"].get("subject_name_candidate")
    return {
        "location_key": observation["location_key"],
        "menu_offset": observation["menu"]["menu_offset"],
        "subject_selector": observation["subject_selector_431b"],
        "subject_name_candidate": name["ascii"] if name and name["ascii_only"] else None,
        "choices": [{"row": row["row"], "label": row["label"]["ascii"],
                     "label_ascii_only": row["label"]["ascii_only"],
                     "record_offset": row["record_offset"], "handler": row["handler"],
                     "row_flags_allow_dispatch": row["active_rectangle"]
                     and not row["disabled_by_metadata"] and row["handler"] != 0}
                    for row in observation["menu"]["rows"]],
        "dialogue": {"status": status,
                     "line_candidate": speech["ascii_projection"] if status == "candidate_line" else None,
                     "box_descriptor": context["box_descriptor"],
                     "rendered_currentness": "unqualified",
                     "other_presentations": "map/status presentation unqualified"},
        "sites": observation["site_witness"],
        "menu_admission_sha256": observation["menu_admission_sha256"],
        "dialogue_witness_sha256": observation["dialogue_witness_sha256"],
    }
