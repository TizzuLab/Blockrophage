#!/usr/bin/env python3
"""Build the Gantt workbook (Blockcourse_Gantt_FS2027.xlsx) from the spec below.

The workbook is the single source of the schedule; tools/schedule/gantt2readme.py
draws it into the README and the companion. This script writes the Overview sheet
and the four week sheets from the SPEC and keeps the Legend sheet (colours, texts)
of the existing file, updating only its text cells listed in LEGEND_TEXT.

Layout of a week sheet (calendar): one column per day, one row per hour, 09:00 to
16:00 (a Tuesday has 13:00 to 16:00; its morning is the students' other lectures).
All four groups follow the same plan, each at its own hood. Below the hour grid: a
Staff row and a Resources row, one cell per day.

Hand edits in Excel are fine, but a rebuild overwrites the Overview and the week
sheets, so put lasting changes into the SPEC.

Course window (since 2026-10-28): Tuesday 13:00 to Friday 17:00.

Usage: python3 tools/schedule/gantt_build.py && python3 tools/schedule/gantt2readme.py
"""
from __future__ import annotations

import datetime as dt
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

HERE = Path(__file__).resolve().parent
XLSX = HERE / "Blockcourse_Gantt_FS2027.xlsx"

# ---------------------------------------------------------------- styles
FILL = {  # must match the Legend sheet, column A
    "PLENARY": "1F4E5F", "FACILITY": "8B1E3F", "EXP1": "C6E0B4", "EXP2": "BDD7EE",
    "DRY": "FFE699", "POSTER": "D9C3E9", "EXT": "F8CBAD", "BUFFER": "EDEDED",
}
FONT_RGB = {"PLENARY": "FFFFFF", "FACILITY": "FFFFFF", "BUFFER": "5A5A5A"}
BOLD = {"PLENARY", "FACILITY"}
HEADER_FILL, META_FILL = "F2F2F2", "FAFAFA"
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
HOURS = [9, 10, 11, 12, 13, 14, 15, 16]
HEADER_ROWS = 3          # title, subtitle, day header
FIRST_HOUR_ROW = HEADER_ROWS + 1

SUBTITLE = ("Dark cells in bold are plenary and mandatory. Everything else is the default plan for "
            "all four groups; each group has its own hood all day, so bench work may shift with your "
            "supervisors' agreement. Lectures and dry lab: conference room HPL F22. Bench: HPL F27.2.")

LUNCH = (12, 1, "Lunch", "BUFFER")
OTHER = (9, 3, "Your other lectures (not course time)", "BUFFER")
CUTTING_EDGE = (16, 1, "Cutting Edge Immunology Seminar 16:30-17:30 (tbd)", "PLENARY")
HOODS = "4 hoods HPL F27.2, one per group, available at all times."
F22 = "Conference room HPL F22 for lectures and dry lab."

