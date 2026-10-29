# ELISA: standard curve and back-calculation of the samples.
#
# Open in RStudio and press Source. Paths are built with here() from the repository
# folder.
#
# Input: one row per well with the columns
#   well, type ("standard" or "sample"), condition, standard_pg_ml (standards only),
#   replicate, od450, dilution_factor
# The 0 pg/mL standard is the blank.
#
# Output in code/elisa/output/: elisa_results.csv (per well),
# elisa_summary.csv (per condition), elisa_figure.png

## load packages
library(ggplot2)
library(dplyr)
library(patchwork)
library(here)

# input
# replace csv file name with your data
input <- here("code", "elisa", "example_data", "il6_lps_raw264_2026-09.csv")

# output
outdir <- here("code", "elisa", "output")
dir.create(outdir, showWarnings = FALSE)

plate <- read.csv(input)

# 1. Blank: mean OD of the 0 pg/mL standard wells, subtracted from every well.
blank <- mean(plate$od450[plate$type == "standard" & plate$standard_pg_ml == 0])
plate$od_corr <- plate$od450 - blank
std <- plate[plate$type == "standard", ]
blank

# 2. Standard curve: four-parameter logistic (4PL)
#   OD = d + (a - d) / (1 + (conc / c)^b)
#   a = OD without IL-6 (lower plateau), d = OD with unlimited IL-6 (upper plateau),
#   c = concentration halfway between the plateaus, b = steepness.
# nls finds a, b, c, d by trial and improvement and needs a first guess:
# a = lowest OD, d = a bit above the highest OD, c = top standard, b = 1.
model <- nls(od_corr ~ d + (a - d) / (1 + (standard_pg_ml / c)^b),
             data = std,
             start = list(a = min(std$od_corr), d = max(std$od_corr) * 1.2,
                          c = max(std$standard_pg_ml), b = 1))
p <- coef(model)
p

# The same formula solved for the concentration: OD in, pg/mL out.
od_to_conc <- function(od) {
  p["c"] * ((p["a"] - p["d"]) / (od - p["d"]) - 1)^(1 / p["b"])
}

# How well does the curve fit the standards? R² = 1 - (spread left around the
# curve) / (total spread of the standard ODs). 1 is a perfect fit; a good ELISA
# standard curve is above 0.99.
r2 <- 1 - sum(residuals(model)^2) / sum((std$od_corr - mean(std$od_corr))^2)
r2
# Question: how would you validate R²? A single number can hide where the curve
# misses. Consider plotting it, e.g. residuals(model) against the standard
# concentration, or each standard's known vs back-calculated value.

# 3. Samples: concentration from the curve, times the dilution.
# Only wells between the lowest and the top standard are trusted (in_range).
lowest_std <- min(std$standard_pg_ml[std$standard_pg_ml > 0])
top_std <- max(std$standard_pg_ml)
samp <- plate[plate$type == "sample", ]
samp$conc_pg_ml <- od_to_conc(samp$od_corr) * samp$dilution_factor
samp$conc_pg_ml[samp$od_corr <= p["a"]] <- 0   # at or below the blank: no IL-6 detected
samp$in_range <- samp$od_corr >= min(std$od_corr[std$standard_pg_ml == lowest_std]) &
                 samp$od_corr <= max(std$od_corr[std$standard_pg_ml == top_std])
samp$condition <- factor(samp$condition, levels = unique(samp$condition))
write.csv(samp, file.path(outdir, "elisa_results.csv"), row.names = FALSE)

summ <- samp |>
  group_by(condition) |>
  summarise(mean_pg_ml = mean(conc_pg_ml), sd_pg_ml = sd(conc_pg_ml),
            n = n(), out_of_range = sum(!in_range))
write.csv(summ, file.path(outdir, "elisa_summary.csv"), row.names = FALSE)
summ

# 4. Figure.
# Left: the curve drawn far beyond the standards so the whole S-shape is visible.
# The standards (shaded) usually cover only the lower, nearly straight part.
curve <- data.frame(standard_pg_ml = 10^seq(-1, 6, length.out = 400))
curve$od_corr <- predict(model, newdata = curve)

p1 <- ggplot() +
  annotate("rect", xmin = lowest_std, xmax = top_std, ymin = -Inf, ymax = Inf,
           fill = "lightblue", alpha = 0.3) +
  geom_hline(yintercept = c(p["a"], p["d"]), linetype = "dashed", colour = "grey50") +
  geom_vline(xintercept = p["c"], linetype = "dashed", colour = "grey50") +
  geom_line(data = curve, aes(standard_pg_ml, od_corr)) +
  geom_point(data = std[std$standard_pg_ml > 0, ], aes(standard_pg_ml, od_corr), shape = 21, fill = "white") +
  geom_point(data = samp[samp$conc_pg_ml > 0, ], aes(conc_pg_ml, od_corr), colour = "steelblue") +
  scale_x_log10() +
  labs(x = "IL-6 (pg/mL, log scale)", y = "OD 450 nm, blank-subtracted",
       title = sprintf("Standard curve, 4PL, R² = %.3f", r2),
       subtitle = "Shaded: standards. Dashed: plateaus a, d and midpoint c.\nOpen circles: standards. Blue: samples.") +
  theme_classic()

# Right: concentration per condition, mean ± SD and the single wells.
p2 <- ggplot(summ, aes(condition, mean_pg_ml)) +
  geom_col(fill = NA, colour = "steelblue", width = 0.6) +
  geom_errorbar(aes(ymin = mean_pg_ml - sd_pg_ml, ymax = mean_pg_ml + sd_pg_ml), width = 0.2) +
  geom_jitter(data = samp, aes(condition, conc_pg_ml), width = 0.08, height = 0, colour = "steelblue") +
  labs(x = NULL, y = "IL-6 (pg/mL)", title = "IL-6 per condition",
       subtitle = "Bar: mean ± SD of triplicate wells. Points: wells.") +
  theme_classic() +
  theme(axis.text.x = element_text(angle = 20, hjust = 1))

p1 + p2
ggsave(file.path(outdir, "elisa_figure.png"), p1 + p2, width = 10, height = 4.25)
