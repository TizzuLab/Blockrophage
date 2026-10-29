# Code

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

Analysis templates for the course. Every template is R, run in the RStudio project
you cloned on the first Friday; all paths are built with `here()` from the
repository folder.

## Step 0: the packages

Once, on the first Friday, open [`00_setup.R`](00_setup.R) in RStudio and press
Source (or `source("code/00_setup.R")` in the console). It installs Seurat,
ggplot2, dplyr, readr, patchwork and here from a dated package snapshot, and DESeq2
from Bioconductor: the same
versions for everyone, ready-built for Windows, macOS and Linux (on Linux DESeq2 is
compiled, about 3 minutes).
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
| `scrnaseq/` | The in silico arm, three parts (below). Parts 1 to 3 written; run from GEO in about 2 min | GEO matrices and count table, downloaded by the scripts | figures, Seurat objects, signatures |
| `qpcr/` | ΔΔCt for the X01 extension | Ct export | figures |

`[TODO: write the remaining templates; each folder gets a README, an `example_data/`
subfolder and one script that runs end to end on the example data. `elisa/` is the
model.]`

## The in silico arm, `scrnaseq/`

Two datasets; nobody starts from raw reads:

- `GSE186658`: single-cell RNA-seq of mouse peritoneal injury sites, sterile or
  contaminated (CLP), two mice each (Zindel et al. 2021, Nat Commun). The scripts
  download the filtered count matrices from GEO and run quality control,
  normalisation, clustering and the macrophage markers themselves, on a laptop, in
  about a minute and a half ([`scrnaseq/`](scrnaseq/README.md)); the macrophage
  subclusters are **not** annotated.
- `GSE113836`: bulk RNA-seq of RAW 264.7 and bone marrow macrophages in medium,
  LPS plus IFNγ or IL-4, two replicates each (Huffaker et al. 2021, Nat Commun).
  The script downloads the raw count table from GEO and writes the sample sheet
  from the GEO sample descriptions.

Three parts, matched to the dry-lab halves of weeks 2 and 3:

1. **Load and look** (week 2). Download and load the data, make the QC figure
   (cells per sample before and after filtering), cluster, and find the macrophages
   by `Adgre1`, `Cd68`, `Csf1r`, `Fcgr1` and `Mertk` (`01_load_and_qc.R`,
   `02_cluster.R`).
2. **Derive the signatures** (week 3). Differential expression in the bulk data,
   M(IFNγ+LPS) versus M(-) and M(IL-4) versus M(-), in RAW 264.7 cells; take the top
   genes by a stated rule; compare with the Murray et al. 2014 table and with the
   consolidated sets of Colombo et al. 2024 (`03_signatures.R`, DESeq2; limma-voom
   with Glimma as the alternative).
3. **Score the tissue** (week 3). Score every macrophage in the single-cell object
   against both signatures (`AddModuleScore` or equivalent), plot the two scores
   against each other and on the UMAP, and answer: how much of the tissue population
   does either signature explain, and what do cells with both scores high mean for
   the M1/M2 axis (`04_score.R`).

Optional extensions that start from here: annotate the Gata6+, Folr2+ Selenop+ and
Trem2+ Spp1+ populations; rerun the pipeline from the GEO matrices; integrate with a
true in vitro single-cell dataset (Sanin et al. 2022 `[TODO: accession]`).

The answer key lives in a separate private repository and is released after the
course.