# ---------------------------------------------------------------- spec
# days: (header, tuesday?, blocks, staff, resources); blocks: (start hour, span, text, kind).
SPEC = [
    dict(
        n=1, title="Week 1: orientation (Thu 18 - Fri 19 March 2027)",
        days=[
            ("Thu 18 Mar", False,
             [(9, 1, "Welcome and safety briefing (Tea Kocijan)", "PLENARY"),
              (10, 2, "Lecture: tissue macrophages and nomenclature (Joel Zindel)", "PLENARY"),
              LUNCH,
              (13, 1, "Group formation", "PLENARY"),
              (14, 3, "Experiment planning with your supervisors: choose your PRR axis and your extension. "
                      "Read P01, P02 and P09 for Friday and Tuesday.", "DRY")],
             "Rooms, safety officer. Groups formed at 13:00; supervisors sit with their group from then on.",
             F22),
            ("Fri 19 Mar", False,
             [(9, 3, "Hands-on introduction to mammalian cell culture with the staff culture: hood and sterile "
                     "technique, microscope, P02 scrape, count, split and seed, cell counter. Lab tour.", "EXP1"),
              LUNCH,
              (13, 4, "Dry lab setup: clone the course repository, build the environment with your chatty, run "
                      "the ELISA template on example data. Group plan submitted at 17:00.", "DRY")],
             "Staff culture split and counted, one flask per group at 09:00. Dry lab: walk around, unblock "
             "installs. Fallback environment ready [TODO]. Collect the group plans at 17:00.",
             HOODS + " Cell counter. " + F22 + " Own laptops, Wi-Fi."),
        ],
    ),
    dict(
        n=2, title="Week 2: Exp 1, establish the line (Tue 23 - Thu 25 March 2027)",
        days=[
            ("Tue 23 Mar", True,
             [OTHER, LUNCH,
              (13, 4, "P01 Thaw your own vial, count (T0), seed the flask and the counting wells. P09 Seed the "
                      "MTT growth-curve columns.", "EXP1")],
             "Medium warmed, one vial per group at 13:00. Supervisor at the hood with each group for the thaw. "
             "Counting plates and MTT plates ready.",
             HOODS + " Cell counter."),
            ("Wed 24 Mar", False,
             [(9, 1, "P01 Count 1. P09 Seed the standard curve, MTT on column 1", "EXP1"),
              (10, 2, "Inspect the flask, medium change. P09 MTT on the standard curve at 11:00; reads at 12:30 "
                      "and 14:30", "EXP1"),
              LUNCH,
              (13, 1, "Facility lecture: flow cytometry and FlowJo (Florian Mair) [TODO: confirm slot with the "
                      "facility]", "FACILITY"),
              (14, 3, "Dry lab: scRNA-seq part 1, load the preprocessed object, QC figure. Poster: draft the "
                      "introduction. P01 Count 2 at 15:00", "DRY")],
             "Cultures inspected 08:00. Counted staff suspension for the standard curves at 09:00. Plate reader "
             "12:30 (column 1) and 14:30 (standard curve).",
             HOODS + " Plate reader. " + F22 + " FlowJo seats [TODO]."),
            ("Thu 25 Mar", False,
             [(9, 1, "P01 Count 3. P09 MTT on column 2 (read 12:30)", "EXP1"),
              (10, 1, "Journal club 1 (tbd): the M1/M2 nomenclature revision [TODO: paper]; one group presents, "
                      "all read", "PLENARY"),
              (11, 1, "P03 Freeze your own vials from the flask. Clean-up", "EXP1"),
              LUNCH,
              (13, 2, "Dry lab: FlowJo on example data. Growth curve and doubling time from your counts. Poster: "
                      "why does this matter (significance). P09 MTT on column 3 at 12:30, read 16:00", "DRY"),
              (15, 1, "P01 Count 4, the last point. Discard the counting wells; nothing stays in culture over "
                      "the break", "EXP1"),
              (16, 1, "Debrief week 2: what worked, plan for Exp 2", "PLENARY")],
             "Freezing boxes in the -80. Plate reader 12:30 and 16:00. Collect all cultures at 17:00. Easter: "
             "vials to -140 on Fri 26 Mar; thaw backup RAW on Wed 31 Mar, split Fri 2 Apr: enough cells to plate "
             "four groups on Tue 6 Apr.",
             HOODS + " -80 box per group; Mr Frosty or equivalent [TODO: lab standard]. Plate reader. " + F22),
        ],
    ),
    dict(
        n=3, title="Week 3: Exp 2, challenge and read out (Tue 6 - Fri 9 April 2027)",
        days=[
            ("Tue 6 Apr", True,
             [OTHER, LUNCH,
              (13, 3, "P02 Plate cells from the staff culture, spin the plate down, 2 h to adhere [TODO: confirm "
                      "before the course that RAW cells adhere in 2 h after a spin]. Meanwhile P01 re-thaw your "
                      "own vial (viability = Exp 1 readout). Then P05 Challenge overnight with LPS.", "EXP2"),
              CUTTING_EDGE],
             "Staff culture split Fri 2 Apr, counted at 12:30: enough cells to plate four groups. Plate maps "
             "checked before anyone pipettes. LPS aliquots at working concentration. Supervisor at the hood for "
             "the re-thaw.",
             HOODS + " Plate centrifuge."),
            ("Wed 7 Apr", False,
             [(9, 3, "P05 Harvest: supernatants to -20 in aliquots for the ELISA, cells for flow cytometry "
                     "(P08).", "EXP2"),
              LUNCH,
              (13, 1, "Lecture: single-cell transcriptomics for immunologists, what a signature score means "
                      "(tbd)", "PLENARY"),
              (14, 3, "P08 Flow staining of the harvested cells, fix the stained cells (4 °C until "
                      "acquisition). P06 Coat the ELISA plates with capture antibody, overnight at 4 °C "
                      "[TODO: check the ELISA protocol]", "EXP2")],
             "Tubes labelled, -20 space for supernatants. Antibody panel, viability dye, fixation buffer. ELISA "
             "plates and capture antibody.",
             HOODS + " Cooled centrifuge. Fridge for the fixed cells and the coated plates. " + F22),
            ("Thu 8 Apr", False,
             [(9, 1, "Journal club 2 (tbd): the peritoneal injury single-cell paper behind GSE186658 [TODO: "
                     "paper]; one group presents, all read", "PLENARY"),
              (10, 2, "Cytometer slot, groups A+B: P08 Acquire [TODO: facility reservation]. Groups C+D: P06 "
                      "ELISA, blocking and samples [TODO: timing against the protocol]; scRNA-seq part 2 during "
                      "the incubations", "FACILITY"),
              LUNCH,
              (13, 3, "Cytometer slot, groups C+D: P08 Acquire [TODO: facility reservation]. Groups A+B: P06 "
                      "ELISA, blocking and samples [TODO: timing against the protocol]; scRNA-seq part 2 during "
                      "the incubations", "FACILITY"),
              (16, 1, "ELISA: finish the detection steps or set the overnight step [TODO: protocol]", "EXP2")],
             "Escort the groups to the facility. ELISA reagents, plate reader booked.",
             "Cytometer: 2 slots of 2 h [TODO: facility]. Plate reader (450 nm). " + HOODS + " " + F22),
            ("Fri 9 Apr", False,
             [(9, 3, "FlowJo session: gating of your own data, export statistics (with the facility, tbd)", "DRY"),
              LUNCH,
              (13, 3, "ELISA analysis: plate read if outstanding, standard curve, concentrations. Flow statistics "
                      "in R. scRNA-seq part 2 continued. Poster: results so far", "DRY"),
              (16, 1, "Debrief Exp 2: results, extension choices, rescue decisions", "PLENARY")],
             "FlowJo seats [TODO]. Plate reader. Staff culture kept for groups that need the rescue path (a "
             "repeat of Exp 2 in week 4).",
             F22 + " FlowJo seats [TODO]. Plate reader. " + HOODS),
        ],
    ),
    dict(
        n=4, title="Week 4: extensions, poster, presentations (Tue 13 - Fri 16 April 2027)",
        days=[
            ("Tue 13 Apr", True,
             [OTHER, LUNCH,
              (13, 3, "Extension of your choice (bench steps), or rescue path: repeat Exp 2 (plate, spin, 2 h, "
                      "LPS challenge overnight)", "EXT"),
              CUTTING_EDGE],
             "Reagents for the extensions agreed on Fri 9 Apr. Staff culture ready for rescue groups to plate.",
             HOODS + " Extension-specific instruments as agreed."),
            ("Wed 14 Apr", False,
             [(9, 1, "Lecture: scientific writing, from data to argument, poster structure, figure design, honest "
                     "limits (tbd)", "PLENARY"),
              (10, 2, "Extension, continued, or rescue path: harvest, flow staining, ELISA", "EXT"),
              LUNCH,
              (13, 3, "Dry lab: analysis of Exp 2 and the extension, scRNA-seq part 3, score the tissue "
                      "macrophages. Poster: figures and legends", "POSTER"),
              (16, 1, "Failure round: each group presents one thing that went wrong and what it taught them",
               "PLENARY")],
             "Poster template distributed, printing booked [TODO: printer]. Rescue groups: cytometer slot [TODO: "
             "facility], ELISA Wed, result on the poster by Thursday.",
             HOODS + " " + F22),
            ("Thu 15 Apr", False,
             [(9, 3, "Poster production with your supervisor: final figures and legends", "POSTER"),
              LUNCH,
              (13, 1, "Final checks. Printing deadline 14:00: poster PDF committed to the group branch", "POSTER"),
              (14, 1, "Recap and Q&A (tbd): the course in one hour, then open questions with the teaching staff",
               "PLENARY"),
              (15, 2, "Free: extension analysis, notebook, group branch", "BUFFER")],
             "Posters printed Thu after 14:00 [TODO: printer].",
             F22 + " Printer [TODO]. Poster boards."),
            ("Fri 16 Apr", False,
             [(9, 2, "Lab clean-up; notebook and group branch finalised", "DRY"),
              (11, 1, "Feedback round with the teaching staff; course evaluation", "PLENARY"),
              LUNCH,
              (13, 3, "Poster presentations and discussion; prize", "PLENARY"),
              (16, 1, "Apéro", "PLENARY")],
             "Jury, prize, evaluation form, clean-up checklist. Apéro ordered [TODO: catering].",
             F22 + " Apéro room [TODO: catering]."),
        ],
    ),
]

