# Dune II enemy attacks and controlled hazards

This continues the [economy and campaign work](DUNE2_ECONOMY.md) with the original
Dune II v1.0 executable. The completed enemy encounter demonstrates a reactive
defense: the scout returned fire, withdrew, and joined two fresh defenders with
all seven own units still allocated. It does not demonstrate a pre-damage alert.
The separate worm experiment is in progress at this checkpoint.

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

## Current worm frontier and retained failures

The exact loose scenario override has been verified through original Restart:
one Fremen Sandworm was constructed, and a fresh tactical sample contained all
seven own units at their original full HP. An independent screenshot-only
observer reported no visible danger in that hidden-start frame. Hidden presence
is not a successful detection.

The first batch attempt then exposed a private client/runner interface error:
the batch generated a nonnumeric request-name prefix, while the existing runner
requires a numeric prefix. The runner closed and reaped cleanly before executing
that request. The batch journal correctly retained its pending reservation.
The helper's earlier static review missed this cross-file contract; compatibility
is not qualified by that review. The corrected helper now emits a numeric prefix. Four focused offline tests
against the actual runner grammar independently passed; the corrected live batch
is still pending at this checkpoint.

Earlier attempts also retain an unsupported uppercase key token rejected at the
logo, and loss of access to a paused process before Restart. Neither is a worm
outcome. The original m2 save remains the recovery source. No uncertain request
is replayed in a consumed epoch, and no native saved-state restore is qualified.

Next: run the corrected short-cadence no-response control, then restart into a
fresh response trial. Publish actual visible-warning, first-harm, and evacuation
outcomes separately, including failures.

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
passed. These results do not qualify a public automatic Dune II threat provider,
a worm early-warning result, or a new campaign victory.
