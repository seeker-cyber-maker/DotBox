# DotBox product brief

Status: design baseline, 14 November 2026. Requirements below are intended
behavior, not claims of implemented or measured DotBox capabilities.

## Current milestone — 16 November 2026

Finish the independent engine/framework extraction first. Reuse working fDisBull
components, own the native build recipe and storage, and verify a clean install
without fDisBull. Preserve game-specific experiments while deferring additional
gameplay and audio work. The first integration priority is the Codex/WebRTC
harness's existing Take over / Return control flow. Keep native input guards
separate from supported platform ownership observation and synchronization;
local transfer tests do not qualify that outer integration.

## Purpose

Let a person and Dot play an original DOS game together, visibly, in DOSBox-X
on Dot's own computer. The player should be able to participate without
handling debugger plumbing or waiting for a complete reverse engineering effort.
The planned public introduction is an r/Codex Showcase demonstrating this experience.

The graphical game remains authoritative. Z scenes provide a common action
and observation interface, with an optional text representation and progress HUD.
The product does not need a replacement game, UDL-to-UIL conversion or UDC.

## Preparing once, then learning during play

On first boot without a compatible project, perform bounded operational
preparation: establish the executable/resource edition, connect the controls,
verify movement or menu navigation, observe useful state and prepare a small
starting buffer of Z scenes and actions. A few minutes is the initial product
target; it must be measured end to end, including agent work and dispatch time.

Persist the results so later runs and compatible community packages skip control
rediscovery. Validate the relevant compatibility assumptions before reuse.
Measure both cold preparation and the path using an existing harness.

After preparation, add only what helps the next part of play. Unknown scenes
remain usable through established manual controls while better actions are
developed. Repeated pre-release trials should refine the preparation process;
full game recovery is not an admission requirement.

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
