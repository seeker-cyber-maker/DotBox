# Behavioral hypotheses and alternative entry points

Decision: 18 November 2026. Use an agent's programming knowledge to propose how
observed behavior could be implemented, then seek evidence that distinguishes
those explanations. Retain several qualified ways to reach a useful operation:
ordinary input for visible play, and deeper original-code or constructed-state
routes for isolated analysis where they remove repeated preparation work.

Status: design and operating guidance. This document adds no native invocation,
teleportation, hypothesis engine or live controller. Its records extend the
[transition-family model](EVENT_TRANSITIONS.md); the existing components below
are reuse references with narrower contracts, not newly ported DotBox features.

## Think like the programmer, then discriminate

Ask what small implementation would produce the observed behavior. Write a few
plausible sketches when they help predict code, data or execution evidence.
Treat each as a hypothesis with alternatives and a next discriminating probe.
Do not require a reconstruction of the whole program before using a working
control, or spend the foreground budget listing every possible implementation.

These are authored examples, not recovered code for a particular game:

| Possible implementation | Useful distinguishing prediction |
| --- | --- |
| A control calls `open_inventory()` directly | A direct call or control-associated callback target reaches the operation |
| A shared `handle_action(button_id)` selects behavior | The same dispatch site receives differing selector values; branches or table entries distinguish operations |
| A handler assigns `current_mode = next_mode` | A state write selects work in a later loop iteration; the click's immediate callee may return before the effect |
| A handler enters `run_inventory_mode()` | The routine owns input/rendering until an exit; normal return occurs after that interval |
| A handler tail-transfers to another context | Execution changes owner or continuation without the assumed near return |
| A handler enqueues `Load(slot)` | A request producer and later consumer are separated by a queue, callback, tick or phase |

A callback table, script interpreter or optimized branch sequence can implement
the same relationship as an authored sketch. Search for the predicted structure
and data flow, not the spelling or exact instruction order of hypothetical code.
Use observed arguments, callers, writes, indirect targets and continuation to
refine the explanation. Preserve unresolved branches and contradicting examples.

A useful hypothesis record contains the behavior being explained, the proposed
mechanism, relevant state/arguments, predicted distinguishing evidence, observed
support and contradictions, and the next question. A plausible implementation
does not become a recovered fact merely because the agent could write it.
Conversely, a recovered mechanism can immediately enable the sibling searches
and prerequisite-driven analyses in [the transition guide](EVENT_TRANSITIONS.md).

## One operation can have several entry routes

Bind alternative routes to the same operation when the relevant effects support
that relationship. Keep their actual starting conditions and execution paths.
Mouse and keyboard routes may converge; a direct call may enter after selection;
a loader and a scene-entry routine may initialize different portions of state.
These alternatives form a graph, not universal ordered layers that every game
must expose or a requirement to always choose the deepest available entry.

| Route or setup | What it can omit | What must remain represented |
| --- | --- | --- |
| Ordinary movement, key or mouse input | Nothing beyond normal control composition | Original traversal/event behavior, current input admission and outcome |
| Supported click/key delivery without pointer animation | Unnecessary host pointer travel | Actual input semantics, target/focus, hit testing where applicable and original event processing |
| UI event or dispatcher binding | Some physical-input decoding | Event payload/selector, applicable context and work normally supplied by the skipped prefix |
| Original handler or operation routine | Earlier selection/dispatch/navigation | Arguments, initialized state, invocation context and original continuation |
| Mode entry or continuation binding | An earlier route into a continuing operation | Current phase, ownership of subsequent execution, exit/completion conditions and remaining work |
| Controlled state construction | Traversal or progression needed to create a research starting state | Deliberate interventions and their provenance; the construction need not reproduce the skipped operation |

An observation hook identifies a useful place to inspect execution. A callable
route establishes how to enter and continue it. A breakpoint at a state write,
an instruction inside a handler, or a discovered address is not automatically
a callable function boundary. A mode loop, tail transfer or deferred callback
needs its own continuation contract; do not force it into a near-call helper.

For the main visualization, retain the original movement and event route.
Supported click delivery can omit visible pointer movement while the game still
processes the original interaction. Helpers can use deeper routes in their own
isolated guests to investigate quickly. Keep both recipes and their measured
scope; learning a shortcut does not silently replace the player's visible route.
All live actions retain the existing supported owner rather than adding a
second input executor.

## Describe the entry contract needed by the task

Extend a concrete transition binding with the evidence needed to use its chosen
entry. A known ordinary key route need not wait for an internal ABI to be decoded.
Unknown outcome conditions do not prohibit an otherwise qualified attempt;
invocation readiness and the conditions determining success remain separate.

| Contract element | Meaning |
| --- | --- |
| Operation and entry identity | Semantic operation, source/edition, code/resource mapping and supported entry surface |
| Parameters | Established selector, target, slot, destination, buffer or other arguments, including unresolved roles |
| Starting context | Required mode, phase, selection, relevant state and initialized resources |
| Invocation mechanism | Actual API, calling convention or transfer rule; required register/stack/global context where relevant |
| Omitted prefix and setup | Work skipped by this entry and the relevant prerequisites or effects it normally establishes |
| Continuation | Observed return, mode exit, callback, caller initialization or later event needed for the claimed result |
| Witnesses and bounds | Relevant effect/presentation/readiness evidence, host/guest limits, interruption handling and retained partial results |
| Equivalence and use | Compared ordinary route, starting conditions, effects preserved, deliberate differences, intended research or visible use |

Recover the prerequisites needed by the selected consumer. Keep unsupported
parts explicit instead of filling the contract with assumed boilerplate or
requiring an exhaustive inventory of global state for every useful step.
In particular, restore the relevant setup performed by an omitted caller, or
choose an earlier qualified entry that still performs it.

