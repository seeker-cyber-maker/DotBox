# Repositories and publication

## Shared-source integration in progress

DotBox and fDisBull are being consolidated into one source tree, with separate
products and Agent BBS projects. DotBox prioritizes rapid self-harness development
and the earliest useful controls. fDisBull focuses on recovery and recompilation
through UDL–UIL–UDC. Shared reversing mechanisms live in `packages/fdisbull-core`;
DotBox lives under `apps/dotbox` and does not require the full fDisBull application.

The first integration is committed and verified at
`64fe84f253978a699c5d95f012961c5b694e2580`, published with its original Git
history on
[`codex/shared-dotbox-core-20261121`](https://github.com/seeker-cyber-maker/fDisBull/tree/codex/shared-dotbox-core-20261121)
in `seeker-cyber-maker/fDisBull`. [Draft PR #90](https://github.com/seeker-cyber-maker/fDisBull/pull/90)
tracks review against `main`; it remains open and unmerged. The current
standalone source and existing installations remain the available baseline
until the integration is accepted.

The verified checkpoint preserves the original DotBox history and both import
parents. Its source bundle, recovery instructions and test evidence are stored
on [Agent BBS](https://agent-bbs-native.tiga-rce.chatgpt.site), report
`report-3bf3ffc1-1220-47f3-8cca-c882397a883f`, under fDisBull task
`e-2978aede-8739-4282-9b28-cacb7067aea2`. DotBox acceptance remains separately
tracked in task `e-2a790853-3b58-4551-94b0-5e365d08fa5d`.

QEMU work continues under its existing owner. QEMU becomes fDisBull's primary
backend only after parity qualification; DOSBox-X remains DotBox's backend and
then fDisBull's explicit fallback. This source integration changes no backend
default, native binary, release or live session.

## Legacy-only publication policy

The rules below continue to cover changes made to these standalone repositories.
Shared-code changes use the combined source and linked project records above.

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
The user requires every completed, reviewable development or test checkpoint
to be committed to both repositories and recorded on Agent BBS. Use the current
work branch and preserve each repository's own parent history. A test-only
checkpoint can contain an authored result receipt with the exact tested source,
command, outcome and limitations. Keep commercial data, raw captures and private
runtime material outside Git; retain their durable evidence identities on the
board. Verify both published heads and trees before calling the checkpoint
complete. Keep routine progress and discussion on the BBS rather than adding
repository comments. This standing instruction authorizes checkpoint publication;
it does not authorize merging, releasing packages or changing unrelated branches.
The release portal is the planned binary-package delivery venue; source mirroring
and package publication are separate operations.

The standalone Python service contains the extracted runtime subset and does
not require fDisBull at runtime. Native source preparation is owned by DotBox;
its pinned base and ownership overlay retain their upstream provenance.
The native ownership overlay contains modified
DOSBox-X source under GPL-2.0-or-later, as recorded in `native/README.md`.
Preserve the upstream notices and corresponding source when distributing an
emulator binary. This source contribution includes no native binary or game data.
