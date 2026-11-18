# DotBox

Play DOS games with Dot using an independent DOSBox-X session framework.
The original graphical game remains authoritative.

Dot's planned [internal game model](docs/WORLD_MODEL.md) retains entities,
relationships, rules, evidence and her own useful abstractions. Z-scenes are
bounded views of that knowledge plus current observations. The proposed model
uses exact structured queries with optional text/vector retrieval; the current
observation store is only one part. `dotbox guide --topic world` explains the
design and its implementation boundary.

[Reverse engineering](docs/REVERSE_ENGINEERING.md) remains available to resolve
ambiguous state and discover relationships, including native games and reused
storage. The next [Dune transfer test](docs/DUNE_VALIDATION.md) covers menus,
selected entities and strategic orders after a frozen generic baseline. The
new `reversing` and `dune` guide topics document required work and prior evidence;
they do not claim a newly implemented live analyzer or Dune harness.

The primary experience is [Dot as the game's conversational interface](docs/CONVERSATIONAL_PLAY.md):
describe the current scene, offer useful choices, interpret the player's intent
and carry it out. Autonomous play uses the same scene/action model. A small
[guide-informed opening pass](docs/GUIDE_RECONSTRUCTION.md) supplies the game's
goal and a checklist of expected objects and exits, which Dot reconciles with
the actual game. Description length, who chooses, and hints remain separate preferences.
When usage permits, Dot can spawn full cloud agents to prepare likely upcoming
scenes while Dot narrates and operates the live game. Graphical movement is
useful progress and natural preparation time. `dotbox guide --topic lookahead`
documents bounded prediction, independent worker candidates and adoption at a
fresh action boundary. These are operating requirements; this cut does not add
a cloud scheduler or qualify live movement/voice concurrency.

This development cut extracts the working transport, input validation, screenshot
handling and immutable learned controls from fDisBull. It does not import or
require an installed fDisBull package or analysis database. The package now
includes a bounded offline inspection kit, a saved next-question journal and
the play instructions, with its pinned x86 decoder as a required dependency.
It also owns the small [AGI V2 logic/resource reader](docs/ENGINE_AWARE_PREPARATION.md)
and a [state-bound walking planner](docs/NAVIGATION.md), so compatible engine
evidence and long straight route legs can be prepared without the full analyzer.
A compatible DOSBox-X native build is a separate explicit runtime input.

Start with [standalone installation](docs/STANDALONE.md), the
[native source/build recipe](docs/STANDALONE_NATIVE.md), and
[persistent controls](docs/PERSISTENT_CONTROLS.md).
For a local Apple Silicon build, use the
[Mac build-and-test helper](docs/LOCAL_MACOS_BUILD.md). It builds the pinned
native source and requires eight actual native fixture passes, with no skips.
A fresh Mac Studio build passed all eight fixtures, four headless and four
visible, on 17 November 2026. See the
[sanitized native-build receipt](https://github.com/seeker-cyber-maker/DotBox/blob/codex/local-macos-build-20261117/docs/evidence/local-macos-native-2026-11-17.json).
A separate [cloud Linux build](docs/LOCAL_LINUX_TEST.md) also passed all eight
fixtures, and an ordinary-input Police Quest run completed the locker-to-shower
controls endpoint. These results qualify the recorded developer-build fixtures
and one functional game route. Original-Dot desktop integration, reusable route
and timing qualification, and complete memory rewind remain separate gates.

For the current development slice, read [incremental play](docs/INCREMENTAL_PLAY.md)
and the [installed learning kit](docs/LEARNING_KIT.md). `dotbox guide` gives Dot a
short starting procedure; `dotbox doctor` checks offline tools and packaged
resources without launching a game. Use a known applicable control for the
selected intent now, observe
its effect and save the recipe afterward. Learn only the next missing interaction.
The current 15-second/two-probe learning allowance is an evaluation policy,
not a measured promise of seamless play.

The current scene slice renders provider-reported facts, keeps guide expectations
internal, and returns a scene-bound intent without executing input. Its
[stateful scene tools](docs/STATEFUL_SCENES.md) persist observations and flags,
reject selections made stale by offscreen updates, distinguish enabled actions
from input readiness, and separate useful suggestions from commands available
on request. `dotbox scene look` passively describes the current scene; `record`,
`present --store`, `choose --store` and internal `memory` use the saved observation
stream. `dotbox guide --topic state` explains the provider adapter contract.
The offline slice does not yet extract live game flags, recognize scenes, parse
arbitrary speech, fetch walkthroughs or connect a live voice frontend.

For development continuation, read the [current handoff](docs/DEVELOPMENT_HANDOFF.md).

The first milestone is the engine and its ownership boundary: one guest survives
client calls, frames can be observed, and stale agent input is refused after
explicit human handoff in diagnostic mode. Normal input stays on the desktop
harness path, with direct agent input RPCs disabled. Codex's **Take over / Return control** buttons belong to
the outer WebRTC harness. The optional [ownership bridge](docs/OWNERSHIP_BRIDGE.md)
uses fresh viewer observations to coordinate cooperating agent turns. Native
ownership stays separate. A coordination-only receiver can run without an
emulator. The real viewer-to-headless-receiver handoff is verified over the existing
private SSH route, using harmless data callbacks. The saved operations environment
starts. Actual desktop-tool input through the turn wrapper remains unqualified.
The [connection follow-up](docs/evidence/studio-connection-repair-2026-11-16.json)
verifies restored Studio attachment with a sandboxed default. In the checked
attachment, Dot's desktop-tool session reinitialized and its bound cloud app
variable was unavailable. The original cloud desktop and coordinator still need
a shared supported execution path for the input check.
The optional [ownership connector](docs/OWNERSHIP_CONNECTOR.md) now connects Dot
through an existing private Secure MCP Tunnel. Live reads match Dot, human after
Take over, and Dot after Return control. Paused foreground observation returns
unknown; no unattended sampler or input grant is implied. See the
[connection permissions](connectors/ownership/permissions.review.json) and
[live verification](docs/evidence/ownership-connector-live-2026-11-16.json).
The [earlier preflight](docs/evidence/desktop-ownership-preflight-2026-11-16.json)
also records the fix preventing asynchronous callbacks from being reported as
completed synchronous actions. The separate `Client.run_turn_step_async` now
awaits a cooperative Python callback between checks of one unchanged lease.
It does not expose CUA tools to Python or qualify live Dot input.

`dotbox agi inspect` produces a bounded private census for the explicit AGI
2.917/uncompressed V2 profile. It identifies conditions, state writers and
resource candidates; static references do not establish current flag meanings
or available actions. `dotbox route plan` minimizes distance, then turns, and
compresses a route into straight legs. `route check` rejects proposals made
stale by changed supplied scene/state, geometry or conditions. Both commands
are offline and send no input.

[Recovery and saved-game evidence](docs/RECOVERY_AND_SAVES.md) specifies how to
reuse native checkpoints to recover from a stall or crash, invalidate the old
timeline and learn from controlled save contrasts. The existing raw restore
primitive still needs a qualified restore transaction before DotBox can offer
live rewind. Revert restores memory; mounted files keep their current versions,
with no matching filesystem rollback. Selected long legs likewise
need integration with the existing monitored x/y and TAS control machinery.
The [recovered AITD work](docs/AITD_REUSE.md), available through
`dotbox guide --topic aitd`, supplies prior walking feedback, manipulation
planning and reference-backed menu methods. Its research helper that replaces
save files is explicitly excluded from memory revert.
The user-selected [Police Quest acceptance tests](docs/POLICE_QUEST_ACCEPTANCE.md)
are changing in the locker room and reaching the showers, then recovering from
late arrival at the first briefing. The first has one successful functional
run on the cloud Linux computer, including shower activation and cleanup through
ordinary controls. A reusable route and complete timing trace remain open;
the missed-briefing memory-recovery trial has not run. `dotbox guide --topic
policequest` supplies the EGA-specific conditions and static timer findings.
The guide itself adds no game-control or recovery operation.
Additional engines, game-specific routes, HUD and audio transport remain later
work. There is no published release or qualified Dot cloud installation yet.

[Verification](docs/evidence/standalone-engine-2026-11-16.json) · [Extraction boundary](docs/EXTRACTION.md) · [Product brief](docs/PRODUCT.md) · [Repositories](docs/REPOSITORIES.md)

See the [Codex viewer code investigation](docs/CODEX_VIEWER_CODE_ANALYSIS.md) for
ownership signals, actual-source offline checks, live viewer results and remaining
bridge boundaries. Movement through that ownership bridge, recovery and audio
still need qualification; the separate local controls run does not close them.
