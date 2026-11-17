# DotBox

Play DOS games with Dot using an independent DOSBox-X session framework.
The original graphical game remains authoritative.

The primary experience is [Dot as the game's conversational interface](docs/CONVERSATIONAL_PLAY.md):
describe the current scene, offer useful choices, interpret the player's intent
and carry it out. Autonomous play uses the same scene/action model. A small
[guide-informed opening pass](docs/GUIDE_RECONSTRUCTION.md) supplies the game's
goal and a checklist of expected objects and exits, which Dot reconciles with
the actual game. Description length, who chooses, and hints remain separate preferences.

This development cut extracts the working transport, input validation, screenshot
handling and immutable learned controls from fDisBull. It does not import or
require an installed fDisBull package or analysis database. The package now
includes a bounded offline inspection kit, a saved next-question journal and
the play instructions, with its pinned x86 decoder as a required dependency.
A compatible DOSBox-X native build is a separate explicit runtime input.

Start with [standalone installation](docs/STANDALONE.md), the
[native source/build recipe](docs/STANDALONE_NATIVE.md), and
[persistent controls](docs/PERSISTENT_CONTROLS.md).

For the current development slice, read [incremental play](docs/INCREMENTAL_PLAY.md)
and the [installed learning kit](docs/LEARNING_KIT.md). `dotbox guide` gives Dot a
short starting procedure; `dotbox doctor` checks offline tools and packaged
resources without launching a game. Use a known applicable control for the
selected intent now, observe
its effect and save the recipe afterward. Learn only the next missing interaction.
The current 15-second/two-probe learning allowance is an evaluation policy,
not a measured promise of seamless play.

The current scene slice adds `dotbox scene present`, `checklist` and `choose`.
It renders authored current facts, keeps guide expectations internal, and returns
a scene-bound intent without executing input. It does not yet recognize scenes,
parse arbitrary speech, fetch walkthroughs or connect a live voice frontend.

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

Additional AGI readers, walking, game-specific routes and HUD experiments remain
preserved in the original development checkout. They are deferred from this
standalone cut. Audio transport is also deferred. There is no published release
or qualified Dot cloud installation yet.

[Verification](docs/evidence/standalone-engine-2026-11-16.json) · [Extraction boundary](docs/EXTRACTION.md) · [Product brief](docs/PRODUCT.md) · [Repositories](docs/REPOSITORIES.md)

See the [Codex viewer code investigation](docs/CODEX_VIEWER_CODE_ANALYSIS.md) for
ownership signals, actual-source offline checks, live viewer results and remaining
bridge boundaries. Audio and game work remain deferred.
