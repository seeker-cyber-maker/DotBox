# Recovery, rewind and saved-game evidence

Decision: 17 November 2026. Dot should recover from getting stuck, dying or
crashing a car, then continue the selected playthrough with what it learned.
This document specifies the next integration. **DotBox does not yet expose a
qualified player-facing checkpoint or rewind operation.** The offline state
store and persistent controls do not restore a running game.

When the player chooses recovery, or delegates retries within an autonomous
goal, a qualified implementation should proceed within that intent without
another technical approval prompt. The remaining gate is implementation and
qualification on original Dot, including its existing ownership flow.

## Choose the right recovery unit

| Unit | Meaning and intended use |
| --- | --- |
| Game-created save | The game's loader restores a semantic play position. Useful for durable progress and discovering important state. Loading can rebuild derived values and reset transient state; this is not an exact machine/frame rewind. |
| Full native checkpoint | Compatible emulator machine state plus explicit input metadata and verified external-file scope. Useful before a risky interaction. Exactness applies only to the declared captured scope. |
| Frame timeline | A bounded sequence of full native checkpoints at completed renderer frames followed by safe CPU boundaries. Useful for recovering before a collision and retaining a failed attempt for analysis. |
| CPU delta, instruction trace or scene-store copy | Partial evidence/model state. None establishes full machine, device, host-file or game recovery. |

Label a recovery point with evidence that it precedes the failure and permits
useful input. The newest frame may already be inside an unavoidable crash.
Preserve the failed attempt, its input receipts and observations as immutable
history. Learned controls and the reason to try a different route survive;
inventory, flags, position and readiness must be observed again after restore.

## Learn state from saves, one change at a time

Game saves are a strong source of state hypotheses: the game deliberately
preserves values needed later. They are not a complete description of every
live variable. A loader may reconstruct derived values, and saves may omit
pending input, animations, timers or device state.

1. Bind the executable, edition and selected resources. Establish an observed
   baseline, save through the game's existing qualified control, and retain a
   private frozen copy after the write completes.
   Retain a repeated baseline save without an intended game action as a control
   for timestamps, counters and other save-time changes. Observe any autonomous
   progression during that interval; "no input" does not mean frozen game state.
2. Perform one meaningful action, such as taking a key or opening a window.
   Observe its actual effect, save again, and retain a second frozen copy.
3. Record identities and inspect bounded, aligned windows. For example, with
   an actual executable and two distinct save basenames:

   ```sh
   dotbox inspect identity /private/frozen/GAME.EXE --resource /private/frozen/before.sav --resource /private/frozen/after.sav
   dotbox inspect diff /private/frozen/before.sav /private/frozen/after.sav --length 64 --limit 16
   ```

   Choose a window within both files. The diff requires equally sized windows;
   it reads two independent files and supplies no atomic capture or causal
   interpretation. Identity's resource fingerprint covers the explicitly named
   evidence set here; retain the game's edition/resource binding separately.
   Compare logical offsets only when the container/layout makes them comparable;
   changed compression or record order may require a format decoder first.
4. Correlate changes with engine-aware hints. For AGI, logic references to
   variables, flags, inventory objects and room transitions are more useful
   starting points than disassembling the whole interpreter. A static reference
   or changed byte remains a hypothesis, not a current flag observation.
5. Using a qualified recovery path in an isolated experiment, load each save
   through the real game loader and observe the reconstructed state. Repeat a
   small contrast when needed. Separate counters, checksums, compression and
   incidental changes from the candidate meaning before promoting a binding.

Use the existing [inspection implementation](../src/dotbox/inspection.py) and
[stateful scene contract](STATEFUL_SCENES.md). Save comparison does not require
complete game reconstruction. Keep commercial saves, snapshots and raw evidence
private; published fixtures must be authored and small. Worker experiments use
their own guests and mutable files, never the player's mounted directory.

## Required restore transaction

The single live controller owns the complete operation, coordinated with the
supported outer Dot ownership flow. Background workers can suggest a recovery
point but cannot restore the player or publish their clone's facts as live.

1. **Preflight before effects.** Verify checkpoint bytes/hash, source, edition,
   selected resources, emulator build, runtime profile/load identity and file
   scope. Check current ownership, expected generation and the stopped safe
   point. Resolve unsupported or incompatible state before loading anything.
2. **Fence old work at native admission.** On the emulation thread, validate
   the expected control generation and advance it before uncertain restore
   effects. Preserve the current owner rather than restoring an old owner or
   lease from a snapshot. Clean held/queued keyboard and mouse input, including
   pending host events. Outer action checks alone cannot make this atomic.
3. **Restore the complete declared scope.** Reconstruct frame-key state only
   under an explicit policy. Exact TAS playback may require the saved keys;
   interactive recovery should use a neutral checkpoint or release restored
   keys as a separately recorded input before continuing. Old steering must
   never resume silently. Ambiguous or partial restoration ends in an
   incomplete stopped/closed state, with no automatic replay or resume.
4. **Establish a fresh timeline.** Assign a new restore epoch, provider context
   and `branch_id`; create a new `SceneStore`. Invalidate old selection tokens,
   routes, coordinate observations, pending actions and worker candidates.
   Retain the earlier branch as history without copying its reports into
   current facts. A restore epoch complements input generation fencing.
