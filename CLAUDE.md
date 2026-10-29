# Notes for Claude Code sessions in this repository

This is Blockrophage, the open block course on macrophage biology (D-BIOL, ETH Zürich,
spring 2027), course lead Joel Zindel. Course script: `README.md`. Lab protocols:
`protocols/`. Analysis code: `code/`. Read `llms.txt` for the map of the repository.

## Branches

- `main` is the published version and is protected. Nobody pushes to it; the course
  lead merges `dev` into `main` by pull request.
- `dev` is the course lead's working branch.
- **Contributors work on their own branch from `dev`** and open a pull request into
  `dev`; the course lead reviews and merges. Name it after the person and the task,
  e.g. `romy/protocol-validation`. Never push to `dev` or `main` directly.
- A pull request into `dev` may show the check "Generated files are stale". That is
  expected for contributors: after the merge, a bot regenerates those files on `dev`.

## Generated files: never edit by hand

`stuff/companion/*.md`, `stuff/figures/schedule/*.svg`, `stuff/tools/schedule/schedule_text.md`, and the
blocks between `<!-- companion:begin -->`/`end` and the schedule markers in `README.md`.

## Protocol validation (spring 2027: Romy)

Romy is a student who tests the protocols at the bench before the first course run.
She needs a bit of help at the beginning: in her first sessions go step by step,
explain what each git command does before running it, and ask before every commit
and push. Help her with the setup first:

1. git: `git config --global user.name` and `user.email`, clone the repository,
   create her branch from `dev` (`git switch dev && git pull && git switch -c romy/protocol-validation`).
2. `.gitignore`: explain what it does and check together that her own material stays
   out of the repository. Personal notes, photos, Word exports and drafts go into
   `_local/`, which is ignored. If she copies files from Windows into WSL, the
   `*:Zone.Identifier` files that appear are ignored too. If she needs more
   personal entries, they go into `.git/info/exclude`, not into `.gitignore`.
3. A Word copy of all protocols for printing or comments at the bench:
   `sudo apt install pandoc`, then from the repository folder
   `pandoc protocols/C*.md protocols/X*.md protocols/S*.md -o _local/Blockrophage_protocols.docx`.

How a validation round goes:

- One protocol at a time. Record at the bench what was done, what differed from the
  page, and the values measured (counts, times, volumes, ODs).
- Then edit the protocol's `.md` file on her branch: replace values that turned out
  wrong, resolve `[TODO: ...]` items she has tested, add a failure mode she ran into.
  Write in the protocol's tone; follow the conventions in `protocols/00_TEMPLATE.md`
  (times in bold boxes like **`37 °C, 5% CO2, 16 h`**, callouts at the left margin).
- One commit per protocol with a message that says what was tested and changed, e.g.
  "C1: thaw tested 2027-02-10, viability 92%, centrifugation step confirmed".
- Pull request into `dev` when a protocol is done, with a short summary of what was
  tested and what is still open.

## Rules for every session

- The "Under construction" notices stay until the course lead removes them.
- No animals anywhere in the repository (no animal pictures, icons or emoji).
- Lab SOPs and protocols from the lab's internal collection are not copied into this
  public repository; the protocol pages reference them by name.
- Changes to `README.md` (the course script) are always shown to the course lead.
- Content over tooling: the goal is protocols that work at the bench, not new tools.
