# Single-cell RNA-seq (Experiment 2)

One standard single-cell workflow, from the count matrices to your own signature.
Every script follows the published Seurat tutorial; read it alongside the script:
it is the conventional way, written by the people who built the method. Use your AI
tool to explain a step or an error, then check what it says against the tutorial
and against the object in front of you.

| Script | Follows |
|---|---|
| `01` to `03` | Seurat, [guided clustering tutorial](https://satijalab.org/seurat/articles/pbmc3k_tutorial) (Hao et al. 2024, [Nat Biotechnol](https://doi.org/10.1038/s41587-023-01767-y)) |
| `04`, `05` | Seurat, [`AddModuleScore`](https://satijalab.org/seurat/reference/addmodulescore) and the [cell-cycle vignette](https://satijalab.org/seurat/articles/cell_cycle_vignette), same idea (Tirosh et al. 2016, [Science](https://doi.org/10.1126/science.aad0501)) |

Open each script in RStudio and press Source, in order. Paths come from `here()`,
so it does not matter which folder RStudio is in, as long as it is the course
project.

```
01_load_and_qc.R    # download from GEO, load, QC, filter   (~35 s)
02_cluster.R        # normalise, PCA, clusters, UMAP: which cells are macrophages   (~50 s)
03_markers.R        # markers of the macrophage clusters: which is M1, which M2?   (~25 s)
04_m1_m2_score.R    # score: classic M1/M2 markers and the in vitro consensus   (~15 s)
05_own_signature.R  # your own signature from the single-cell literature, for the poster
```

Needs the packages from [`00_setup.R`](../00_setup.R). Times and memory
(peak about 3.5 GB) measured on a laptop-class machine.

## Data

GSE186658 (Zindel et al. 2021, Nat Commun): mouse peritoneal injury sites
("buttons") 24 h after surgery, sterile (`B24h1`, `B24h2`) or with microbial
contamination by cecal ligation and puncture (`BCLP24h1`, `BCLP24h2`), female
C57BL/6, 10x Genomics. GEO holds the filtered count matrices (110 MB, 13,657 cells);
`01_load_and_qc.R` downloads them once into `data/`.

The consensus signatures in `04` come from Colombo et al. 2024
([PLOS ONE](https://doi.org/10.1371/journal.pone.0297872)), who ranked the genes
induced by IFNγ, LPS, IFNγ + LPS and IL-4 across the public RNA-seq experiments of
mouse macrophages in vitro. `04` downloads their supplementary table S1 and takes
the 30 top-ranked genes for IFNγ and for IL-4, the two polarizers of your bench
work.

`data/` and `output/` are not tracked by git.

## What you decide, and write into your notebook

- QC thresholds (`01`): look at `output/qc_violins.png` first. The defaults
  (200 to 6,000 genes, less than 10% mitochondrial reads) keep 11,730 cells.
- Number of principal components and the clustering resolution (`02`): check
  `ElbowPlot(cells)`; the defaults (20 PCs, resolution 0.5) give 14 clusters.
- Which clusters are macrophages (`02`): from `output/macrophage_markers.png`,
  with the reason.
- Which macrophage cluster is M1 and which is M2 (`03`), from their markers,
  **before** you run `04`.
- Your own signature (`05`): which paper, which genes, and why.

## To discuss in the group

- Why your UMAP may differ from your neighbour's, and what `set.seed()` does.
- Manual annotation from a few markers versus automated, reference-based
  annotation (e.g. SingleR with the ImmGen reference): bias, agreement, trust.
- Your M1 and M2 clusters from `03` against the scores in `04`. Why do the
  neutrophils come out most "M1" with the classic markers, and why does the picture
  fade with the 30-gene consensus?
- M1/M2 was defined in a dish, with a few markers. Is it wrong, or a description
  that fits one setting and one depth of readout? Compare with your RAW 264.7
  cells at the bench.
- What a module score is relative to (random control genes of similar
  expression), and whether the sterile versus CLP difference holds per mouse.

## Potential extensions

No ready-made scripts here: you start from a paper, the way analyses start in a
lab, and adapt the pipeline yourself. The snippets show the core pieces, not the
whole way. Talk to your supervisor first.

### Macrophages are everywhere: take the workflow to your field

Every organ has its macrophages: microglia in the brain, Kupffer cells in the
liver, alveolar macrophages in the lung, Langerhans cells in the skin, osteoclasts
in bone, and many more in tumours, infection, fibrosis and atherosclerosis. Pick an
organ or a disease that interests you, find a published single-cell study, and run
`01` to `05` on its data.

- Where to look: the paper's "Data availability" section, then
  [GEO](https://www.ncbi.nlm.nih.gov/gds) or
  [CELLxGENE](https://cellxgene.cziscience.com/datasets). Prefer count matrices
  (`matrix.mtx`, `barcodes.tsv`, `features.tsv`, or a 10x `.h5` file): Seurat reads
  them directly. Check the size first: 8 GB of memory holds about 20,000 cells.

  ```r
  counts <- Read10X_h5(here("code", "scrnaseq", "data", "my_sample.h5"))
  cells <- CreateSeuratObject(counts, min.cells = 3)
  cells <- cells[, sample(colnames(cells), 15000)]   # too many cells? subsample
  ```

- What changes: the QC thresholds (another lab, another tissue), the markers that
  find the macrophages (which hold in your organ?), and, in a human dataset, the
  gene names.

  ```r
  cells[["percent_mt"]] <- PercentageFeatureSet(cells, pattern = "^MT-")   # human genes are upper case
  ```

- Then go further with the tools of the field (installed from GitHub, not from
  CRAN: ask us for help):
  - who talks to whom: [CellChat](https://github.com/jinworks/CellChat) (Jin et al.
    2021, [Nat Commun](https://doi.org/10.1038/s41467-021-21246-9)), ligands and
    receptors between your macrophages and their neighbours;
  - which signal drives a state: [NicheNet](https://github.com/saeyslab/nichenetr)
    (Browaeys et al. 2020, [Nat Methods](https://doi.org/10.1038/s41592-019-0667-5)),
    the ligands that best explain the genes up in your macrophages;
  - from monocyte to macrophage: [monocle3](https://cole-trapnell-lab.github.io/monocle3/docs/trajectories/)
    (Cao et al. 2019, [Nature](https://doi.org/10.1038/s41586-019-0969-x)), cells
    ordered along a path in pseudotime.

  ```r
  cds <- SeuratWrappers::as.cell_data_set(macs)   # monocle3 starts from your Seurat object
  cds <- cluster_cells(cds) |> learn_graph()
  cds <- order_cells(cds)                         # you choose where the path starts, and why
  ```

- Questions: are the M1/M2 scores of `04` any more convincing in your organ? Which
  signature from your field describes the macrophages better (`05`)? If your
  dataset is human: what would it take to compare it with mouse, and what could go
  wrong?

### More

- **Annotation by a reference instead of by eye.** SingleR with the ImmGen
  reference ([SingleR book](https://bioconductor.org/books/release/SingleRBook/);
  Aran et al. 2019, [Nat Immunol](https://doi.org/10.1038/s41590-018-0276-y)): does
  it agree with your clusters from `02` and `03`?
- **Activation in vivo.** Compare your macrophages with the monocyte-derived
  activation paths that Sanin et al. 2022 found across tissues and diseases
  ([Sci Immunol](https://doi.org/10.1126/sciimmunol.abl7482)).
