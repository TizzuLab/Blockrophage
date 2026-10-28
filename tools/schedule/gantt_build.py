#!/usr/bin/env python3
"""Build the Gantt workbook (Blockcourse_Gantt_FS2027.xlsx) from the spec below.

The workbook is the single source of the schedule; tools/schedule/gantt2readme.py
draws it into the README and the companion. This script writes the Overview sheet
and the four week sheets from the SPEC and keeps the Legend sheet (colours, texts)
of the existing file, updating only its text cells listed in LEGEND_TEXT.

Hand edits in Excel are fine, but a rebuild overwrites the Overview and the week
sheets, so put lasting changes into the SPEC.

Course window (since 2026-10-28): Tuesday 13:00 to Friday 17:00. Monday and Tuesday
morning belong to the students' other lectures.

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
FULL_DAY = [9, 10, 11, 12, 13, 14, 15, 16]
TUE_PM = [13, 14, 15, 16]
GROUPS = ["A", "B", "C", "D"]
PAIR = {"AB": ["A", "B"], "CD": ["C", "D"], "all": GROUPS}

SUBTITLE = ("Bold fixed-layer sessions are plenary and mandatory; wet-lab times listed for a "
            "group are guaranteed; everything else is orientation and may move with your "
            "supervisors' agreement.")

LUNCH = (12, 1, "Lunch", "BUFFER")
SEMINAR = (16, 1, "Seminar", "PLENARY")
CUTTING_EDGE = (16, 1, "Cutting Edge Immunology Seminar 16:30-17:30 (tbd)", "PLENARY")

# ---------------------------------------------------------------- spec
# days: (header, slots). fixed/blocks: (day index, start hour, span in hours, text, kind).
# blocks are keyed by pair ("all", "AB", "CD"). staff/resources: one text per day.
SPEC = [
    dict(
        n=1, title="Week 1: orientation (Thu 18 - Fri 19 March 2027), 09:00-17:00",
        days=[("Thu 18 Mar", FULL_DAY), ("Fri 19 Mar", FULL_DAY)],
        fixed=[
            (0, 9, 1, "Welcome and safety briefing (Tea Kocijan)", "PLENARY"),
            (0, 10, 2, "Lecture: tissue macrophages and nomenclature (Joel Zindel)", "PLENARY"),
            (0, 13, 1, "Group formation", "PLENARY"),
        ],
        blocks={
            "all": [(0, 9, 3, "Plenary", "PLENARY"), (0,) + LUNCH, (0, 13, 1, "Group formation", "PLENARY"),
                    (0, 14, 3, "Experiment planning with your supervisors: choose your PRR axis and your "
                               "extension. Read P01, P02 and P09 for Friday and Tuesday.", "DRY"),
                    (1,) + LUNCH],
            "AB": [(1, 9, 3, "Hands-on introduction to mammalian cell culture with the staff culture: hood "
                             "and sterile technique, microscope, P02 scrape, count, split and seed, cell "
                             "counter. Lab tour.", "EXP1"),
                   (1, 13, 4, "Dry lab setup: clone the course repository, build the environment with your "
                              "chatty, run the ELISA template on example data. Group plan submitted at 17:00.", "DRY")],
            "CD": [(1, 9, 3, "Dry lab setup: clone the course repository, build the environment with your "
                             "chatty, run the ELISA template on example data.", "DRY"),
                   (1, 13, 4, "Hands-on introduction to mammalian cell culture with the staff culture: hood "
                              "and sterile technique, microscope, P02 scrape, count, split and seed, cell "
                              "counter. Lab tour. Group plan submitted at 17:00.", "EXP1")],
        },
        staff=["Rooms, safety officer. Groups formed at 13:00; supervisors sit with their group from then on.",
               "Staff culture split and counted for the introduction, one flask per pair at 09:00 and 13:00. "
               "Dry lab: walk around, unblock installs. Fallback environment ready [TODO]. Collect the group "
               "plans at 17:00."],
        resources=["Seminar room all day",
                   "Hoods: 2 groups per half day [TODO: hoods available]. Computer room or own laptops; Wi-Fi."],
        notes="Course weeks run Tuesday 13:00 to Friday 17:00; Monday and Tuesday morning belong to your other "
              "lectures. Nothing of yours is in culture before Tuesday 23 March: Friday is practice on the staff "
              "culture so that the thaw on Tuesday is routine.",
    ),
    dict(
        n=2, title="Week 2: Exp 1, establish the line (Tue 23 - Thu 25 March 2027)",
        days=[("Tue 23 Mar", TUE_PM), ("Wed 24 Mar", FULL_DAY), ("Thu 25 Mar", FULL_DAY)],
        fixed=[
            (0,) + CUTTING_EDGE,
            (1, 10, 1, "Lecture: tissue repair I, macrophages in injury and repair (tbd)", "PLENARY"),
            (1, 13, 1, "Facility lecture: flow cytometry and FlowJo (Florian Mair) [TODO: confirm slot with the facility]", "FACILITY"),
            (2, 10, 1, "Journal club 1 (tbd): the M1/M2 nomenclature revision [TODO: paper]; one group presents, all read", "PLENARY"),
            (2, 16, 1, "Debrief week 2: what worked, plan for Exp 2", "PLENARY"),
        ],
        blocks={
            "all": [(0, 13, 3, "P01 Thaw your own vial, count (T0), seed the flask and the counting wells. P09 Seed "
                               "the MTT growth-curve columns. Hood shifts: A+B 13:00, C+D 14:30", "EXP1"),
                    (0,) + SEMINAR,
                    (1, 9, 1, "P01 Count 1. P09 Seed the standard curve, MTT on column 1", "EXP1"),
                    (1, 10, 1, "Lecture", "PLENARY"), (1,) + LUNCH, (1, 13, 1, "Facility lecture", "FACILITY"),
                    (2, 9, 1, "P01 Count 3. P09 MTT on column 2", "EXP1"),
                    (2, 10, 1, "Journal club", "PLENARY"), (2,) + LUNCH,
                    (2, 15, 1, "P01 Count 4, the last point. Discard the counting wells; nothing stays in "
                               "culture over the break", "EXP1"),
                    (2, 16, 1, "Debrief", "PLENARY")],
            "AB": [(1, 11, 1, "Bench: inspect the flask, medium change. P09 MTT on the standard curve at 11:00", "EXP1"),
                   (1, 14, 3, "Dry lab: scRNA-seq part 1, load the preprocessed object, QC figure. Poster: draft "
                              "the introduction. P01 Count 2 at 15:00", "DRY"),
                   (2, 11, 1, "P03 Freeze your own vials from the flask. Clean-up", "EXP1"),
                   (2, 13, 2, "Dry lab: FlowJo on example data. Growth curve and doubling time from your counts. "
                              "Poster: why does this matter (significance)", "DRY")],
            "CD": [(1, 11, 1, "Dry lab: scRNA-seq part 1, load the preprocessed object, QC figure. P09 MTT on the "
                              "standard curve at 11:00 (5 min)", "DRY"),
                   (1, 14, 3, "Bench: inspect the flask, medium change. P01 Count 2 at 15:00. Poster: draft the "
                              "introduction", "EXP1"),
                   (2, 11, 1, "Dry lab: FlowJo on example data. Growth curve so far. Poster: why does this matter "
                              "(significance)", "DRY"),
                   (2, 13, 2, "P03 Freeze your own vials from the flask. Clean-up", "EXP1")],
        },
        staff=["Medium warmed, one vial per group at 13:00 and 14:30. Supervisor at the hood with the group for "
               "the thaw. Counting plates and MTT plates ready.",
               "Cultures inspected 08:00. Counted staff suspension for the standard curves at 09:00. Plate reader "
               "12:30 (column 1) and 14:30 (standard curve). Look at every flask before it goes back in the incubator.",
               "Freezing boxes in the -80. Plate reader 12:30 (column 2) and 16:00 (column 3, MTT added 12:30). "
               "Collect all cultures at 17:00. Easter: vials to -140 on Fri 26 Mar; thaw backup RAW on Wed 31 Mar, "
               "split Fri 2 Apr: enough cells to seed four groups on Tue 6 Apr."],
        resources=["Hoods: all four groups in two shifts [TODO: hoods available]. Incubator: one shelf per group. "
                   "Cell counter.",
                   "Hoods: 2 groups per half day. Plate reader. Computer room / laptops; FlowJo seats [TODO]",
                   "-80 freezer box per group; Mr Frosty or equivalent [TODO: lab standard]. Plate reader. "
                   "Computer room / laptops"],
        notes="Exp 1 is a real experiment: five trypan-blue counts from Tuesday 14:00 to Thursday 15:00 (about 0, "
              "19, 25, 43 and 49 h) give a growth curve and a doubling time against the published 15 to 24 h; the "
              "MTT columns are a second readout, viability of your own vial after the break the third. Counts come "
              "from the counting wells, one well per count, so the flask is only touched for the medium change and "
              "the freeze. P09 steps are 5 to 20 minute visits; the dry-lab pair pops over. Good Friday 26 March: "
              "no course.",
    ),
    dict(
        n=3, title="Week 3: Exp 2, challenge and read out (Tue 6 - Fri 9 April 2027)",
        days=[("Tue 6 Apr", TUE_PM), ("Wed 7 Apr", FULL_DAY), ("Thu 8 Apr", FULL_DAY), ("Fri 9 Apr", FULL_DAY)],
        fixed=[
            (0,) + CUTTING_EDGE,
            (1, 13, 1, "Lecture: single-cell transcriptomics for immunologists, what a signature score means (tbd)", "PLENARY"),
            (2, 9, 1, "Journal club 2 (tbd): the peritoneal injury single-cell paper behind GSE186658 [TODO: paper]; "
                      "one group presents, all read", "PLENARY"),
            (2, 10, 2, "Cytometer slot, groups A+B [TODO: facility reservation]", "FACILITY"),
            (2, 13, 2, "Cytometer slot, groups C+D [TODO: facility reservation]", "FACILITY"),
            (3, 16, 1, "Debrief Exp 2: results, extension choices, rescue decisions", "PLENARY"),
        ],
        blocks={
            "all": [(0, 13, 3, "P02 Plate cells from the staff culture, spin the plate down, 2 h to adhere [TODO: "
                               "confirm before the course that RAW cells adhere in 2 h after a spin]. Meanwhile P01 "
                               "re-thaw your own vial (viability = Exp 1 readout). Then P05 Challenge overnight with "
                               "LPS. Hood shifts: A+B 13:00, C+D 13:30", "EXP2"),
                    (0,) + SEMINAR,
                    (1, 9, 3, "P05 Harvest: supernatants to -20 in aliquots for the ELISA, cells for flow cytometry "
                              "(P08). Hood shifts: A+B 09:00, C+D 09:30", "EXP2"),
                    (1,) + LUNCH, (1, 13, 1, "Lecture", "PLENARY"),
                    (1, 14, 3, "P08 Flow staining of the harvested cells, fix the stained cells (4 \u00b0C until "
                               "acquisition). P06 Coat the ELISA plates with capture antibody, overnight at 4 \u00b0C "
                               "[TODO: check the ELISA protocol]", "EXP2"),
                    (2, 9, 1, "Journal club", "PLENARY"), (2,) + LUNCH,
                    (2, 16, 1, "ELISA: finish the detection steps or set the overnight step [TODO: protocol]", "EXP2"),
                    (3, 9, 3, "FlowJo session: gating of your own data, export statistics (with the facility, "
                              "tbd)", "DRY"),
                    (3,) + LUNCH,
                    (3, 13, 3, "ELISA analysis: plate read if outstanding, standard curve, concentrations. Flow "
                               "statistics in R. scRNA-seq part 2 continued. Poster: results so far", "DRY"),
                    (3, 16, 1, "Debrief", "PLENARY")],
            "AB": [(2, 10, 2, "P08 Acquire at the facility (cytometer slot)", "FACILITY"),
                   (2, 13, 3, "P06 ELISA IL-6 and TNF on the supernatants: blocking, samples, detection [TODO: "
                              "timing against the protocol]. During incubations: scRNA-seq part 2, derive the "
                              "signatures from the bulk RAW 264.7 dataset", "EXP2")],
            "CD": [(2, 10, 2, "P06 ELISA IL-6 and TNF on the supernatants: blocking, samples, detection [TODO: "
                              "timing against the protocol]. During incubations: scRNA-seq part 2, derive the "
                              "signatures from the bulk RAW 264.7 dataset", "EXP2"),
                   (2, 13, 3, "P08 Acquire at the facility (cytometer slot), then ELISA detection steps", "FACILITY")],
        },
        staff=["Staff culture split Fri 2 Apr, counted at 12:30: enough cells to plate four groups. Plate maps "
               "checked before anyone pipettes. LPS aliquots at working concentration. Supervisor at the hood for "
               "the re-thaw.",
               "Tubes labelled, -20 space for supernatants. Antibody panel, viability dye, fixation buffer. ELISA "
               "plates and capture antibody.",
               "Escort the groups to the facility. ELISA reagents, plate reader booked.",
               "FlowJo seats [TODO]. Plate reader. Staff culture kept for groups that need the rescue path (see Notes)."],
        resources=["Hoods: all four groups in two shifts. Plate centrifuge. Incubator shelves.",
                   "Hoods. Cooled centrifuge. Fridge for the fixed cells and the coated plates.",
                   "Cytometer: 2 slots of 2 h [TODO: facility]. Plate reader (450 nm).",
                   "FlowJo seats [TODO]. Plate reader. Computer room / laptops."],
        notes="Core readouts of Exp 2: flow cytometry and ELISA. One overnight LPS challenge (about 18 h, Tuesday "
              "15:00 to Wednesday 09:00); record the real time. Adhesion in 2 h after a spin is to be confirmed "
              "before the course [TODO]. ELISA timing is to be checked against the protocol: the capture antibody "
              "coats overnight Wed to Thu; blocking or sample incubation may run during the cytometer slot or "
              "overnight [TODO]. The definitive cytometer slots need the facility. Goal: all data by Thursday "
              "evening, Friday for analysis. Polarization (P04) and Griess (P07) are extensions.",
    ),
    dict(
        n=4, title="Week 4: extensions, poster, presentations (Tue 13 - Fri 16 April 2027)",
        days=[("Tue 13 Apr", TUE_PM), ("Wed 14 Apr", FULL_DAY), ("Thu 15 Apr", FULL_DAY), ("Fri 16 Apr", FULL_DAY)],
        fixed=[
            (0,) + CUTTING_EDGE,
            (1, 9, 1, "Lecture: scientific writing, from data to argument, poster structure, figure design, honest "
                      "limits (tbd)", "PLENARY"),
            (1, 16, 1, "Failure round: each group presents one thing that went wrong and what it taught them", "PLENARY"),
            (2, 14, 1, "Recap and Q&A (tbd): the course in one hour, then open questions with the teaching staff", "PLENARY"),
            (3, 11, 1, "Feedback round with the teaching staff; course evaluation", "PLENARY"),
            (3, 13, 3, "Poster presentations and discussion; prize", "PLENARY"),
            (3, 16, 1, "Apéro", "PLENARY"),
        ],
        blocks={
            "all": [(0, 13, 3, "Extension of your choice (bench steps), or rescue path: repeat Exp 2 (plate, spin, 2 h, "
                               "LPS challenge overnight; see Notes)", "EXT"),
                    (0,) + SEMINAR,
                    (1, 9, 1, "Lecture", "PLENARY"), (1,) + LUNCH, (1, 16, 1, "Failure round", "PLENARY"),
                    (2, 9, 3, "Poster production with your supervisor: final figures and legends", "POSTER"),
                    (2,) + LUNCH,
                    (2, 13, 1, "Final checks. Printing deadline 14:00: poster PDF committed to the group branch", "POSTER"),
                    (2, 14, 1, "Recap and Q&A", "PLENARY"),
                    (2, 15, 2, "Free: extension analysis, notebook, group branch", "BUFFER"),
                    (3, 9, 2, "Lab clean-up; notebook and group branch finalised", "DRY"),
                    (3, 11, 1, "Feedback round", "PLENARY"), (3,) + LUNCH,
                    (3, 13, 3, "Poster presentations", "PLENARY"), (3, 16, 1, "Apéro", "PLENARY")],
            "AB": [(1, 10, 2, "Extension, continued, or rescue path: harvest, flow staining, ELISA", "EXT"),
                   (1, 13, 3, "Dry lab: analysis of Exp 2 and the extension, scRNA-seq part 3, score the tissue "
                              "macrophages. Poster: figures and legends", "POSTER")],
            "CD": [(1, 10, 2, "Dry lab: analysis of Exp 2 and the extension, scRNA-seq part 3, score the tissue "
                              "macrophages. Poster: figures and legends. Rescue path: harvest at 09:00 (15 min)", "POSTER"),
                   (1, 13, 3, "Extension, continued, or rescue path: flow staining, ELISA", "EXT")],
        },
        staff=["Reagents for the extensions agreed on Fri 9 Apr. Staff culture ready for rescue groups to plate.",
               "Poster template distributed, printing booked [TODO: printer]. Rescue groups: cytometer slot [TODO: facility], "
               "ELISA Wed, result on the poster by Thursday.",
               "Posters printed Thu after 14:00 [TODO: printer].",
               "Jury, prize, evaluation form, clean-up checklist. Apéro ordered [TODO: catering]."],
        resources=["Hoods: all four groups in two shifts. Extension-specific instruments as agreed.",
                   "Hoods Tue and Wed only. Seminar room Wed to Fri.",
                   "Printer [TODO]. Poster boards.",
                   "Seminar room. Apéro room [TODO: catering]."],
        notes="Rescue path for a failed Exp 2: repeat it in week 4. Plate, spin and challenge Tue 13:00, harvest and "
              "stain Wed 09:00, ELISA Wed, acquisition in a week-4 cytometer slot [TODO: facility]; result on the "
              "poster by Thu. Printing deadline Thu 14:00. Tuesdays 16:30-17:30: Cutting "
              "Edge Immunology Seminar.",
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
        ("Week 3", [("Other lectures", "BUFFER"), ("Morning: other lectures. 13:00 plate, spin, 2 h, LPS challenge overnight; re-thaw own vial", "EXP2"),
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
             "lectures. Tuesday afternoons are all-bench in two hood shifts; Wednesday and Thursday run the "
             "checkerboard (half wet lab, half dry lab per group); see the week sheets.",
             "Course hours Tue 13:00-17:00, Wed-Fri 09:00-17:00, lunch 12:00-13:00. Weeks 2-4: Cutting Edge "
             "Immunology Seminar Tue 16:30-17:30."],
}

LEGEND_TEXT = {
    "B8": "Wet lab Exp 2: challenge, read out (flow cytometry, ELISA)",
    "A2": "Built by tools/schedule/gantt_build.py on {today}. Hand edits are fine, but a rebuild overwrites the "
          "Overview and the week sheets; lasting changes go into the script. After editing, run "
          "tools/schedule/gantt2readme.py.",
    "B14": "One sheet per week. Course hours Tue 13:00-17:00 and Wed-Fri 09:00-17:00; Monday and Tuesday morning "
           "are the students' other lectures. One cell per hour: four on Tuesday, eight on a full day (three in "
           "the morning, lunch 12:00-13:00, four in the afternoon). Rows: fixed layer, one row per group, shared "
           "staff row, resources, notes.",
    "B15": "Lecture slots, journal clubs, facility lecture, cytometer slots, the Tuesday Cutting Edge Immunology "
           "Seminar (16:30-17:30), writing lecture, recap, presentations. Drawn by the teaching staff, thick "
           "border, locked. Everything else is flexible.",
    "B17": "Wednesday and Thursday: two groups at the bench in the morning and two in the dry lab, swapped after "
           "lunch. Tuesday afternoons and the Friday harvest are all-bench in two hood shifts (A+B first, C+D "
           "90 min later). It is a default, not a rule: it keeps two hoods sufficient and the cytometer at two "
           "groups per slot. A group that deviates justifies its hood time against the other three. Pairs stay "
           "fixed within a week, because the group that starts an overnight step harvests it. The morning pair "
           "swaps between weeks.",
    "B18": "Exp 1 (week 2): establish the RAW 264.7 line. Thaw on Tuesday afternoon, five trypan-blue counts to "
           "Thursday afternoon (growth curve, doubling time), MTT columns as a second readout, freeze your own "
           "vials on Thursday; viability of your vial after the break is the third readout. Exp 2 (week 3): "
           "plate RAW cells, spin, 2 h adhesion, overnight LPS challenge; readouts flow cytometry and ELISA. "
           "Polarization (P04) and Griess (P07) are extensions. Protocol IDs (P01...) refer to protocols/ in the course repository.",
    "B19": "Week 1: environment and templates. Week 2: scRNA-seq part 1 (QC), FlowJo on example data, growth "
           "curve. Week 3: scRNA-seq part 2 (signatures from the bulk RAW 264.7 dataset) during the ELISA "
           "incubations, own flow and ELISA data on Friday. Week 4: scRNA-seq part 3 (scoring of the tissue "
           "macrophages), extension analysis and poster figures. Downtime "
           "at any point: poster introduction and significance.",
    "B20": "A group whose Exp 2 failed repeats it in week 4: plate, spin and challenge Tue 13 April at 13:00, "
           "harvest and stain Wed 14 at 09:00, ELISA Wed 14, acquisition in a week-4 cytometer slot [TODO: facility].",
    "B24": "[TODO] Cytometer slots: dates and times from the facility (week 3 Thursday 8 April, 10:00-12:00 and "
           "13:00-15:00; rescue and extension slots week 4).",
    "B25": "[TODO] Facility lecture: slot on Wed 24 March 13:00.",
    "B27": "[TODO] Hoods available to the course per half day; Tuesday afternoons need all four groups in two shifts.",
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


def put(ws, row, c1, c2, text, kind=None, **kw):
    cell = ws.cell(row=row, column=c1, value=text)
    style(cell, kind, **kw)
    if c2 > c1:
        ws.merge_cells(start_row=row, start_column=c1, end_row=row, end_column=c2)
        for c in range(c1 + 1, c2 + 1):
            style(ws.cell(row=row, column=c), kind, **kw)
    return cell


def build_week(wb, spec):
    ws = wb.create_sheet(f"Week {spec['n']}")
    # column map: (day index, hour) -> column
    col, c = {}, 2
    day_cols = []
    for d, (hdr, slots) in enumerate(spec["days"]):
        c0 = c
        for h in slots:
            col[(d, h)] = c
            c += 1
        day_cols.append((c0, c - 1))
    ncols = c - 1
    ws.column_dimensions["A"].width = 24
    for cc in range(2, ncols + 1):
        ws.column_dimensions[get_column_letter(cc)].width = 13

    put(ws, 1, 1, ncols, spec["title"], bold=True, color="1F4E5F", wrap=False, valign="center")
    put(ws, 2, 1, ncols, SUBTITLE, color="5A5A5A", wrap=False, valign="center")
    for r, lbl in ((3, "Day"), (4, "Half day"), (5, "Slot")):
        put(ws, r, 1, 1, lbl, bold=True, fill=HEADER_FILL, valign="center")
    for d, (hdr, slots) in enumerate(spec["days"]):
        c0, c1 = day_cols[d]
        put(ws, 3, c0, c1, hdr, bold=True, fill=HEADER_FILL, valign="center")
        segs = []
        if 9 in slots:
            segs += [(9, 11, "Morning 09:00-12:00"), (12, 12, "Lunch 12:00-13:00")]
        segs.append((13, 16, "Afternoon 13:00-17:00"))
        for h0, h1, txt in segs:
            put(ws, 4, col[(d, h0)], col[(d, h1)], txt, bold=True, fill=HEADER_FILL, valign="center")
        for h in slots:
            put(ws, 5, col[(d, h)], col[(d, h)], f"{h:02d}:00", bold=True, fill=HEADER_FILL, valign="center")

    labels = ["Fixed layer\n(lectures, facility)"] + [f"Group {g}\nsupervisors: ______ / ______" for g in GROUPS] + \
             ["Staff (shared)\nprep and supervision", "Resources\n(hand-written capacity)", "Notes"]
    row_of_group = {g: 7 + i for i, g in enumerate(GROUPS)}
    for i, lbl in enumerate(labels):
        put(ws, 6 + i, 1, 1, lbl, bold=True, fill=HEADER_FILL, valign="center")
    for r in range(6, 11):
        ws.row_dimensions[r].height = 84
    ws.row_dimensions[11].height = 60
    ws.row_dimensions[12].height = 48
    ws.row_dimensions[13].height = 54

    for d, h, span, text, kind in spec["fixed"]:
        put(ws, 6, col[(d, h)], col[(d, h)] + span - 1, text, kind)
    for pair, blocks in spec["blocks"].items():
        for g in PAIR[pair]:
            for d, h, span, text, kind in blocks:
                put(ws, row_of_group[g], col[(d, h)], col[(d, h)] + span - 1, text, kind)
    for r, texts in ((11, spec["staff"]), (12, spec["resources"])):
        for d, txt in enumerate(texts):
            c0, c1 = day_cols[d]
            put(ws, r, c0, c1, txt, fill=META_FILL)
    put(ws, 13, 2, ncols, spec["notes"], fill=META_FILL)
    ws.freeze_panes = "B6"
    return ws


def build_overview(wb):
    ws = wb.create_sheet("Overview", 1)
    ws.column_dimensions["A"].width = 12
    for c in "BCDEF":
        ws.column_dimensions[c].width = 34
    ws["A1"] = OVERVIEW["title"]
    ws["A1"].font = Font(bold=True, color="1F4E5F")
    for i, day in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri"]):
        put(ws, 3, 2 + i, 2 + i, day, bold=True, fill=HEADER_FILL, valign="center")
    put(ws, 3, 1, 1, "", fill=HEADER_FILL)
    for r, (label, cells) in enumerate(OVERVIEW["rows"], start=4):
        put(ws, r, 1, 1, label, bold=True, fill=HEADER_FILL, valign="center")
        ws.row_dimensions[r].height = 48
        for i, cell in enumerate(cells):
            if cell is None:
                put(ws, r, 2 + i, 2 + i, None)
            else:
                put(ws, r, 2 + i, 2 + i, cell[0], cell[1])
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
