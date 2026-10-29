#!/usr/bin/env Rscript
# Part 1b: normalise, cluster, and find the macrophages.
#
# Usage (from this folder): Rscript 02_cluster.R
# Input:  output/after_qc.rds from 01_load_and_qc.R
# Output: output/umap_clusters.png, output/umap_condition.png,
#         output/macrophage_markers.png, output/clustered.rds

suppressPackageStartupMessages({
  library(Seurat)
  library(ggplot2)
  library(patchwork)
})

cells <- readRDS("output/after_qc.rds")

# 1. The standard Seurat steps. Each one is a choice; the defaults are stated.
cells <- NormalizeData(cells)                          # counts per cell scaled to 10,000, log
cells <- FindVariableFeatures(cells, nfeatures = 2000) # the 2,000 most variable genes
cells <- ScaleData(cells)                              # each gene centred and scaled
cells <- RunPCA(cells, npcs = 30)
dims <- 1:20                                           # check ElbowPlot(cells) and say why
cells <- FindNeighbors(cells, dims = dims)
cells <- FindClusters(cells, resolution = 0.5)        # higher resolution, more clusters
cells <- RunUMAP(cells, dims = dims)

ggsave("output/umap_clusters.png",
       DimPlot(cells, label = TRUE) + NoLegend(), width = 6, height = 5.5)
ggsave("output/umap_condition.png",
       DimPlot(cells, group.by = "condition"), width = 7, height = 5.5)

# 2. Where are the macrophages? Five markers that together mark them in the mouse.
markers <- c("Adgre1", "Cd68", "Csf1r", "Fcgr1", "Mertk")
p <- FeaturePlot(cells, features = markers, ncol = 3) /
  DotPlot(cells, features = markers) + RotatedAxis()
ggsave("output/macrophage_markers.png", p, width = 12, height = 12)

saveRDS(cells, "output/clustered.rds")
cat("Clusters:", nlevels(cells$seurat_clusters),
    ". Decide which clusters are macrophages from macrophage_markers.png.\n")
