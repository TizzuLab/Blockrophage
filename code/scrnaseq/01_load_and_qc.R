#!/usr/bin/env Rscript
# Part 1a: download, load and quality-control the single-cell data.
#
# Usage: open in RStudio and press Source, or Rscript code/scrnaseq/01_load_and_qc.R
# Paths are built with here() from the repository folder; R's working directory
# must be inside the repository (always the case in the RStudio project).
#
# Data: GSE186658 (Zindel et al. 2021, Nat Commun), mouse peritoneal injury sites
# ("buttons") 24 h after surgery, sterile (B24h) or with microbial contamination by
# cecal ligation and puncture (BCLP24h), two mice each, 10x Genomics. GEO holds the
# filtered count matrices, 110 MB; they are downloaded once into code/scrnaseq/data/.
#
# Output in code/scrnaseq/output/: qc_violins.png, qc_cells_per_sample.csv,
#         after_qc.rds (the filtered object for 02_cluster.R)

library(Seurat)
library(ggplot2)
library(here)

data_dir <- here("code", "scrnaseq", "data")
out_dir <- here("code", "scrnaseq", "output")
dir.create(data_dir, showWarnings = FALSE)
dir.create(out_dir, showWarnings = FALSE)

# 1. Download once and check that the file is complete.
tar_file <- file.path(data_dir, "GSE186658_RAW.tar")
url <- "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE186nnn/GSE186658/suppl/GSE186658_RAW.tar"
if (!file.exists(tar_file)) {
  options(timeout = 600)
  download.file(url, tar_file, mode = "wb")
}
stopifnot(tools::md5sum(tar_file) == "f63ee50eaeccb04c07502c55d8d49a31")
if (length(list.files(data_dir, pattern = "matrix.mtx.gz$")) < 4) {
  untar(tar_file, exdir = data_dir, tar = "internal")
}

# 2. One Seurat object per sample, then merged into one.
samples <- c("GSM5658643_B24h1", "GSM5658644_B24h2",
             "GSM5658645_BCLP24h1", "GSM5658646_BCLP24h2")
objects <- lapply(samples, function(s) {
  counts <- ReadMtx(mtx      = file.path(data_dir, paste0(s, "_matrix.mtx.gz")),
                    cells    = file.path(data_dir, paste0(s, "_barcodes.tsv.gz")),
                    features = file.path(data_dir, paste0(s, "_features.tsv.gz")))
  CreateSeuratObject(counts, project = sub("^GSM[0-9]+_", "", s), min.cells = 3)
})
cells <- merge(objects[[1]], objects[-1], add.cell.ids = sub("^GSM[0-9]+_", "", samples))
cells <- JoinLayers(cells)
cells$sample <- cells$orig.ident
cells$condition <- ifelse(grepl("CLP", cells$sample), "contaminated (CLP)", "sterile")

# 3. Quality metrics: genes and molecules per cell, and the share of mitochondrial
# reads (high in dying cells).
cells[["percent_mt"]] <- PercentageFeatureSet(cells, pattern = "^mt-")

p <- VlnPlot(cells, features = c("nFeature_RNA", "nCount_RNA", "percent_mt"),
             group.by = "sample", pt.size = 0, ncol = 3)
ggsave(file.path(out_dir, "qc_violins.png"), p, width = 12, height = 4.5)

# 4. Filter. Look at qc_violins.png first: these thresholds are a starting point,
# and the choice goes into your notebook with the reason.
min_genes <- 200
max_genes <- 6000
max_mt <- 10
before <- table(cells$sample)
cells <- subset(cells, nFeature_RNA > min_genes & nFeature_RNA < max_genes & percent_mt < max_mt)
after <- table(cells$sample)

qc <- data.frame(sample = names(before), before = as.vector(before), after = as.vector(after[names(before)]))
write.csv(qc, file.path(out_dir, "qc_cells_per_sample.csv"), row.names = FALSE)
print(qc)

saveRDS(cells, file.path(out_dir, "after_qc.rds"))
cat("Kept", ncol(cells), "cells. Next: 02_cluster.R\n")