OVERVIEW = {
    "title": "Overview: the four weeks at a glance (default plan)",
    "rows": [  # (label, [(Mon..Fri text, kind or None)])
        ("Week 1", [None, None, None, ("Welcome, lectures, group formation, planning with supervisor", "PLENARY"),
                    ("Hands-on cell-culture introduction on the staff culture; dry lab setup; plans submitted", "EXP1")]),
        ("Week 2", [("Other lectures", "BUFFER"), ("Morning: other lectures. 13:00 Exp 1: thaw, T0, seed", "EXP1"),
                    ("Exp 1: counts 1 and 2, MTT, medium change; flow lecture", "EXP1"),
                    ("Exp 1: counts 3 and 4, freeze; debrief", "EXP1"), ("Good Friday", "BUFFER")]),
        ("Easter", [("Break 26 Mar - 4 Apr; staff thaw backup cells", "BUFFER"), None, None, None, None]),
        ("Week 3", [("Other lectures", "BUFFER"),
                    ("Morning: other lectures. 13:00 plate, spin, 2 h, LPS challenge overnight; re-thaw own vial", "EXP2"),
                    ("Harvest cells and supernatants; flow staining and fix; ELISA plates coated", "EXP2"),
                    ("Flow acquisition (A+B morning, C+D afternoon); ELISA in the other half", "EXP2"),
                    ("FlowJo session; ELISA analysis; debrief", "EXP2")]),
        ("Week 4", [("Other lectures", "BUFFER"),
                    ("Morning: other lectures. 13:00 extensions or rescue path", "EXT"),
                    ("Writing lecture; extensions; poster; failure round", "POSTER"),
                    ("Poster production; printing deadline 14:00; recap and Q&A", "POSTER"),
                    ("Clean-up, feedback; poster presentations, prize, Apéro", "PLENARY")]),
    ],
    "foot": ["Course weeks run Tuesday 13:00 to Friday 17:00; Monday and Tuesday morning are the students' other "
             "lectures. All four groups follow the same plan, each at its own hood; see the week sheets.",
             "Course hours Tue 13:00-17:00, Wed-Fri 09:00-17:00, lunch 12:00-13:00. Lectures and dry lab in "
             "conference room HPL F22, bench in HPL F27.2. Cutting Edge Immunology Seminar Tue 16:30-17:30 in "
             "weeks 3 and 4."],
}

