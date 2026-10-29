#!/usr/bin/env Rscript
# Part 5: your own signature, for the poster.
#
# Usage: open in RStudio, fill in your signature below, and press Source.
# Run 02_cluster.R first.
#
# M1 and M2 were defined in a dish. Since single-cell RNA-seq, macrophages are also
# described by the states found in tissues. Starting points (find the gene lists in
# the papers and their supplementary tables, or build your own from 03):
# - lipid-associated macrophages: Jaitin et al. 2019, Cell,
#   https://doi.org/10.1016/j.cell.2019.05.054
# - scar-associated macrophages: Ramachandran et al. 2019, Nature,
#   https://doi.org/10.1038/s41586-019-1631-3
# - three resident subsets across organs: Dick et al. 2022, Sci Immunol,
#   https://doi.org/10.1126/sciimmunol.abf7777
# - cavity macrophages and Gata6: Rosas et al. 2014, Science,
#   https://doi.org/10.1126/science.1251414
# - the injured peritoneum of this dataset: Zindel et al. 2021, Nat Commun,
#   https://doi.org/10.1038/s41467-021-27612-x
#
# Output in code/scrnaseq/output/: own_signature.png

library(Seurat)
library(ggplot2)
library(patchwork)
library(here)

out_dir <- here("code", "scrnaseq", "output")

cells <- readRDS(file.path(out_dir, "clustered.rds"))

# Your signature: mouse gene names, and where they come from.
my_signature <- c()      # e.g. c("Gene1", "Gene2", "Gene3")
signature_name <- ""     # e.g. "lipid-associated, Jaitin 2019"

table(my_signature %in% rownames(cells))

cells <- AddModuleScore(cells, features = list(my_signature), name = "own")

p <- FeaturePlot(cells, features = "own1", order = TRUE) + ggtitle(signature_name) |
  VlnPlot(cells, features = "own1", pt.size = 0) + NoLegend() + ggtitle(signature_name)
ggsave(file.path(out_dir, "own_signature.png"), p, width = 12, height = 5)

aggregate(cells$own1, list(cluster = cells$seurat_clusters), median)

# Questions:
# - Which clusters carry your signature? Does it differ between sterile and
#   contaminated (CLP) sites, per mouse?
# - Your signature came from another tissue, another disease, maybe another
#   species. What does it mean if it fits here, and what if it does not?
# - Compared with M1 and M2 in 04: which description of these macrophages would
#   you put on your poster, and why?
