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
- Predictive-preparation continuation:
  `codex/predictive-scene-preparation-20261117`, based on primary conversation
  commit `676ed6fdc16cafccbd4d676a016a5d5d4deeb463` (draft PR #5).
  Its independent mirror parent is `e3e2548c5cefda60406ee4a8402edbbea1d9684a`;
  their shared tree is `e25e44aa791ecc4159985a9c093d56e9c7e8737b`.
- Stateful-scene continuation: `codex/state-aware-scenes-20261117`,
  based on primary predictive-preparation commit
  `2322cfbf16441343ea998d76479b7b4fbfd59340` (draft PR #6).
  Its independent mirror parent is `c88464e656912e41a74b986f416d0380e804623f`;
  their shared tree is `93e2baa150ea6e6234e23bad9ebb24c43217ac36`.
- The state continuation is now published as [draft PR #7](https://github.com/seeker-cyber-maker/DotBox/pull/7).
  Primary head is `cb72a966411a821cb860c56760675891fc0d0ea3`; independent mirror
  head is `a7c8556a992a2a64a4474104e44a36f1cf2d8c84`. Their verified shared tree is
  `4dc1a12a2e871b980db37ea78decf5d85768b4f1`. The user's explicit GitHub update
  instruction resolved the earlier automatic publication-review refusal.
- The AGI/navigation continuation is published as [draft PR #8](https://github.com/seeker-cyber-maker/DotBox/pull/8).
  Primary head is `f9572d84943c57dcdb83587f85966619ef392325`; independent mirror
  head is `b018024963dac96e75785b0fc084c63d697333a2`. Their verified shared tree is
  `707ab7a0a3ce0cb68087368389c48895ad6cd448`.
- The memory-recovery continuation is published as [draft PR #9](https://github.com/seeker-cyber-maker/DotBox/pull/9),
  branch `codex/memory-recovery-20261117`. Its initial fence snapshot has primary
  head `f364476892b309ff76fa024a739b36c2c0f6fc73`, mirror head
  `727babb122f2bc09bbfe311635e0c9b38e423c5c`, and shared tree
  `9d88e87fb4990f47a74da9f8f1c6c1609c8eb810`. The Police Quest acceptance
  specification continues on that draft branch, preserving both histories.
- Local-build continuation: `codex/local-macos-build-20261117`, based on primary
  memory-recovery head `2b61471a5159825e466ab8c201aa6e3c7cd306a2` and independent
  mirror head `d12764adc1feccfd1361af45a67c1f36ce651adf`. Their shared input tree
  is `f63ffc7cc7bddadf80db6c8355f238be146c1d90`. Use this implementation branch
  for the local build; do not assume the draft stack is merged into `main`.
- At inspection, `main` was the design baseline at
  `10fa86d8a91bb75e0ccf3da346bc9f72eab91d03`; it did not contain the implementation.

Read `AGENTS.md`, `docs/PRODUCT.md`, `docs/CONVERSATIONAL_PLAY.md`,
`docs/GUIDE_RECONSTRUCTION.md`, `docs/INCREMENTAL_PLAY.md` and
`docs/LEARNING_KIT.md`, `docs/ENGINE_AWARE_PREPARATION.md`, `docs/NAVIGATION.md`
and `docs/RECOVERY_AND_SAVES.md` for the current work. Read `docs/OWNERSHIP_BRIDGE.md` and
`docs/OWNERSHIP_CONNECTOR.md` before changing the ownership boundary. Follow
`docs/REPOSITORIES.md` for publication. Earlier AGI/walking/HUD experiments stay
in the original developer's private checkout and snapshot. This continuation
inspected the installed fDisBull 0.34.1 package and selected pinned source; the
user's exact old x/y TAS script remains unidentified. The latest board-led
recovery did retrieve the AITD movement/menu source described in `AITD_REUSE.md`.

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

## Current continuation: local Mac build and strict native tests

Version `0.1.0.dev7` adds `scripts/build_local_macos.py` for a fresh, private
Apple Silicon build with two compiler jobs, the pinned bundled SDL2, an ordinary
Python wheel/isolated installation and retained stage logs. Required system
dependencies remain an explicit Terminal setup step. The procedure is packaged
as `dotbox guide --topic macos`; the executable helper requires the full source
checkout, not only an exported operational kit.

`scripts/test_native.py` requires the explicit native executable and exact
JUnit identities/counts. All eight selected fixtures must execute without skips;
four headless or four visible tests can instead be selected and are reported as
that limited scope. The executable must have the same SHA-256 before and after
the run. A source receipt is metadata, not an independent binary attestation.
Installed-wheel doctor evidence remains separate from fixtures importing the
checkout's source. Runner unit tests use authored reports and do not run DOSBox-X.

No connection to the Mac Studio or fresh macOS native build was established in
this continuation. The selected cloud executor is Linux; its SSH client failed
before a connection attempt. This does not diagnose the Studio or require an AI
agent to run the local compiler. Start with the logged-in Mac Terminal command
in [LOCAL_MACOS_BUILD.md](LOCAL_MACOS_BUILD.md), inspect the saved result and
continue from any actual compiler/runtime failure. A headless pass alone cannot
qualify visible execution. Full original-Dot input and the two Police Quest
trials remain later integration gates; this continuation adds no rewind API.

Final source verification passed **802 tests**, with exactly **eight native
executable skips**. The supplied pinned base enabled the real overlay application
and repeat-application check. The new build helper has 38 focused checks and the
strict runner has 28; these include authored process cleanup and read-only pip
configuration probes, not emulator acceptance. An ordinary wheel and clean
offline installation match all 35 runtime modules, 48 resources and 18 topics;
the installed `macos` guide, export and doctor pass. Independent review found
no remaining blocker after the cancellation and pip-probe fixes. See the
[sanitized helper verification](evidence/local-macos-build-2026-11-17.json).

## Retained continuation: memory-only recovery and recovered AITD work

Version `0.1.0.dev6` corrects the recovery contract and adds a native source-level
restore admission fence. Revert restores memory and necessary machine/device
state; it must not replace files with older copies. A changed, closed autosave
does not itself block recovery. Immutable source/resources, mount configuration
and concrete saved-handle dependencies remain separate compatibility checks.

The native overlay advertises `input.restore_control=dotbox-restore-control-1`.
Raw `state.load` now requires `expected_generation`. The emulation-thread check
preserves owner and advances generation before cleanup/loading; stale generation
is rejected before effects. Old tagged input stays invalid after an admitted
failure. This is not a `memory_checkpoint` capability or a public Python recovery
API. The serializer and explicit `frame_keys` policy are unchanged. Native
load can rehydrate keyboard hardware state; neutral capture and verification
remain necessary. Newer mutable files must not be restored from history.

Two source audits found that DOS handle reconstruction can flush current pending
writes while reopening a file. That is persistence of current writes, not disk
rollback, and should not be confused with the historical backup/restore path
already disabled by `AGENT_StateFile`. Qualify the I/O boundary before exposing
interactive recovery. A small initial profile can exclude active writable
handles/pending writes/mutable disk images while allowing changed closed saves.
Do not omit DOS handle restoration or claim byte-preserving load without proof.

The original Charming board's stored fDisBull handoff led to the preserved
source/history archive. All 69 indexed artifacts matched size/hash. Eight
AITD continuation Python files and earlier menu/reference helpers were recovered.
Their ordinary walking controller uses current X/Z/heading, bends and bounded
stall/divergence checks; its object planner includes actor contact stances.
DotBox keeps its existing heading-aware planner and stronger footprint/safety
admission. Menus use sparse current-state and highlighted-selection guards,
with modal exclusion and separate selection/execution outcomes.

The old AITD continuation's `load()` explicitly replaces `SAVE0.ITD` from a
retained copy. Exclude that research policy from memory revert. The new installed
`aitd` topic documents the reusable parts, exact provenance and missing private
calibration. No AITD source/asset or new game-specific adapter is imported.
Historical AITD tests/replay timings were not rerun.

The existing service identity already includes native generation. An authenticated
socket regression verifies that a same-owner generation change invalidates the
old turn while an ordinary `state_revision` change does not. It does not repair
the ownership boundary automatically. A future complete recovery controller must
handle admitted failure, fresh branch/store and coherent post-restore observations;
offline SceneStores and worker candidates do not invalidate themselves.

Matching upstream source is available and both patch stages can be verified.
A compatible complete native build and original-Dot live recovery remain
unqualified on this host. The available fDisBull binary is a different native
revision and is not substituted for this overlay. The recovered walking/menu
work remains a controller reference. The user has now selected the concrete
Police Quest controls and rewind trials below as the next live acceptance goals.

### User-selected Police Quest trials: specified, not executed

The controls endpoint is changing in the locker room, closing the locker and
walking to the usable showers. Water activation is an optional separate action.
The recovery endpoint is missing the first briefing, restoring a predeadline
memory checkpoint while preserving newer disk files, and successfully attending.
Use the separate starting states and predicates in
[Police Quest acceptance](POLICE_QUEST_ACCEPTANCE.md), also installed as
`dotbox guide --topic policequest`.

Fresh read-only inspection of the supplied EGA 2.0G/AGI 2.917 files established
the two timer mechanisms: late arrival tests engine minutes on entry from the
lobby, while newspaper return accelerates a separate event countdown. Recent
key activity can affect the countdown without resetting the clock. The shower
approach stays in room 5; called LOGIC 39 is not a destination. These are static
findings and candidate observation predicates, not qualified live mappings.

The retained census matched nine resource files and all 118 LOGIC payloads.
The coordinator reran a private check of 34 operations and 16 conditions against
the current bytes; hashes and mtimes remained unchanged. No game or native
session was launched. The original interpreter's clock/pause behavior, live
route and memory restore remain unverified. This follow-up changes operational
resources and evidence only; runtime code and native patch are unchanged.
The existing source kit suite passed 23 checks. An ordinary wheel and clean
offline installation agree with the source on all 35 runtime modules and
47 operational resources, with 17 topics. The installed `policequest` command,
resource export and offline doctor passed; native qualification remains false.
See the [acceptance investigation receipt](evidence/police-quest-acceptance-2026-11-17.json).

### Initial memory-fence snapshot verification

| Check | Result |
| --- | --- |
| Full source suite with exact base native source supplied | 736 passed, 8 native-binary skips, 36.01 seconds |
| Independent focused native/service review | 21 passed, 4 native-binary skips; no blocking finding |
| Direct wheel and wheel rebuilt from sdist | Both built; all package bytes match |
| Source / both wheels / clean offline installation | 35 runtime modules and 46 resources match; 16 guide topics |
| Four copied focused suites outside the checkout | 44 passed, 4 native-binary skips, 3.12 seconds |
| Pinned native source and overlay | Upstream tree reconstructed; 37 base-result hashes and the 38-file final recipe verified; repeat application leaves bytes unchanged |
| Recovered AITD source archive | All 69 indexed artifact sizes and hashes matched |

The installed package used Python 3.12.14, Pillow 12.3.0, iced-x86 1.22.0 and
pytest 9.2.0, with no fDisBull or optional MCP available. The exact-base native
patch application test ran; the eight full-suite skips all require a matching
native executable. No emulator binary was built, native session launched, game
input delivered or end-to-end rewind qualified. See the
[sanitized memory-recovery receipt](evidence/memory-recovery-2026-11-17.json).

## Prior continuation: engine-aware preparation, routes and recovery

Version `0.1.0.dev5` owns the small AGI V2 logic/resource census and an offline
walking planner, with `agi`, `navigation` and `recovery` installed guide topics.
The AGI reader keeps the existing census contract, requires explicit profile
2.917, preserves per-resource failures and emits a private report plus a compact
summary. It supplies static conditions, state-write sites and resource/room
candidates; it does not read live flags, decode original-game saves or qualify
interactions. The high-bit IF displacement range remains opaque because the
consulted interpretations disagree; ordinary forward IF and signed GOTO remain
covered. The selected first-party source and license status are in `EXTRACTION.md`.

The walking planner reuses `fdisbull-spatial-map-1`, including collision footprint
and coordinate domains. Bounded heading-aware A* minimizes distance, then turns.
Unknown ground and unresolved hazards stay unavailable. All portal footprints
are blocked: plan an approach before a separately selected crossing. Collinear
steps become long legs. A proposal binds exact supplied map, scene, conditions
and state branch; `route check` reruns bounded deterministic planning and rejects
stale or edited content. Neither command establishes live freshness or moves
the actor. Existing x/y monitored controllers and frame/TAS key edges are useful
integration references, not a second input owner or a shipped live executor.

The prior recovery audit found full native checkpoint and frame-timeline machinery
already present in fDisBull and raw `state.save/load` in DotBox's native base.
Before dev6, raw load had no expected-control-generation admission/bump. The
service's run/session/generation/owner identity could consequently remain
unchanged through a world restore. That audit called for a restore fence,
input cleanup, new branch/context, immutable-dependency checks and fresh observations as
specified in `RECOVERY_AND_SAVES.md`; dev6 implements only the native control
fence portion. Ordinary `state_revision` is not a substitute
because ordinary input and saves advance it too. The user's subsequent correction
requires memory-only recovery: mounted host files retain their current versions,
and an unrelated changed autosave must not block restore. Do not implement a
matching filesystem snapshot or copy fDisBull's blanket mutable-file restriction.
Qualify native DOS handle/device behavior as well as the Python boundary.
Qualify one capture and restore
before promising a rolling rewind buffer. No live rewind was added here.

Saved-game differences are hypotheses for persistent state. Compare repeated
baseline saves, one meaningful action, static writers/consumers and observations
after the real loader reconstructs state. Keep commercial resources, saves and
raw reports private. The current static AGI reader is not a save-file decoder.

Independent review found and fixed two preparation-bound issues in the first
AGI extraction: layout was parsed before checking instruction/code limits, and
message aliases could multiply decoded text outside those limits. Code spans
and attempted instructions are now charged before more parsing. Shared text
budgets cover messages, initial object names and vocabulary; aliases reuse
unique work while emitted literal occurrences remain charged. Incremental JSON
hashing/encoding bounds the complete report before file creation. A failed
report cap produces no file. Coverage distinguishes logical alias entries from
actual attempted/admitted work. The new text allowance defaults to 256 KiB;
the report allowance defaults to 8 MiB with a 16 MiB hard ceiling.

Final verification on the calibrated build:

- **733 source tests passed, 7 native checks skipped**, in 34.72 seconds.
  The native checks require the actual source/executable acceptance inputs.
- **412 installed tests passed, 0 skipped**, in 16.60 seconds, from 13 suites
  copied outside the checkout and using authored fixtures exported from the
  installed wheel. The first invocation lacked those fixture files; that setup
  error was corrected without changing the runtime.
- **35 runtime modules, 45 resources and 15 guide topics** match source, direct
  wheel, sdist-rebuilt wheel and the clean offline installation. Neither fDisBull
  nor optional MCP is installed there. No source import is used.
- Independent AGI regression review passed all 56 focused tests and reproduced
  both original budget failures after correction. Independent navigation review
  passed 59 focused tests plus 632 separate route-oracle comparisons with no
  mismatch. The 160-by-168 authored grid used 486 expanded states for 326 steps,
  one turn and two legs under the normal 10,000-state allowance.
- Independent installed guidance/CLI review passed ten scenario checks across
  15 invocations, followed by four narrow final default/help/doctor checks.

Read-only runs against the existing private AGI resources decoded all 90
King's Quest I LOGICs and 118 Police Quest I EGA LOGICs with no layout, code,
instruction, text or value-analysis budget stop in resolve mode. The selected
profile was explicitly 2.917; prior edition identification was retained. Static
room candidates remain 81 and 42, respectively, with zero qualified executable
interactions. The first 4 MiB report default refused the roughly 4.6 MB Police
Quest census, so the final 8 MiB default was tested successfully on both games.
Final local command times, including process launch and report write, were
0.947/0.962 seconds for King's Quest outline/resolve and 1.883/1.961 seconds for
Police Quest. These exclude agent dispatch and live gameplay. Input hashes and
mtimes stayed unchanged. King's Quest still reports four sound-resource errors;
its resource-integrity flag stays false while its LOGIC coverage remains useful.
Original resources and full reports remain private. See
`docs/evidence/agi-navigation-kit-2026-11-17.json` for the sanitized receipt.

## Prior continuation: game state and useful choices

The user requires persistent game flags, offscreen consequences, independent
opening/lock state, useful option filtering and passive scene description.
Version `0.1.0.dev4` adds `scene_state.py` and extends the bounded scene packet.
The engine/provider remains authoritative; no second puzzle-rule interpreter
or expected-effect application was added.

`SceneStore` records the latest provider snapshot and last reported facts in a
private SQLite store bound to source, edition, optional selected resources,
provider, session and timeline. Increasing observation revisions prevent late
results from replacing newer state; an identical current repeat is idempotent.
Selection through the store checks its latest packet atomically, including
offscreen changes. The returned intent preserves the provider context token
and still requires a live admission/ownership check before any input.

An optional stable entity ID joins the same object or global flag across rooms.
Facts without it remain scene-local, preventing two doors with the same label
from replacing each other's memory. Sparse missing facts remain historical;
they are not reaffirmed or changed to false. Private provider outcome receipts
retain effect status and phase without creating flags. Current public facts,
provider enabled/readiness assertions and suggestion policy remain separate.
An incidental verb may be available on request without appearing in the default
menu; preference cannot override admission. Passive `look` returns the supplied
current scene description without input or a new choice prompt.

The new `state` guide and authored closed/open-window examples ship in the
ordinary package. `record`, `present --store`, `choose --store`, `look` and
internal `memory` are offline commands; no fDisBull installation is required.
Existing packets preserve their previous behavior when optional fields are
absent. Providers must supply current action gates; the supported Z verb list
alone is insufficient. Live flag extraction, observation delivery, provider
token rechecks and voice/input integration remain qualification work.

The source suite passed **616 tests with 7 native skips** in 34.98 seconds.
The focused scene/policy/state/CLI/package suite passed **131 tests** in 0.60
seconds. Independent review found a cross-scene identity collision in the first
store draft; the stable-entity/scene-local key fix and regression cases are
included. A fresh offline installation passed **295 tests, 0 skipped** across
11 suites copied outside the source tree, in 15.57 seconds. All **27 runtime
modules and 40 resources** match source, direct wheel, sdist-rebuilt wheel and
installation; the package has 12 guide topics. The installed authored window
sequence persisted the observed change, refused its old selection, preserved
explicit incidental input and returned passive descriptions. The environment
contains neither fDisBull nor optional MCP, and no source import was used.
An independent reader used only the installed guides/examples/APIs and passed
eight authored window, readiness, offscreen, delivery-order, door-identity and
restore/reopen scenarios. It found no blocking issue in the documented offline
contract. This was an executed offline scenario review, not native async timing
or live gameplay qualification.
The checks and their limits are recorded in
`docs/evidence/stateful-scenes-2026-11-17.json`.

## Prior continuation: predictive preparation during movement

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
