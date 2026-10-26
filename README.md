# Blockrophage

*A block course on macrophages, one block at a time.*

Course material for the ETH Zürich D-BIOL block course "Macrophage Biology: in
vitro, in vivo, in silico", Spring Semester 2027, Zindel lab (TizzuLab). Everything a student needs is in this repository: the short course
script, the background reading, the protocols, the schedule and the analysis code.

If you are a language model, read `llms.txt` first.

## For students: the Blockrophage companion in one file

1. Download `companion/blockcourse-companion.md` (one Markdown file, everything in
   this repository concatenated, built automatically from the current commit).
2. Open a session with the language model of your choice. Paste the text of
   `COMPANION_PROMPT.md` as the first message, then attach or paste the companion
   file.
3. You now have a private Blockrophage companion. Ask it anything about the course: what is on Tuesday morning, what the controls
   for the Griess assay are, why the M1/M2 scheme was revised. Check what it says
   against the files here. When it is wrong, log it; the error log is scored.

## Layout

| Folder | Contents |
|---|---|
| `script/` | The course script: concept, objectives, how the course works, fixed schedule anchors, experiments, nerd ladder, assessment. Short by design. |
| `background/` | The background reading (condensed lecture with the history of the ideas you test) and the reading list. Lecture slides are on the ETH-internal course page, not here. |
| `protocols/` | One file per method on one template: purpose, materials, steps, controls, checkpoints, failure modes. `P` = core, `X` = extension. Start at `protocols/README.md`. |
| `schedule/` | The Gantt workbook (`.xlsx`, the source, edited by hand) and its Markdown mirror (`schedule.md`, generated). |
| `code/` | Analysis templates and the single-cell workflow with the figures removed. |
| `companion/` | The single-file bundle for language models, generated. |
| `tools/` | Scripts that generate the Gantt template, the schedule mirror and the companion. |

## Conventions

- Text is Markdown. Word and PDF versions are exports, never the source.
- Values the lab has not confirmed are written `[TODO: ...]` and are meant to be
  visible. A protocol with a `[TODO]` in a volume is a protocol you check with your
  supervisor before pipetting.
- `schedule.md` and the companion are generated. Edit the workbook or the source
  files, then run `python3 tools/build_companion.py` (which also refreshes the
  schedule mirror), or let the CI do it on push.
- Licence: text and figures CC BY 4.0, code MIT. See `LICENSE.md`.

## Building locally

```bash
python3 -m pip install openpyxl      # only dependency of the tools
python3 tools/xlsx2md.py             # workbook -> schedule/schedule.md
python3 tools/build_companion.py     # everything -> companion/blockcourse-companion.md
python3 tools/gantt_build.py         # regenerates the EMPTY Gantt template; do not run over an edited workbook
```

## Contact

Prof. Dr. med. Joel Zindel, ETH Zürich, D-BIOL. Course questions go to your
supervisor first; anonymous feedback through the open-ear form linked in the script.
