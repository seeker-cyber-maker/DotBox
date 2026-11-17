# Installed learning kit

The development package includes the agent instructions, offline inspection
tools and a persisted short learning frontier. A normal installation must not
depend on the source checkout for these features.

## Agent entry points

```sh
dotbox doctor
dotbox guide
dotbox guide --topic learning
dotbox guide --topic inspection
dotbox inspect --help
dotbox learn --help
```

`doctor` checks the installed resource hashes and executes a small authored x86
decoder self-check and checks for a stable learning-journal clock identity. The
current clock binding supports Linux and macOS; other hosts need a qualified
clock adapter before the journal is ready. It reports offline-kit readiness separately from native
game readiness. It performs no native launch, input, ownership probe or network
request. A successful offline-kit check is not a playable-runtime qualification.

The default guide starts from the next useful game action. Full play guidance,
runtime-control distinctions, inspection recipes, learning policy and native
source/build instructions are included as package resources. Load the topic
needed now instead of loading every reference into the agent context.
The exported set contains these operational topics and native preparation
inputs. Historical evidence and development-handoff links in shared documents
refer to the full source repository, not additional installed tool requirements.

## Bounded offline inspection

```sh
dotbox inspect identity /private/game/PLAY.EXE --resource /private/game/RESOURCE.DAT
dotbox inspect strings /private/evidence/window.bin --length 256 --limit 16
dotbox inspect find /private/evidence/window.bin --hex 'CD 16' --length 256
dotbox inspect disassemble /private/evidence/window.bin --bits 16 --length 64 --limit 12
dotbox inspect diff /private/evidence/before.bin /private/evidence/after.bin --length 64
```

Use only explicitly selected files and windows. Results retain offsets, hashes,
limits and truncation; they do not claim complete game understanding. Decoder
instruction-pointer origins are window-relative unless the caller supplies one.
A supplied origin does not prove a live address mapping. Compare ranges only
when their offsets or explicit origins establish the same selected address span.

The included `iced-x86==1.22.0` dependency supplies decoding. No separate fDisBull,
analysis database, Capstone, LLVM or symbolic solver is required for this kit.
Dependency wheels and their notices belong in the final offline distribution;
an ordinary pip install alone is not an offline installer.

## Retain one question

```sh
dotbox learn focus --store /private/game/learning.db --source-sha256 '<actual-sha256>' \
  --context '<current-observation-reference>' --scene 'current menu' \
  --goal 'open the selected item' --question 'does Enter select it?' \
  --next 'observe the resulting screen' --fallback 'use the visible selection control'
dotbox learn status --store /private/game/learning.db --source-sha256 '<actual-sha256>'
```

The fallback is an agent assertion, not an automatic applicability check. Use an
already applicable known control immediately without starting a learning focus
merely to give it a name. Use `learn admit` only when a concrete missing control
needs another bounded investigation, and `learn record` to retain candidate,
observed or failed findings with evidence references. A journal admission never
grants desktop input.

The default 15-second/two-probe allowance is an evaluation setting. It includes
elapsed time between CLI calls. Repeating the same context does not reset it.
Changing context requires explicit retirement of old work. The store binds a
source hash and clock identity, preserves evidence records, and must remain in
the private game workspace. Its labels are agent-reported evidence, not certified
game progress or automatic control promotion.

## Native source resources

```sh
dotbox kit-export --directory /private/dotbox/source-resources
python /private/dotbox/source-resources/scripts/prepare_native.py --help
```

The export creates a new directory and refuses an existing destination. It
contains the reviewed native patches, pinned recipe, preparation helpers and
GPL notices, along with play guidance and examples. It does not compile or fetch
anything. Follow the included `docs/STANDALONE_NATIVE.md` during packaging, before
play, to prepare and qualify the actual native payload.

## Distribution boundary

| Component | This Python package | Complete player distribution |
| --- | --- | --- |
| Offline inspection APIs and learning journal | Included | Included |
| Playbook and operational recipes | Included and hash checked | Included |
| Required decoder | Declared pinned installation dependency | Its compatible wheel/library included offline |
| Native patches, preparation scripts and notices | Included | Matching source/notices retained |
| Prepared DOSBox-X binary and host libraries | Separate runtime input | Included for the measured target platform |
| Compatible Python and dependency wheelhouse | Supplied by installation environment | Included or verified as already present |
| Original Dot input/capture integration | Separate live gate | Qualified before a player-ready claim |

The old wheel contained Python modules only. The new build stages a reviewed
resource manifest into the wheel and records each resource hash. Both direct
wheel builds and wheels rebuilt from a source distribution must preserve it.
Native source packaging does not establish a working native binary.

Memory/register capture, bounded live traces, engine-specific readers and
automatic scene applicability remain separate implementation slices. The native
backend already provides relevant primitives, but direct raw-RPC exposure would
skip ownership, timing and consistency checks. See [the method](INCREMENTAL_PLAY.md)
for the intended short capture followed by offline analysis.
