# Standalone DOSBox-X source and build

DotBox includes the source patches, recipe, hashes and license notices needed to
prepare its ownership-enabled DOSBox-X. No fDisBull checkout or Python package
is needed. Preparation requires Python 3.12 or later, Git, and either network
access to the pinned public DOSBox-X commit or a local Git repository containing
that commit. Preparation does not compile or install a binary.

From the DotBox source root, choose a new source directory outside the checkout:

```sh
python scripts/prepare_native.py /path/to/new/dotbox-dosbox-x
```

This fetches only the pinned commit into temporary storage, exports that
immutable commit, applies the included stable native patch followed by DotBox's
cooperative-input patch, verifies all 38 changed/new result files, and publishes
the prepared directory after every check passes. Existing output is verified
and reused; conflicting content is refused. A failed attempt removes only its
own temporary preparation directory. The output's `.dotbox-source.json` records
the recipe, upstream and patch identities, and explicitly records that no
native build was performed.

For offline preparation, use a local upstream Git object store:

```sh
python scripts/prepare_native.py /path/to/new/dotbox-dosbox-x \
  --upstream /path/to/dosbox-x-git-repository
python scripts/prepare_native.py /path/to/new/dotbox-dosbox-x --check
```

The local repository may have active changes. Preparation reads the exact
pinned Git commit and does not read, reset or alter its working tree. The check
command verifies the recipe inputs, the preparation receipt and every native
file changed by either patch. It does not validate unmodified upstream files,
build products, host libraries or a binary's behavior.

## Source identity

[`native/build-recipe.json`](../native/build-recipe.json) is the DotBox recipe.
It retains the complete base patch to preserve its independently recorded
identity rather than reconstructing a reduced patch with different provenance.
Only the native patch, its manifest and GPL text are copied from fDisBull;
fDisBull's application, disassembler, package, other emulator profiles and game
data are not native preparation dependencies.

| Input | Pin |
| --- | --- |
| DOSBox-X commit | `029bd65c5dcc7cdc7f2e14e35278620d9707d969` |
| DOSBox-X tree | `68005f10ab25418b40621875ad8e7a4bd867335c` |
| Base patch origin | fDisBull `ce91c303f2fccd1db9b1e3917ecc8c98473bfdb9`, `experimental/dosbox-x` |
| Base patch SHA-256 | `bc0ca8c93deaf6cb96eea91e39176b2713ab333e29bfefcf730e1a1d3c75eb2f` |
| Cooperative-input patch SHA-256 | `4bb0c1f6e908f0e52be291ddc97c4456e3d9ddd6bbf0bf5ba5a1a8fb454dd58d` |
| Native ownership protocol | `dotbox-input-control-1` |

The existing [`native/manifest.json`](../native/manifest.json) and ownership
patch are preserved. The historical `fdisbull_*` field names identify the
overlay's base provenance; they are not runtime imports or checkout selectors.
The original base manifest is retained verbatim. Its historical verification
fields are not claims about a newly prepared or built DotBox delivery.

## Build

Install the host's normal DOSBox-X development prerequisites: a C/C++ toolchain,
autoconf, automake, libtool, pkg-config, SDL2 development files, ncurses,
libpng/zlib and Zstandard development files. Upstream configure may detect
additional optional system libraries. NASM and Python Pillow are needed only
for upstream assembly-fixture acceptance, not to prepare this source.

In the prepared directory, run the commands retained in the recipe:

```sh
./autogen.sh
./configure --enable-sdl2 --enable-debug=heavy --enable-dosbox_agent \
  --enable-agent-zstd --disable-avcodec --disable-libslirp --disable-libfluidsynth
make -j2
```

The resulting executable is `src/dosbox-x`. SDL2, heavy debugging and the native
agent must be enabled; a stock DOSBox-X executable lacks DotBox's protocol.
The flags preserve the already exercised native configuration. Build memory
and prerequisites are host-dependent; follow the host's heavy-job policy when
applicable. Preparation and ordinary metadata tests do not start a heavy build.

Keep build output outside Git. Before distributing a binary, retain its hash,
host/architecture, toolchain/configuration and linked-library identities, the
full corresponding prepared source, and required notices. See
[`native/dosbox-x/NOTICES.md`](../native/dosbox-x/NOTICES.md) and
[`native/dosbox-x/COPYING`](../native/dosbox-x/COPYING).

## Qualification boundaries

The source preparation was replayed locally without compiling. Its 38 final
source hashes match the existing prepared ownership-enabled native tree. This
proves source preparation, not a fresh native build or binary reproducibility.
The earlier local arm64 executable is historical evidence; this source recipe
does not silently substitute it for a newly built delivery.

For each intended host, build and identify a fresh executable, then run the
DotBox native protocol and full-service acceptance tests with
`DOTBOX_DOSBOX_EXECUTABLE=/absolute/path/to/src/dosbox-x`. Native acceptance must
exercise actual startup, screenshot/state access, agent-to-host ownership,
return to agent, held-input cleanup, rejection of stale input, continued play
and process cleanup. Dot's supported takeover event source and visible
keyboard/mouse behavior must be checked on Dot's actual desktop separately.
Source tests, an executable's existence and prior fDisBull qualification do not
establish that desktop result. Packaging, binary distribution and runtime
activation are separate delivery checks.
