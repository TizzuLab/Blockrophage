#!/usr/bin/env Rscript
# Part 1b: normalise, cluster, and find the macrophages.
#
# Usage: open in RStudio and press Source, or Rscript code/scrnaseq/02_cluster.R
# Input:  after_qc.rds from 01_load_and_qc.R, in code/scrnaseq/output/
# Output in code/scrnaseq/output/: umap_clusters.png, umap_condition.png,
#         macrophage_markers.png, clustered.rds

library(Seurat)
library(ggplot2)
library(patchwork)
library(here)

out_dir <- here("code", "scrnaseq", "output")

cells <- readRDS(file.path(out_dir, "after_qc.rds"))

# 1. The standard Seurat steps. Each one is a choice; the defaults are stated.
cells <- NormalizeData(cells)                          # counts per cell scaled to 10,000, log
cells <- FindVariableFeatures(cells, nfeatures = 2000) # the 2,000 most variable genes
cells <- ScaleData(cells)                              # each gene centred and scaled
cells <- RunPCA(cells, npcs = 30)
dims <- 1:20                                           # check ElbowPlot(cells) and say why
cells <- FindNeighbors(cells, dims = dims)
cells <- FindClusters(cells, resolution = 0.5)        # higher resolution, more clusters
cells <- RunUMAP(cells, dims = dims)

# To discuss once you compare with the other groups: same data, same script, but
# your clusters or UMAP may not look exactly like your neighbour's. PCA, clustering
# and UMAP all start from random numbers. Seurat fixes them by default (the seed.use
# and random.seed arguments), yet package versions and computers still differ. What does set.seed() do,
# where would you put it, and what does it mean if a cluster only exists with one
# seed?

ggsave(file.path(out_dir, "umap_clusters.png"),
       DimPlot(cells, label = TRUE) + NoLegend(), width = 6, height = 5.5)
ggsave(file.path(out_dir, "umap_condition.png"),
       DimPlot(cells, group.by = "condition"), width = 7, height = 5.5)

# 2. Where are the macrophages? Five markers that together mark them in the mouse.
markers <- c("Adgre1", "Cd68", "Csf1r", "Fcgr1", "Mertk")
p <- FeaturePlot(cells, features = markers, ncol = 3) /
  DotPlot(cells, features = markers) + RotatedAxis()
ggsave(file.path(out_dir, "macrophage_markers.png"), p, width = 12, height = 12)

# Calling a cluster "macrophage" from five markers is manual annotation: quick and
# transparent, but it depends on which markers you pick and on what you expect to
# see (interpreter bias). Question: how would automated annotation compare? A
# reference-based tool (e.g. SingleR with the ImmGen reference from celldex) labels
# each cell by similarity to sorted, known cell types. Where do the two agree, and
# where would you trust which?

saveRDS(cells, file.path(out_dir, "clustered.rds"))
cat("Clusters:", nlevels(cells$seurat_clusters),
    ". Decide which clusters are macrophages from macrophage_markers.png.\n")
