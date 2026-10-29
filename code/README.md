# Code: the in silico arm

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

This course emphasizes reproducible data analysis using a scripted approach in R. 
Most of us use RStudio and we will show you how to clone a project and get started; 
Since the paths are all relative (using the `here()` package) you can in principle
source (or "run") the scripts directly in your local repo.

## The idea: from a tidy CSV to a paper figure

The ELISA analysis is the example. It starts from a tidy CSV, one row per well as
it comes off the plate reader, and ends with a figure as it would go into a paper:
the standard curve, the concentrations, the plot by condition. Everything in
between is code, nothing is done by hand, so the analysis is 100% reproducible:
anyone with the same data and the same code gets the same figure. That is not
always the case in science.

Everyone does the ELISA analysis in the course, on their own plate, and we look at
this code in depth together. For your other assays, qPCR, Griess, or even flow
cytometry, you are encouraged to do the same in R, and we support you. AI tools are
perfect to get started; but you will need to read the code and explain what it
does, and for that the AI tools are a great help too. We provide templates for the
ELISA and for the single-cell analysis of Experiment 2 only; the rest is yours.

## Step 0: the packages

Remember from class: base R comes with many functions, but we often need more.
More comes in packages, written by others and shared through CRAN. This lab works
in the tidyverse dialect of R: `ggplot2` for figures, `dplyr` for tables, `readr`
for reading files. A package is installed once and loaded in every session that
uses it:

```r
install.packages(c("ggplot2", "dplyr", "readr"))   # once: downloads them to your computer
library(ggplot2)                                   # every session: makes its functions available
packageVersion("ggplot2")                          # which version you have
```

That is how you will add any package your own analysis needs later. But packages
come in versions, and versions can differ in what a function does. So that we all
work with the same packages, we install the course packages with a setup script
instead, from a dated snapshot.

Before any script, including the ELISA: once, on the first Friday, we will open
[`00_setup.R`](00_setup.R) in RStudio and press
Source (or `source("code/00_setup.R")` in the console). It installs Seurat,
ggplot2, dplyr, readr, patchwork, here and readxl from a dated package
snapshot: the same versions for everyone. If you already have R projects whose package versions you want to keep: talk to us and we set you up with renv, which keeps the course packages separate. If you
work on Linux: Seurat needs one system library, `sudo apt install libglpk40`. And if your laptop has less than 8 GB of memory, tell us before the course: the
single-cell part needs about 4 GB, and the lab has a few spare machines.

## The templates

We provide templates but expect the students to look at the code, not at the AI tool's
description of the object, and we'll discuss what the code does. And who knows, maybe we 
introduced a couple bugs for teaching purposes.

| Folder | Purpose | Input | Output |
|---|---|---|---|
| [`elisa/`](elisa/README.md) | Four-parameter logistic standard curve, concentration table, plots by condition (C5). Runs on the lab's IL-6 example data | tidy CSV (one row per well) | `elisa_results.csv`, `elisa_summary.csv`, figure |
| [`scrnaseq/`](scrnaseq/README.md) | Experiment 2, three parts (below), five scripts; run from GEO in about 3 min | GEO matrices and a published signature table, downloaded by the scripts | figures, Seurat objects, scores |

## Single-cell RNA-seq (Experiment 2), `scrnaseq/`

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