LEGEND_TEXT = {
    "B8": "Wet lab Exp 2: challenge, read out (flow cytometry, ELISA)",
    "A2": "Built by tools/schedule/gantt_build.py on {today}. Hand edits are fine, but a rebuild overwrites the "
          "Overview and the week sheets; lasting changes go into the script. After editing, run "
          "tools/schedule/gantt2readme.py.",
    "B14": "One sheet per week: one column per day, one row per hour. Course hours Tue 13:00-17:00 and Wed-Fri "
           "09:00-17:00; Monday and Tuesday morning are the students' other lectures. Below the hour grid: a "
           "staff row and a resources row, one cell per day.",
    "B15": "Lecture slots, journal clubs, facility lecture, cytometer slots, the Tuesday Cutting Edge Immunology "
           "Seminar (16:30-17:30) in weeks 3 and 4, writing lecture, recap, presentations. Drawn by the teaching "
           "staff, dark cells, thick border, locked. Everything else is flexible.",
    "B16": "Plenary sessions (dark cells, bold) are mandatory. All four groups follow the same plan. Each group "
           "has its own laminar flow hood in HPL F27.2, reserved all day every day, so bench work may shift with "
           "the supervisors' agreement. Lectures and dry lab in conference room HPL F22. Nobody submits a "
           "timetable.",
    "B17": "No checkerboard: with four hoods, all four groups do the same thing at the same time, which keeps "
           "supervision simple. Where the cytometer forces a split (week 3 Thursday), two groups acquire while "
           "the other two run the ELISA, then swap.",
    "B18": "Exp 1 (week 2): establish the RAW 264.7 line. Thaw on Tuesday afternoon, five trypan-blue counts to "
           "Thursday afternoon (growth curve, doubling time), MTT columns as a second readout, freeze your own "
           "vials on Thursday; viability of your vial after the break is the third readout. Exp 2 (week 3): "
           "plate RAW cells, spin, 2 h adhesion, overnight LPS challenge; readouts flow cytometry and ELISA. "
           "Polarization (P04) and Griess (P07) are extensions. Protocol IDs (P01...) refer to protocols/ in "
           "the course repository.",
    "B19": "Week 1: environment and templates. Week 2: scRNA-seq part 1 (QC), FlowJo on example data, growth "
           "curve. Week 3: scRNA-seq part 2 (signatures from the bulk RAW 264.7 dataset) during the ELISA "
           "incubations, own flow and ELISA data on Friday. Week 4: scRNA-seq part 3 (scoring of the tissue "
           "macrophages), extension analysis and poster figures. Downtime at any point: poster introduction and "
           "significance.",
    "B20": "A group whose Exp 2 failed repeats it in week 4: plate, spin and challenge Tue 13 April at 13:00, "
           "harvest and stain Wed 14 at 09:00, ELISA Wed 14, acquisition in a week-4 cytometer slot [TODO: facility].",
    "B24": "[TODO] Cytometer slots: dates and times from the facility (week 3 Thursday 8 April, 10:00-12:00 and "
           "13:00-15:00; rescue and extension slots week 4).",
    "B25": "[TODO] Facility lecture: slot on Wed 24 March 13:00.",
    "B27": "Hoods: four in HPL F27.2, one per group, reserved all day every day (settled 2026-10-28). Conference "
           "room HPL F22 reserved for lectures and dry lab.",
}


