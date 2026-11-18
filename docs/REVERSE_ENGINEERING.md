# Reverse engineering as an ongoing world-model capability

Decision: 18 November 2026. Reverse engineering remains available throughout
play and preparation. It resolves ambiguous facts, discovers relationships and
improves Dot's internal model. AGI is one efficient evidence provider; it does
not define the world-model schema or limit which games DotBox can investigate.

Status: this guide defines the required workflow and current implementation
gaps. It does not add a native cross-reference analyzer or a live debugger
capture API. Read [the world model](WORLD_MODEL.md) for how evidence becomes
retained knowledge and [the kit](LEARNING_KIT.md) for shipped commands.

## Ask a question that changes understanding

An investigation can support a current action, explain a discrepancy, or prepare
a likely future consumer. Examples include:

- Does this value identify the selected troop or describe every troop?
- Which later branch consumes the flag written by this switch?
- Is the displayed number authoritative, a cached copy or a derived total?
- Does this menu option change a job immediately or queue it for a later tick?
- Is an indirect pointer selecting a different entity after a menu transition?
- Is the same address being reused after an overlay or object lifetime changes?

Keep that question, the competing explanations and the evidence that would
distinguish them. A useful result is a reusable relationship with conditions and
provenance, not merely another disassembly listing or a confident label.

Use the cheapest sufficient evidence. Known engine formats, resource tables,
save contrasts, string references, native code and runtime access observations
can complement one another. An engine reader may leave ambiguities that require
native analysis even when the game's engine is otherwise supported.

Check existing recovered work before starting a new investigation. The
[DinoPark reuse map](DINOPARK_REUSE.md) identifies mechanics reports, native
state readers, qualified routes and specific remaining questions. Reuse that
knowledge with its source and edition bindings. Investigate a missing consumer,
contradictory observation or unsupported context; do not repeat settled
economics or infer live readiness from an old successful run.

## Connect investigation to the world model

1. **Identify the unresolved claim.** Bind it to the relevant entities, source
   edition, current model revision and known observation context.
2. **Collect candidates from available evidence.** Reuse cached analyses; inspect
   relevant resources, byte ranges, readers, writers and callers. Preserve
   indirect references and missing coverage.
3. **Follow the value in context.** Determine which definition can reach a
   consumer under which conditions, including intervening writes, pointer or
   record selection and different lifetimes. A textual address match is only
   a candidate cross-reference.
4. **Choose a discriminating observation or experiment.** Compare controlled
   before/after reports or capture a bounded execution/access window when the
   qualified runtime supports it. Repeated unchanged-intent observations help
   separate timers and incidental changes from the selected action.
5. **Return a structured finding.** Record the candidate meaning, raw bindings,
   relevant readers/writers, conditions, evidence, alternatives and the next
   unresolved question. Update model knowledge without applying predicted game
   effects to the observation store.
6. **Reuse and invalidate deliberately.** Cache the result with resource/profile
   and model identities. Recheck dynamic bindings after a new observation,
   entity lifetime, code mapping, restart or rewind makes them stale.

Useful model relations include `reads`, `writes`, `derived_from`, `selects`,
`affects` and `requires`. Preserve the difference between a possible static
access, an access observed in one execution, and a supported causal conclusion.
Two values changing together do not establish causality. A runtime trace proves
what happened on that path, not that every path has been covered.

## A shared variable and reused storage are different cases

**One state value used elsewhere**
: A writer in one location and a consumer in another can reveal a cross-scene
  dependency. Establish whether the consumer receives that definition, whether
  another write intervenes, and which guards apply. This can connect a switch
  to a remote exit or a resource count to an action prerequisite.

**One storage location with several meanings**
: Registers, scratch memory, unions, object slots, selected-record pointers and
  overlays can reuse storage. Equal addresses or indexes are insufficient to
  merge semantic entities.

For example, in authored pseudocode a scratch value might hold a troop ID in
one menu and a destination ID in another. That does not make the destination a
troop. Conversely, several routines reading the same persistent job field may
belong to one meaningful dependency.

