#!/usr/bin/env Rscript
# Part 3: score every macrophage in the tissue against the M1 and M2 signatures.
#
# Usage: open in RStudio and press Source. Run 02_cluster.R and 03_signatures.R first.
#
# A module score is the mean expression of the signature genes in a cell minus the
# mean expression of control genes picked at random from genes of similar overall
# expression (Tirosh et al. 2016, Science, https://doi.org/10.1126/science.aad0501).
# Read the Seurat help page and the cell-cycle vignette, which uses the same idea:
#   https://satijalab.org/seurat/reference/addmodulescore
#   https://satijalab.org/seurat/articles/cell_cycle_vignette
#
# Input:  clustered.rds, signature_M1.txt, signature_M2.txt, in code/scrnaseq/output/
# Output in code/scrnaseq/output/: umap_scores.png, scores_scatter.png,
#         scores_violin.png, scores_per_cell.csv

library(Seurat)
library(ggplot2)
library(patchwork)
library(here)

out_dir <- here("code", "scrnaseq", "output")

cells <- readRDS(file.path(out_dir, "clustered.rds"))
sig_m1 <- readLines(file.path(out_dir, "signature_M1.txt"))
sig_m2 <- readLines(file.path(out_dir, "signature_M2.txt"))

# Your decision from 02_cluster.R: which clusters are macrophages. Write the reason
# into your notebook.
macrophage_clusters <- c(1, 2, 5, 6)

# 1. Score every cell. Genes missing from the single-cell data are left out (Seurat
# warns); check how many of each signature are actually used.
table(sig_m1 %in% rownames(cells))
table(sig_m2 %in% rownames(cells))
set.seed(1)   # the control genes are drawn at random
cells <- AddModuleScore(cells, features = list(sig_m1, sig_m2), name = "score_M")
# The new columns are score_M1 and score_M2.

# 2. On the UMAP: where in the tissue are the two signatures?
p <- FeaturePlot(cells, features = c("score_M1", "score_M2"), split.by = "condition",
                 order = TRUE, keep.scale = "feature") & theme_classic()
ggsave(file.path(out_dir, "umap_scores.png"), p, width = 10, height = 9)

# 3. The macrophages only: the two scores against each other.
macs <- subset(cells, idents = macrophage_clusters)
scores <- FetchData(macs, vars = c("seurat_clusters", "sample", "condition",
                                   "score_M1", "score_M2"))

# Cut-off for calling a cell "high": a score above 0 means the signature genes are
# higher than their random controls. That is a choice; say why you keep or change it.
cutoff <- 0
scores$call <- ifelse(scores$score_M1 > cutoff,
                      ifelse(scores$score_M2 > cutoff, "both", "M1 only"),
                      ifelse(scores$score_M2 > cutoff, "M2 only", "neither"))

p <- ggplot(scores, aes(score_M1, score_M2, colour = seurat_clusters)) +
  geom_point(size = 0.4) +
  geom_hline(yintercept = cutoff, linetype = "dashed") +
  geom_vline(xintercept = cutoff, linetype = "dashed") +
  facet_wrap(~ condition) +
  labs(x = "M1 score (LPS + IFNγ)", y = "M2 score (IL-4)", colour = "cluster") +
  theme_classic()
ggsave(file.path(out_dir, "scores_scatter.png"), p, width = 9, height = 4.5)

p <- VlnPlot(macs, features = c("score_M1", "score_M2"), group.by = "seurat_clusters",
             split.by = "condition", pt.size = 0) & theme_classic()
ggsave(file.path(out_dir, "scores_violin.png"), p, width = 10, height = 4.5)

# 4. How much of the tissue population does either signature explain?
round(100 * prop.table(table(scores$condition, scores$call), margin = 1), 1)
cor(scores$score_M1, scores$score_M2)
aggregate(cbind(score_M1, score_M2) ~ sample, data = scores, FUN = median)

write.csv(scores, file.path(out_dir, "scores_per_cell.csv"))
cat("Scored", ncol(macs), "macrophages in clusters",
    paste(macrophage_clusters, collapse = ", "), ".\n")

# Questions:
# - A module score is relative: relative to what? Score only the macrophages
#   (subset first, then AddModuleScore) and compare. Does the share of "high"
#   cells change, and why?
# - M1 has 50 genes, M2 only 20. What does that do to the spread of each score,
#   and can you compare an M1 score of 0.3 with an M2 score of 0.3?
# - What does a cell with both scores high mean for the M1/M2 axis? Is it one
#   axis, two, or something the in vitro stimuli do not capture at all?
# - Which cells outside your macrophage clusters score high, and does that change
#   how you read the macrophage result?
# - Do the scores shift from sterile to contaminated (CLP)? Two mice per condition:
#   compare per sample (scores$sample), not per cell. Why?
# - Change the signature rule in 03 (more genes, a stricter fold change): which of
#   your answers here survive?