# ---------------------------------------------------------------- helpers
def style(cell, kind=None, bold=False, fill=None, color=None, wrap=True, valign="top", halign=None):
    f = fill or (FILL[kind] if kind else None)
    if f:
        cell.fill = PatternFill("solid", fgColor=f)
    c = color or (FONT_RGB.get(kind, "1A1A1A") if kind else None)
    cell.font = Font(bold=bold or (kind in BOLD), color=c)
    cell.alignment = Alignment(wrap_text=wrap, vertical=valign, horizontal=halign)
    cell.border = BORDER


def put(ws, r1, c, text, kind=None, r2=None, c2=None, **kw):
    """Write text at (r1, c), merge down to r2 and across to c2 when given."""
    r2 = r2 or r1
    c2 = c2 or c
    cell = ws.cell(row=r1, column=c, value=text)
    style(cell, kind, **kw)
    for r in range(r1, r2 + 1):
        for cc in range(c, c2 + 1):
            if (r, cc) != (r1, c):
                style(ws.cell(row=r, column=cc), kind, **kw)
    if (r2, c2) != (r1, c):
        ws.merge_cells(start_row=r1, start_column=c, end_row=r2, end_column=c2)
    return cell


def build_week(wb, spec):
    ws = wb.create_sheet(f"Week {spec['n']}")
    ndays = len(spec["days"])
    ncols = 1 + ndays
    ws.column_dimensions["A"].width = 9
    for cc in range(2, ncols + 1):
        ws.column_dimensions[get_column_letter(cc)].width = 46
    row_of = {h: FIRST_HOUR_ROW + i for i, h in enumerate(HOURS)}
    staff_row = FIRST_HOUR_ROW + len(HOURS)
    res_row = staff_row + 1

    put(ws, 1, 1, spec["title"], c2=ncols, bold=True, color="1F4E5F", wrap=False, valign="center")
    put(ws, 2, 1, SUBTITLE, c2=ncols, color="5A5A5A", wrap=True, valign="center")
    ws.row_dimensions[2].height = 32
    put(ws, 3, 1, "Time", bold=True, fill=HEADER_FILL, valign="center")
    for h in HOURS:
        put(ws, row_of[h], 1, f"{h:02d}:00", bold=True, fill=HEADER_FILL, valign="center")
        ws.row_dimensions[row_of[h]].height = 64
    put(ws, staff_row, 1, "Staff", bold=True, fill=HEADER_FILL, valign="center")
    put(ws, res_row, 1, "Resources", bold=True, fill=HEADER_FILL, valign="center")
    ws.row_dimensions[staff_row].height = 90
    ws.row_dimensions[res_row].height = 64

    for d, (hdr, _tuesday, blocks, staff, resources) in enumerate(spec["days"]):
        c = 2 + d
        put(ws, 3, c, hdr, bold=True, fill=HEADER_FILL, valign="center")
        for h, span, text, kind in blocks:
            put(ws, row_of[h], c, text, kind, r2=row_of[h] + span - 1)
        put(ws, staff_row, c, staff, fill=META_FILL)
        put(ws, res_row, c, resources, fill=META_FILL)
    ws.freeze_panes = "B4"
    return ws


