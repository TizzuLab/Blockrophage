#!/usr/bin/env Rscript
# ELISA standard curve and back-calculation.
#
# Usage:
#   Rscript elisa_standard_curve.R [input.csv] [output_dir]
# Defaults: example_data/il6_lps_raw264_2026-09.csv and ./output
#
# Input: one row per well with the columns
#   well, type ("standard" or "sample"), condition, standard_pg_ml (standards only),
#   lps_ng_ml (samples; optional), replicate, od450, dilution_factor
# The 0 pg/mL standard is the blank.
#
# Output: output/elisa_results.csv (per well), output/elisa_summary.csv (per
# condition), output/elisa_figure.png (standard curve + concentrations).
#
# Fit: four-parameter logistic (4PL) by nls; if that fails, a log-log linear fit
# on the non-zero standards. The console says which was used.

suppressPackageStartupMessages(library(ggplot2))

args <- commandArgs(trailingOnly = TRUE)
input <- if (length(args) >= 1) args[1] else "example_data/il6_lps_raw264_2026-09.csv"
outdir <- if (length(args) >= 2) args[2] else "output"
dir.create(outdir, showWarnings = FALSE, recursive = TRUE)

d <- read.csv(input, stringsAsFactors = FALSE)
stopifnot(all(c("well", "type", "condition", "od450") %in% names(d)))
if (!"dilution_factor" %in% names(d)) d$dilution_factor <- 1
d$dilution_factor[is.na(d$dilution_factor)] <- 1

# 1. Blank: mean OD of the 0 pg/mL standard wells.
std <- d[d$type == "standard", ]
blank <- mean(std$od450[std$standard_pg_ml == 0])
d$od_corr <- d$od450 - blank
std <- d[d$type == "standard", ]
cat(sprintf("Blank (0 pg/mL standard, n = %d): OD %.4f\n", sum(std$standard_pg_ml == 0), blank))

# 2. Standard curve.
fit_4pl <- function(x, y) {
  # a = lower asymptote, d = upper asymptote, c = inflection (pg/mL), b = slope.
  # Several start sets: a curve that is still linear at the top standard has its
  # upper asymptote far above the data, and nls needs to be told so.
  starts <- list(list(a = min(y), d = max(y) * 1.2, c = max(x), b = 1),
                 list(a = min(y), d = max(y) * 3, c = max(x) * 3, b = 1),
                 list(a = min(y), d = max(y), c = median(x[x > 0]), b = 1))
  for (st in starts) {
    m <- tryCatch(nls(y ~ d + (a - d) / (1 + (x / c)^b), start = st,
                      control = nls.control(maxiter = 1000, warnOnly = FALSE)),
                  error = function(e) NULL)
    if (!is.null(m)) return(m)
  }
  NULL
}
model <- fit_4pl(std$standard_pg_ml, std$od_corr)
if (!is.null(model)) {
  p <- coef(model)
  method <- "4PL"
  predict_od <- function(x) p["d"] + (p["a"] - p["d"]) / (1 + (x / p["c"])^p["b"])
  invert <- function(y) {
    out <- p["c"] * ((p["a"] - p["d"]) / (y - p["d"]) - 1)^(1 / p["b"])
    out[y <= p["a"]] <- 0            # at or below the lower asymptote
    out[y >= p["d"]] <- NA           # at or above the upper asymptote
    as.numeric(out)
  }
  cat(sprintf("Fit: 4PL  a = %.4f  d = %.4f  c = %.1f pg/mL  b = %.3f\n", p["a"], p["d"], p["c"], p["b"]))
} else {
  nz <- std[std$standard_pg_ml > 0 & std$od_corr > 0, ]
  lmfit <- lm(log(od_corr) ~ log(standard_pg_ml), data = nz)
  k <- coef(lmfit)
  method <- "log-log linear (4PL failed)"
  predict_od <- function(x) exp(k[1] + k[2] * log(x))
  invert <- function(y) { out <- rep(0, length(y)); ok <- y > 0; out[ok] <- exp((log(y[ok]) - k[1]) / k[2]); as.numeric(out) }
  cat(sprintf("Fit: log-log linear (4PL did not converge)  slope = %.3f\n", k[2]))
}
r2 <- 1 - sum((std$od_corr - predict_od(std$standard_pg_ml))^2) / sum((std$od_corr - mean(std$od_corr))^2)
cat(sprintf("R^2 on standards: %.4f\n", r2))

