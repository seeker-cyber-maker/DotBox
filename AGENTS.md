# DotBox contributor guidance

Read README.md and docs/PRODUCT.md before implementation. The repository remains a development project; do not describe planned behavior
as a working release. The current source priority is packaged, incremental
control learning and Dot as the game's conversational interface. Read
docs/CONVERSATIONAL_PLAY.md, docs/GUIDE_RECONSTRUCTION.md,
docs/INCREMENTAL_PLAY.md, docs/LEARNING_KIT.md and docs/STATEFUL_SCENES.md.
For engine state, movement or recovery, read docs/ENGINE_AWARE_PREPARATION.md,
docs/NAVIGATION.md and docs/RECOVERY_AND_SAVES.md. The packaged AGI V2 census and
walking planner are offline candidates; live observations, movement execution
and generation-fenced full-state restore remain separate integration gates.
Revert restores in-memory machine state, preserving current disk versions.
Do not implement a matching filesystem rollback or reject every changed autosave.
Read docs/AITD_REUSE.md before repeating movement/menu discovery: prior source
has been recovered, but its save-slot replacement policy is excluded from rewind.
The user's live acceptance goals are Police Quest's locker-to-shower controls
and late-briefing memory rewind. One ordinary-input functional controls run
passed on the cloud Linux computer; repeatable harness/timing qualification and
memory rewind remain open. Read docs/POLICE_QUEST_ACCEPTANCE.md for the measured
scope, edition-bound starting states and timer findings. Do not replace
guest-clock evidence with a host wait.
Build and test the offline
inspection kit, saved short frontier and installed play instructions while the
original-Dot ownership/input qualification remains a separate gate. DotBox must
own its required analysis dependencies without an fDisBull installation.
Preserve prior experiments; keep game-specific expansion and audio scoped to
their later milestones rather than making full-game recovery a prerequisite.
When available usage permits, Dot may spawn full cloud agents to prepare
candidate upcoming scenes. Prioritize selected graphical movement and use its
natural duration for predictive preparation. Read the play skill's continuous
play reference (`dotbox guide --topic lookahead`) for separate worker deadlines,
one foreground learning focus, isolated candidates and adoption on arrival.
Codex/WebRTC Take over / Return control belongs to the outer harness; do not
recreate its UI or label a native-only handoff as platform synchronization.

For cooperative play or a cloud worker extending the harness, read
[the DotBox play skill](skills/dotbox-play/SKILL.md), then only the reference
needed for the current task. It prioritizes a bounded opening buffer and the
next playable interaction. Read the files directly; this contribution does not
assume an installed skill-discovery command.

## Product boundaries

- Target visible DOSBox-X play on Dot's own computer and its takeover flow.
- Permit one-time bounded preparation, persist learned controls, and reuse
  compatible harnesses without repeating discovery.
- Keep the original graphical game authoritative. Z scenes supply the facts and
  choices for player-led conversation and autonomous play through one action model.
- A known control is used immediately only for a selected player intent or a
  delegated autonomous goal. Guide expectations support reconstruction; current
  narration requires current permitted observations. Keep detail, agency and
  assistance preferences independent.
- Build operational harness slices during play. Full game recovery, QEMU and
  the UDL/UIL/UDC conversion pipeline are outside the first release.
- Prefer interpreter state for supported engines; keep the named Dune case
  held out from initial engine-specific development and record prior exposure.
- Distinguish observed game progression from harness coverage.

## Evidence and implementation

Use supported runtime/control APIs. Verify takeover-state access before relying
on it. One controller owns live guest mutation; background work consumes frozen
observations and proposes updates. Preserve existing harness revisions and
private evidence. Verify current state before reusing prior benchmark claims.
Cloud workers may test their own isolated guests, with separate mutable files;
they cannot change the player's live state or active revision. Never slow
ordinary movement or pad narration to conceal unfinished preparation.

Keep original commercial game files, assets, saves, emulator states, private
analysis databases, raw memory dumps and credentials outside Git. Public harness
analysis should be small, authored and sufficient for operational adaptation.
Do not import target-derived material or code without reviewing its publication
scope and required license/attribution notices.

Make incremental changes and run proportionate checks. Validate the actual Dot
runtime before choosing Python versions or bundling dependencies. Do not infer
that fDisBull package qualification also qualifies DotBox or an untested host.

Read docs/REPOSITORIES.md before publication. Preserve both account repositories
and their independent histories. Do not force-push, install synchronization,
publish packages or create scheduled work merely to complete a coding slice.
For a local Mac build, read docs/LOCAL_MACOS_BUILD.md. Build helpers and authored
runner tests do not qualify macOS execution; the native gate must execute its
selected fixtures with no skips, and gameplay/rewind remain separate checks.