def build_overview(wb):
    ws = wb.create_sheet("Overview", 1)
    ws.column_dimensions["A"].width = 12
    for c in "BCDEF":
        ws.column_dimensions[c].width = 34
    ws["A1"] = OVERVIEW["title"]
    ws["A1"].font = Font(bold=True, color="1F4E5F")
    for i, day in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri"]):
        put(ws, 3, 2 + i, day, bold=True, fill=HEADER_FILL, valign="center")
    put(ws, 3, 1, "", fill=HEADER_FILL)
    for r, (label, cells) in enumerate(OVERVIEW["rows"], start=4):
        put(ws, r, 1, label, bold=True, fill=HEADER_FILL, valign="center")
        ws.row_dimensions[r].height = 48
        for i, cell in enumerate(cells):
            if cell is None:
                put(ws, r, 2 + i, None)
            else:
                put(ws, r, 2 + i, cell[0], cell[1])
    r = 4 + len(OVERVIEW["rows"]) + 1
    for txt in OVERVIEW["foot"]:
        ws.cell(row=r, column=1, value=txt)
        r += 1
    return ws


def main():
    wb = load_workbook(XLSX)
    for name in list(wb.sheetnames):
        if name != "Legend":
            del wb[name]
    legend = wb["Legend"]
    today = dt.date.today().isoformat()
    for ref, txt in LEGEND_TEXT.items():
        legend[ref] = txt.format(today=today)
    build_overview(wb)
    for spec in SPEC:
        build_week(wb, spec)
    wb.save(XLSX)
    print(f"wrote {XLSX} ({len(SPEC)} week sheets)")


if __name__ == "__main__":
    main()
