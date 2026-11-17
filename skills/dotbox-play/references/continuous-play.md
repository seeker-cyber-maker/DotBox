# Continuous play with optional workers

Use this reference for the play lead and a worker preparing one harness slice.
Keep the game's immediate continuation ahead of speculative research.
The default path uses one play lead. Add a worker only when an available worker
can answer a specific question without delaying current play.
Player-led conversation waits for the player's scene decision when it is not
already known. Autonomous play chooses within the delegated goal. Both use the
same observation and action contracts; working controls do not decide agency.

## Retain the live owner

Reuse the established process/service and its supported client interface.
Determine the installed build's lifecycle before choosing a transport: a
persistent service may support short-lived clients, while a controller that owns
the guest through an open stream may close it on EOF. Do not transfer fDisBull
`z-controller` process rules to DotBox without checking the actual implementation.
Read the current runtime's help or documentation only when needed for that decision.

Keep session descriptors, ownership leases, games, saves, projects and output
stores in a private writable workspace outside Git ancestry. In cloud tasks,
`$HOME` may itself be inside a checkout. Ephemeral scratch storage is not a
durability guarantee. Preserve the private workspace through the environment's
supported persistence mechanism and verify the receipt before claiming reuse.
Retained controls do not necessarily retain the live guest or its game state.

Inspect takeover-state access once when establishing the runtime, and again
after a relevant change or failure. A visible button, chat owner or lack of input
is not an ownership API. If programmatic state is unavailable, keep that gap
explicit and use an agreed handoff. Never claim that a development service's
manual owner selection is integrated with the built-in desktop control channel.

## Keep the buffer useful

Store only a short frontier: current scene/action, immediate next likely need,
usable fallback, worker question and its bound. At startup this may cover a menu,
opening room and first exit. During play it follows the user's actual branch.
Do not create the frontier merely to name a control already usable now. Act,
observe its effect and save the recipe afterward without replay.

An operational slice connects entry/readiness, bounded input, observed effect
and a usable next state. Learn it from the authentic graphical game, retain the
small recipe and reuse it on the next visit. A scene plan, control label or
accepted input is not evidence of that complete slice. Share one relevant frame
or snapshot among compatible questions; avoid revisiting menus or redoing probes
just to give each worker a separate observation.

If an optimized action is pending, continue through its working input route.
If the next interaction is blocked, give it priority now: stop the unrelated
worker, learn the smallest missing input and publish a usable partial. Do not
pause the game to finish a broad harness plan. Save/checkpoint discovery is useful
when available, but must not gate otherwise working movement and interaction.

Use the entrypoint's recorded preparation budget and deadline (default 180 s).
Write them before launch/input. At readiness emit `buffer_usable`; on a miss emit
`budget_expired` once, retain the working subset and use an available route.
Never reset the deadline to make a long preparation look short. Record each
launch before process creation and distinguish installer/setup from the configured
game without dropping either from the end-to-end timeline. Capture actual waits,
failed actions and observation gaps as they happen, not at the final summary.

For a missing current control, use the separate `dotbox learn` focus: one goal,
observed context, question, next interaction and fallback. The default trial
bound is 15 seconds and two probe admissions, including elapsed reasoning and
dispatch time. Reopening or updating the same context keeps its deadline and
probe count. Retire work explicitly when a real route change supersedes it.
On exhaustion, use the applicable fallback or explain the game-facing block.
The helper cannot stop an already running tool or grant input permission.
Optional improvements with a working route add no intentional wait.

For persisted mouse controls, use [runtime controls](runtime-controls.md).
Coordinates are absolute original-frame pixels. In explicit native diagnostic
mode, the server handles the bounded pause/fresh-frame/click/continue transaction.
Default desktop mode uses its supported outer input path; native `act` is refused.
In either mode, do not keep the guest paused while
the model reads frames or writes recipes. Its returned coordination markers can
be joined to the caller's command journal. A continue response acknowledges a
command rather than the exact instant of guest resumption. Compare only the
same interval definitions across trials; candidate-marker time is not the
worker's full reasoning time, and a configured replay is not a cold run.

