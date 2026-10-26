#!/usr/bin/env python3
"""Mirror the hand-edited Gantt workbook into schedule/schedule.md.

Reads every sheet whose name starts with "Week", resolves merged cells and fill
colours (mapped back to activity blocks via the Legend sheet) and writes one
Markdown table per day: rows = Fixed / groups / staff / resources, columns =
morning / afternoon. The Markdown is what the LLM companion reads, so the Excel
stays the single source for the schedule and this file is regenerated, never
edited by hand.

Usage: python3 tools/xlsx2md.py [workbook.xlsx] [schedule.md]
"""
from __future__ import annotations

import sys
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
XLSX = ROOT / "schedule" / "Blockcourse_Gantt_FS2027.xlsx"
MD = ROOT / "schedule" / "schedule.md"

HEADER_ROWS = 5  # title, subtitle, day, half day, slot


def rgb6(cell):
    fg = cell.fill.fgColor if cell.fill and cell.fill.fill_type == "solid" else None
    if fg is None or fg.rgb is None or not isinstance(fg.rgb, str):
        return None
    return fg.rgb[-6:].upper()


def legend_map(wb):
    """fill hex -> short activity label, from the Legend sheet."""
    ws = wb["Legend"]
    m = {}
    for row in ws.iter_rows(min_row=1, max_row=60, max_col=2):
        a, b = row[0], row[1]
        h = rgb6(a)
        if h and a.value and b.value:
            m[h] = str(b.value).split(":")[0].split(" (")[0]
    return m


def merged_lookup(ws):
    """cell coordinate -> top-left anchor coordinate for merged ranges."""
    anchor = {}
    for rng in ws.merged_cells.ranges:
        tl = ws.cell(row=rng.min_row, column=rng.min_col)
        for r in range(rng.min_row, rng.max_row + 1):
            for c in range(rng.min_col, rng.max_col + 1):
                anchor[(r, c)] = tl
    return anchor


def collect(ws, anchor, legend, row, c_from, c_to):
    """Unique (label, text) pairs across a span of columns, in order."""
    out, seen = [], set()
    for c in range(c_from, c_to + 1):
        cell = anchor.get((row, c), ws.cell(row=row, column=c))
        if cell.value is None:
            continue
        key = cell.coordinate
        if key in seen:
            continue
        seen.add(key)
        label = legend.get(rgb6(cell))
        text = " ".join(str(cell.value).split())
        out.append(f"[{label}] {text}" if label and label != "Buffer / free" else text)
    return "; ".join(out) if out else "-"


def week_to_md(ws, legend):
    anchor = merged_lookup(ws)
    lines = [f"## {ws['A1'].value}", ""]
    # days from row 3 merged headers
    days = []
    for rng in ws.merged_cells.ranges:
        if rng.min_row == 3 and rng.min_col >= 2:
            days.append((rng.min_col, ws.cell(row=3, column=rng.min_col).value))
    days.sort()
    labels = []
    r = HEADER_ROWS + 1
    while ws.cell(row=r, column=1).value:
        labels.append((r, " ".join(str(ws.cell(row=r, column=1).value).split())))
        r += 1
    notes_rows = [r for r, l in labels if l.lower().startswith("notes")]
    for c0, day in days:
        lines += [f"### {day}", "", "| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |", "|---|---|---|"]
        for rr, label in labels:
            if rr in notes_rows:
                continue
            am = collect(ws, anchor, legend, rr, c0, c0 + 3)
            pm = collect(ws, anchor, legend, rr, c0 + 4, c0 + 7)
            lines.append(f"| {label} | {am} | {pm} |")
        lines.append("")
    for rr in notes_rows:
        note = collect(ws, anchor, legend, rr, 2, ws.max_column)
        if note != "-":
            lines += [f"Notes: {note}", ""]
    return lines


def main(xlsx=XLSX, md=MD):
    wb = load_workbook(xlsx)
    legend = legend_map(wb)
    out = ["# Schedule (mirror of the Gantt workbook)", "",
           f"Generated from `{Path(xlsx).name}` by `tools/xlsx2md.py`. Do not edit; edit the workbook and rerun.",
           "Activity blocks in brackets. The fixed layer is drawn by staff; group rows are the groups' own plans.", ""]
    for ws in wb.worksheets:
        if ws.title.startswith("Week"):
            out += week_to_md(ws, legend)
    # Legend rules and open items, verbatim
    ws = wb["Legend"]
    out += ["## Legend, rules and open items", ""]
    for row in ws.iter_rows(min_row=4, max_col=2):
        a, b = row[0].value, row[1].value
        if a and b and a not in ("Colour",):
            out.append(f"- **{a}**: {b}")
        elif b and not a:
            out.append(f"- {b}")
    out.append("")
    Path(md).write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {md}")


if __name__ == "__main__":
    args = sys.argv[1:]
    main(*(Path(a) for a in args))
