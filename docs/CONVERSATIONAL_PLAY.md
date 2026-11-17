# Dot as the game's conversational interface

Decision: 17 November 2026. DotBox supports autonomous play and makes Dot the
player's conversational interface to an original game. In the latter mode, Dot
describes the current situation, offers useful choices and carries out the
player's intent. The original game still determines state and outcomes.

The user named [The Magic Door](https://www.themagicdoor.org/) as an interaction
reference. Its official description presents an Alexa adventure in which the
listener chooses what to do. DotBox applies that conversational pattern to an
existing graphical or text game. This is a design reference, not an integration
with that product or a claim that DotBox already has a live voice frontend.

## One scene model, two decision makers

Both player-led and autonomous play use the same observations, scene facts,
choices, control references and outcome checks. In player-led mode, Dot offers
choices and waits for the player's intent. In autonomous mode, Dot selects the
next useful action within the delegated goal. A known control alone does not
authorize Dot to make the player's game decision.

Keep three preferences separate:

| Preference | Changes | Does not establish |
| --- | --- | --- |
| Decision maker: player-led or autonomous | Who selects the next action; a delegated route can be bounded | Input ownership or permission to ignore a new player instruction |
| Description: brief, normal or detailed | Wording, pacing and amount of grounded detail | Additional objects, hidden contents, exits or successful outcomes |
| Assistance: discovery, hints on request or walkthrough | Which guide-derived help may be disclosed and used to advise choices | Evidence that a guide describes the current save state |

The requested initial guide pass is guide-informed play. A player can receive
spoiler-light narration even when Dot has read guides, but that is not a blind
agent run. A future strict blind trial must restrict the lead's inputs before
exposure. Do not turn these preferences into repeated setup questions: honor
the existing session preference, infer an ordinary conversational default and
ask only when a meaningful game choice or an ambiguous request needs it.

Autonomy can be local: "Get us back to the lobby" delegates that route, while
"Let me choose the rooms" retains scene decisions. Description length does not
change that delegation. An interruption or takeover cancels a queued input
intention; the high-level goal can be retained for fresh interpretation later.

## The conversation loop

1. Observe the current game and preserve the current observation identity.
2. Describe the relevant known facts and offer a small useful choice set.
3. Resolve the player's words, or the autonomous planner's choice, to an intent.
4. Check the current state and supported input owner, then perform one bounded
   action through the existing control path.
5. Observe its actual effect and describe the change. Save useful metadata
   without repeating input. Extend only the next needed scene fact or control.

When the player has already expressed an unambiguous intent and the control is
applicable, act without an extra menu or confirmation. Offered choices are
suggestions, not an exhaustive grammar. "Open it" needs clarification or a fresh
observation when the intended current target is not uniquely identifiable.
A novel request can become the next
bounded investigation; it must not be invented as an already working action.

Distinguish conversational inspection from game input. "Describe the barrel in
more detail" can use facts already observed. "Look inside the barrel" may be a
new game action whose result is still unknown. Do not expose hidden contents
because a guide mentions them. "Try the key in the door" can be a valid bounded
attempt; its wording must not promise that the door will unlock.

The game may continue while the player speaks or considers a choice. This
document does not introduce an automatic pause. Before acting on an earlier
menu, refresh any state made stale by time, animation, a transition or takeover.
Real-time gameplay and voice timing require separate measurement.

## Ground the meaning; let Dot phrase it

The Z-scene supplies a compact account of facts and available actions. Dot can
choose natural wording, emphasis and pacing from that account. A deterministic
renderer provides a fallback and a testable reference. It does not need to
script every sentence that Dot can say.

The player view carries permitted fact IDs and stable choice IDs. Dot's prose
may combine or shorten supplied facts, but must not introduce a new actionable
noun, sound, condition, exit, consequence or success. Rich narration should
make known facts easier to imagine, without turning invented atmosphere into
false game affordances. More description does not silently enable hints.

The initial renderer returns `narration` for the scene and a separate
`choice_prompt` built from a short suggested list. The complete eligible
choice list remains available for free-form requests or "what else?". Dot may
rephrase these fields naturally while preserving their facts and action IDs.
Compose a reply from the permitted facts and choices as well as the suggested
text; a brief narration can omit a known detail that matters to the current
question. Do not treat the narration string alone as the complete scene model.

Illustrative authored examples, not verified maps of commercial games:

| Scene | Grounded conversational rendering |
| --- | --- |
| A visible closed mailbox and a usable opening control | "There is a closed mailbox here. Would you like me to open it?" |
| A station lobby with a visible radio, key and two observed doorways | "A radio is on the table and a key hangs on the wall. We can inspect the radio, take the key, or use one of the doorways." |
| A visible barrel with usable inspection input | "There is a barrel in the room. Would you like me to look inside?" |

These choices require known current input routes. If the barrel's contents have
not been observed, no description mode can include them. If a third station
doorway appears only in a guide, it belongs in the internal checklist until
verified. A previously unseen but currently observed object is still usable
even when every guide omitted it.

## Two views of one incomplete scene

The player view answers: what can be described now, and which useful actions
are currently available? The internal reconstruction view answers: what did
the guides lead us to expect, what matches, and what remains uncertain?

For the station example, two or three sources might mention a key, radio and
three doors. Dot can create five expected-object checks, then match four to the
current observation. The third doorway remains a local search lead. Its
destination is a separate fact that may need an actual transition or reliable
engine observation. Seeing a door does not establish where it leads.

This checklist does not need to be complete before play proceeds. If the player
chooses the radio and that route works, use it. Seek the third doorway only when
it matters to the current choice or a cheap observation reveals it. Counts are
coverage of the selected expectations, never a percentage of game completion.

See [guide-assisted reconstruction](GUIDE_RECONSTRUCTION.md) for the initial
documentation pass, source conflicts, conditional claims and the game goal.

## Current offline contract

The initial `dotbox-scene-1` document describes one bounded observation context.
It is an authored adapter contract, not a complete game model or a new parser
for Z-machine story files. Existing fDisBull scene experiments were not imported
or qualified by this slice.

| Section | Contract |
| --- | --- |
| Identity | Executable SHA-256, edition, optional fingerprint of explicitly selected resources, scene ID and observation ID |
| Current facts | Stable ID, subject/predicate/value, player text, optional detail, audience, observation ID and evidence reference |
| Choices | Stable ID, label, required fact IDs, observation ID, availability assertion and an existing control or ordinary-input-route reference |
| Guide sources | Source reference, edition and origin group; copied guides can share a group |
| Guide claims | Subject/predicate/value, short summary, source ID and any unresolved condition |

Source/context, semantic observations, audience classification and input-route
availability are caller assertions. Hashes preserve document identity; the
compiler does not recognize the scene from pixels or verify those assertions.
Unknown data stays unknown. Omitting an object from a partial frame does not
establish that it is absent. Explicit negative facts must state their actual
scope, such as absence from a checked inventory rather than the whole world.

The player projection excludes guide claims, internal facts, stale facts and
choices whose current requirements are unmet. Detail modes use the same
permitted facts and choices. The internal checklist retains matching,
unresolved, conflicting, conditional and edition-inapplicable expectations.
Condition text is retained as unchecked in this first version; no condition
evaluator or automatic guide extraction is implied.

Selecting a choice returns a non-executing intent bound to the scene document
hash and observation ID. A changed document/context requires a refreshed
selection. This check cannot discover that a caller supplied an old observation
as current; the later executor must recheck live applicability and ownership.
Existing default desktop mode still refuses native `act` and other input RPCs.

The module does not implement natural-language intent resolution, speech, game
input, scene recognition, a goal planner or a global world graph. Dot supplies
the language/planning behavior; subsequent adapters connect the scene intent
to the qualified execution path. Overall goal and session preferences belong
in the small game/session brief, rather than being inferred from presentation
detail or guide vote counts.

## Acceptance

Use authored mailbox, station and barrel records first. Verify that guide-only
objects never enter current narration, incomplete coverage preserves usable
actions, verbosity preserves the permitted choices, and stale selections are
refused. Verify the actually installed package, including the examples and
topic guide. Then separately test the real conversation/action/observation loop
and measure player-visible delay. An offline prose rendering is not evidence
of voice integration or autonomous game completion.
