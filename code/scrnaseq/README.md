# Single-cell RNA-seq: the in silico arm

Run from this folder, in order. Each script reads the output of the one before.

```
Rscript 01_load_and_qc.R   # download from GEO, load, QC, filter   (~35 s)
Rscript 02_cluster.R       # normalise, PCA, clusters, UMAP, macrophage markers   (~50 s)
```

Needs the packages from [`code/setup`](../setup/README.md). Times and memory
(peak about 3.5 GB) measured on a laptop-class machine.

## Data

GSE186658 (Zindel et al. 2021, Nat Commun): mouse peritoneal injury sites
("buttons") 24 h after surgery, sterile (`B24h1`, `B24h2`) or with microbial
contamination by cecal ligation and puncture (`BCLP24h1`, `BCLP24h2`), female
C57BL/6, 10x Genomics. GEO holds the filtered count matrices (110 MB, 13,657 cells);
`01_load_and_qc.R` downloads them once into `data/` and checks the MD5 sum.
`data/` and `output/` are not tracked by git.

## What you decide, and write into your notebook

- QC thresholds (`01`): look at `output/qc_violins.png` first. The defaults
  (200 to 6,000 genes, less than 10% mitochondrial reads) keep 11,730 cells.
- Number of principal components and the clustering resolution (`02`): check
  `ElbowPlot(cells)`; the defaults (20 PCs, resolution 0.5) give 14 clusters.
- Which clusters are macrophages (`02`): from `output/macrophage_markers.png`,
  with the reason.
