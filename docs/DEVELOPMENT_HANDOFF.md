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
- Learning-kit continuation: `codex/incremental-learning-kit-20261117`,
  based on primary async-turn-fence commit
  `999dc0ed788e6b20593166a4e9e40b2c2525004e` (draft PR #3). The independent
  mirror's matching parent is `69c5289786b2752bffd669bdf605745432a7929c`;
  those parents have identical trees but different account commit metadata.
- Conversational-scene continuation: `codex/conversational-scenes-20261117`,
  based on primary learning-kit commit `605f41240f271f2311a997495b3eb0292c574f35`
  (draft PR #4). Its independent mirror parent is
  `c131661fece58a3d096938df5632d2986cf0ed90`; their shared tree is
  `55265b1641e9d97a8f52e1e427fa2d3039c6ff0d`.
- Current predictive-preparation continuation:
  `codex/predictive-scene-preparation-20261117`, based on primary conversation
  commit `676ed6fdc16cafccbd4d676a016a5d5d4deeb463` (draft PR #5).
  Its independent mirror parent is `e3e2548c5cefda60406ee4a8402edbbea1d9684a`;
  their shared tree is `e25e44aa791ecc4159985a9c093d56e9c7e8737b`.
- At inspection, `main` was the design baseline at
  `10fa86d8a91bb75e0ccf3da346bc9f72eab91d03`; it did not contain the implementation.

Read `AGENTS.md`, `docs/PRODUCT.md`, `docs/CONVERSATIONAL_PLAY.md`,
`docs/GUIDE_RECONSTRUCTION.md`, `docs/INCREMENTAL_PLAY.md` and
`docs/LEARNING_KIT.md` for the current work. Read `docs/OWNERSHIP_BRIDGE.md` and
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

## Current continuation: predictive preparation during movement

The user clarified that Dot can spawn full cloud agents when usage permits.
Dot narrates, orchestrates retrieval and controls the live game while workers
prepare candidate scenes for selected or likely accessible upcoming locations.
Graphical movement is useful progress and a natural preparation window; instant
text choices may provide little such time. This continuation makes that method
explicit in the installed guides and removes the previous instruction against
creating a cloud environment merely to parallelize.

Keep one foreground blocker and a bounded predictive queue. Each worker has a
near-term consumer, frozen evidence/branch identity, useful-by point, hard work
bound and early partial output. Workers can edit and test their own candidates
in isolated environments, including separate mutable files. Dot retains the
single live owner, checks actual destination/state and adopts compatible
revisions between completed actions. A clone result is evidence for that clone,
not progression in the player's game.

Start appropriate known movement promptly. Do not slow walking, add detours or
pad narration to buy preparation time. On early arrival, use a working ordinary
route immediately; a late worker does not imply a stall. The lead's existing
15-second/two-probe journal is unchanged and is not a distributed worker queue
or a blanket background deadline. Arrival, new screenshots and late results
cannot reset an existing focus. Capture foreground blocked intervals separately
from traversal, user decisions, worker duration and adoption costs.

`dotbox guide --topic lookahead` aliases the packaged continuous-play reference.
This is a documentation/resource continuation of `0.1.0.dev3`, with 37 resources;
it changes no Python runtime module, learning-store API or ownership behavior.
It does not implement a cloud scheduler, predictive recognizer, movement monitor
or concurrent voice frontend. Qualification of the real flow remains pending.
Fresh verification: the existing package suite passed **21 source checks** and
**21 checks copied outside the checkout** against a fresh offline installation.
All **26 runtime modules and 37 resources** match source, wheel and installed
bytes; `lookahead` and `continuous` return identical guide content. An independent
reader of the installed guides found no blocking contradiction across six
movement, route-change, late-worker, usage-loss, takeover and instant-text cases.
That review is a policy walkthrough, not an executed concurrency test.
The installed-package and independent scenario evidence is recorded in
`docs/evidence/predictive-scene-preparation-2026-11-17.json`.

Use existing provider scene/workflow/Z contracts when integrating the result of
the separate fDisBull 0.34.1 study. The DotBox scene packet remains a bounded
presentation/evidence boundary; selected reusable modules must eventually ship
inside DotBox rather than require a separate end-user fDisBull installation.

## Prior continuation: conversational scenes

The user clarified that autonomous play is supported, while the primary
experience is Dot acting as the game's conversational interface. Z-scenes
provide grounded descriptions and choices; Dot phrases them according to the
player's preferences. An initial manual/guide pass supplies the broad goal and
expected objects/exits as a reconstruction checklist. The Magic Door was named
as an interaction reference, not an integration target.

Version `0.1.0.dev3` adds `scenes.py` and `dotbox scene` with four offline
operations: present, checklist, validate and choose. A closed, bounded authored
packet keeps current observation claims separate from guide expectations.
Brief/normal/detailed player views retain the same permitted facts and choices;
their deterministic narration and choice prompt provide a fallback for Dot's
own phrasing. The internal checklist preserves disagreements, unknown editions,
copied-source groups and unchecked conditions without voting claims into truth.

Choice selection is bound to the exact document digest and observation ID. It
returns an intent with no input execution, no ownership grant and no inferred
outcome. Choices reference existing immutable controls or ordinary supported
input routes; there is no second raw input language. All semantic observations,
audience classifications and route applicability remain caller assertions.

The guide/skill now distinguishes player-led choice from autonomous delegation.
"Act now" applies to an already selected intent or delegated goal. A bounded
guide pass fits the existing preparation timeline, and incomplete reconstruction
does not block a working route. Description length, decision maker and hint
preference are separate. Guide-informed narration does not imply blind play.

The wheel contains 37 operational resources, including two new topic guides
and authored mailbox/station/barrel examples. Doctor projects and selects the
mailbox fixture without executing an action. The examples contain no commercial
game data; their source identities and input-route references are illustrative.

Current source verification: **551 passed, 7 native skips** in 33.84 seconds.
The new scene suite has **45 passing cases** and the package suite **21**,
including exported-example CLI round trips. Independent review found no
confirmed blocking defect. A fresh-reader eight-scenario test exercised offline
projection/selection and produced the intended game-facing decisions; wording
about zero/ambiguous targets and using the full scene view was clarified.

Direct and sdist-rebuilt wheels have identical package bytes. All **26 runtime
modules and 37 operational resources** match source, both wheels and the fresh
installation. Installing from local dependency wheels with `--no-index` passed;
there is no source import, fDisBull or optional MCP in that environment. Eight
copied suites outside the source tree passed **230 tests, 0 skipped**, in
15.87 seconds. Installed mailbox/station/barrel projection and selection checks
also passed, including detail invariance, partial coverage, hidden-content
exclusion, stale-observation refusal and zero execution. Python/dependency
versions remain those recorded for the preceding learning-kit slice.

See [the scene receipt](evidence/conversational-scenes-2026-11-17.json) for the
completed installation results, exact artifacts and qualification boundaries.
No automatic guide extractor, condition evaluator, natural-language parser,
scene recognizer, goal planner, live input adapter or voice frontend is supplied
by this offline module.

## Prior continuation: incremental learning kit

The user redirected the available offline development time toward ordinary
players: DotBox should supply the reversing machinery, and Dot should learn
only what is needed next without making working play wait for harness authoring.

Version `0.1.0.dev2` adds three modules and five CLI entry points:

- `inspection.py` / `dotbox inspect`: explicit COM/MZ/resource identity, bounded
  strings, masked byte patterns, real 16/32-bit iced-x86 decoding and frozen-range
  diffs. Limits and exact selected-byte identities travel with each result.
- `learning.py` / `dotbox learn`: one private SQLite focus, a non-renewing default
  15-second/two-probe admission allowance, explicit retirement and immutable
  caller-reported evidence. Same-context updates do not reset time or counts.
- `kit.py` / `dotbox guide`, `doctor`, `kit-export`: installed progressive
  instructions, resource-integrity/decoder/clock checks and a private new-directory
  export of the native preparation resources. No command launches a native game.

The core dependency now includes `iced-x86==1.22.0`. Setuptools stages an explicit
32-file resource manifest into the wheel, generating a hash/size catalog. The
play skill and its references are included; no installed personal-skill plugin
was changed. Native patches and source notices are packaged, while a prepared
native executable, platform libraries and the final player installer remain
separate requirements.

The method now says: use an applicable known action immediately, observe its
effect, then save useful metadata without replay. No named scene, wrapper or
complete starting buffer gates an already usable control. A current missing
interaction gets one bounded question; a working fallback takes priority over
optional research. The 180-second initial preparation ceiling is not a minimum
wait or a per-room reset. One agent is sufficient; workers are optional.

Default desktop input and diagnostic native `act` are now distinguished in all
current play/control guides. The old dependent-prototype startup pointer was
replaced with the standalone route. Budget enforcement covers admissions only;
it cannot preempt reasoning/tools, recognize scenes or grant input ownership.

### Learning-kit verification

| Check | Result |
| --- | --- |
| Inspection, learning and resource/CLI cases | 36 + 27 + 17 = 80 passed |
| Full source suite | 502 passed, 7 native skips, 32.91 seconds |
| Direct wheel and wheel rebuilt from sdist | Both built; package bytes match |
| Source / both wheels / isolated installation | All 25 modules and 32 resources match |
| Fresh installation from local wheelhouse only | Passed with no index and no fDisBull or optional MCP |
| Seven copied suites outside source checkout | 181 passed, 0 skipped, 15.74 seconds |
| Installed authored workflow | Identity, admitted decode, candidate receipt, expiry/fallback and retirement passed |
| Fresh-reader instruction forward-test | All seven decision scenarios resolved; wording ambiguities corrected |
| Independent implementation review | Concrete findings fixed; no remaining material issue found |

The tested interpreter is Python 3.12.14 on Linux; Pillow is 12.3.0, iced-x86
1.22.0 and pytest 9.2.0. Source checks also had optional MCP 2.3.0. The Linux clock
identity was exercised; the macOS branch remains unexecuted. The runtime still
lacks the two native inputs listed in the earlier verification, hence the same
seven skips. The small authored CLI commands took about 0.06–0.14 seconds each
in one host run; this excludes model and dispatch time and is not player latency.

See [the learning-kit receipt](evidence/incremental-learning-kit-2026-11-17.json)
for artifact identities, scope, commands, reviews and qualification limits.

## Prior continuation: asynchronous turn fence

An additive `Client.run_turn_step_async(lease, action)` fences a fresh Python
coroutine on an executor that already has supported action and coordinator
access. It snapshots one receipt, checks it without blocking the event loop,
awaits the callback, then checks the unchanged receipt. It preserves completed
results on postcheck interruption and propagates cancellation with inspection
guidance. It rejects prestarted and nested deferred work. There is no retry,
renewal, permission change or change to the synchronous helper.

The new regression tests use a real authenticated loopback coordinator and
harmless data callbacks. They do not operate a desktop or launch a game.

## Prior turn-fence verification

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

## Next development and live gates

First connect one small real scene to the qualified observation/input path:
present useful choices, resolve an unambiguous player intent, perform a bounded
ordinary action and describe only its observed result. Establish the exact game
edition and a small cited goal/guide brief. Test the same scene under bounded
autonomous delegation. A complete world graph or scene checklist is not required.
Speech can consume the same view and intent contract after the text loop works;
actual voice availability and pacing remain integration measurements.

Then qualify one selected movement leg with a real cloud worker preparing the
destination: verify timely partial delivery, fresh arrival checks and adoption
between actions. Exercise a different exit, late result with a working fallback,
usage loss, takeover and an instantaneous text transition. Measure first-input
latency, confirmed effect, natural travel and actual foreground blocks on the
same lead timeline; do not infer latency improvements from this guide change.

When that route needs native evidence, expose a short owned capture transaction
that validates an entire bounded plan, captures only the required memory/register
packet and resumes before model reasoning. The pinned native backend requires a
stopped guest for those reads; raw RPC passthrough is not an acceptable shortcut.
Test consistency, aggregate limits, partial failure and takeover behavior before
any real-game use. Then add one edition-scoped engine reader or applicability
predicate only when it resolves a near-term play question. Existing descriptive
control metadata does not enforce resource identity or live scene recognition.

The live gates remain separate:

1. Establish a supported path on the original Dot executor that can check a
   turn receipt and complete its existing desktop action without switching
   environments. The Python helper alone does not provide that path, and the
   status-only MCP connector does not expose it.
2. Keep the three-second receiver freshness contract. Use the same unchanged
   receipt before and after a harmless authorized input and observation of
   its visible effect. Record takeover, return and interruption behavior.
3. Qualify the standalone native package on that actual Dot runtime, including
   frame/input operation, persisted controls and process cleanup.
4. Measure the new method on cold start, warm reuse and a real room/menu
   transition. Include agent reasoning and dispatch in interruption timings;
   keep animations and user decisions distinct. Full game recovery and audio
   remain later work. Keep private game files and raw runtime evidence outside Git.

These are sampled cooperation checks, not an atomic capture lock. A transition
entirely between samples can be missed; the outer harness still owns capture
and input already in flight. No live ownership probe, desktop input, environment
switch, tunnel change, game launch or release publication was performed here.
