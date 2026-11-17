# Extraction boundary and provenance

The independent engine uses the smaller persistent-play branch at
`59dc4d7ae24e666358a96db9c4acc1789ded5cf8` as its starting point. The original
lead checkout, its uncommitted AGI/walking/HUD experiments and the prior draft PR
remain preserved. A private 119-file source snapshot with hashes was captured
before this extraction. No commercial game data was copied into the repository.

## Reused working components

| DotBox component | Source and treatment |
| --- | --- |
| `native_rpc.py` | Existing fDisBull DOSBox JSON-lines transport, owned process cleanup and protocol checks; extracted with local launch-profile imports. |
| `native_session.py` | DOS-only launch, source attestation and cleanup responsibilities extracted from DebugSession; no Project, analyzer or code database. COM/MZ entry checks are explicitly bounded samples. |
| `screenshot_codecs.py`, `operation_budget.py` | Existing screenshot validation and nested RPC deadline machinery with local imports. Pillow remains a declared dependency. |
| `keyboard_input.py`, `input_macros.py`, `local_auth.py` | Existing keyboard/macro bounds and private credentials, reduced to standalone operations. |
| `backend.py`, `service.py`, `client.py` | Existing persistent-play facade and ownership guards, adapted to the local runtime/store. |
| `harness.py` | Existing immutable keyboard and absolute-mouse control semantics, now backed by the independent store. |
| Native agent base and ownership overlay | Exact pinned working DOSBox-X patches, manifests and GPL notices; DotBox owns preparation without an fDisBull checkout. |

Extracted modules identify their original source path and commit. Python
transport/session/screenshot/budget provenance is fDisBull integration
`9853c99952c2c0b77f2d9e33f99a05f0a242882b`; native base/input-validation
provenance is `ce91c303f2fccd1db9b1e3917ecc8c98473bfdb9`. These are source
identities, not a claim that upstream release qualification transfers to DotBox.

## Deliberate boundary changes

The new store contains executable identity, one original-source version and
immutable authored controls. It stores no mapped executable bytes, proof state,
static analysis or debugger history. Both source and version hashes bind actual
original executable bytes. Old FDB mapped-version identities are not invented
or silently migrated. Existing FDBs are refused before writes; original files
remain usable by their original tools. Legacy keyboard document syntax and the
canonical control-manifest hash scheme remain supported.

Normal desktop input belongs to the outer Codex/WebRTC harness. DotBox enables
the native host input path for both Dot and user desktop events and refuses
parallel direct input/play/pause RPCs. It reports the current outer owner as
unknown. The explicit `--manual-control` diagnostic mode verifies native host /
agent transfer and cleanup without claiming platform event integration.
Execution RPCs lack an atomic ownership parameter; guarded auto-resume rechecks
stop and ownership under the single-native-controller contract.

## Deferred work

No new AGI interpreter, pathfinder, game route, HUD or audio transport was added.
Those experiments remain separate. Actual Dot cloud deployment, the supported
outer ownership event/provider, Windows support, broad game qualification,
portable native library bundling and release publication remain separate checks.
The native executable used for acceptance is the existing matching build; this
change verifies standalone source preparation and does not claim a fresh native
compilation. No global installation was replaced.
