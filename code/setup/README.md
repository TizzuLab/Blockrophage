# Setup: the R packages for the course

Install R and RStudio first (February email). Then, once, on the first Friday:

```r
source("code/setup/install.R")
```

It installs Seurat, ggplot2, dplyr, readr and patchwork from a dated snapshot of the
Posit Package Manager: the same versions for everyone, as ready-built binaries for
Windows, macOS and Linux, so nothing is compiled on your laptop. It takes about a
minute (tested: 144 packages, 415 MB) and ends by printing the versions; copy them
into your notebook.

Linux only: Seurat's clustering needs one system library, installed once with
`sudo apt install libglpk40` (Ubuntu/Debian). Windows and macOS need nothing else.

Laptop: 8 GB of memory is enough; the single-cell pipeline peaks at about 3.5 GB.
