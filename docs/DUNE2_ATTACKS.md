# Dune II enemy attacks and controlled hazards

This continues the [economy and campaign work](DUNE2_ECONOMY.md) with the original
Dune II v1.0 executable. The completed enemy encounter demonstrates a reactive
defense: the scout returned fire, withdrew, and joined two fresh defenders with
all seven own units still allocated. It does not demonstrate a pre-damage alert.
The controlled worm run now establishes a dangerous encounter and an earlier,
uncertain visual hazard cue. A completed evacuation remains the next test.

## Original enemy encounter

The unchanged mission-two save started with a 130-HP Quad, three 100-HP Trikes,
three 20-HP Soldiers, and a 400-HP Construction Yard. Root scouted through the
original interface, observed Ordos ground units, selected Attack, selected a
target, then chose Retreat and rallied two defenders through separate actions.

| Milestone | Observed result |
| --- | --- |
| Last intact scout sample | 130 HP at guest 62,205 ms |
| First captured harm | 128 HP at 67,205 ms; onset lies in (62,205, 67,205] |
| Later explicit recognition | Root reported ground contact and damage at 69,505 ms |
| Return fire | Selected Raider fell from 80 to 66 HP |
| Retreat decision | Quad had 109 HP before the order |
| Withdrawal | Quad then sampled at 104, 98, and 74 HP |
| Recovered formation | Quad guarding at 74 HP beside two Trikes at 100 HP |
| Stable HP window | 17.7 guest seconds from the first 74-HP sample through final Guard |
| Other own assets | All six other units retained baseline HP; Yard retained 400 HP |

The earlier captured hit was found during independent review. The later moment
when root noticed the enemies must not be backdated into an early warning.
The combat audit contains hostile and friendly bullets and correlated attack
targets, but does not assign each hit to a particular projectile. One enemy
Trooper still retained a Quad-correlated target at the final fence. This supports
a recovered scout and a bounded interval without further sampled HP loss;
it does not establish permanent safety or defeat of the enemy force.

### Preserve independent actions

An accepted input is not yet an observed game effect. The Attack-selection click
was followed by 100 guest ms, at which point the original UI still had ordinary
unit selection. A separate 200-ms observation, with no repeated click, established
target selection. Only then was the target point selected. Retreat, camera
movement, each defender selection, each Move selection and destination, and the
final Guard command were likewise separate, freshly observed primitives.

The two defenders were ordered individually. This is not a claim of native
multi-unit selection or a drag-selection capability in the original game.
The [generic RTS contracts](RTS_PRIMITIVES.md) retain their existing visibility,
commandability, phase, and observation-fence requirements.

## A worm needs a different harm model

Pinned OpenDUNE is a useful research map; original executable evidence remains
authoritative. The original version differs in a way that matters here:

- Its discovery path checks alliance before the worm-warning branch. A natural
  Fremen worm is allied with Atreides for that check, so this warning path is
  suppressed.
- Its worm script uses a different owner comparison and can still target an
  Atreides unit. The warning classification does not establish safety.
- The original swallow path removes/frees the victim before the swallow effect
  and sound. The freed record can retain positive HP. An HP-only monitor can
  therefore miss the loss.
- The special worm renderer supports a possible pre-contact surface cue when
  its terrain/viewport predicates pass. Hidden coordinates or a source rendering
  candidate do not establish that a screenshot actually contains that cue.

The original scenario-two setup has no authored worm. The controlled experiment
uses a separate copy with one added, original-style Fremen worm record. The
preserved ordinary m2 save and all 21 original resource files remain unchanged.
Original Load restores the save; a separately selected original Restart is
required to construct the added scenario unit. Restart also enters the original
Mentat briefing, whose messages and Proceed button require their own observations.

## Observation and scoring contract

Keep three channels separate:

| Channel | Role |
| --- | --- |
| Screenshot-only observer | Identify actual visible cues without RAM, hidden coordinates, or fixture details |
| Private own-status/source-state observer | Audit explicitly enrolled own slots and the current source UI text state |
| Experiment and unrestricted audit | Verify the authored trigger and explain later behavior; never supply hidden warning features |

The private read-only observer validates stopped capture context, neutral input,
ten contiguous RAM receipts, frame/RAM identities, and original source guards.
It records HP changes, observed slot release, and identity invalidation. Allocated
off-map units are not declared dead, and changed identities are not assigned a
cause. A fresh enrollment and declared boundary are required after Load/Restart.
Unobserved same-signature reuse remains a sampling limitation.

Source-active viewport text is a diagnostic, not proof of delivered text or audio.
The observer excludes stale modal buffers, historical hint bits, speech queues,
hidden enemy records, and fixture coordinates from warning decisions. Its
delivered-warning, pre-harm-warning, current-visibility, and action-admission
fields remain false. It performs no response input.

A pre-harm result requires an actual recognized visible cue and the watched own
unit still intact at the same stopped fence, followed by later harm in a
no-response control or a separately demonstrated dangerous control. Record the
warning at actual observer/root receipt time; do not backdate it to an older
PNG. With sampled evidence, report intervals rather than an invented exact hit
or swallow timestamp. Model evaluation while the guest is paused does not
establish continuous real-time performance.

## Controlled worm loss and earlier visual cue