## Brief a worker with one near-term consumer

Supply only what the worker needs:

```text
Role/question: prepare the exit control for the next room.
Consumer/priority: play lead, after the current opening interaction.
Inputs: allowed frozen observation and revision, target/resource identity,
        relevant working controls, user clues and the observed input recipe.
Ownership/policy: no shared-guest mutation; selected assistance and information
                  policy; only the supplied evidence is player-visible.
Output: separate declarative candidate, entry/readiness, expected result,
        decisive evidence, tested scope, fallback and remaining unknowns.
Bound: one transition and a short explicit probe/time limit; return useful
       partials early and stop when superseded or the bound expires.
```

A worker normally analyzes frozen observations or prepares authored definitions.
An isolated guest is optional and requires actual support, authorized use and
separate mutable project, game/save directory and session. A copied emulator
checkpoint does not isolate host-mounted files. Without isolation, return one
bounded probe for the lead at a safe play boundary instead of taking over input.

Use the platform's available parallel workers; a task list alone does not create
a scheduler. Do not rely on a worker continuing after its cloud task ends.
Without parallelism, keep the same priorities and interleave brief authoring
steps with play. Do not create a new external environment just to parallelize.

## Promote a complete, compatible revision

Only the play lead publishes the active revision. Keep worker candidates separate
and preserve the last working revision. Check source/resource identity, current
applicability, assistance policy, parameter contracts and declared dependencies.
Retain a separately callable input fallback if an optimized implementation would
otherwise hide it. Select an immutable revision explicitly when the runtime
supports that contract; never assume an automatic latest selection.

Use the runtime's actual validation and promotion interface. Declaration checks
alone do not verify an effect. Validate the smallest applicable operation during
ordinary play or a safe bounded coordination point, then observe the result.
Do not replay a previously performed action merely to record its recipe. If
publication or execution fails after possible effects, inspect current state
before recovery; do not silently repeat a turn, submission or save overwrite.

Prefer declarative community controls. Optional executable extensions require a
separate trust decision, side-effect-free loading and a compatible runtime; do
not import unknown code into the live owner to discover what it does. Publish
between completed actions, preserving contracts used by existing routes. Defer
an inapplicable or breaking candidate and keep using the working revision.

## Yield and resume without undoing progress

Before a planned handoff, settle movement and release controller-owned holds
through the supported input path while the agent still owns input. On abrupt
ownership loss, do not inject cleanup during the user's turn; reconcile safely
after ownership returns. Frozen-evidence work can continue throughout user play.
Live observations must be supported and passive; if capture would advance or
pause the guest, retain an observation gap rather than interrupting play.

On a supported ownership return or explicit handback, observe the current game,
reconcile owned input state, refresh scene/runtime bindings and retire queued
intentions from the previous scene. Worker results from an earlier checkpoint
need current applicability checks. Never restore the user's old state just to
make a candidate fit. Separate harness coverage from observed game progression.

## Preserve blind information boundaries

The requested guide-informed path may read compatible guides for the overall
goal and nearby reconstruction checks. Keep those expectations separate from
current narration, and record guide exposure. The rules below apply to a strict
blind policy chosen for a session or evaluation; hiding read solutions from
spoken prose alone does not restore that policy.

For blind play, do not send the lead hidden units, future objectives, random
outcomes or spoiler labels through worker notes, scene names, readiness metadata
or logs. Give workers the allowed observation subset. Generic control mechanics
can be shared without target secrets; a worker that needs forbidden facts should
return a sanitized operational result or defer the action. An isolated future
scene does not authorize using its information in the current game.
If forbidden information has already reached the lead, record that exposure and
qualify subsequent blind-play claims; withholding it from the user does not undo
the lead's knowledge. Restrict further inputs and continue only within the agreed
information policy.

Keep the user-facing response about the current game and available actions.
Routine research belongs in the background dossier. A real block, consequential
choice or ownership question deserves a brief explicit handoff; unfinished
research should not become recurring progress chatter during otherwise usable play.
