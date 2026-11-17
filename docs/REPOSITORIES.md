# Repositories and publication

DotBox uses two independent public repositories with matching source history:

- Primary: https://github.com/seeker-cyber-maker/DotBox
- Mirror: https://github.com/TiGa-RCE/DotBox

They are independent repositories rather than a fork relationship. Either can
retain the source if the other account becomes unavailable. GitHub permissions
and Codex installation access remain account-specific.

In the original local checkout, `origin` names the primary and `mirror` names
the second repository. Publish an inspected commit to both without forcing:

```sh
git push origin main
git push mirror main
```

Authenticate each operation as an account with access to that destination.
Never put tokens in remote URLs or repository files. If either push fails,
report the divergence and reconcile the actual heads before continuing.
Do not use `git push --mirror` or overwrite unrelated history.

No automatic synchronization service or scheduled workflow is installed by
this bootstrap. Future publication needs to update both repositories explicitly.
The release portal is the planned binary-package delivery venue; source mirroring
and package publication are separate operations.

The standalone Python service contains the extracted runtime subset and does
not require fDisBull at runtime. Native source preparation is owned by DotBox;
its pinned base and ownership overlay retain their upstream provenance.
The native ownership overlay contains modified
DOSBox-X source under GPL-2.0-or-later, as recorded in `native/README.md`.
Preserve the upstream notices and corresponding source when distributing an
emulator binary. This source contribution includes no native binary or game data.
