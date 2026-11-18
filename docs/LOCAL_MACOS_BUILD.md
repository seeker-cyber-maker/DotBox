# Build and test locally on Apple Silicon macOS

The local compiler and tests run directly in Terminal; they do not need an AI
agent or a weekly usage allowance. This procedure builds the current DotBox
Python package and its patched DOSBox-X, then requires real native fixture
tests to pass. **The helper has not yet been executed on the Mac Studio.**
Its orchestration tests are not evidence of a successful macOS build.

Use a native arm64 Terminal in a logged-in desktop session for the full test.
The initial output is a developer executable plus an isolated Python environment,
not a signed application bundle or a portable offline release. Original game
files are not needed for the eight authored native fixtures.

## 1. Get the implementation checkout and prerequisites

Use the `codex/local-macos-build-20261117` branch, which includes the earlier
DotBox implementation. At this continuation, `main` is not that implementation.
Choose an unused checkout directory so existing work is preserved:

```sh
git clone --branch codex/local-macos-build-20261117 \
  https://github.com/seeker-cyber-maker/DotBox.git ~/DotBox-local
cd ~/DotBox-local
```

The independent `TiGa-RCE/DotBox` repository carries the same source on its own
history. Use either repository, not both for one build.

Xcode Command Line Tools must already work. `xcode-select -p` checks the selected
installation; if it is absent, run `xcode-select --install`, finish
[Apple's installer](https://developer.apple.com/documentation/xcode/installing-the-command-line-tools)
and return to Terminal. Use native Apple Silicon Homebrew at
`/opt/homebrew`, then install the required formulas:

```sh
/opt/homebrew/bin/brew install python@3.12 autoconf automake pkgconf libpng zstd ncurses
```

The helper does not install Homebrew, change the selected SDK, invoke `sudo` or
install system packages. It reports missing prerequisites before starting work.
The source needs C++14; the selected Apple Clang toolchain provides that language
mode. NASM, fDisBull, FFmpeg, FluidSynth and libslirp are not prerequisites for
this selected build and DotBox fixture set.

SDL2 is built from the source already included in the pinned DOSBox-X commit
(version 2.32.10 with its upstream IME changes). This deliberately records one
SDL implementation for the first qualification. Homebrew's current
[`sdl2` alias](https://formulae.brew.sh/formula/sdl2-compat) installs an SDL3-backed
compatibility layer, which would be a separate runtime to qualify. Homebrew
[`ncurses`](https://formulae.brew.sh/formula/ncurses) is keg-only; the helper passes
its include and library locations explicitly.

## 2. Run one build-and-test command

Choose a **new absolute output directory outside the checkout**, on a volume
with room for the upstream source, compiler output, virtual environment and
logs. Keep prior attempts if they are useful for diagnosis. The helper refuses
an existing destination and does not delete it or resume it implicitly.

```sh
/opt/homebrew/bin/python3.12 scripts/build_local_macos.py \
  --work-dir "$HOME/dotbox-build-01"
```

The default mode is `all`. It installs the Python package into an isolated
virtual environment, checks the installed offline kit, prepares the exact
pinned source, builds bundled SDL2 and patched DOSBox-X with **two compiler jobs**,
records the executable and linked libraries, then invokes the strict eight-test
native gate. Progress and per-stage logs identify where a failure occurred.
Nothing is installed into the system application directories.

Source preparation normally fetches the pinned public DOSBox-X commit. Python
installation also needs package downloads unless suitable packages are already
available to pip. For a local upstream Git object store, add:

```sh
/opt/homebrew/bin/python3.12 scripts/build_local_macos.py \
  --work-dir "$HOME/dotbox-build-02" \
  --upstream /absolute/path/to/dosbox-x-git-repository
```

`--upstream` requires the pinned Git commit and tree objects; a loose source
directory does not qualify. It makes that source-preparation step local, not
the entire dependency installation offline. The exact source pins and manual
build recipe remain in [standalone native preparation](STANDALONE_NATIVE.md).

## 3. Read the result, then use that executable

The output directory retains the prepared native source, its
`.dotbox-source.json`, compiler configuration/logs, the Python environment,
executable identity and the native test report. `result.json` records the
overall outcome and stage. The native report contains its own `result.json`,
`pytest.log` and `junit.xml`.

| Path within the output directory | Purpose |
| --- | --- |
| `native/src/dosbox-x` | Compiled developer executable |
| `venv/bin/dotbox` | Installed DotBox command |
| `wheels/` | DotBox wheel and resolved Python dependencies |
| `doctor.json` | Installed offline-kit check |
| `result.json` and `logs/` | Build outcome, identities and stage diagnostics |
| `native-tests/result.json` | Selected native acceptance result |
| `native-tests/pytest.log`, `native-tests/junit.xml` | Native test execution evidence |

Acceptance requires the selected tests' exact names and counts, pytest exit
zero, **no skipped/failed/errored test**, and an unchanged executable SHA-256
before and after execution. A successful source hash check or ordinary pytest
exit zero cannot substitute for this gate. Optional source-receipt metadata is
identified by hash; it is not independent proof that a supplied binary was
built from that source.

The installed-package check runs `python -I -m dotbox doctor` from outside the
checkout. The native fixtures deliberately use the checkout's source and test
files. These are separate evidence scopes: the doctor verifies the installed
offline kit; the native gate verifies the selected source/native combination.

| Mode | Required execution | What it establishes |
| --- | --- | --- |
| `all` (default) | Eight fixtures: four headless and four visible | Both selected native scopes on this host |
| `headless` | Four fixtures | Partial qualification without a visible desktop |
| `visible` | Four fixtures | The visible portion only |

For a remote shell without a usable desktop, select `--mode headless` explicitly.
Headless success is not full local qualification. The full or visible mode
refuses an explicitly configured dummy/offscreen SDL video driver; it does not
silently change the user's environment. A successful SSH connection alone does
not establish that Cocoa can create visible windows in that session.

## Repeat native tests without recompiling

After a build, use its virtual environment and executable with a new report
directory. From the same DotBox checkout:

```sh
"$HOME/dotbox-build-01/venv/bin/python" scripts/test_native.py \
  --executable "$HOME/dotbox-build-01/native/src/dosbox-x" \
  --source-receipt "$HOME/dotbox-build-01/native/.dotbox-source.json" \
  --report-dir "$HOME/dotbox-visible-check-01" \
  --mode visible
```

Use `--mode all` for the complete eight-test gate. The runner's total test limit
is 300 seconds by default; `--timeout-seconds` can set an explicit larger bound
for diagnosis. Timeouts are failures, not skips. Run `--help` for either helper
without starting a build or emulator.

Keep test reports private by default. They contain local paths and diagnostics;
inspect them before sharing. Commercial game files, saves, frames and emulator
states remain outside Git.

## What comes after a native pass

The fixtures exercise native launch, authored COM/MZ programs, observations,
ownership transitions, stale-input rejection, restore admission fencing and
service/control persistence. They do not complete the original-Dot desktop
handoff or implement a player-facing memory rewind operation.

Next qualify the two [Police Quest trials](POLICE_QUEST_ACCEPTANCE.md): ordinary
locker-room clothing change followed by walking to the usable showers, and a
late-briefing failure followed by memory-only recovery and successful attendance.
The second trial still needs the complete recovery transaction; the current
native restore fence alone is insufficient. Preserve current disk files during
revert and use observed guest-clock state for the deadline.

Retain the full corresponding prepared source, required notices, compiler
configuration and linked-library identities with any candidate binary. A
portable bundle, dependency collection and signing/distribution are later
delivery steps after the developer executable passes locally.
