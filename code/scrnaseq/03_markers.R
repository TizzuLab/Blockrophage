#!/usr/bin/env Rscript
# Part 3: what makes each macrophage cluster different?
#
# Usage: open in RStudio and press Source. Run 02_cluster.R first.
# The step follows the Seurat tutorial, "Finding differentially expressed features
# (cluster biomarkers)":
#   https://satijalab.org/seurat/articles/pbmc3k_tutorial
#
# Input:  clustered.rds from 02_cluster.R, in code/scrnaseq/output/
# Output in code/scrnaseq/output/: macrophage_markers.csv, macrophage_top_markers.png

library(Seurat)
library(ggplot2)
library(dplyr)
library(here)

out_dir <- here("code", "scrnaseq", "output")

cells <- readRDS(file.path(out_dir, "clustered.rds"))

# Your decision from 02_cluster.R: which clusters are macrophages.
macrophage_clusters <- c(1, 2, 5, 6)
macs <- subset(cells, idents = macrophage_clusters)

# Markers: genes higher in one macrophage cluster than in the other macrophage
# clusters, expressed in at least a quarter of its cells.
markers <- FindAllMarkers(macs, only.pos = TRUE, min.pct = 0.25, logfc.threshold = 0.5)
write.csv(markers, file.path(out_dir, "macrophage_markers.csv"), row.names = FALSE)

top <- markers |>
  group_by(cluster) |>
  slice_max(avg_log2FC, n = 10)
top

ggsave(file.path(out_dir, "macrophage_top_markers.png"),
       DotPlot(macs, features = unique(top$gene)) + RotatedAxis(),
       width = 14, height = 4)

# Before you run 04: which of your macrophage clusters is M1 and which is M2?
# Write it into your notebook, with the genes that made you decide.

# Questions:
# - Look up the top genes of each cluster. What do they tell you about where the
#   cells come from (resident or recruited from the blood) and what they do?
# - Did you have to choose an M1 and an M2 cluster? How sure are you?
