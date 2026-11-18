# DotBox product brief

Status: design baseline updated 18 November 2026. Requirements below are intended
behavior, not claims of implemented or measured DotBox capabilities.

## Current milestone — 17 November 2026

Package the incremental learning machinery and instructions so Dot can use them
without another repository, analyzer installation or available local worker.
Make Dot the conversational interface: offer grounded scene descriptions and
choices, then carry out the player's intent. Autonomous play selects from the
same scene/action model within a delegated goal. Use a known applicable control
immediately for that intent and learn only what blocks the next interaction.
Persist useful controls and evidence without replaying input.
When usage permits, Dot can spawn full cloud agents to prepare likely upcoming
scenes while Dot narrates and controls the live game. Prioritize selected
movement as progress and natural preparation time; keep one foreground blocker
and a bounded predictive frontier. Single-agent play is the fallback when
workers are unavailable.
Track observed game flags, inventory and object states across the selected
route, including confirmed offscreen consequences. Keep open/closed separate
from locked/unlocked and unknown. Refresh action admission after state changes,
remove redundant suggestions and preserve uncommon commands for explicit
requests. Treat response text, committed effects and input readiness separately
so conversation and preparation can continue during supported pending actions.
The [state contract](STATEFUL_SCENES.md) defines the offline record and the live
provider responsibilities; no predicted action effect becomes game truth.
Use [small engine-specific readers](ENGINE_AWARE_PREPARATION.md) when they expose
state more directly than native-code analysis. Treat saved-game records as
evidence for important persistent state, then qualify meanings through controlled
observations and restoration. Prefer [long straight walking legs](NAVIGATION.md)
with bounded feedback over repeated stops and turns. [Rewind](RECOVERY_AND_SAVES.md)
should recover from a stuck route or collision through a qualified checkpoint,
with a new timeline and invalidated old choices, routes and worker candidates.
Recovery restores in-memory machine state; files on disk keep their current
versions. A newer closed autosave is not rolled back or itself a reason to refuse rewind.
See [the method](INCREMENTAL_PLAY.md) and [package boundary](LEARNING_KIT.md).
The [conversation contract](CONVERSATIONAL_PLAY.md) and
[guide-assisted reconstruction](GUIDE_RECONSTRUCTION.md) define the current scene slice.

The independent engine/framework extraction remains the foundation. Preserve
game-specific experiments while building bounded reusable engine and movement
tools. Live gameplay integration and audio remain separate work.
The live integration gate remains the Codex/WebRTC
harness's existing Take over / Return control flow. Keep native input guards
separate from supported platform ownership observation and synchronization;
local transfer tests do not qualify that outer integration.

## Purpose

Let a person and Dot play an original DOS game together, visibly, in DOSBox-X
on Dot's own computer. The player should be able to participate without knowing
that a harness is required, handling debugger plumbing or waiting for a complete
reverse engineering effort. DotBox supplies that machinery and Dot operates it.
The planned public introduction is an r/Codex Showcase demonstrating this experience.

The graphical game remains authoritative. Z scenes provide a common action
and observation interface for descriptions, meaningful choices and control
selection. Dot can improvise the phrasing from grounded facts, with a deterministic
renderer as a fallback. Description detail, decision maker and assistance level
are independent preferences. A progress HUD remains optional.
The product does not need a replacement game, UDL-to-UIL conversion or UDC.

Dot must be able to construct and revise her own [internal game model](WORLD_MODEL.md):
typed entities, relationships, conditional rules, evidence, hypotheses and
task-specific abstractions. Z-scenes expose a relevant current view of that
larger model, combined with provider observations and action admission. Use a
local relational foundation for exact identities, state and dependencies, with
optional text/vector indexes for finding relevant knowledge. Predictive models
and simulations support planning without independently advancing game state.

## Preparing once, then learning during play

Precompute the complete supported static resource set when cheap and bounded,
then cache conditional world drafts. Incremental work applies to semantic
enrichment, live verification and controls; it does not require postponing a
whole-game bytecode scan until each room is visited. Complete world recovery
remains unnecessary for starting useful play.

On first boot without a compatible project, perform bounded operational
preparation: establish the executable/resource edition, connect the controls,
verify a useful movement or menu action and retain the smallest useful slice.
If an applicable control already works, start play without waiting for a named
scene or a complete buffer. The existing 180-second cold-preparation budget is
a ceiling, not a required wait. Measure it end to end, including agent work and
dispatch time. Missing current controls get a separate initial evaluation bound
of 15 seconds/two probe admissions; optional improvements must not delay a
working route. These settings need real player-flow measurements.

Include a bounded documentation pass: establish the broad goal and control
conventions, then collate two or three compatible guides when useful and available.
Their objects, exits and route dependencies become expected-scene checklists.
Current observations determine what can be described or offered now; guide
agreement does not establish current state. Index later material for retrieval
along the chosen route. Missing sources or incomplete checklists do not gate play.

Persist the results so later runs and compatible community packages skip control
rediscovery. Validate the relevant compatibility assumptions before reuse.
Measure both cold preparation and the path using an existing harness.

After preparation, add only what helps the next part of play. Unknown scenes
remain usable through established manual controls while better actions are
developed. Repeated pre-release trials should refine the preparation process;
full game recovery is not an admission requirement.

