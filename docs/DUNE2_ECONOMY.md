# Dune II economy, construction and mission-one validation

Status: 19 November 2026. An original Dune II v1.0 run built a Windtrap and
Refinery, completed a full field-harvesting and refining cycle, exercised
separate Harvest and Return commands, and reached the original first-mission
success modal. The run then completed the result presentation, statistics and
local Hall of Fame entry, and reached the campaign's next-region selection map.
This is an authored operational knowledge slice backed by private
captures and original-code analysis. The [evidence receipt](evidence/dune2-economy-2026-11-19.json)
records provenance and the scope of each check. A subsequent separate slice
verified production Hold/Resume, bare-rock Windtrap placement, limited Repair
and ordinary same-process Save/Load. Its [repair and save/load receipt][next-checks]
keeps those tests distinct from the earlier complete-foundation mission win.

The public [RTS primitives](RTS_PRIMITIVES.md) remain generic contracts. This
contribution adds no public Dune II provider, memory reader, live input route or
desktop-ownership integration. The observed result covers Atreides mission one;
full-campaign completion is unqualified. Post-success presentation and campaign
progression are observed through that selection frontier. No next region was
selected and no second mission was started within this validation.

## Source and edition boundary

The original executable is identified by SHA-256
`d49f45729babd298fd72d0f623cc3cfaa4c3d144ab38e53f24355f2208b4e5a0`.
An executable hash anchors compatibility but does not identify every resource,
loaded overlay or runtime allocation. New installations still need their own
resource and mapping checks.

