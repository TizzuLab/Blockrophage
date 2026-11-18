# Flow panels: emission spectra of every dye, one row per laser.
#
# Why: two dyes excited by the same laser and emitting close together spill into
# each other's detectors. Seeing the curves on top of each other shows where
# compensation will matter (C3 minimal panel, X02 full panel).
#
# Data: public spectra from FPbase (https://www.fpbase.org; Lambert, Nat Methods
# 2019), downloaded when you run the script, so you need internet. Nothing is
# stored in the repository.
#
# Output: protocols/figures/C3_minimal_panel_spectra.png and
#         protocols/figures/X02_full_panel_spectra.png

## load packages
library(ggplot2)
library(dplyr)
library(here)

# 1. The panels. One row per dye: the laser that excites it, the target, and the
#    FPbase spectrum id of its emission spectrum (look ids up on fpbase.org,
#    "Spectra viewer", or ask us). Keep this in step with the panel tables in
#    protocols/C3_flow_cytometry.md and protocols/X02_peritoneal_cells_flow.md.
#    BV786 (BD) is plotted with the spectrum of BV785 (BioLegend), the same dye.

panel <- tribble(
  ~dye,             ~target,      ~laser,          ~fpbase_em, ~minimal,
  "BUV395",         "F4/80",      "UV 355 nm",      4727,      FALSE,
  "BUV496",         "CD45",       "UV 355 nm",      4729,      FALSE,
  "BUV563",         "CD11c",      "UV 355 nm",      4731,      FALSE,
  "BV421",          "CD86",       "Violet 405 nm",  4739,      TRUE,
  "eFluor 506",     "live/dead",  "Violet 405 nm",  4205,      TRUE,
  "BV605",          "CD3",        "Violet 405 nm",  4745,      FALSE,
  "BV650",          "CD206",      "Violet 405 nm",  4747,      TRUE,
  "BV786",          "CD117",      "Violet 405 nm",  4753,      FALSE,
  "AF488",          "Ly-6G",      "Blue 488 nm",    205,       FALSE,
  "Spark Blue 550", "CD19",       "Blue 488 nm",    6632,      FALSE,
  "PerCP-Cy5.5",    "Ly-6C",      "Blue 488 nm",    4545,      FALSE,
  "PE-Dazzle 594",  "Siglec-F",   "YG 561 nm",      4799,      FALSE,
  "PE-Cy7",         "Arg1",       "YG 561 nm",      4336,      TRUE,
  "AF700",          "MHCII",      "Red 637 nm",     197,       TRUE,
  "APC-Cy7",        "CD11b",      "Red 637 nm",     4715,      FALSE
)

lasers <- c("UV 355 nm" = 355, "Violet 405 nm" = 405, "Blue 488 nm" = 488,
            "YG 561 nm" = 561, "Red 637 nm" = 637)

# 2. Download the spectra: one CSV, a wavelength column plus one column per dye.
url <- paste0("https://www.fpbase.org/spectra_csv/?q=",
              paste(panel$fpbase_em, collapse = ","))
wide <- read.csv(url, check.names = FALSE)

# The columns are named after FPbase's dye names plus " em", in no fixed order;
# this lookup maps them back to the names we use in the panel.
fpbase_names <- c(
  "BD Horizon BUV395" = "BUV395", "BD Horizon BUV496" = "BUV496",
  "BD Horizon BUV563" = "BUV563", "Brilliant Violet 421" = "BV421",
  "Fixable Viability Dye eFluor 506" = "eFluor 506",
  "Brilliant Violet 605" = "BV605", "Brilliant Violet 650" = "BV650",
  "Brilliant Violet 785" = "BV786", "Alexa Fluor 488" = "AF488",
  "Spark Blue 550" = "Spark Blue 550", "PerCP-Cy5.5" = "PerCP-Cy5.5",
  "PE/Dazzle 594" = "PE-Dazzle 594", "PE-Cy7" = "PE-Cy7",
  "Alexa Fluor 700" = "AF700", "APC/Cy7" = "APC-Cy7")

