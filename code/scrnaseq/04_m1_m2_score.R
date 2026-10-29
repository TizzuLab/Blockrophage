#!/usr/bin/env Rscript
# Part 4: score every cell against M1 and M2 signatures.
#
# Usage: open in RStudio and press Source. Run 02_cluster.R first.
#
# Two kinds of signature:
# - the classic markers, from before sequencing (see Murray et al. 2014, Immunity,
#   https://doi.org/10.1016/j.immuni.2014.06.008),
# - a consensus ranking across the public RNA-seq experiments of mouse macrophages
#   stimulated in vitro (Colombo et al. 2024, PLOS ONE, https://doi.org/10.1371/journal.pone.0297872),
#   downloaded from the paper's supplementary table S1. We take the 30 top-ranked
#   genes for IFNγ (as in your M(IFNγ) wells) and for IL-4 (as in your M(IL-4) wells).
#
# A module score is the mean expression of the signature genes in a cell minus that
# of random control genes of similar expression (Tirosh et al. 2016, Science,
# https://doi.org/10.1126/science.aad0501; Seurat: https://satijalab.org/seurat/reference/addmodulescore).
#
# Input:  clustered.rds from 02_cluster.R, in code/scrnaseq/output/
# Output in code/scrnaseq/output/: scores_violin.png, scores_umap.png

library(Seurat)
library(ggplot2)
library(readxl)
library(here)

data_dir <- here("code", "scrnaseq", "data")
out_dir <- here("code", "scrnaseq", "output")

cells <- readRDS(file.path(out_dir, "clustered.rds"))

# 1. The classic markers.
classic_m1 <- c("Nos2", "Tnf", "Il1b", "Il6", "Il12b", "Cxcl9", "Cxcl10", "Cd86")
classic_m2 <- c("Arg1", "Mrc1", "Chil3", "Retnla", "Ccl17", "Ccl24", "Mgl2")

# 2. The consensus signatures, downloaded once.
colombo_file <- file.path(data_dir, "Colombo2024_S1.xlsx")
url <- "https://journals.plos.org/plosone/article/file?type=supplementary&id=10.1371/journal.pone.0297872.s001"
if (!file.exists(colombo_file)) download.file(url, colombo_file, mode = "wb")
ifng <- head(read_excel(colombo_file, sheet = "IFN UP")$Name, 30)
il4 <- head(read_excel(colombo_file, sheet = "IL4 UP")$Name, 30)
ifng
il4

# 3. Score every cell, not only the macrophages: the other cells are your control.
cells <- AddModuleScore(cells, features = list(classic_m1, classic_m2, ifng, il4), name = "score")
cells$M1_classic <- cells$score1
cells$M2_classic <- cells$score2
cells$IFNg_consensus <- cells$score3
cells$IL4_consensus <- cells$score4
scores <- c("M1_classic", "M2_classic", "IFNg_consensus", "IL4_consensus")

ggsave(file.path(out_dir, "scores_violin.png"),
       VlnPlot(cells, features = scores, pt.size = 0, ncol = 2),
       width = 12, height = 8)
ggsave(file.path(out_dir, "scores_umap.png"),
       FeaturePlot(cells, features = scores, ncol = 2, order = TRUE),
       width = 10, height = 9)

# Median score per cluster.
aggregate(cells@meta.data[scores], list(cluster = cells$seurat_clusters), median)

# Questions:
# - Compare with your notebook: are your M1 and M2 clusters from 03 the ones that
#   score highest here?
# - With the classic markers, which cluster is the most "M1"? Is it a macrophage
#   cluster at all (look back at 02)? Which genes of the classic list make that happen?
# - Classic markers versus consensus: why does the picture change? What does a list
#   of 7 genes measure that a list of 30 does not, and the other way round?
# - At the bench your RAW 264.7 cells were polarized with IFNγ or IL-4. Do the
#   tissue macrophages look like either of them? Where would they need to be?
# - You split subpopulations into two poles. Does that fit what you found in 03?
