# DotBox

Play DOS games with Dot using an independent DOSBox-X session framework.
The original graphical game remains authoritative.

This development cut extracts the working transport, input validation, screenshot
handling and immutable learned controls from fDisBull. It does not import or
require an installed fDisBull package, analysis database, disassembler or proof
engine. A compatible DOSBox-X native build is a separate explicit runtime input.

Start with [standalone installation](docs/STANDALONE.md), the
[native source/build recipe](docs/STANDALONE_NATIVE.md), and
[persistent controls](docs/PERSISTENT_CONTROLS.md).

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