5. **Verify, observe, continue.** Check the native register/input result and
   obtain a newly completed frame plus a coherent provider observation.
   Historical screenshots are not fresh restored observations. Reevaluate
   action readiness and the selected goal, then continue through the qualified
   controller with a revised route or action.

Do not use `state_revision` as the ownership epoch: it changes on ordinary
keyboard/mouse mutations, execution transitions and even `state.save`.
Doing so would invalidate normal turns. A restore-specific identity and a
native generation bump are required.

## Existing seams and the extraction boundary

The following fDisBull references are package-relative paths in the studied
**0.34.1** offline package. They describe reusable behavior, not a requirement
for users to install fDisBull or proof of DotBox runtime qualification.

| Source seam | Existing behavior / integration requirement |
| --- | --- |
| `fdisbull/debugger.py`: `DebugSession.save_state`, `_capture_native_checkpoint`, `load_state`, `_restore_native_checkpoint` | Full native bytes, hash/compatibility checks, bounded mounted-file manifest, input/register verification, runtime-binding invalidation and close on partial restore. `disk_restore=False`; changed mounted files are refused. |
| `fdisbull/debug_timeline.py`: `FrameTimelineSessionMixin.timeline_start`, `timeline_advance`, `timeline_rewind`, `timeline_pin` | Bounded RAM history, frame input edges, explicit branching and durable pinning. Delta retention still captures full native state at each point. |
| `fdisbull/player_checkpoints.py`: `save`, `load`; `debug_experiments.py`: `save_experiment`, `restore_experiment` | Durable private slots, provenance, projection/binding checks and incomplete-state handling; useful for durable player recovery. |
| `fdisbull/runtime_observations.py`: `_invalidate_runtime_bindings`; `text_projection.py`: `TextProjectionHandle._read` | A new `_runtime_epoch` invalidates prior runtime bindings and participates in projection freshness tokens. |
| [Native state RPC patch](../native/dosbox-x/headless-agent.patch): `state.save`, `state.load` | Stopped-target serialization and frame-key sidecar exist. Raw `state.load` does not admit an expected control generation or advance DotBox's ownership generation. Do not expose it as a recovery shortcut. |
| [Native input control](../native/dotbox_input_control.h): `DotBoxInputControl::Transfer`; [input patch](../native/input-control.patch) | Generation checks, same-owner generation advance and input cleanup provide a seam for a new native restore transaction. Add a distinct advertised capability and exercise it under restore failures. |
| [Native session](../src/dotbox/native_session.py), [backend](../src/dotbox/backend.py), [service](../src/dotbox/service.py), [client](../src/dotbox/client.py) | Existing transport, single backend owner and cooperative outer turn checks. No public recovery API; service bridge identity currently uses run/session/generation/owner. Wire successful and failed restore invalidation through these layers. |
| [Scene store](../src/dotbox/scene_state.py): `SceneStore` | Existing branch/context binding rejects mixed histories; a restore must create a new store. Persistence of this store or control recipes is not native checkpoint persistence. |

The smallest executable recovery slice is one explicitly captured, verified
full checkpoint and one fenced restore through the controller, with fresh
observation afterward. Qualify this before adding a rolling frame buffer.
Authored isolated native tests can verify mechanics; they cannot substitute
for the original-Dot desktop/ownership qualification.

## Mutable files and capture cost

A native snapshot does not rewind mounted host files. fDisBull hashes the
mounted directory before/after capture and before restore, and rejects changed
files. DotBox must either keep that restriction or implement a separately
qualified, matching file snapshot with an explicit mutable-file scope. Never
combine old machine state with newer saves or worker output. Do not restore
unrelated host files. Immutable game resources and mutable saves need distinct
roles even when the game stores them together.

Bound retained frames, bytes, capture count, per-state size and wall time.
Measure pause, serialization, file hashing, compression and fresh-frame costs
on the intended runtime. Delta storage reduces retained bytes, not necessarily
capture time. Select sparse useful checkpoints before promising continuous
rewind; ordinary movement must not be extended to hide capture work.

## Acceptance cases for implementation

- Ordinary input advances state revisions without invalidating an unchanged
  ownership turn; a restore rejects all old-generation input and old choices.
- A held steering key cannot survive as an unowned or implicit resumed input.
  Explicit TAS restoration and neutral interactive recovery have tested receipts.
- Source/build/resource mismatch and changed external files fail before native
  load; a partial/unknown load cannot be retried or resumed automatically.
- Restoring after a simulated collision produces a new branch, fresh frame and
  verified playable state. The failed attempt remains immutable knowledge.
- Old inventory/door reports, routes and worker results cannot be presented as
  current; learned control recipes remain available after rechecking applicability.
- A save-file contrast yields only a candidate state meaning until real loader
  observations corroborate it. Derived and transient state remain distinguished.
- Capture/restore limits and measured latency cover the actual native path;
  authored offline checks and original-Dot integration results are reported
  separately. Recovery within an already selected intent needs no extra prompt.
