#!/usr/bin/env python3
"""Mirror the hand-edited Gantt workbook into schedule/schedule.md.

Reads every sheet whose name starts with "Week", resolves merged cells and fill
colours (mapped back to activity blocks via the Legend sheet) and writes:

- schedule/week-N.svg: one colour-coded Gantt drawing per week (GitHub renders
  SVG inside Markdown, it cannot render the workbook itself),
- schedule/schedule.md: the drawings plus one text table per day, which is what
  the LLM companion reads,
- schedule/schedule.html: a standalone page with the drawings, for embedding.

The Excel stays the single source for the schedule; these files are regenerated,
never edited by hand.

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


import html as _html
import textwrap

LABEL_W, SLOT_W = 200, 64
HEADER_H = (26, 20, 18)
ROW_H = {"fixed": 72, "group": 96, "staff": 72, "resources": 60, "notes": 48}
FONT_SIZE = 11
CHAR_W = 6.3


def row_kind(label):
    l = label.lower()
    if l.startswith("fixed"): return "fixed"
    if l.startswith("group"): return "group"
    if l.startswith("staff"): return "staff"
    if l.startswith("resources"): return "resources"
    if l.startswith("notes"): return "notes"
    return "group"


def font_rgb6(cell):
    try:
        c = cell.font.color.rgb
        return c[-6:] if isinstance(c, str) else "1A1A1A"
    except Exception:
        return "1A1A1A"


def wrap_text(text, width, height):
    max_chars = max(8, int((width - 8) / CHAR_W))
    max_lines = max(1, int((height - 6) / (FONT_SIZE + 2)))
    lines = textwrap.wrap(" ".join(str(text).split()), max_chars)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1][: max(0, max_chars - 1)] + "…"
    return lines


def svg_text(x, y, lines, color, bold=False, size=FONT_SIZE):
    out = []
    for i, ln in enumerate(lines):
        out.append(f'<text x="{x:.0f}" y="{y + (i + 1) * (size + 2):.0f}" font-size="{size}" '
                   f'fill="#{color}"{" font-weight=\"bold\"" if bold else ""}>{_html.escape(ln)}</text>')
    return "\n".join(out)


def week_to_svg(ws, legend_items):
    """Draw one week sheet as an SVG string. legend_items: [(label, fill hex, font hex)]."""
    merged = {}
    inside = set()
    for rng in ws.merged_cells.ranges:
        merged[(rng.min_row, rng.min_col)] = (rng.max_row, rng.max_col)
        for r in range(rng.min_row, rng.max_row + 1):
            for c in range(rng.min_col, rng.max_col + 1):
                if (r, c) != (rng.min_row, rng.min_col):
                    inside.add((r, c))
    ncols = ws.max_column
    nslots = ncols - 1
    width = LABEL_W + nslots * SLOT_W
    labels = []
    r = HEADER_ROWS + 1
    while ws.cell(row=r, column=1).value:
        labels.append((r, " ".join(str(ws.cell(row=r, column=1).value).split())))
        r += 1
    heights = {rr: ROW_H[row_kind(l)] for rr, l in labels}
    y_of = {}
    y = 0
    for i, hr in enumerate(HEADER_H):
        y_of[3 + i] = y; y += hr
    for rr, _ in labels:
        y_of[rr] = y; y += heights[rr]
    legend_h = 26 + 18 * ((len(legend_items) + 1) // 2)
    height = y + 10 + legend_h

    def x_of(c):
        return 0 if c == 1 else LABEL_W + (c - 2) * SLOT_W

    def cell_w(c1, c2):
        return (x_of(c2) + (SLOT_W if c2 > 1 else LABEL_W)) - x_of(c1)

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" '
             f'font-family="Arial, Helvetica, sans-serif">',
             f'<rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>']
    # header + body cells
    rows_to_draw = [3, 4, 5] + [rr for rr, _ in labels]
    for rr in rows_to_draw:
        rh = HEADER_H[rr - 3] if rr <= 5 else heights[rr]
        for c in range(1, ncols + 1):
            if (rr, c) in inside:
                continue
            c2 = merged.get((rr, c), (rr, c))[1]
            cell = ws.cell(row=rr, column=c)
            x, w = x_of(c), cell_w(c, c2)
            fill = rgb6(cell) or ("F2F2F2" if (rr <= 5 or c == 1) else "FFFFFF")
            bold = bool(cell.font and cell.font.bold)
            thick = fill in ("1F4E5F", "8B1E3F")
            parts.append(f'<rect x="{x}" y="{y_of[rr]}" width="{w}" height="{rh}" fill="#{fill}" '
                         f'stroke="#{"1A1A1A" if thick else "BFBFBF"}" stroke-width="{2 if thick else 0.8}"/>')
            if cell.value is not None:
                size = 10 if rr == 5 else FONT_SIZE
                lines = wrap_text(cell.value, w, rh)
                if rr <= 5:
                    # centred headers
                    parts.append(svg_text(x + 4, y_of[rr] + (rh - len(lines) * (size + 2)) / 2, lines, "1A1A1A", bold=True, size=size))
                else:
                    parts.append(svg_text(x + 4, y_of[rr] + 2, lines, font_rgb6(cell), bold=bold or c == 1))
    # legend
    ly = y + 10
    parts.append(f'<text x="4" y="{ly + 14}" font-size="11" font-weight="bold" fill="#1A1A1A">Legend</text>')
    for i, (label, fh, fc) in enumerate(legend_items):
        col, row = i % 2, i // 2
        lx, lyy = 4 + col * (width // 2), ly + 22 + row * 18
        parts.append(f'<rect x="{lx}" y="{lyy}" width="26" height="13" fill="#{fh}" stroke="#BFBFBF" stroke-width="0.8"/>')
        parts.append(f'<text x="{lx + 32}" y="{lyy + 11}" font-size="10.5" fill="#1A1A1A">{_html.escape(label)}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def legend_items(wb):
    ws = wb["Legend"]
    items = []
    for row in ws.iter_rows(min_row=1, max_row=60, max_col=2):
        a, b = row[0], row[1]
        h = rgb6(a)
        if h and a.value and b.value:
            items.append((str(b.value), h, font_rgb6(a)))
    return items


def week_to_md(ws, legend, svg_name=None):
    anchor = merged_lookup(ws)
    lines = [f"## {ws['A1'].value}", ""]
    if svg_name:
        lines += [f"![{ws['A1'].value}]({svg_name})", "", "<details><summary>Text version (what the companion reads)</summary>", ""]
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
    if svg_name:
        lines += ["</details>", ""]
    return lines


def main(xlsx=XLSX, md=MD):
    wb = load_workbook(xlsx)
    legend = legend_map(wb)
    out = ["# Schedule (mirror of the Gantt workbook)", "",
           f"Generated from `{Path(xlsx).name}` by `tools/xlsx2md.py`. Do not edit; edit the workbook and rerun.",
           "Activity blocks in brackets. The fixed layer is drawn by staff; group rows are the groups' own plans.", "",
           "> **Under construction.** First run spring 2027; this is a template, not a confirmed timetable.", ""]
    items = legend_items(wb)
    svgs = []
    for ws in wb.worksheets:
        if ws.title.startswith("Week"):
            n = ws.title.split()[-1]
            svg_name = f"week-{n}.svg"
            svg = week_to_svg(ws, items)
            (Path(md).parent / svg_name).write_text(svg, encoding="utf-8")
            svgs.append((str(ws["A1"].value), svg))
            out += week_to_md(ws, legend, svg_name)
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
    print(f"wrote {md} and {len(svgs)} SVG files")
    html_path = Path(md).with_suffix(".html")
    page = ["<!doctype html>", "<html lang=\"en\"><head><meta charset=\"utf-8\">",
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">",
            "<title>Blockrophage schedule</title>",
            "<style>body{font-family:Arial,Helvetica,sans-serif;margin:16px;color:#1a1a1a;background:#fff}"
            "svg{max-width:100%;height:auto;display:block;margin:0 0 24px}h1{font-size:1.4rem}h2{font-size:1.1rem;margin-top:28px}"
            ".note{border-left:4px solid #8B1E3F;padding:6px 10px;background:#fbf3f5}</style></head><body>",
            "<h1>Blockrophage: schedule template, FS 2027</h1>",
            "<p class=\"note\"><b>Under construction.</b> First run spring 2027; this is a template, not a confirmed timetable. "
            "Source: <code>Blockcourse_Gantt_FS2027.xlsx</code> in the course repository; this page is generated.</p>"]
    for title, svg in svgs:
        page += [f"<h2>{_html.escape(title)}</h2>", svg]
    page += ["</body></html>"]
    html_path.write_text("\n".join(page), encoding="utf-8")
    print(f"wrote {html_path}")


if __name__ == "__main__":
    args = sys.argv[1:]
    main(*(Path(a) for a in args))
