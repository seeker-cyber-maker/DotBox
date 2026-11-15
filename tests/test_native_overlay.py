"""Compiled ownership policy and the actual pinned source overlay boundary."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess

import pytest


ROOT = Path(__file__).resolve().parents[1]
NATIVE = ROOT / 'native'


def _applicator():
    spec = importlib.util.spec_from_file_location('dotbox_native_overlay', NATIVE / 'apply_overlay.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ownership_handoffs_reject_stale_input_and_clean_once(tmp_path):
    compiler = shutil.which('c++') or shutil.which('g++')
    if compiler is None:
        pytest.skip('C++ compiler required for ownership policy check')
    source = tmp_path / 'ownership.cpp'
    source.write_text(r'''
#include "dotbox_input_control.h"
#include <cassert>
#include <string>
using dosbox_agent::DotBoxInputControl;
int main() {
    DotBoxInputControl control;
    std::string error;
    int cleanups = 0;
    auto cleanup = [&]() { ++cleanups; };
    assert(!control.State().host && control.State().generation == 0);
    assert(control.CanInject(false, 999, &error)); // legacy agent client
    assert(control.CanInject(true, 0, &error));
    assert(!control.Transfer(true, 0, false, cleanup, &error));
    assert(cleanups == 0 && control.State().generation == 0);
    assert(!control.Transfer(true, 1, true, cleanup, &error));
    assert(cleanups == 0);
    assert(control.Transfer(true, 0, true, cleanup, &error));
    assert(cleanups == 1 && control.State().host && control.State().generation == 1);
    assert(!control.CanInject(false, 0, &error));
    assert(!control.CanInject(true, 1, &error));
    assert(!control.Transfer(false, 0, true, cleanup, &error));
    assert(cleanups == 1 && control.State().host);
    assert(control.Transfer(false, 1, true, cleanup, &error));
    assert(cleanups == 2 && !control.State().host && control.State().generation == 2);
    assert(!control.CanInject(true, 0, &error)); // queued before takeover
    assert(!control.CanInject(true, 1, &error));
    assert(control.CanInject(true, 2, &error));
    assert(control.Transfer(false, 2, true, cleanup, &error));
    assert(cleanups == 3 && control.State().generation == 3);
    control.Reset();
    assert(!control.State().host && control.State().generation == 0);
}
''')
    binary = tmp_path / 'ownership'
    subprocess.run([compiler, '-std=c++11', '-Wall', '-Wextra', '-Werror',
                    '-I', str(NATIVE), str(source), '-o', str(binary)], check=True)
    subprocess.run([str(binary)], check=True)


def test_overlay_manifest_binds_patch_and_shared_policy():
    manifest = json.loads((NATIVE / 'manifest.json').read_text())
    assert manifest['format'] == 'dotbox-native-overlay-1'
    assert hashlib.sha256((NATIVE / 'input-control.patch').read_bytes()).hexdigest() == manifest['overlay_sha256']
    assert hashlib.sha256((NATIVE / 'dotbox_input_control.h').read_bytes()).hexdigest() == manifest['result_files']['include/agent/dotbox_input_control.h']


def test_wrong_source_is_rejected_without_writes(tmp_path):
    before = sorted(tmp_path.rglob('*'))
    with pytest.raises(ValueError, match='does not match pinned base'):
        _applicator().apply_overlay(tmp_path)
    assert sorted(tmp_path.rglob('*')) == before


def test_pinned_overlay_applies_and_repeats_without_mutation(tmp_path):
    prepared = os.environ.get('DOTBOX_DOSBOX_BASE_SOURCE')
    if not prepared:
        pytest.skip('DOTBOX_DOSBOX_BASE_SOURCE required for real source-application check')
    manifest = json.loads((NATIVE / 'manifest.json').read_text())
    for name in manifest['base_files']:
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(Path(prepared) / name, target)
    app = _applicator()
    assert app.apply_overlay(tmp_path, check=True)['status'] == 'compatible'
    assert not (tmp_path / 'include/agent/dotbox_input_control.h').exists()
    assert app.apply_overlay(tmp_path)['status'] == 'applied'
    after = {name: (tmp_path / name).read_bytes() for name in manifest['result_files']}
    assert app.apply_overlay(tmp_path)['status'] == 'already_applied'
    assert after == {name: (tmp_path / name).read_bytes() for name in after}


def _native_project(tmp_path):
    executable = os.environ.get('DOTBOX_DOSBOX_EXECUTABLE')
    if not executable:
        pytest.skip('DOTBOX_DOSBOX_EXECUTABLE required for real native protocol checks')
    Project = pytest.importorskip('fdisbull.project').Project
    program = tmp_path / 'INPUT.COM'
    # Authored fixture: select mode 13h, then loop with interrupts enabled.
    program.write_bytes(bytes.fromhex('b81300cd10ebfe'))
    return executable, Project.create(tmp_path / 'input.fdb', program, image='com')


def test_native_headless_refuses_host_owner_without_mutation(tmp_path):
    executable, project = _native_project(tmp_path)
    with project:
        with project.debugger(executable, tmp_path, version=1) as debug:
            assert debug.rpc.capabilities['input']['cooperative_control'] == 'dotbox-input-control-1'
            initial = debug.call('input.control')
            assert (initial['owner'], initial['generation']) == ('agent', 0)
            with pytest.raises(ValueError, match='visible agent window'):
                debug.call('input.control', {'owner': 'host', 'expected_generation': 0})
            after = debug.call('input.control')
            assert (after['owner'], after['generation']) == ('agent', 0)
            with pytest.raises(ValueError):
                debug.call('input.keyboard.frame_edges', {'edges': [], 'control_generation': 'invalid'})
        assert debug.rpc.process.poll() is not None


def test_native_visible_owner_transfers_reset_and_reject_stale_inputs(tmp_path, monkeypatch):
    executable, project = _native_project(tmp_path)
    monkeypatch.delenv('SDL_VIDEODRIVER', raising=False)
    with project:
        with project.debugger(executable, tmp_path, version=1, window=True) as debug:
            debug.call('input.keyboard.press', {'key': 'a', 'hold_ms': 500, 'control_generation': 0})
            before = debug.call('input.keyboard.state')['keyboard']
            assert before['pending_events'] > 0
            host = debug.call('input.control', {'owner': 'host', 'expected_generation': 0})
            assert (host['owner'], host['generation'], host['input_reset']) == ('host', 1, True)
            keyboard = debug.call('input.keyboard.state')['keyboard']
            assert keyboard['pending_events'] == 0 and keyboard['owned_keys'] == 0
            for params in ({'key': 'a'}, {'key': 'a', 'control_generation': 1}):
                with pytest.raises(ValueError, match='owned by the host'):
                    debug.call('input.keyboard.press', params)
            with pytest.raises(ValueError, match='owned by the host'):
                debug.call('input.mouse.button', {'button': 'left', 'pressed': True, 'control_generation': 1})
            with pytest.raises(ValueError, match='generation changed'):
                debug.call('input.control', {'owner': 'agent', 'expected_generation': 0})
            agent = debug.call('input.control', {'owner': 'agent', 'expected_generation': 1})
            assert (agent['owner'], agent['generation']) == ('agent', 2)
            with pytest.raises(ValueError, match='generation changed'):
                debug.call('input.keyboard.press', {'key': 'a', 'control_generation': 0})
            debug.call('input.keyboard.press', {'key': 'a', 'control_generation': 2})
            # Reconcile queued agent input before closing the fixture.
            reset = debug.call('input.control', {'owner': 'agent', 'expected_generation': 2})
            assert reset['generation'] == 3
            keyboard = debug.call('input.keyboard.state')['keyboard']
            assert keyboard['pending_events'] == 0 and keyboard['owned_keys'] == 0
        assert debug.rpc.process.poll() is not None
