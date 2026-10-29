# Code

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

Analysis templates for the course. Every template is R unless stated, pinned with
`renv` `[TODO: lockfile]`. You build the environment on the first day with your
AI tool; a prebuilt fallback exists `[TODO: where]`.

The rule for all of it: run the code and look at the object, not at the AI tool's
description of the object.

| Folder | Purpose | Input | Output |
|---|---|---|---|
| `elisa/` | Four-parameter logistic standard curve, concentration table, plots by condition. Written; runs on the lab's IL-6 example data | tidy CSV (one row per well) | `elisa_results.csv`, `elisa_summary.csv`, figure |
| `griess/` | Linear nitrite standard, concentration table, plots | plate-reader export, plate map | `griess_results.csv`, figures |
| `flow/` | Reads the population statistics exported from FlowJo and plots them. Gating is done in FlowJo, not in R | FlowJo CSV export | figures |
| `growth_curve/` | Optional (extension, X05): doubling time from counts, with the published value as a reference line | counts table | figure, doubling time |
| `scrnaseq/` | The in silico arm, three parts (below) | preprocessed objects shipped by the staff | figures |
| `qpcr/` | ΔΔCt for the X01 extension | Ct export | figures |

`[TODO: write the remaining templates; each folder gets a README, an `example_data/`
subfolder and one script that runs end to end on the example data. `elisa/` is the
model.]`

## The in silico arm, `scrnaseq/`

The teaching staff preprocess two datasets and ship small objects, so nobody starts
from raw reads:

- `GSE186658`: single-cell RNA-seq of mouse peritoneal injury sites, two conditions,
  two mice each (Zindel et al. 2021, Nat Commun). Shipped as a Seurat object with
  quality control, normalisation, clustering and a coarse cell-type annotation
  already done; the macrophage subclusters are **not** annotated.
- `GSE113836`: bulk RNA-seq of RAW 264.7 and bone marrow macrophages stimulated with
  LPS plus IFNγ or with IL-4 `[TODO: verify contents, replicates and raw counts]`.
  Shipped as a count matrix with a sample sheet.

Three parts, matched to the dry-lab halves of weeks 2 and 3:

1. **Load and look** (week 2). Open the single-cell object, reproduce the QC figure
   (cells per sample before and after filtering), find the macrophages by `Adgre1`,
   `Cd68`, `Csf1r`, `Fcgr1` and `Mertk`.
2. **Derive the signatures** (week 3). Differential expression in the bulk data,
   M(IFNγ+LPS) versus M(-) and M(IL-4) versus M(-), in RAW 264.7 cells; take the top
   genes by a stated rule; compare with the Murray et al. 2014 table and with the
   consolidated sets of Colombo et al. 2024.
3. **Score the tissue** (week 3). Score every macrophage in the single-cell object
   against both signatures (`AddModuleScore` or equivalent), plot the two scores
   against each other and on the UMAP, and answer: how much of the tissue population
   does either signature explain, and what do cells with both scores high mean for
   the M1/M2 axis.

Optional extensions that start from here: annotate the Gata6+, Folr2+ Selenop+ and
Trem2+ Spp1+ populations; rerun the pipeline from the GEO matrices; integrate with a
true in vitro single-cell dataset (Sanin et al. 2022 `[TODO: accession]`).

The answer key lives in a separate private repository and is released after the
course.