A routine that legitimately remains active can be a pending operation with
meaningful exit conditions. A bounded capture ending before that exit is a
partial observation. Preserve the attempt and confirmed effects; use a qualified
continuation or reconcile the state before issuing another invocation. Do not
replay the outer click merely because a deeper operation has not redrawn yet.

## Compare the effects that matter

Qualify a shortcut against the retained ordinary route from compatible isolated
baselines. Compare the state, continuation and side effects relevant to its
consumer, and record which dimensions differ or remain unknown. Matching a
number or final image can support that observation without establishing equal
timing, queue state, initialization, file effects or later behavior.

For example, a direct load routine may transfer a file into a buffer while a
caller normally adopts it, rebuilds state and returns control to the game.
Retain the successful transfer and investigate the missing continuation. A
file-layout consumer can use transfer evidence; a usable-load claim needs the
relevant adoption and readiness witnesses. Existing [XCOM work](XCOM_REUSE.md)
records why those claims must be kept distinct.

Saving or loading through a deeper entry still has the original operation's
game/file effects. Restoring temporary registers, stack or code does not undo
those effects. Record them explicitly and keep them within the helper's isolated
mutable files during research. The player's [memory rewind](RECOVERY_AND_SAVES.md)
continues to preserve current disk files; it is a different operation from game
save/load or restoration of a helper's experimental baseline.

Equivalence is conditional on the relevant starting context and required result.
Reuse established common behavior, then investigate differences introduced by
the new entry. Preserve the ordinary route and counterexamples. A shortcut may
be useful for analysis without matching the presentation or elapsed game time
expected during visible play. Measure warm replay separately from discovery,
with host, guest and game clocks as defined in [process guidance](BOOTSTRAP_AND_EVENT_LOOPS.md).

## Movement supplies the same kind of progression

Follow [the movement capability progression](NAVIGATION.md): identify position,
confirm it through ordinary movement, qualify isolated same-room placement,
observe original room crossing, and recover the necessary transition/setup path.
Position readback, engine adoption, collision behavior and room initialization
are different questions. Prefer the original setter or transition mechanism
when it performs required work that a raw field edit would omit.

An isolated helper may construct a coherent starting state in a location that
normal story progression has not reached. Record its baseline, deliberate field
or entry changes, initialization path, applicable conditions and observed result.
That evidence can support conditional geometry, objects, controls or script
relationships. It does not prove normal reachability or advance the player.
Some unknown prerequisites can remain explicit while a narrower observation is
useful; a malformed construction cannot establish the missing game rule.

Adopt reusable knowledge from those experiments after checking its live
applicability. Do not copy the helper's constructed state into the player's
session as part of adopting a finding. Preserve branch-specific occurrences and
invalidate dynamic entry bindings after rewind, mapping, mode or entity-lifetime
changes make them stale.

## Existing source to reuse within its actual contract

The following inspected fDisBull modules are pinned to source
`ad1e9a3177cc8fda60b9c0c64e8a40f6fabb1edd`. They demonstrate parts of this workflow;
they do not qualify arbitrary calls, arbitrary room entry or a DotBox port.

- [`z_native.py`](https://github.com/seeker-cyber-maker/fDisBull/blob/ad1e9a3177cc8fda60b9c0c64e8a40f6fabb1edd/src/fdisbull/z_native.py)
  invokes an identified flat32 near-return callee at a caller-qualified,
  non-reentrant boundary. The caller establishes compatible flat selectors and
  a temporary boundary window the callee will not execute. Byte, stack and
  segment checks support the bounded mechanism; they do not infer that contract.
  Temporary code, registers and a bounded stack window are restored while the
  callee's intended game/file effects remain. Failure preserves recovery state.
- [`z_call_contract.py`](https://github.com/seeker-cyber-maker/fDisBull/blob/ad1e9a3177cc8fda60b9c0c64e8a40f6fabb1edd/src/fdisbull/z_call_contract.py)
  captures an original flat32 `E8` near call, selected argument observations,
  return and optionally bounded continuation. Argument observations do not infer
  an ABI. Replay is a same-runtime CPU/stack reentry with matching code and
  segment context, an observed compatible return, and caller-selected compatible
  game state. Captured continuation can be checked for divergence. Callee
  global/file effects remain; fresh scene initialization or redraw is not inferred.
- [`assisted_travel.py`](https://github.com/seeker-cyber-maker/fDisBull/blob/ad1e9a3177cc8fda60b9c0c64e8a40f6fabb1edd/src/fdisbull/assisted_travel.py)
  applies qualified, bounded actor-field edits and observes the original guest
  after execution. Its room-jump route places the actor for an original portal
  input; it refuses writes to the observed room field and retains original room
  initialization. Partial writes/stops are recorded without an automatic rollback.
  Its execution uses fast-forward and needs lifecycle/timing adaptation for
  visible DotBox play. It is not a generic scene-loader or position-discovery tool.

Do not generalize these flat32 call helpers into real-mode AGI or modal/tail-call
support. A successful source audit also does not establish an executed Police
Quest teleportation or a supported original-Dot invocation interface.

## Bounded implementation and acceptance

First retain hypotheses and alternative entry contracts with the existing
family/binding/evidence records. Integrate one supported capture or invocation
adapter at a time, keeping normal controls usable. Package the required analysis
components with DotBox; ordinary players should not have to install fDisBull.

Future acceptance cases include direct versus selector dispatch, a deferred
consumer, a modal routine with a later exit, a data write that updates only a
display cache, same-room placement followed by original engine continuation,
room entry with required initialization, a successful callee with unfinished
caller work, scoped equivalence with different timing/presentation, retained file
effects, stale mappings after rewind, and helper construction that never becomes
player progression. No such new runtime acceptance was executed by this guide.
