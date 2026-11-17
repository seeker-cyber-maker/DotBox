# DotBox development handoff

Updated 17 November 2026. This is a development continuation, not a release or
proof of live desktop input through the ownership fence.

## Start here

- Primary repository: `seeker-cyber-maker/DotBox`.
- Independent mirror: `TiGa-RCE/DotBox`.
- Active upstream implementation: draft PR #2, branch
  `codex/standalone-engine-20261116`, inspected at
  `3e011712c628b86642003e780fbf482e5c913018`.
- Follow-up branch: `codex/async-turn-fence-20261117`, based on that exact commit.
- At inspection, `main` was the design baseline at
  `10fa86d8a91bb75e0ccf3da346bc9f72eab91d03`; it did not contain the implementation.

Read `AGENTS.md`, `docs/PRODUCT.md`, `docs/OWNERSHIP_BRIDGE.md` and
`docs/OWNERSHIP_CONNECTOR.md` before changing the ownership boundary. Follow
`docs/REPOSITORIES.md` for publication. Earlier AGI/walking/HUD experiments stay
in the original developer's private checkout and snapshot; this task did not
inspect or modify those private originals.

## What was already working

The standalone Python package owns its transport, input validation, screenshot
handling, SQLite store and persistent control definitions. It does not require
fDisBull. A prepared native DOSBox-X executable remains a separate dependency.
The normal desktop harness owns keyboard/mouse capture; direct native agent
input is disabled in that mode.

The latest upstream [live connector receipt](
evidence/ownership-connector-live-2026-11-16.json) records read-only original-Dot
observations for Dot control, human takeover and Dot return. Stopped sampling
returns unknown. Its historical 407 source and 180 installed-wheel checks were
run on the previous host and are not results from this continuation.

The connector is status-only: no turn claims/checks/releases, input, frames,
files or shell. A status response never grants input. The receipt reports that
the publisher was stopped and connection processes were left running; their
current live state was not rechecked here.

## This continuation

An additive `Client.run_turn_step_async(lease, action)` fences a fresh Python
coroutine on an executor that already has supported action and coordinator
access. It snapshots one receipt, checks it without blocking the event loop,
awaits the callback, then checks the unchanged receipt. It preserves completed
results on postcheck interruption and propagates cancellation with inspection
guidance. It rejects prestarted and nested deferred work. There is no retry,
renewal, permission change or change to the synchronous helper.

The new regression tests use a real authenticated loopback coordinator and
harmless data callbacks. They do not operate a desktop or launch a game.

## Verification

Fresh baseline on Python 3.12.14: **400 passed, 7 skipped** in 28.80 seconds.
The skips require `DOTBOX_DOSBOX_EXECUTABLE` or `DOTBOX_DOSBOX_BASE_SOURCE`,
neither supplied to this task. The checked dependency set is Pillow 12.3.0,
pytest 9.2.0 and optional MCP 2.3.0.

Final verification:

| Check | Result |
| --- | --- |
| New asynchronous regressions | 22 passed |
| Combined client/ownership suite | 101 passed, 0 skipped |
| Full source suite | 422 passed, 7 native skips, 32.60 seconds |
| Ordinary isolated wheel build | Passed |
| Client/ownership suite from the installed wheel outside the source checkout | 101 passed, 0 skipped, 15.26 seconds |
| Source, wheel and installed runtime identities | All 22 modules match exactly |
| Installed base package without fDisBull or optional MCP | Verified |
| Independent code review and cancellation experiment | No blocking finding; experiment exit 0 |

The first regression failed on the missing async API before implementation.
The final checks confirm local Python cooperation only. See the
[sanitized verification receipt](evidence/async-turn-fence-2026-11-17.json) for
commands, package identities, setup corrections and qualification limits.

Reproduce source checks in a project virtual environment with:

```sh
python -m pip install '.[test,connector]'
python -m pytest -q -ra
```

## Next concrete gate

1. Establish a supported path on the original Dot executor that can check a
   turn receipt and complete its existing desktop action without switching
   environments. The Python helper alone does not provide that path, and the
   status-only MCP connector does not expose it.
2. Keep the three-second receiver freshness contract. Use the same unchanged
   receipt before and after a harmless authorized input and observation of
   its visible effect. Record takeover, return and interruption behavior.
3. Qualify the standalone native package on that actual Dot runtime, including
   frame/input operation, persisted controls and process cleanup.
4. Resume gameplay, AGI/pathfinding work and audio only in the approved later
   milestones. Keep private game files and raw runtime evidence outside Git.

These are sampled cooperation checks, not an atomic capture lock. A transition
entirely between samples can be missed; the outer harness still owns capture
and input already in flight. No live ownership probe, desktop input, environment
switch, tunnel change, game launch or release publication was performed here.