Use the player's normal traversal, necessary animations and decision time for
bounded predictive preparation. Workers can inspect frozen evidence and test
candidate scenes in their own isolated environments. A worker's useful-by point
is estimated arrival or the next consumer; its hard work bound is separate from
the lead's foreground learning allowance. Do not extend movement or narration
to cover missed preparation. Recheck the actual destination, state and revision
before adopting a result between actions. Existing usable movement and controls
take precedence over finishing a scene catalogue.

## Taking control and following progress

Integrate with Dot's computer's existing take-control / release-control flow.
First determine whether a supported tool or event exposes that state. Do not
assume the takeover UI implies programmatic state access. If no supported state
surface is available, document the gap and evaluate an explicit handoff within
DotBox; do not silently infer ownership from a lack of input.

One session controller serializes live input, pause/resume and probes. Handoff
must release held inputs and invalidate observations made stale by user play.
Dot can analyze frozen observations and prepare harness changes while the user
plays. Adopt updates between actions, after validating their starting conditions.
Live probing must have short, visible, bounded coordination points.

Keep the game available independently of a single agent tool call. Observe
progress while the user has control through supported frame/state capture and
an event journal, with explicit gaps when observation is unavailable.

The Z HUD distinguishes current observed context, last observed user action,
learned/available controls, harness coverage and work in progress. Harness
coverage is not a percentage of game completion. Observation gaps and stale
context must remain visible internally rather than becoming invented progress.

## Minimum useful understanding

Use the cheapest reliable source of operational state. For supported AGI
editions, prefer interpreter variables, objects, input and room state through
a small engine adapter. Use targeted native inspection where needed. Expose
frames, controls, bounded waits and checkpoints first; use memory reads,
watches, short traces and disassembly only to resolve a concrete operational need.
Helpers that change gameplay beyond ordinary inputs must identify that assistance.

An engine logic census supplies candidate flags, conditions, writers and readers;
it cannot infer current state merely from a script or guide. Compare repeated
baseline saves before a one-action save contrast, and use a qualified load to
check restored state and derived presentation. Save-format offsets and meanings
remain edition-specific. An emulator checkpoint and a game's own save cover
different state scopes. Memory revert does not restore older save-file bytes;
loading through the game's own menu reads the current disk file.

Movement must use the game's controls while monitoring appropriate debugger
x/y or equivalent observations. Plan with the actual collision footprint and
current hazards, favor fewer turns at equal distance, and keep long legs
interruptible without adding artificial stops. Crossing a room boundary is a
separate selected transition. Vehicle dynamics require their own controller;
a walking grid does not establish safe driving. Recovery must clear obsolete
input, fence old controllers and refresh game observations before further play.

Begin with an exact supported King's Quest or Police Quest edition. Use the
menu/choice-driven Dune adventure as a held-out non-AGI case; confirm the exact
edition before running it. Keep Dune-specific discoveries out of the initial
AGI development path so the later test measures generality.

## Shareable harness and compatibility notes

A package should contain game/resource identity, engine assumptions, scene and
action revisions, recognition and starting conditions, dependencies, coverage,
and small checks establishing operational outcomes.

Include minimal analysis that helps relocate the operational components in
nearby editions: named roles, address/signature anchors, data layouts, relevant
offset relationships, known differences and bounded validation recipes. Gather
only the facts needed for an action or adaptation; do not export a whole analysis
database or require full reverse engineering. Use hashes and authored structural
notes rather than copied original game code, messages or assets in public bundles.

A mostly matching edition is a candidate for adaptation, not permission to use
old addresses unchecked. Revalidate the affected controls/state reads and retain
both the original mapping and the adapted revision. Support small updates and
explicit conflict handling when users combine discoveries.

Prefer declarative recipes for community packages. Treat any optional native
or Python extension as executable code requiring its own trust decision.
Keep original game files, personal saves and private runtime evidence separate.

## Installation and runtime

Target Dot's own computer, including its visible desktop and built-in handoff.
Do not require the player to connect a separate personal computer or set up a
container or external cloud environment for this experience.
Dot-managed cloud worker tasks are allowed when the platform supplies them and
usage permits; their provisioning belongs to Dot. A worker's isolated guest
does not replace or gain control of the player's live session.

Tailor fDisBull's offline-package approach to a DOSBox-X-only payload. The planned
download venue is https://release.brewsterjennings.ca, independently of GitHub
or GitLab release-download availability. This brief does not claim a DotBox
package has been uploaded or qualified there.

Record the actual Dot runtime's OS, architecture, Python ABI, display/audio
support and relevant bundled package versions. Bundle missing or incompatible
dependencies and, where necessary, a compatible CPython. Do not assume an older
Python workaround or a QEMU dependency is required without testing the DOSBox-X
path. Retain dependency identities and required license/source notices.

## Existing evidence and secondary use

Prior King's Quest play, including reported advanced routes and glitch
experiments, is a reuse lead. Locate its existing project and records before
repeating substantial discovery. Preserve private originals and distinguish
observed artifacts from reported progress. Do not claim whole-game completion
or publish private game evidence on the basis of that report.

A secondary use is playing with Dot after Codex weekly usage is exhausted.
Validate observation, action, small harness updates and later reuse in Dot's
actual tool context without depending on a delegated Work/Codex task. This is
an acceptance question, not a promised usage-limit bypass.
