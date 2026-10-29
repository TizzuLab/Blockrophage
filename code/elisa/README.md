# ELISA: standard curve and concentrations

Template for C5. One script, one example dataset, runs end to end:

Open the script in RStudio and press Source: it runs on the example data and writes
to `code/elisa/output/`. For your own plate, from the terminal:

```
Rscript code/elisa/elisa_standard_curve.R my_plate.csv my_output_folder
```

Needs `ggplot2` and `here` from [`00_setup.R`](../00_setup.R); everything else is base R.

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
2. Standard curve: four-parameter logistic fit (`nls`), with a log-log linear
   fallback on the non-zero standards if the 4PL does not converge. The console
   says which one was used and gives R² on the standards.
3. Samples: back-calculated from the curve, multiplied by `dilution_factor`,
   flagged when the OD is below the lowest or above the highest standard.
4. Output in `output/`: `elisa_results.csv` (per well), `elisa_summary.csv` (mean,
   SD, n per condition, number of flagged wells), `elisa_figure.png` (standard
   curve with samples overlaid; concentration per condition).

The `output/` folder is not tracked; the figure for the protocol page is copied to
`protocols/figures/`.