# 3. Back-calculate samples, apply dilution, flag the range.
lo <- min(std$od_corr[std$standard_pg_ml > 0]); hi <- max(std$od_corr)
top_std <- max(std$standard_pg_ml); bottom_std <- min(std$standard_pg_ml[std$standard_pg_ml > 0])
d$conc_pg_ml <- NA_real_; d$flag <- ""
s <- d$type == "sample"
d$conc_pg_ml[s] <- invert(d$od_corr[s]) * d$dilution_factor[s]
d$flag[s & d$od_corr < lo] <- sprintf("below lowest standard (%g pg/mL)", bottom_std)
d$flag[s & d$od_corr > hi] <- sprintf("above top standard (%g pg/mL)", top_std)
d$flag[s & is.na(d$conc_pg_ml)] <- "not calculable (above upper asymptote)"
d$fit <- method
write.csv(d, file.path(outdir, "elisa_results.csv"), row.names = FALSE)

samp <- d[s, ]
samp$condition <- factor(samp$condition, levels = unique(samp$condition))
summ <- aggregate(conc_pg_ml ~ condition, samp, function(v) c(mean = mean(v), sd = sd(v), n = length(v)))
summ <- data.frame(condition = summ$condition, mean_pg_ml = summ$conc_pg_ml[, "mean"],
                   sd_pg_ml = summ$conc_pg_ml[, "sd"], n = summ$conc_pg_ml[, "n"])
summ$flagged_wells <- sapply(summ$condition, function(cc) sum(samp$flag[samp$condition == cc] != ""))
write.csv(summ, file.path(outdir, "elisa_summary.csv"), row.names = FALSE)
cat("\nPer condition (pg/mL):\n"); print(summ, row.names = FALSE, digits = 4)

# 4. Figure: standard curve with samples overlaid; concentration per condition.
ink <- "#1F2933"; muted <- "#6B7280"; blue <- "#2A6EBB"; grey_pt <- "#9AA3AE"
theme_course <- theme_minimal(base_size = 11) +
  theme(panel.grid.minor = element_blank(), panel.grid.major = element_line(colour = "#E5E7EB", linewidth = 0.3),
        axis.text = element_text(colour = ink), axis.title = element_text(colour = ink),
        plot.title = element_text(colour = ink, face = "bold", size = 11),
        plot.subtitle = element_text(colour = muted, size = 9), plot.background = element_rect(fill = "white", colour = NA))

