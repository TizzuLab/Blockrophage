# Single-cell and bulk RNA-seq: the in silico arm

Every script follows the published tutorial of its package. Read the tutorial
alongside the script: it is the conventional way, written by the people who built
the method. Use your AI tool to explain a step or an error, then check what it says
against the tutorial and against the object in front of you.

| Script | Follows |
|---|---|
| `01`, `02` | Seurat, [guided clustering tutorial](https://satijalab.org/seurat/articles/pbmc3k_tutorial) (Hao et al. 2024, [Nat Biotechnol](https://doi.org/10.1038/s41587-023-01767-y)) |
| `03` | DESeq2, [vignette](https://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html) (Love et al. 2014, [Genome Biol](https://doi.org/10.1186/s13059-014-0550-8)) |
| alternative to `03` | limma-voom with Glimma, [RNAseq123 workflow](https://bioconductor.org/packages/release/workflows/vignettes/RNAseq123/inst/doc/limmaWorkflow.html) (Law et al. 2016, [F1000Research](https://doi.org/10.12688/f1000research.9005.3)) |

Open each script in RStudio and press Source, in order; each reads the output of
the one before. Paths come from `here()`, so it does not matter which folder RStudio
is in, as long as it is the course project.

```
01_load_and_qc.R   # download from GEO, load, QC, filter   (~35 s)
02_cluster.R       # normalise, PCA, clusters, UMAP, macrophage markers   (~50 s)
03_signatures.R    # bulk RNA-seq, DESeq2: M1 and M2 signatures   (~10 s)
```

Needs the packages from [`00_setup.R`](../00_setup.R). Times and memory
(peak about 3.5 GB) measured on a laptop-class machine.

## Data

GSE186658 (Zindel et al. 2021, Nat Commun): mouse peritoneal injury sites
("buttons") 24 h after surgery, sterile (`B24h1`, `B24h2`) or with microbial
contamination by cecal ligation and puncture (`BCLP24h1`, `BCLP24h2`), female
C57BL/6, 10x Genomics. GEO holds the filtered count matrices (110 MB, 13,657 cells);
`01_load_and_qc.R` downloads them once into `data/`.

GSE113836 (Huffaker et al. 2021, [Nat Commun](https://doi.org/10.1038/s41467-021-22923-5)):
bulk RNA-seq of RAW 264.7 and bone marrow macrophages, each in medium, LPS + IFNγ
("M1") or IL-4 ("M2"), two replicates each, as a raw count table (300 kB).
`03_signatures.R` downloads it and uses the six RAW 264.7 samples.

`data/` and `output/` are not tracked by git.

## What you decide, and write into your notebook

- QC thresholds (`01`): look at `output/qc_violins.png` first. The defaults
  (200 to 6,000 genes, less than 10% mitochondrial reads) keep 11,730 cells.
- Number of principal components and the clustering resolution (`02`): check
  `ElbowPlot(cells)`; the defaults (20 PCs, resolution 0.5) give 14 clusters.
- Which clusters are macrophages (`02`): from `output/macrophage_markers.png`,
  with the reason.
- The signature rule (`03`): the default (up at least 4-fold, adjusted p < 0.05,
  the 50 most significant) gives 50 genes for LPS + IFNγ (Acod1, Cxcl10, Cd40,
  Stat1, ...) but only 20 for IL-4 (Mrc1, Arg1, Mgl2, Il10, ...).

## To discuss in the group

- Why your UMAP may differ from your neighbour's, and what `set.seed()` does.
- Manual annotation from a few markers versus automated, reference-based
  annotation (e.g. SingleR with the ImmGen reference): bias, agreement, trust.
- DESeq2 versus limma-voom: the same signature? And a cell line versus primary bone
  marrow macrophages from the same dataset.
