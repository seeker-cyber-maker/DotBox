# DotBox

Play DOS games with Dot. Keep what she learns, and share it.

DotBox is a development fDisBull spin-off focused on cooperative play in DOSBox-X
on Dot's own computer. The original graphical game is the main experience.
An optional Z-scene view exposes the same learned controls and observations
as readable objects, actions and a progress HUD.

The first session can spend a few minutes preparing controls and a small set
of starting scenes. Later sessions reuse that work. A shared compatible
harness should let another user start playing without rediscovering the controls.
Dot keeps extending the harness in useful slices as the game progresses.

The prototype provides a persistent play service and immutable learned controls,
including absolute mouse clicks in original game-frame coordinates. A compatible
fDisBull core and ownership-enabled DOSBox-X are prepared separately. There is
no packaged DotBox release yet; actual Dot-cloud takeover remains unqualified.

Start with the [play skill](skills/dotbox-play/SKILL.md),
[local play instructions](docs/PLAYABLE_SLICE.md) and
[persistent controls](docs/PERSISTENT_CONTROLS.md). The skill sets a recorded
startup budget and grows actions along the player's current route.

## Intended experience

- Run the game on Dot's visible desktop and use the computer's existing
  take-control / release-control flow.
- Keep playing while Dot prepares harness improvements from observations.
- Learn enough to operate the next interaction, then persist it immediately.
- Read interpreter state directly where an engine adapter makes that practical.
- Track the current game situation separately from what the harness understands.
- Reuse small analysis notes to adapt harnesses to nearby game editions.

The first implementation targets DOSBox-X only. Game conversion through
UDL, UIL or UDC and QEMU are outside the first release.

Read the [product brief](docs/PRODUCT.md), [initial work plan](docs/ROADMAP.md)
and [repository publication notes](docs/REPOSITORIES.md).

## Repositories and delivery

- Primary: [seeker-cyber-maker/DotBox](https://github.com/seeker-cyber-maker/DotBox)
- Independent mirror: [TiGa-RCE/DotBox](https://github.com/TiGa-RCE/DotBox)
- Planned package delivery: [Brewster Jennings release portal](https://release.brewsterjennings.ca)

Both repositories carry the same source history. Game files, personal saves,
private analysis databases and credentials stay outside these repositories.

The project builds on ideas and capabilities in
[fDisBull](https://github.com/seeker-cyber-maker/fDisBull).
