"""Optional full-service acceptance against an actual owned DOSBox-X process."""

import base64
from io import BytesIO
import importlib.util
import os
from pathlib import Path
import threading
import time

import pytest

from dotbox.backend import FDisBullBackend
from dotbox.client import Client
from dotbox.service import PlayService


def test_real_game_survives_clients_and_native_ownership_changes(tmp_path):
    executable = os.environ.get("DOTBOX_DOSBOX_EXECUTABLE")
    if not executable:
        pytest.skip("DOTBOX_DOSBOX_EXECUTABLE required for full native play-service acceptance")
    pytest.importorskip("fdisbull.project")
    Image = pytest.importorskip("PIL.Image")
    source = Path(__file__).resolve().parents[1] / "examples/input_playground.py"
    spec = importlib.util.spec_from_file_location("dotbox_playground_fixture", source)
    fixture = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fixture)
    game_dir = tmp_path / "game"
    game_dir.mkdir()
    program = game_dir / "PLAY.COM"
    program.write_bytes(fixture.program())
    backend_objects, native_processes, failures = [], [], []

    def backend_factory():
        backend = FDisBullBackend({"project": tmp_path / "play.fdb", "program": program,
                                  "game_dir": game_dir, "executable": executable, "image": "com"})
        backend_objects.append(backend)
        native_processes.append(backend._session.rpc.process)
        return backend

    service = PlayService(backend_factory, tmp_path / "session", manual_control=True)
    ready = threading.Event()

    def serve():
        try:
            service.run(on_ready=lambda _: ready.set())
        except BaseException as error:
            failures.append(error)
            ready.set()

    worker = threading.Thread(target=serve)
    worker.start()
    descriptor = tmp_path / "session/session.json"

    def square(client, expected_x):
        deadline = time.monotonic() + 5
        while time.monotonic() < deadline:
            reply = client.request("frame")
            if reply["ok"]:
                image = Image.open(BytesIO(base64.b64decode(reply["result"]["png_base64"]))).convert("RGB")
                pixels = image.load()
                positions = [(x, y) for y in range(image.height) for x in range(image.width)
                             if pixels[x, y][1] > 200 and pixels[x, y][0] < 120 and pixels[x, y][2] < 120]
                if positions:
                    left = min(x for x, _ in positions)
                    top = min(y for _, y in positions)
                    if (left, top) == (expected_x, 100):
                        return reply["session"]
            time.sleep(0.02)
        raise AssertionError("Original game did not reach the expected visible position")

    try:
        assert ready.wait(10) and not failures, failures
        first = Client(descriptor)
        initial = first.request("status")["result"]
        agent = first.request("control", {"owner": "agent", "resume": True}, lease=initial)
        assert agent["ok"] and agent["session"]["state"] == "running"
        square(first, 160)
        assert first.request("key", {"key": "right"}, lease=agent["session"])["ok"]
        square(first, 168)
        another_client = Client(descriptor)
        current = another_client.request("status")["result"]
        assert current["run_id"] == initial["run_id"] and current["instance_id"] == initial["instance_id"]
        human = another_client.request("control", {"owner": "human"}, lease=current)
        assert human["ok"] and human["session"]["state"] == "running"
        assert first.request("key", {"key": "right"}, lease=agent["session"])["error"]["code"] == "stale_generation"
        assert another_client.request("key", {"key": "right"}, lease=human["session"])["error"]["code"] == "human_has_control"
        returned = another_client.request("control", {"owner": "agent"}, lease=human["session"])
        assert returned["ok"]
        assert first.request("key", {"key": "left"}, lease=returned["session"])["ok"]
        last = square(first, 160)
        assert last["run_id"] == initial["run_id"]
        assert another_client.request("close", lease=last)["ok"]
    finally:
        service.request_stop()
        worker.join(10)
    assert not worker.is_alive() and not failures, failures
    assert not descriptor.exists()
    assert native_processes and all(process.poll() is not None for process in native_processes)