Bind a native storage hypothesis to the applicable executable/resource identity,
loaded module or overlay, address space and segment/base mapping, width/bit
mask, record or object instance, program/menu context and lifetime. Retain the
session/branch and observation identity for dynamic evidence. Distinguish file
offsets from runtime addresses and symbolic field roles from their current
physical locations. Only include fields established by evidence; unknown
mapping components remain unresolved.

Graph relationships can be contextual. A mapping such as "this field is the
selected entity's job while this menu is active" is more useful and accurate
than permanently renaming one byte as a global job variable.

## Current machinery and missing integration

| Capability | Current source/package scope |
| --- | --- |
| Executable/resource identity | COM/MZ layout and hashes for explicitly selected files; not automatic complete-edition or runtime-mapping proof |
| Strings, masked search and differences | Bounded inspection of explicit files or frozen buffers through `dotbox inspect` |
| Native instruction decoding | Required iced-x86 dependency; bounded 16/32-bit linear disassembly with explicit mapping/reachability limits |
| AGI resource analysis | Supported-profile conditions, write sites, resource references and bounded local value propagation |
| Register/memory/trace/access-breakpoint primitives | Present in the bundled native source, subject to actual build and negotiated capabilities |
| General owned evidence capture/watch/trace workflow | Integration and qualification still required at the normal DotBox session interface |
| Native CFG, xrefs, definition/use chains and storage-lifetime analysis | Not provided by the current linear decoder; a separate analysis layer is required |

The package must own the compatible modules and dependencies it needs. It must
not send an ordinary player to install fDisBull or another analyzer when an
ambiguity appears. Reuse appropriately scoped existing components during
development instead of requiring their source checkout at gameplay time.
Do not advertise the presence of raw native primitives as a qualified public
investigation workflow.

## Keep capture short and analysis off the play path

Cheap deterministic whole-resource scans and cached reader/writer indexes can
be prepared broadly. Semantic and runtime investigation can continue on a
bounded background frontier. The foreground missing-control allowance limits
how long research blocks the next interaction; it does not prohibit deeper
analysis on an isolated worker or during explicit preparation.

Only the live controller coordinates an investigation that affects guest
execution. A future capture operation must check current ownership, validate
the complete bounded request and retain one coherent observation context.
Capture only the selected register/memory windows, then resume a pause owned
by that operation before model reasoning or database work. Do not resume a
pre-existing breakpoint, exited guest or unknown stop automatically.

Watch/trace collection needs separate capability checks, execution/event limits,
cleanup and precise stop/ownership handling. It is not an unlimited breakpoint
that parks the player's game while Dot thinks. Workers consume frozen evidence
or investigate their own isolated guests. Controlled state changes belong in
those experiments, with their effects recorded; ordinary player actions remain
on the qualified input path.

When an existing control is sufficient, keep using it for the selected intent.
When ambiguous state really blocks the action, investigate that question or
state the actual game-facing block. Current uncertainty must not become an
invented rule just to keep a menu full.

## Next reusable implementation and acceptance

The first live integration is an ownership-aware bounded evidence capture
operation feeding the existing offline inspector and future world store.
Add access traces and native relationship analysis in independently qualified
slices. Keep their evidence/output contract engine-neutral so an AGI reader,
a native Dune binding and another engine adapter can feed the same model.

Use authored fixtures for a persistent flag with two consumers, an intervening
overwrite, two meanings sharing one byte, a pointer-selected record, overlay
reuse, a derived display value, an incidental timer change and a stale capture
after rewind. Verify that an observed access alone cannot set a semantic fact
or enable an unqualified action. Later test the useful workflow on the actual
selected game and record both discovery cost and reuse.

[Dune validation](DUNE_VALIDATION.md) defines the next non-AGI transfer target.
[Incremental play](INCREMENTAL_PLAY.md) and [stateful scenes](STATEFUL_SCENES.md)
retain the live action and observation contracts.