The exact loose scenario override was activated through original Restart.
A fresh tactical enrollment contained all seven own units at full HP and the
400-HP Yard. The screenshot-only observer found no danger in the hidden-start
frame. The root-selected no-response control then audited own status and source
text every 50 guest ms; initial endpoint image reviews occurred every 500 ms.

| Control milestone | Observed result |
| --- | --- |
| Tactical enrollment | Guest 25,207 ms, revision 49 |
| First recognized candidate cue | Sample 90, stopped at 29,707 ms, revision 139; all own assets intact |
| Original visual confidence | New curved/speckled sand patch; possible environmental hazard, identity uncertain |
| Last intact Trike sample | Sample 155, 32,957 ms, revision 204; used/allocated, 100 HP |
| First recorded release | Sample 156, 33,007 ms, revision 205; unused/unallocated, residual 100 HP |
| Candidate-to-release lead | More than 3,250 and at most 3,300 guest ms |
| Other assets at release | Six units and Yard retained full HP and allocation |
| Later visible effect | Separate 250-ms observation showed a mouth-like effect replacing the Trike sprite |

The first loss is bounded to `(32,957, 33,007]` guest ms. The sample-156 PNG was
2 ms older than stopped RAM and byte-identical to sample 155's PNG: the unit
still appeared in that image after its allocation had been released. Neither
an older sprite nor positive HP in freed storage establishes continued survival.

The separate unrestricted audit attributes this release to the original worm
swallow path: the victim's script marker changes, the worm's remaining-swallow
count decreases, its target clears, and the post-swallow delay appears. This is
more specific evidence than an unattributed HP change or an omitted scene entity.

That audit also supports the earlier patch as a worm-rendered cue. The relevant
pixels were unchanged through sample 88, changed at sample 89, and persisted in
sample 90. All sampled map fog/unveiled fields stayed unchanged, while the worm
entered its source renderer's unveiled gate. This is strong post-hoc attribution,
not a recovered per-pixel draw receipt. The actual live recognition remains
sample 90, with its original uncertainty; it must not be backdated to sample 89
or relabeled as confirmed worm classification at recognition.

All 157 enrollment/control source-text samples had an inactive counter and no
signal. This does not establish that no audio occurred between captures. The
control used 7,800 guest ms and 547 completed frames. After the candidate warning
was recorded, a prospective decision at sample 140 permitted up to 2,500 guest ms
between endpoint image reviews while retaining the 50-ms own/source checks;
only 800 guest ms elapsed before the first loss stopped the helper.

### Response frontier and retained failures

A separately selected original Restart restored all seven units. At 5,000 guest
ms after its fresh enrollment, the image-only observer recognized a new patch
resembling the earlier cue, again with no observed own harm. Root selected the
visible Trike through the original UI. The next Move request failed before input:
root supplied `selected_unit_index` in `require_controls`, but that helper checks
fields of `economy_controls`, where this field is absent. The runner terminated
and exited cleanly. No Move, evacuation, or prevention result is established by
this attempt. The correction is to use the supported guard fields and inspect
selection separately under the existing exact-head/frame checks.

Earlier retained failures include an unsupported uppercase key token at the
logo, loss of access to a paused process before Restart, and an invalid batch
request-name prefix rejected before execution. The batch filename fix passed
four focused offline tests against the actual runner grammar and subsequently
completed the 156-sample live control. A later orchestration reset preserved the
native process; the journal and queue were inspected before continuing without
replaying a request or resetting the trial budget.

A source interpretation was also corrected: the observed Area Guard entry path
does execute the original startup delay. Original branch/callback evidence and
the live countdown establish that behavior. The 120 argument becomes 24
scheduler countdown visits in that callback; it is not a universal 120-ms grace
period or permission to defer observation.

The ordinary m2 recovery save and all 21 original resources remain unchanged.
A fresh process will repeat the response test with the corrected caller. No
uncertain request is replayed in a consumed epoch, and native saved-state
restoration remains outside this qualification.

### Learning for the RTS model

Keep affiliation, danger, command permission, and lifecycle separate. This
natural-owner worm can bypass an alliance-based warning path while still
swallowing an own unit. A visible but uncertain environmental cue can justify a
selected cautionary move of a currently commandable own unit; the cue does not
need to be promoted into a confirmed enemy identity. Selection, choosing Move,
and choosing a destination remain separate observed actions. An external own
lifecycle audit can detect a release, but it does not turn hidden coordinates
into a player-visible warning or automatically identify the cause.

## Evidence and validation

The authored, non-binary receipt is
[dune2-attacks-2026-11-19.json](evidence/dune2-attacks-2026-11-19.json).
Private RAM, screenshots, saves, commercial resources, authored scenario fixture,
and disassembly stay outside Git. Private reports are identified by hashes in
the receipt.

Independent enemy review checked 37 frozen captures and replayed the own-status
observer over 36 subsequent samples. It found six HP-decrease events, all on the
Quad, and no own-slot release. All 21 original resource identities and m2 still
matched. The private threat observer's 15 focused offline tests independently
passed. The completed control independently verified all 156 response/audit pairs
and their capture chains. It supports a tentative visible pre-harm hazard cue
and a source-attributed worm loss. These results do not qualify confirmed worm
classification at recognition, successful evacuation, a public automatic threat
provider, continuous unpaused reaction, or a new campaign victory.
