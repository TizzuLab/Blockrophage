#!/usr/bin/env python3
"""Write protocols/C3_panels.xlsx from the panel tables in protocols/C3_flow_cytometry.md.

The Markdown tables are the source; this only copies them into a workbook with one
sheet per panel, for printing, ordering and the lab's panel workbook.

Usage: python3 stuff/tools/panels/c3_panels_xlsx.py
"""
import re
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[3]
MD = ROOT / "protocols" / "C3_flow_cytometry.md"
OUT = ROOT / "protocols" / "C3_panels.xlsx"

text = MD.read_text(encoding="utf-8")
blocks = re.findall(r"<summary><b>(.+?)</b>.*?</summary>\s*\n(.*?)</details>", text, re.S)
assert len(blocks) == 2, f"expected 2 panels, found {len(blocks)}"

wb = Workbook()
wb.remove(wb.active)
for title, body in blocks:
    rows = [l for l in body.splitlines() if l.startswith("|")]
    cells = [[c.strip().strip("`") for c in r.strip("|").split("|")] for r in rows]
    cells = [r for r in cells if not set("".join(r)) <= set("-: ")]  # drop separator row
    ws = wb.create_sheet(title.replace(" panel", "").strip()[:31])
    for row in cells:
        ws.append(row)
    for c in ws[1]:
        c.font = Font(bold=True)
        c.fill = PatternFill("solid", fgColor="DDEBF7")
    for i, col in enumerate(zip(*cells), start=1):
        ws.column_dimensions[get_column_letter(i)].width = min(40, max(len(v) for v in col) + 2)
    ws.freeze_panes = "A2"
wb.save(OUT)
print(f"wrote {OUT.relative_to(ROOT)} ({', '.join(wb.sheetnames)})")
