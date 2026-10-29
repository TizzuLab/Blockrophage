# Code

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

Analysis templates for the course. Every template is R, run in the RStudio project
you cloned on the first Friday; all paths are built with `here()` from the
repository folder.

## Step 0: the packages

Once, on the first Friday, open [`00_setup.R`](00_setup.R) in RStudio and press
Source (or `source("code/00_setup.R")` in the console). It installs Seurat,
ggplot2, dplyr, readr, patchwork, here and readxl from a dated package
snapshot: the same versions for everyone, ready-built for Windows, macOS and Linux,
nothing compiled.
A few minutes; it ends by printing the versions, which go into your notebook.

- First time with R: just run it.
- Already have R projects whose package versions you want to keep: talk to us
  first, and we set you up with renv, which keeps the course packages separate.
- Linux only: Seurat needs one system library, `sudo apt install libglpk40`.
- 8 GB of memory is enough; the single-cell pipeline peaks at about 3.5 GB.

## The templates

The rule for all of it: run the code and look at the object, not at the AI tool's
description of the object.

| Folder | Purpose | Input | Output |
|---|---|---|---|
| `elisa/` | Four-parameter logistic standard curve, concentration table, plots by condition. Written; runs on the lab's IL-6 example data | tidy CSV (one row per well) | `elisa_results.csv`, `elisa_summary.csv`, figure |
| `griess/` | Linear nitrite standard, concentration table, plots | plate-reader export, plate map | `griess_results.csv`, figures |
| `flow/` | Reads the population statistics exported from FlowJo and plots them. Gating is done in FlowJo, not in R | FlowJo CSV export | figures |
| `growth_curve/` | Optional (extension, X05): doubling time from counts, with the published value as a reference line | counts table | figure, doubling time |
| `scrnaseq/` | The in silico arm, three parts (below), five scripts; run from GEO in about 3 min | GEO matrices and a published signature table, downloaded by the scripts | figures, Seurat objects, scores |
| `qpcr/` | ΔΔCt for the X01 extension | Ct export | figures |

`[TODO: write the remaining templates; each folder gets a README, an `example_data/`
subfolder and one script that runs end to end on the example data. `elisa/` is the
model.]`

## The in silico arm, `scrnaseq/`

One dataset, one standard single-cell workflow; nobody starts from raw reads:
`GSE186658`, single-cell RNA-seq of mouse peritoneal injury sites, sterile or
contaminated (CLP), two mice each (Zindel et al. 2021, Nat Commun). The scripts
download the filtered count matrices from GEO and run everything on a laptop, in
about three minutes ([`scrnaseq/`](scrnaseq/README.md)); the macrophage
subclusters are **not** annotated.

Three parts, matched to the dry-lab halves of weeks 2 and 3:

1. **Load and look** (week 2). Download and load the data, make the QC figure
   (cells per sample before and after filtering), cluster, and find the macrophages
   by `Adgre1`, `Cd68`, `Csf1r`, `Fcgr1` and `Mertk` (`01_load_and_qc.R`,
   `02_cluster.R`).
2. **M1 or M2?** (week 3). Find the markers of the macrophage clusters and decide,
   before any score, which cluster is M1 and which M2 (`03_markers.R`). Then score
   every cell with the classic M1/M2 markers and with the in vitro consensus
   signatures of Colombo et al. 2024 for IFNγ and IL-4 (`04_m1_m2_score.R`). The
   point: the dichotomy is not wrong, it is a description made for one setting and
   one depth of readout; in tissue it fades.
3. **Your own signature** (week 3 to the poster). Pick a macrophage state from the
   single-cell literature (lipid-associated, scar-associated, resident subsets,
   cavity macrophages, ...) or build one from your markers, score it, and put it on
   the poster (`05_own_signature.R`).

Where to go from here, for groups that want more: see
[potential extensions](scrnaseq/README.md#potential-extensions).

The answer key lives in a separate private repository and is released after the
course.