# 3. Long format: one row per dye and wavelength, emission scaled to a peak of 1.
spectra <- bind_rows(lapply(names(wide)[-1], function(col) {
  data.frame(dye = fpbase_names[[sub(" em$", "", col)]],
             wavelength = wide$wavelength,
             emission = wide[[col]])
})) |>
  filter(!is.na(emission), wavelength <= 850) |>
  group_by(dye) |>
  mutate(emission = emission / max(emission)) |>
  ungroup() |>
  left_join(panel, by = "dye") |>
  mutate(laser = factor(laser, levels = names(lasers)),
         label = paste0(dye, "\n", target))

# 4. Colour every dye by the colour of light at its emission peak (what the eye
#    would see), dark red for the far red and infrared it cannot see.
wavelength_colour <- function(nm) {
  r <- g <- b <- 0
  if (nm < 440)      { r <- (440 - nm) / 60; b <- 1 }
  else if (nm < 490) { g <- (nm - 440) / 50; b <- 1 }
  else if (nm < 510) { g <- 1; b <- (510 - nm) / 20 }
  else if (nm < 580) { r <- (nm - 510) / 70; g <- 1 }
  else if (nm < 645) { r <- 1; g <- (645 - nm) / 65 }
  else               { r <- 1 }
  dim <- if (nm < 420) 0.4 + 0.6 * (nm - 380) / 40 else if (nm > 700) max(0.35, 1 - (nm - 700) / 150) else 1
  rgb(max(r, 0) * dim, max(g, 0) * dim, max(b, 0) * dim)
}

peaks <- spectra |>
  group_by(dye, label, laser, minimal) |>
  slice_max(emission, n = 1, with_ties = FALSE) |>
  ungroup()

# Labels sit above the peak; when two peaks of one laser are closer than 40 nm,
# the second label goes one step higher so they do not overlap.
stagger <- function(pk) {
  pk |>
    arrange(laser, wavelength) |>
    group_by(laser) |>
    mutate(label_y = ifelse(c(Inf, diff(wavelength)) < 40, 1.45, 1.03)) |>
    ungroup()
}
dye_colours <- setNames(sapply(pmax(peaks$wavelength, 380), wavelength_colour), peaks$dye)

# 5. The figure: one row per laser, the laser line dashed, each dye labelled at
#    its peak.
plot_panel <- function(spec, pk, title) {
  laser_lines <- data.frame(laser = factor(names(lasers), levels = names(lasers)),
                            nm = lasers) |>
    filter(laser %in% spec$laser)
  ggplot(spec, aes(wavelength, emission, fill = dye, colour = dye)) +
    geom_vline(data = laser_lines, aes(xintercept = nm), linetype = "dashed",
               colour = "grey40", inherit.aes = FALSE) +
    geom_area(alpha = 0.35, position = "identity", linewidth = 0.6) +
    geom_text(data = stagger(pk), aes(y = label_y, label = label), vjust = 0, size = 2.8,
              lineheight = 0.9, show.legend = FALSE) +
    facet_wrap(~ laser, ncol = 1, drop = TRUE) +
    scale_fill_manual(values = dye_colours, guide = "none") +
    scale_colour_manual(values = dye_colours, guide = "none") +
    scale_x_continuous(breaks = seq(350, 850, 50)) +
    scale_y_continuous(breaks = c(0, 0.5, 1)) +
    coord_cartesian(xlim = c(340, 850), ylim = c(0, 1.8)) +
    labs(title = title, x = "Wavelength (nm)", y = "Emission (normalized)",
         caption = "Spectra: FPbase.org. Dashed line: excitation laser.") +
    theme_minimal(base_size = 10) +
    theme(panel.grid.minor = element_blank(),
          strip.text = element_text(face = "bold", hjust = 0))
}

figdir <- here("protocols", "figures")

minimal <- plot_panel(filter(spectra, minimal), filter(peaks, minimal),
                      "C3 minimal panel: emission spectra by laser")
ggsave(file.path(figdir, "C3_minimal_panel_spectra.png"), minimal,
       width = 7, height = 4, dpi = 200, bg = "white")

full <- plot_panel(spectra, peaks, "X02 full panel: emission spectra by laser")
ggsave(file.path(figdir, "X02_full_panel_spectra.png"), full,
       width = 7, height = 8, dpi = 200, bg = "white")
