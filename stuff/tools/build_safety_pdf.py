"""Build the printable admission sheet (safety/Blockrophage_admission_sheet.pdf)
from its ground truth, safety/README.md.

Run from the repository root:
    python stuff/tools/build_safety_pdf.py           # rebuild if the md changed
    python stuff/tools/build_safety_pdf.py --check   # only say whether the PDF is stale

Needs pandoc and xelatex (CI installs them). The PDF stores a fingerprint (sha256)
of the md in its "Keywords" field; if the fingerprint matches, nothing is rebuilt.
As long as the md contains a "[TODO", the PDF is marked as a draft.
"""

import datetime
import hashlib
import os
import re
import subprocess
import sys
import tempfile

SOURCE = "safety/README.md"
TARGET = "safety/Blockrophage_admission_sheet.pdf"
PANDOC = os.environ.get("PANDOC", "pandoc")  # e.g. PANDOC="quarto pandoc" locally

text = open(SOURCE, encoding="utf-8").read()
fingerprint = "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()

# 1. Is the PDF already up to date? Read the fingerprint stored in it.
stored = ""
if os.path.exists(TARGET):
    info = subprocess.run(["pdfinfo", TARGET], capture_output=True, text=True).stdout
    match = re.search(r"^Keywords:\s*(\S+)", info, flags=re.M)
    if match:
        stored = match.group(1)

if stored == fingerprint:
    print("Admission sheet PDF is up to date.")
    sys.exit(0)
if "--check" in sys.argv:
    print("Admission sheet PDF is stale (safety/README.md changed).")
    sys.exit(1)

# 2. Turn the web page into a print page.
draft = "[TODO" in text
lines_to_drop = [
    r"^← Back to.*\n\n",                         # link back to the course script
    r"^> \*\*Under construction\.\*\*.*\n\n",    # website notice
    r"^`\[TODO:.*\]`\n\n",                       # open TODO markers
]
for pattern in lines_to_drop:
    text = re.sub(pattern, "", text, flags=re.M)

# The title line becomes the PDF title, the rest is the body.
title, body = text.split("\n", 1)
title = title.lstrip("# ").strip()

# Checkbox and signature lines for paper.
body = body.replace("- [ ] ", r"$\square$ ")
signature_table = "| Name | Date | Signature |\n|---|---|---|\n| | | |\n"
signature_lines = (
    "\\vspace{1.2cm}\n\n"
    "\\noindent\\begin{tabular}{@{}p{0.38\\linewidth}p{0.2\\linewidth}p{0.36\\linewidth}@{}}\n"
    "\\rule{\\linewidth}{0.4pt} & \\rule{\\linewidth}{0.4pt} & \\rule{\\linewidth}{0.4pt} \\\\\n"
    "Name & Date & Signature\n"
    "\\end{tabular}\n"
)
body = body.replace(signature_table, signature_lines)

subtitle = "Version " + datetime.date.today().isoformat()
if draft:
    subtitle = "DRAFT, not yet approved for signing. " + subtitle

# 3. Render with pandoc and xelatex.
with tempfile.TemporaryDirectory() as tmp:
    md_file = os.path.join(tmp, "sheet.md")
    header_file = os.path.join(tmp, "header.tex")
    open(md_file, "w", encoding="utf-8").write(body)
    open(header_file, "w").write(
        "\\usepackage{amssymb}\n"
        "\\usepackage{etoolbox}\\AtBeginEnvironment{longtable}{\\small}\n"
    )
    command = PANDOC.split() + [
        md_file, "-o", TARGET,
        "--pdf-engine=xelatex", "-H", header_file,
        "-V", "title=" + title,
        "-V", "date=" + subtitle,
        "-V", "keywords=" + fingerprint,
        "-V", "geometry:margin=1.9cm", "-V", "fontsize=10pt",
        "-V", "mainfont=DejaVu Sans",
        "-V", "colorlinks=true", "-V", "urlcolor=blue", "-V", "linkcolor=blue",
    ]
    subprocess.run(command, check=True)

print("Wrote " + TARGET + (" (draft)" if draft else ""))
