# Install the R packages for the course, once, on the first Friday.
# Run in RStudio: open this file and press Source, or in the console:
#   source("code/setup/install.R")
#
# Packages come from a dated snapshot of the Posit Package Manager, so everyone
# gets the same versions, as ready-built binaries for Windows, macOS and Linux
# (nothing is compiled on your laptop). Change the date only between course years.

snapshot <- "2026-10-01"

repo <- paste0("https://packagemanager.posit.co/cran/", snapshot)
if (Sys.info()[["sysname"]] == "Linux") {
  codename <- system("lsb_release -cs", intern = TRUE)  # e.g. noble
  repo <- paste0("https://packagemanager.posit.co/cran/__linux__/", codename, "/", snapshot)
  # Linux binaries are only served when R names its version and platform.
  options(HTTPUserAgent = sprintf("R/%s R (%s)", getRversion(),
    paste(getRversion(), R.version$platform, R.version$arch, R.version$os)))
}
options(repos = c(CRAN = repo))

packages <- c(
  "Seurat",     # single-cell analysis (in silico arm)
  "ggplot2",    # figures
  "dplyr",      # tables
  "readr",      # reading CSV files
  "patchwork"   # putting figures side by side
)

install.packages(packages)

# Check: every package loads, and print the versions for your notebook.
for (p in packages) library(p, character.only = TRUE)
cat("\nAll packages loaded. R", R.version$major, ".", R.version$minor, "\n", sep = "")
print(sapply(packages, function(p) as.character(packageVersion(p))))
