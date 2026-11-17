# DotBox: keep the next interaction playable

DotBox is for playing the original graphical game with the user. The player
should not need to know about harnesses, debuggers or the learning machinery.

## Start with the useful action

Establish the installed runtime and supported input owner once. `dotbox doctor`
checks the offline learning kit; it does not establish live game readiness or
grant input. In default desktop mode, use the supported outer desktop tools.
Native `act`, key, click, play and pause RPCs require explicit diagnostic mode
and are refused in normal mode.

When the current observation and a known applicable control suffice, act now.
Observe the result, then save any useful control metadata without repeating the
input. A scene name, wrapper or complete harness is not required before using
visible menu controls or otherwise applicable ordinary movement. Scene-specific
coordinates and state assumptions still need a fresh applicability check.

## Learn one missing interaction

Keep only the current goal, observed context, one operational question, immediate
next interaction and usable fallback. Examples: "Does Enter select this item?"
or "Does releasing Right stop movement?" Avoid full room maps or game recovery.

Use `dotbox learn` when a missing control genuinely blocks progress. Its default
trial allowance is 15 seconds and two probe admissions. The clock includes time
between calls; reopening the same context does not reset it. On exhaustion,
use an applicable fallback or briefly explain the actual game-facing block.
Retire old work explicitly after a real player choice or context change. Never
rename an unchanged question to restart its allowance. The journal cannot stop
running tools, certify an outcome or grant input permission.

Reuse compatible knowledge first. Use visible controls, supplied instructions
or a bounded frozen-file inspection when sufficient. `dotbox inspect` provides
executable/resource hashes, strings, byte patterns, x86 windows and byte diffs.
These tools do not touch a live guest. Do not hold a game paused while reasoning,
reading files, authoring metadata or waiting for a worker. Qualified live capture
must resume the guest before analysis; no general live capture facade ships yet.

Optional improvements cause no intentional gameplay wait when a working route
exists. The older 180-second first-preparation budget is a ceiling, never a
minimum wait or an allowance to restart in each room. Start useful play earlier.

## Retain progress

Separate candidate findings from observed effects. Accepted input alone does
not prove progress. Save evidence references and immutable control revisions;
keep the working revision until a compatible improvement is ready. Saving is
metadata work, never a reason to replay input. After uncertain partial effects,
observe before deciding whether to retry. After human play, refresh the actual
state and retire stale intentions; do not restore an old state to fit a recipe.

One lead is sufficient. Workers are optional and consume bounded frozen evidence.
Keep player communication about the current game and consequential choices.
Keep original games, captures, stores and saves private.

## Read only the next reference you need

- `dotbox guide --topic learning`: incremental method, budgets and measurements.
- `dotbox guide --topic inspection`: inspection/journal commands and package scope.
- `dotbox guide --topic play`: full play skill.
- `dotbox guide --topic controls`: storing and using controls in the actual mode.
- `dotbox guide --topic continuous`: continued play, workers and handoff.
- `dotbox guide --topic runtime`: standalone installation and ownership boundary.
- `dotbox guide --topic native`: preparing native source during packaging.

Use `dotbox inspect --help` or `dotbox learn --help` for exact command syntax.
