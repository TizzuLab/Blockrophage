#!/usr/bin/env python3
"""Write protocols/flow_panels.xlsx from the panel tables in the flow protocols.

The Markdown tables are the source: the minimal panel in C3_flow_cytometry.md and
the full panel in X02_peritoneal_cells_flow.md, each inside a <details> block. This
only copies them into a workbook, one sheet per panel, rows tinted by laser.

Usage: python3 stuff/tools/panels/flow_panels_xlsx.py
"""
import re
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[3]
SOURCES = ["C3_flow_cytometry.md", "X02_peritoneal_cells_flow.md"]
OUT = ROOT / "protocols" / "flow_panels.xlsx"

# Laser cell starts with a coloured square in Markdown; the workbook uses a tint.
TINTS = {"UV": "D9D9D9", "Violet": "E4D7F5", "Blue": "DCE9F8", "YG": "FFF4C2", "Red": "F8D7D7"}

wb = Workbook()
wb.remove(wb.active)
for name in SOURCES:
    text = (ROOT / "protocols" / name).read_text(encoding="utf-8")
    for title, body in re.findall(r"<summary><b>(.+?)</b>.*?</summary>\s*\n(.*?)</details>", text, re.S):
        rows = [l for l in body.splitlines() if l.startswith("|")]
        cells = [[c.strip().strip("`") for c in r.strip().strip("|").split("|")] for r in rows]
        cells = [r for r in cells if not set("".join(r)) <= set("-: ")]  # drop separator row
        cells = [[re.sub(r"^[^\w(]+\s*", "", r[0])] + r[1:] for r in cells]  # drop the square
        ws = wb.create_sheet(title.replace(" panel", "").strip()[:31])
        for row in cells:
            ws.append(row)
        for c in ws[1]:
            c.font = Font(bold=True)
        for row in ws.iter_rows(min_row=2):
            tint = next((v for k, v in TINTS.items() if str(row[0].value).startswith(k)), None)
            if tint:
                for c in row:
                    c.fill = PatternFill("solid", fgColor=tint)
        for i, col in enumerate(zip(*cells), start=1):
            ws.column_dimensions[get_column_letter(i)].width = min(40, max(len(v) for v in col) + 2)
        ws.freeze_panes = "A2"
assert len(wb.sheetnames) == 2, f"expected 2 panels, found {wb.sheetnames}"
wb.save(OUT)
print(f"wrote {OUT.relative_to(ROOT)} ({', '.join(wb.sheetnames)})")
