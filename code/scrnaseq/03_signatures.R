#!/usr/bin/env Rscript
# Part 2: derive the M(IFNγ+LPS) and M(IL-4) signatures from bulk RNA-seq of RAW 264.7.
#
# Usage: open in RStudio and press Source. Run 01_load_and_qc.R first: this script
# uses its gene table to turn Ensembl IDs into gene names.
#
# The steps follow the DESeq2 vignette, read it alongside:
#   https://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html
#   Love, Huber & Anders 2014, Genome Biology, https://doi.org/10.1186/s13059-014-0550-8
#
# Data: GSE113836 (Huffaker et al. 2021, Nat Commun,
# https://doi.org/10.1038/s41467-021-22923-5). RAW 264.7 and bone marrow macrophages,
# each in medium, LPS + IFNγ ("M1") or IL-4 ("M2"), two replicates each; raw counts.
#
# Output in code/scrnaseq/output/: pca_bulk.png, ma_plots.png,
#         deg_M1_vs_medium.csv, deg_M2_vs_medium.csv,
#         signature_M1.txt, signature_M2.txt (for part 3)

library(DESeq2)
library(ggplot2)
library(here)

data_dir <- here("code", "scrnaseq", "data")
out_dir <- here("code", "scrnaseq", "output")

# 1. Download the count table once.
counts_file <- file.path(data_dir, "GSE113836_counts_10625R.txt.gz")
url <- "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE113nnn/GSE113836/suppl/GSE113836_counts_10625R.txt.gz"
if (!file.exists(counts_file)) download.file(url, counts_file, mode = "wb")

counts <- as.matrix(read.delim(counts_file, row.names = 1, check.names = FALSE))

# 2. The sample sheet, written from the GEO sample descriptions (GSM3120946-57).
samples <- data.frame(row.names = colnames(counts),
                      cells = rep(c("RAW", "BMM"), each = 6),
                      treatment = rep(rep(c("medium", "M1", "M2"), each = 2), times = 2))
samples$treatment <- factor(samples$treatment, levels = c("medium", "M1", "M2"))
samples

# The course works with RAW 264.7, so only those six samples.
raw <- samples$cells == "RAW"
dds <- DESeqDataSetFromMatrix(countData = counts[, raw],
                              colData = samples[raw, ],
                              design = ~ treatment)

# Pre-filtering as in the vignette: keep genes with at least 10 reads in at least
# as many samples as the smallest group (here 2).
keep <- rowSums(counts(dds) >= 10) >= 2
dds <- dds[keep, ]

# 3. Look before you test: do the replicates sit together?
vsd <- vst(dds)
ggsave(file.path(out_dir, "pca_bulk.png"),
       plotPCA(vsd, intgroup = "treatment") + theme_classic(), width = 5.5, height = 4)

# 4. Differential expression, each stimulus against medium.
dds <- DESeq(dds)
res_m1 <- results(dds, contrast = c("treatment", "M1", "medium"), alpha = 0.05)
res_m2 <- results(dds, contrast = c("treatment", "M2", "medium"), alpha = 0.05)
summary(res_m1)
summary(res_m2)

png(file.path(out_dir, "ma_plots.png"), width = 2000, height = 900, res = 200)
par(mfrow = c(1, 2))
plotMA(res_m1, ylim = c(-8, 8), main = "LPS + IFNγ vs medium")
plotMA(res_m2, ylim = c(-8, 8), main = "IL-4 vs medium")
dev.off()

# Gene names from the 10x gene table downloaded in part 1 (same names as in the
# single-cell object, which matters for scoring in part 3).
genes <- read.delim(file.path(data_dir, "GSM5658643_B24h1_features.tsv.gz"), header = FALSE)
res_m1$gene <- genes$V2[match(rownames(res_m1), genes$V1)]
res_m2$gene <- genes$V2[match(rownames(res_m2), genes$V1)]

write.csv(as.data.frame(res_m1[order(res_m1$padj), ]), file.path(out_dir, "deg_M1_vs_medium.csv"))
write.csv(as.data.frame(res_m2[order(res_m2$padj), ]), file.path(out_dir, "deg_M2_vs_medium.csv"))

# 5. The signature: a stated rule. Here: up-regulated at least 4-fold
# (log2 fold change > 2) with adjusted p < 0.05, the 50 with the smallest adjusted
# p-value. Change the rule, say why in your notebook, and see what it does in part 3.
signature <- function(res, n = 50) {
  up <- res[which(res$padj < 0.05 & res$log2FoldChange > 2 & !is.na(res$gene)), ]
  head(up$gene[order(up$padj)], n)
}
sig_m1 <- signature(res_m1)
sig_m2 <- signature(res_m2)
sig_m1
sig_m2
writeLines(sig_m1, file.path(out_dir, "signature_M1.txt"))
writeLines(sig_m2, file.path(out_dir, "signature_M2.txt"))

# Compare with the literature: which of your genes are in the Murray et al. 2014
# table and in the consolidated sets of Colombo et al. 2024 (background reading)?

# Questions:
# - Two replicates per group is the minimum. What does that do to the adjusted
#   p-values, and to how far you trust a single gene?
# - The vignette shrinks the fold changes before ranking genes (lfcShrink). Why,
#   and does it change your top 50?
# - The same data contain bone marrow macrophages (BMM). Derive the signatures there
#   too: how much do a cell line and primary cells agree?
# - The other standard: limma-voom, with Glimma for interactive plots you can click
#   through in the browser (glimmaMDS, glimmaMA). Follow the RNA-seq workflow
#   "RNA-seq analysis is easy as 1-2-3 with limma, Glimma and edgeR"
#   (Law et al. 2016, F1000Research, https://doi.org/10.12688/f1000research.9005.3):
#   https://bioconductor.org/packages/release/workflows/vignettes/RNAseq123/inst/doc/limmaWorkflow.html
#   Do DESeq2 and limma-voom give you the same signature?