The semantic reference is OpenDUNE commit
[`ebea79aeba025be2fe9004570e9255044aacc0be`](https://github.com/OpenDUNE/OpenDUNE/tree/ebea79aeba025be2fe9004570e9255044aacc0be),
whose README requests version 1.07 data. Original instructions and coherent
captures established the v1.0 field meanings used here. A concrete difference
is the original 80-slot structure pool versus the reference's 82 slots; modern
structure layouts and pointer sizes cannot be transplanted. Original refining
also uses a fixed non-player multiplier where the reference varies it. This
study was informed by source analysis and earlier control research.

Public content contains authored facts and hashes. Original game files,
images, saves, RAM, disassembly and private analysis records remain excluded.
No OpenDUNE source code is copied into this contribution.

## Construction is a set of independent operations

The observed route uses construction-yard selection, catalogue interaction,
production, placement arming, target preview, placement submission and explicit
tutorial responses. The planner chooses each operation from current state;
these milestones do not become an unconditional input sequence.

| Milestone | Evidence needed before claiming it |
| --- | --- |
| Product selected | Current catalogue choice and producer identity |
| Production started | Allocated off-map product, producer link, busy state and changing countdown |
| Product ready | Countdown reaches zero and the producer reports ready; placement remains separate |
| Placement armed | Current placement mode and the coherent active product |
| Target preview ready | Intended tile agrees with stored and rendered preview positions and current validity |
| Building placed | On-map record, footprint occupancy and relevant house totals |
| Gameplay resumed | Current phase and input readiness after any tutorial or other event |

Independent review checked 52 frozen building/delivery captures, 520 memory
chunk receipts and 50 request/response pairs. Four concrete tiles supported the
Windtrap and six supported the Refinery. Their resulting HP/max HP were
200/200 and 450/450. The Windtrap produced 100 power; adding the Refinery left
production at 100, raised use to 30 and established storage of 1005. Those are
observed values for this original scenario. [Evidence receipt](evidence/dune2-economy-2026-11-19.json)
contains the review identity and milestone hashes.

### Placement needs a current preview position

A failed slab attempt exposed an original ordering rule: the PLACE click
handler calculates the new event tile but passes the stored preview position
to placement. A later hover invocation updates that stored position and its
validity. Moving and clicking together can therefore attempt the preceding
preview tile. Concrete placement revalidates the position it receives; this
is not merely a stale validity display.

The retained refusal left the intended tile unchanged. After the new preview
was observed, a separately chosen click succeeded. Original code corroborates
the argument source and return-before-hover ordering; the first call's arguments
were not captured in a breakpoint trace. Later Windtrap and Refinery placements
used matching current/rendered previews before their single placement clicks.

The provider requirement is a target-bound transaction: move the pointer with
no button held, allow a bounded original-loop update, observe the chosen tile's
preview, and then send one click. Keep the active product, camera, ownership,
frame, phase and observation identity coherent. A refusal remains a refusal;
it does not trigger an automatic second click. The reference has the same
ordering in [GUI_Widget_Viewport_Click][viewport].

### Modals and presentation can outlive a state change

Original tutorials appeared after placement had committed. In one concrete
event, a raw placement pointer still named its now-unused terrain-construction
slot while a nested tutorial suspended cleanup. Retain an aligned raw candidate
as an unused slot; do not manufacture an allocated structure from the pointer.
Later event completion cleared it. Invalid, misaligned or out-of-pool pointers
still require refusal.

Other captures show cleared placement pointers and enabled timer bits while a
tutorial remains visible, or rendered selection and building graphics lagging
the committed state. An old refusal banner also persisted after a later success.
Neither a pointer, timer bit, label nor single banner establishes current input
readiness. `respond_to_event` remains an explicit primitive, and confirmed
placement must survive a later presentation gap. Reference context: [gui.c][gui],
[viewport.c][viewport] and [structure.c][structure].

## Costs, foundations, power and storage

| Item in the tested opening | Cost | Footprint | Observed economic role |
| --- | ---: | --- | --- |
| Concrete slab | 5 | One tile | Four slabs for the Windtrap and six for the Refinery cost 50 in total |
| Windtrap | 300 | 2 by 2 | Full foundation; 100 power production |
| Refinery | 400 | 3 by 2 | Full foundation; 30 power use and 1005 current storage |

The reviewed ledger reconciles from the observed gameplay balance:
`999 - 50 - 300 - 400 - 1 = 248`. The additional one-credit debit is strongly
supported as maintenance by the original deadline/debit code and matching
before/after state; the exact debit instruction was not traced. The earlier
scenario allocation of 1000 is a different milestone.

Production spends credits incrementally with a fractional remainder. Original
code ties progress to producer HP and can put production on hold when credits
are insufficient. Do not infer a universal production-rate multiplier directly
from the power ratio. The current action, countdown, actual credits and hold
state are separate observations. The displayed credit counter animates toward
the ledger and can temporarily disagree with it. [Original evidence receipt](evidence/dune2-economy-2026-11-19.json);
reference [structure.c][structure] and [house.c][house].

Own concrete counts for placement adjacency. Original validation returns zero
for invalid placement and can return a negative missing-foundation count for
otherwise valid ordinary buildings. Bare-rock placement can therefore be legal
with reduced starting HP. A generic building adapter must interpret that
condition, rather than treating every negative result as rejection. The earlier
mission-winning run used complete foundations. The subsequent Windtrap test
below directly verifies a legal bare-rock placement and reduced initial HP;
other footprints and partial-foundation arrangements remain separate tests.
[structure.c][structure] provides the reference correlate.

Storage, actual credits, displayed credits and the scenario's initial
no-storage allowance have distinct roles. The observed capacity is scenario
state, not a promise about every Refinery or Silo in every edition.

## Further original checks: Hold, Repair and ordinary Save/Load

These checks cover one Windtrap in Atreides mission one, across two isolated
original processes. Hold/Resume was observed in the first process before its
later terminal timeout. Bare placement, Repair and Save/Load were observed in
the fresh sliced-wait process; no uncertain operation was replayed. The
[bounded-wait report](evidence/bounded-wait-2026-11-19.json) records that runtime
boundary. The [new evidence receipt][next-checks] records each test's scope.

### Hold and Resume have separately observed effects

The producer's Hold flag, production countdown and actual credits establish
whether production stopped. The product's own record is a different object.
The same production panel can offer Hold, Resume or placement according to
current state; it is not a fixed-action button.

| Observation | Producer countdown | Actual credits | Producer Hold |
| --- | ---: | ---: | --- |
| Hold accepted and observed | 11264 | 974 | On |
| After a separate 3,000 guest-ms observation, with 180 game ticks elapsed | 11264 | 974 | On |
| After an independently selected Resume and 2,000 guest-ms observation | 10496 | 956 | Off |

The countdown and credits changed while the initial Hold input was being
consumed, then remained stable during the independent held interval. This does
not establish instantaneous delivery or a universal production rate. Displayed
credits also lagged the ledger: the held capture's displayed-credit memory field
was 979 while actual credits were 974, and that field later caught up. These
last-completed frames are 1–15 guest ms older than stopped RAM, so sampled
displayed-credit fields need not equal the exact frame digits. [Test receipt][next-checks].

### Bare placement and a bounded repair

The separate preview selected a 2-by-2 Windtrap footprint with four missing
concrete cells and matching stored/rendered position. Original validity was
`-4`; one subsequent placement committed the building at **100/200 HP**, with
raw house power production **50**. Placement and the ensuing construction and
Windtrap tutorials were distinct events, each inspected before the next action.
One preview tile retained a partial-fog overlay despite its unveiled flag. The
successful original placement therefore does not qualify current-visible
admission for all four cells. [Test receipt][next-checks].

After the tutorials, a separately selected Repair action set both Repair and
Hold on the Windtrap. A bounded observation increased HP from **100 to 105** and
reduced actual credits from **699 to 685**. An independently selected repair-off
action cleared both flags. During a further **2,000 guest ms**, HP and credits
remained at 105 and 685. The displayed-credit memory field was still 694 after
the debit, illustrating why accounting needs the actual ledger.

Original instruction analysis explains the observed repair price. For positive
values in this tested case, its fixed-point calculation is:

```text
fraction = floor(10 * 256 / nominal_HP)
credits_per_step = floor((fraction * build_price + 128) / 256)
```

With nominal HP 200 and build price 300, the original result is **14 credits per
paid +5 HP step**. The pinned OpenDUNE [structure.c][structure] uses factor **2**
instead of the original **10**; its repair price cannot be substituted. A later
separate repair interval added 10 HP for 28 credits. Neither interval tested
full repair. The original strict-greater-than completion comparison and the
insufficient-credit branch remain source findings, not live qualifications.
Original analysis and executable hashes are pinned in the [test receipt][next-checks].

The visible Windtrap panel showed output **52** at 105 HP while the raw house
power field still read **50**. After the later interval it showed **57** at
115 HP, with the house field still 50. Ordinary loading subsequently restored
105 HP and the house field read **52**. Keep displayed output, building HP and
stored house totals separate; this test does not establish their general refresh
schedule. [Test receipt][next-checks].

### Ordinary Save/Load restores state and creates an observation boundary

The original Options menu, Save This Game entry, empty slot, description field
and Save confirmation were inspected as separate operations. Saving description
`r1` created a **3,884-byte** `_SAVE000.DAT`; its retained digest and description
anchor the tested file. Menu closure alone was not the success criterion.

The saved state had **105 HP**, **685 credits**, and Repair/Hold off. A deliberate
ordinary repair after saving changed it to **115 HP**, **657 credits**, with both
flags on. Selecting `r1` through the original Load A Game menu restored **105 HP**,
**685 credits**, and both flags off. A further independent observation reached
the completed gameplay frame with those restored facts. This is **same-process
ordinary game Save/Load**. Cross-process loading, other save formats and native
`state.load` remain unqualified. [Test receipt][next-checks]; reference context:
[save.c][save] and [load.c][load].

The initial load capture already held the restored ledger but still reported
displayed credits **65535** and timer mask 1. That displayed value was a transition
sentinel, not spendable funds or a victory balance. The later completed capture
reported actual/displayed credits 685 and timer mask 3. A timer bit or credit
counter alone does not establish current input readiness.

Loading did not rewind the native or game clocks. At the initial restored
capture, the game clock was 2290 and the scenario-start value became 98,
retaining the saved elapsed mission time of **2192**. The reference's
[scenario-time serialization][save-info] offers a correlate; byte-identical
memory or a rewound runtime clock is not the acceptance condition.

Treat the load as a new observation boundary: discard old object keys, selection
intents, targets and placement previews, then inspect fresh rendering and state
before choosing another action. The test records this boundary explicitly. The
sliced-run reader still reports entity candidates, current visibility false and
action admission false; these results install no public Dune II provider.

## Harvester commands and the observed economy loop

The original Harvester action list is Harvest, Move, Return and Stop. Harvest
and Move arm target selection. Return and Stop issue unit commands without a
second target click; completion can still be deferred by movement or scripts.
Original Harvest targeting uses the fresh clicked tile, unlike building
placement's stored-preview argument. Reference: [actioninfo.c][actions],
[widget_click.c][widget] and [viewport.c][viewport].

The run established these separate outcomes:

| Observation | Result and scope |
| --- | --- |
| Refinery placed | Original game allocated and delivered a Harvester without a separate purchase input |
| Starter cargo processed | One preloaded cargo unit produced 7 credits, then the Harvester deployed; this alone was not field collection |
| First field cycle | Cargo reached 100, automatically returned, entered the Refinery, unloaded to zero and redeployed |
| Full-load accounting | Credits rose 255 to 955 and the allied processed-spice statistic rose 7 to 707: exactly 700 for 100 cargo |
| Explicit Harvest | Selecting Harvest armed its target mode; a separate choice of a currently visible field led to 10 cargo |
| Explicit Return | One Return command produced return travel and Refinery entry with that partial load; no target-click sequence followed |
| Result | The original first-mission success modal appeared with actual/displayed credits 1005, cargo zero and processed-spice statistic 777 |
| Campaign continuation | Explicit result responses led through statistics and local score entry to the next-region selection map; the campaign index advanced from 0 to 1 |

The explicit partial load began at 954 credits. Six cargo units unloaded while
actual credits reached 996 and displayed credits still read 977. Processing the
remaining four brought the processed statistic from 749 to 777 and the ledger
to its observed 1005 storage cap. A nominal 70-credit ten-unit load and a
51-credit balance increase are consistent with 19 credits clipped by that cap;
the cap's exact write was not traced. Do not replace observed accounting with
an assumed `cargo * 7` net balance change. Reference: [RefineSpice][script-structure]
and [house.c][house].

The raw flag called `inTransport` has an overloaded meaning. Original harvesting
itself sets the flag while the unit remains on the map and cargo increases.
It cannot alone prove Carryall occupancy. Physical carrying or Refinery entry
needs coherent links, on-map status and the relevant carrier/building state.
Likewise, action ID Harvest alone does not prove collection; current terrain
and cargo growth matter. Reference: [Script_Unit_Harvest][script-unit].

### Automatic search and player knowledge

The original automatic spice-search helper checks terrain, bounds and occupancy
without a player-visibility filter. Its existence does not expose hidden spice
coordinates to the player. Keep the engine's autonomous choice separate from
explicit targeting based on current permitted observations.

Camera movement changes the view; controlled-unit movement supplies scouting
and terrain reveal. A selected Harvest target must be a player-observed field.
The automatic player search radius/retry cadence and complete EMC script flow
are not recovered by this slice. In particular, the reference's radius-20 AI
Carryall branch is not a general player search rule. References:
[Script_General_SearchSpice][script-general], [Map_SearchSpice][map] and
[Unit_RemoveFog][unit].

## Identity and visibility findings for the world adapter

**A slot is not an entity lifetime.** Reviewed captures show one unit slot
holding an opposing Soldier, then explicitly unused, then an owned Harvester.
This establishes actual slot reuse without assigning a cause or attacker to
the earlier unit's disappearance. Selection, logical-group membership and
pending commands need a qualified incarnation or observation-local identity.
This applies the existing [RTS identity contract](RTS_PRIMITIVES.md) and
[reused-storage guidance](REVERSE_ENGINEERING.md).

**The earlier private candidate projection had a confirmed omission.** Its conservative
requirement of an unveiled tile with overlay zero omitted moving own units
that were visibly rendered over nonzero sand-track overlays. Original rendering
analysis confirms that such background overlays can coexist with visible ground
unit sprites. An independent unchanged-reader replay reproduced the omission.

The next test slice qualified a narrow private correction against the frozen
original captures. It retains the old clear-tile diagnostic rows and adds own,
allocated, on-map ground-unit candidates on verified sand-track overlays, with
exact occupancy, matching requested/rendered cameras and the existing viewport
limits. Original renderer hashes and the tactical icon table guard the extension.
Unknown non-fog overlays do not gain this extension. The conservative fog band
remains excluded. Reference [Tile_IsUnveiled][sprites], [Map_IsPositionUnveiled][map] and
[GUI_Widget_Viewport_Draw][viewport] inform that correction; the original and
reference unit-loop bounds differ.

The same screenshot-derived positive regression fails on the unchanged reader
and passes on the candidate, adding exactly the two witnessed own units in the
original scouting capture. Fifty offline checks and replay of all 113 retained
captures passed; an independent review also checked four additional pointer/debug
negatives. All 111 existing saved world outputs were reproduced by the unchanged
reader, and the candidate removed no legacy rows. Two historical decoder refusals
have no saved world output and are retained as such. See the
[qualification receipt](evidence/dune2-observation-qualification-2026-11-19.json).

This correction does not establish current visibility. The old reader had no
qualified phase, frame-relationship or durable entity-lifetime gate to preserve;
those remain missing. Eight result/map captures retain world rows after tactical
icon resources have changed, and the extension disables itself there. A success
modal can still retain matching tactical resources. Resource checks alone are
therefore insufficient. The candidate explicitly reports current visibility and
action admission as false. Its consumer must retain those qualifications and
call the list entity candidates, without a visible-entities alias.

The correction and raw regression fixtures remain private diagnostic material;
this public guide does not install a Dune II reader or provider. Do not treat
projection omission as absence, promote retained modal rows to current game
objects, or broaden action admission from a screenshot alone. The public
projector continues to consume provider-asserted visibility. See the
[world model](WORLD_MODEL.md).

## Result and remaining qualification

The visible original success modal establishes mission-one success. The source
also explains why a quota-like credit number alone was insufficient: original
mission checks have an elapsed-game-time gate and periodic evaluation, and the
quota predicate consumes displayed credits. No tick-rate conversion or win
flag is inferred from a timeout. The private decoder continues to report an
unknown visible-win result; the frame/event witness supplies the success claim.
Reference: [opendune.c][game].

The result presentation was acknowledged explicitly. Proceed opened the results
and advanced the campaign index from 0 to 1. The completed original statistics
show score 89, game-reported time 7 minutes, rank Desert Mongoose, spice totals
777 versus 0, and units destroyed 3 versus 0. These aggregate statistics do not
identify the cause or attacker behind a particular earlier disappearance, and
the game-reported time is not a cold-start or harness-performance measurement.
After local Hall of Fame entry and Resume Game, bounded observation of the
campaign narration reached the next-region selection prompt. The final frontier
is ready for a future region choice; it does not establish that another mission
has begun. Exact success, statistics and campaign-map screenshot hashes are
retained in the [evidence receipt](evidence/dune2-economy-2026-11-19.json).

Building review, later accounting checks, original-source findings and visible
result inspection have separate evidence scopes in the receipt. Full campaign
play, other houses/missions, broad combat/NPC behavior, automatic script recovery,
current-visibility qualification, reusable provider integration and original-Dot
ownership qualification remain separate work. The next adapter should preserve
independent primitives, current observation fences and explicit event responses
while reusing these learned conditions.

[viewport]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/gui/viewport.c
[widget]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/gui/widget_click.c
[gui]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/gui/gui.c
[actions]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/table/actioninfo.c
[structure]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/structure.c
[house]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/house.c
[unit]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/unit.c
[script-structure]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/script/structure.c
[script-unit]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/script/unit.c
[script-general]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/script/general.c
[map]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/map.c
[sprites]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/sprites.c
[game]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/opendune.c

[next-checks]: evidence/dune2-repair-save-load-2026-11-19.json
[save]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/save.c
[load]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/load.c
[save-info]: https://github.com/OpenDUNE/OpenDUNE/blob/ebea79aeba025be2fe9004570e9255044aacc0be/src/saveload/info.c
