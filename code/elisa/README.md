# ELISA: standard curve and concentrations

Template for C5. One script, one example dataset, runs end to end:

Open the script in RStudio and press Source: it runs on the example data and writes
to `code/elisa/output/`. For your own plate, put your CSV into `example_data/` (or
any folder in the repository) and change the file name in the `input` line.

Needs `ggplot2`, `dplyr`, `patchwork` and `here` from [`00_setup.R`](../00_setup.R).

## Input

A tidy CSV with one row per well. Columns: `well`, `type` (`standard` or
`sample`), `condition`, `standard_pg_ml` (standards; the 0 pg/mL rows are the
blank), `lps_ng_ml` (optional), `replicate`, `od450`, `dilution_factor`.

`example_data/il6_lps_raw264_2026-09.csv`: RAW 264.7, 2 × 10^4 cells per 96-well,
LPS 0, 0.1, 1, 10, 100 ng/mL for 16 h in triplicate, mouse IL-6 ELISA (Invitrogen
uncoated kit), standard 500 to 7.8 pg/mL in duplicate, read at 450 nm without
reference filter on a Promega GloMax Discover, Zindel lab, September 2026. The
plate also carried an osteopontin co-stimulation arm, which is not included.

## What the script does

1. Blank: mean OD of the 0 pg/mL standards, subtracted from every well.
2. Standard curve: four-parameter logistic fit (`nls`). The console prints the four
   parameters and reads the standards back off the curve (recovery, 80 to 120% is
   the usual standard).
3. Samples: back-calculated from the curve, multiplied by `dilution_factor`; wells
   at or below the blank are set to 0; `in_range` says whether the OD lies between
   the lowest and the top standard.
4. Output in `output/`: `elisa_results.csv` (per well), `elisa_summary.csv` (mean,
   SD, n and wells out of range per condition), `elisa_figure.png` (standard curve
   with samples overlaid; concentration per condition).

If `nls` stops with an error on your plate, look at the standards first and ask us:
that is the moment to understand the curve, not to work around it.