# The curve is drawn well beyond the standards so that the whole sigmoid is visible:
# the kit range usually sits on the lower, nearly linear limb, and the upper plateau
# of the 4PL often lies above what the reader can measure. The shaded band is the
# range the standards cover; only samples inside it are trusted.
if (method == "4PL") {
  xmin <- min(bottom_std / 10, p["c"] / 300)
  xmax <- max(top_std * 10, p["c"] * 300)
} else {
  xmin <- bottom_std / 10; xmax <- top_std * 10
}
curve <- data.frame(x = exp(seq(log(xmin), log(xmax), length.out = 400)))
curve$y <- predict_od(curve$x)
std_plot <- std[std$standard_pg_ml > 0, ]
samp_plot <- samp[!is.na(samp$conc_pg_ml) & samp$conc_pg_ml > 0, ]
ymax <- if (method == "4PL") max(p["d"], max(std$od_corr)) * 1.05 else max(curve$y) * 1.05
log_breaks <- 10^seq(floor(log10(xmin)), ceiling(log10(xmax)))
p1 <- ggplot() +
  annotate("rect", xmin = bottom_std, xmax = top_std, ymin = -Inf, ymax = Inf, fill = "#E8F0FA", alpha = 0.6) +
  annotate("text", x = sqrt(bottom_std * top_std), y = ymax * 0.72, label = sprintf("kit range\n%s to %s pg/mL", signif(bottom_std, 3), signif(top_std, 3)),
           size = 3, colour = muted) +
  geom_line(data = curve, aes(x, y), colour = ink, linewidth = 0.6) +
  geom_point(data = std_plot, aes(standard_pg_ml, od_corr), shape = 21, fill = "white", colour = ink, size = 2.4, stroke = 0.6) +
  geom_point(data = samp_plot, aes(conc_pg_ml, od_corr), colour = blue, size = 2.4) +
  scale_x_log10(breaks = log_breaks, labels = function(v) format(v, big.mark = ",", scientific = FALSE, trim = TRUE)) +
  scale_y_continuous(limits = c(0, ymax), expand = expansion(mult = c(0, 0.02))) +
  labs(x = "IL-6 (pg/mL, log scale)", y = "OD 450 nm, blank-subtracted",
       title = "Standard curve, drawn to both plateaus",
       subtitle = sprintf("%s fit, R² = %.3f. Open circles: standards. Blue: samples.", method, r2)) +
  theme_course
if (method == "4PL") {
  p1 <- p1 +
    geom_hline(yintercept = c(p["a"], p["d"]), linetype = "22", colour = muted, linewidth = 0.4) +
    annotate("text", x = xmax, y = p["d"], label = sprintf("upper plateau, OD %.1f (beyond the reader)", p["d"]),
             hjust = 1, vjust = 1.5, size = 3, colour = muted) +
    annotate("text", x = xmax, y = p["a"], label = sprintf("lower plateau, OD %.2f", p["a"]),
             hjust = 1, vjust = -0.5, size = 3, colour = muted) +
    geom_vline(xintercept = p["c"], linetype = "22", colour = muted, linewidth = 0.4) +
    annotate("text", x = p["c"], y = ymax * 0.3, label = sprintf("inflection\nc = %.0f pg/mL", p["c"]),
             hjust = -0.08, size = 3, colour = muted)
}

summ$x <- as.numeric(summ$condition); samp$x <- as.numeric(samp$condition)
p2 <- ggplot() +
  geom_col(data = summ, aes(x = condition, y = mean_pg_ml), fill = NA, colour = blue, width = 0.6, linewidth = 0.6) +
  geom_errorbar(data = summ, aes(x = condition, ymin = mean_pg_ml - sd_pg_ml, ymax = mean_pg_ml + sd_pg_ml), width = 0.2, colour = blue, linewidth = 0.5) +
  geom_jitter(data = samp, aes(x = condition, y = conc_pg_ml), width = 0.08, height = 0, colour = blue, size = 2.2, alpha = 0.9) +
  geom_text(data = summ, aes(x = condition, y = mean_pg_ml + sd_pg_ml, label = sprintf("%.0f", mean_pg_ml)), vjust = -0.6, size = 3.2, colour = ink) +
  scale_y_continuous(expand = expansion(mult = c(0, 0.12))) +
  labs(x = NULL, y = "IL-6 (pg/mL)", title = "IL-6 per condition",
       subtitle = "Bar: mean ± SD of triplicate wells. Points: wells.") +
  theme_course + theme(axis.text.x = element_text(angle = 20, hjust = 1))

png(file.path(outdir, "elisa_figure.png"), width = 2000, height = 850, res = 200)
grid::grid.newpage()
grid::pushViewport(grid::viewport(layout = grid::grid.layout(1, 2)))
print(p1, vp = grid::viewport(layout.pos.row = 1, layout.pos.col = 1))
print(p2, vp = grid::viewport(layout.pos.row = 1, layout.pos.col = 2))
invisible(dev.off())
cat(sprintf("\nWrote %s, %s and %s\n", file.path(outdir, "elisa_results.csv"), file.path(outdir, "elisa_summary.csv"), file.path(outdir, "elisa_figure.png")))
