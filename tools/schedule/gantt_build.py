#!/usr/bin/env python3
"""Build the Gantt workbook (Blockcourse_Gantt_FS2027.xlsx) from the spec below.

The workbook is the single source of the schedule; tools/schedule/gantt2readme.py
draws it into the README and the companion. This script writes the Overview sheet
and the four week sheets from the SPEC and keeps the Legend sheet (colours, texts)
of the existing file, updating only its text cells listed in LEGEND_TEXT.

Layout of a week sheet (calendar): one column per day, one row per hour, 08:00 to
16:00 (a Tuesday has 13:00 to 16:00; its morning is the students' other lectures;
every full day opens with a self-study hour).
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
    "PLENARY": "1F4E5F", "FACILITY": "8B1E3F", "EXP1": "C6E0B4", "EXP3": "BDD7EE",
    "DRY": "FFE699", "POSTER": "D9C3E9", "EXT": "F8CBAD", "BUFFER": "EDEDED",
}
FONT_RGB = {"PLENARY": "FFFFFF", "FACILITY": "FFFFFF", "BUFFER": "5A5A5A"}
BOLD = {"PLENARY", "FACILITY"}
HEADER_FILL, META_FILL = "F2F2F2", "FAFAFA"
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
HOURS = [8, 9, 10, 11, 12, 13, 14, 15, 16]
HEADER_ROWS = 3          # title, subtitle, day header
FIRST_HOUR_ROW = HEADER_ROWS + 1

SUBTITLE = ("Dark cells in bold are plenary and mandatory. Everything else is the default plan for "
            "all four groups; each group has its own hood all day, so bench work may shift with your "
            "supervisors' agreement. Lectures and dry lab: conference room HPL F22. Bench: HPL F27.2.")

LUNCH = (12, 1, "Lunch", "BUFFER")
OTHER = (8, 4, "Your other lectures (not course time)", "BUFFER")
SELF_STUDY = (8, 1, "Self-study: reading for the day, notebook, group branch", "BUFFER")
CUTTING_EDGE = (16, 1, "Cutting Edge Immunology Seminar 16:30-17:30 (tbd)", "PLENARY")
HOODS = "4 hoods HPL F27.2, one per group, available at all times."
F22 = "Conference room HPL F22 for lectures and dry lab."

# ---------------------------------------------------------------- spec
# days: (header, tuesday?, blocks, staff, resources); blocks: (start hour, span, text, kind).
SPEC = [
 dict(n=1, title="Week 1: orientation (Thu 18 - Fri 19 March 2027)", days=[
  ("Thu 18 Mar", False, [(9,2,"Welcome address and introductory lecture: macrophages, why they matter, why we do what we do (Joel Zindel), 09:00-10:15","PLENARY"),
   (11,1,"Working in the lab and biosafety (Tea Kocijan), 10:30-12:00: Q&A, then the safety sheet is signed","PLENARY"),LUNCH,
   (13,1,"Introduction of the supervisors (what they do and why) and group formation","PLENARY"),
   (14,3,"Experiment planning with your supervisors: hand-draw the pathway you will test (ligand, receptor, output, how an inhibitor proves it, where the polarizer acts), pick your polarizer, stimulus and cytokine (P04, P05, P06) and your extension. Read P01, P02 and P08 for Friday and Tuesday.","DRY")],
   "Rooms, safety officer. Signed safety sheets collected at 12:00. Supervisors sit with their group from 14:00.", F22),
  ("Fri 19 Mar", False, [(9,3,"Hands-on cell culture with the staff culture: hood and sterile technique, microscope, P02 scrape, count, split and seed, cell counter. Then P01: thaw and seed your group's stock flask (course passage 0). Lab tour.","EXP1"),LUNCH,
   (13,4,"Working with git and RStudio, step by step with the supervisors: GitHub account, install R, RStudio and Git if you did not at home, token, clone the course repository from RStudio, switch to your group's branch, open the ELISA script and run it. Then the first commit: a new text file in notebooks/ with your first notes, saved under a name you like, committed as \"hello world\" and pushed to your branch. Then the rest of the environment with your AI tool. Group plan (the drawing and your menu choices) committed to the group branch at 17:00.","DRY")],
   "One low-passage vial per group. Supervisors carry the stock flasks over the weekend and the break: split every 2 to 3 days, course passage counted from this thaw. Afternoon: one supervisor per two laptops; the 08:00 slot is the installation help desk for latecomers. Collect the plans at 17:00.",
   HOODS+" Cell counter. "+F22+" Own laptops, Wi-Fi.")]),
 dict(n=2, title="Week 2: polarize and characterize (Tue 23 - Thu 25 March 2027)", days=[
  ("Tue 23 Mar", True, [OTHER,LUNCH,(13,2,"P02 and P04: plate cells from your stock with the polarizer already in the seeding suspension. Vehicle control, M(pol) and LPS control on the flow plate (6- or 12-well). Plate-and-polarize in one step, about 19 h. Wet-lab goal: plate at a defined density with a stimulus.","EXP1"),(15,2,"Dry lab: scRNA-seq part 1, load the preprocessed object, QC figure. If the bench runs over, the dry lab moves home.","DRY")],
   "Stock flasks counted per group at 12:30. Polarizers, vehicle and LPS at working concentration; plate maps checked before anyone pipettes.", HOODS+" Cell counter."),
  ("Wed 24 Mar", False, [(9,1,"Facility lecture: flow cytometry and FlowJo (Florian Mair) [TODO: confirm slot]","FACILITY"),(10,2,"P08 Harvest the adherent cells, count, viability dye, Fc block, surface stain","EXP1"),LUNCH,
   (13,2,"P08 continued: optional Arg1 fix and perm, fix, store at 4 °C until acquisition. Wet-lab goal: harvest, staining, fixation. Staining plan and FMOs in the notebook.","EXP1"),(15,2,"Dry lab: scRNA-seq part 1 continued; poster: draft the introduction. If the bench runs over, the dry lab moves home.","DRY")],
   "Antibody panel, viability dye, fix/perm buffers, compensation beads. Nothing in the incubator but the stock flasks.", HOODS+" Cooled centrifuge. Fridge. "+F22),
  ("Thu 25 Mar", False, [(9,3,"P08 Acquisition at the facility, two batches of 1.5 h, two groups each [TODO: reservation]","FACILITY"),LUNCH,(13,3,"FlowJo session: gating, FMOs, export statistics; the first figure [TODO: check with Florian Mair the available teaching seats]. Wet-lab goal: acquisition and gating.","FACILITY"),
   (16,1,"Journal club 1 and debrief in one session: did the polarizer do what the menu says on this readout? Stick or pivot; decision in the group branch","PLENARY")],
   "Escort the groups to the facility. Stock flasks: split, two or three backup vials to -80 per group, carried over the break by the staff. Easter: no course.", "Cytometer: 2 slots of 1.5 h [TODO: facility]. "+F22+" FlowJo seats [TODO].")]),
 dict(n=3, title="Week 3: polarize and challenge (Tue 6 - Fri 9 April 2027)", days=[
  ("Tue 6 Apr", True, [OTHER,LUNCH,(13,3,"P02 and P04: plate from your stock (carried over the break) with the chosen polarizer, own approach or the standard that worked. 96-well for supernatants, extra wells for lysates. Passage the stock.","EXP3"),CUTTING_EDGE],
   "Stock flasks counted at 12:30. Polarizers, stimuli, inhibitors, LPS at working concentration. Plate maps checked.", HOODS+" Plate centrifuge."),
  ("Wed 7 Apr", False, [(9,3,"P05 Challenge: your stimulus, optional inhibitor (TAK-242 1 h before, polymyxin B premixed), LPS on M(-) as everyone's control. Default: overnight, IL-6. Alternative: 6 h, TNF, harvest 15:00. Wet-lab goal: stimulate with inhibitor logic.","EXP3"),LUNCH,
   (13,1,"Lecture: single-cell transcriptomics for immunologists, what a signature score means (tbd)","PLENARY"),(14,2,"Dry lab during the challenge: scRNA-seq part 2, signatures from the bulk RAW 264.7 dataset. TNF groups: harvest at 15:00, supernatants and lysates to the freezer.","DRY"),(16,1,"16:30: coat the ELISA plates with capture antibody, overnight at 4 \u00b0C (P06), 30 min at the bench","EXP3")],
   "Ligands, inhibitors and vehicle ready; -20 space and labelled tubes. Lysis buffers for RNA and protein.", HOODS+" "+F22),
  ("Thu 8 Apr", False, [(9,1,"P05 Harvest (overnight groups): supernatants in aliquots, cells as RNA or protein lysate to the freezer","EXP3"),(10,2,"P06 ELISA: blocking, standards, samples; dry lab in the incubations","EXP3"),LUNCH,
   (13,2,"Dry lab during the ELISA incubations: the assay waits for 3.5 h in total, which is used to prepare the next steps and for dry lab (scRNA-seq part 2). The split of wet and dry lab may shift a little.","DRY"),(15,2,"P06 ELISA: detection and read-out; first look at the numbers. Passage the stock. Wet-lab goal: an ELISA from coating to concentration.","EXP3")],
   "ELISA reagents, plate reader booked. Flow on challenged cells only if a group found a slot in the regular booking.", "Plate reader (450 nm). "+HOODS+" "+F22),
  ("Fri 9 Apr", False, [(9,3,"ELISA analysis: standard curve, concentrations. Flow statistics from week 2 in R. scRNA-seq part 2 continued.","DRY"),LUNCH,(13,3,"Poster: what the story has and what it is missing; week 4 plan agreed with your supervisor (repeat, add, or wrap up)","POSTER"),(16,1,"Debrief Exp 3: results and week 4 decisions","PLENARY")],
   "Stock flasks: keep or freeze according to each group's week 4 plan.", F22+" "+HOODS)]),
 dict(n=4, title="Week 4: close the story (Tue 13 - Fri 16 April 2027)", days=[
  ("Tue 13 Apr", True, [OTHER,LUNCH,(13,3,"Optional, as agreed on 9 April: repeat the polarization or the challenge, or a further experiment. Or dry lab: finish the in silico part and the poster. Never at the cost of wrapping up.","EXT"),CUTTING_EDGE],
   "Reagents for the agreed repeats or extensions. Stock flasks for the groups that plate.", HOODS+" Extension-specific instruments as agreed. "+F22),
  ("Wed 14 Apr", False, [(9,3,"Optional harvest and ELISA for groups at the bench; otherwise poster: figures and legends","EXT"),LUNCH,(13,3,"Wrap up: code, figures and poster; scRNA-seq part 3, score the tissue macrophages","POSTER"),(16,1,"Publish or perish: a critical discussion on scientific integrity and output metrics","PLENARY")],
   "Poster template distributed. Plate reader for the groups that ran an ELISA.", HOODS+" "+F22),
  ("Thu 15 Apr", False, [(9,3,"Wrap up: code, figures and poster, with your supervisor. Print when ready (signprint.ch); the PDF goes to the group branch first","POSTER"),LUNCH,(13,4,"Wrap up, continued: code, figures, poster, group branch. Stock flask frozen or discarded.","POSTER")],
   "Poster boards ready. Exam papers printed. Course evaluation goes out as a written survey.", F22+" Poster boards."),
  ("Fri 16 Apr", False, [(9,1,"Lab cleaning","DRY"),(10,2,"Finish the group branch; poster pickup, self-service","DRY"),LUNCH,(13,1,"Written exam, individual [TODO: duration and room]","PLENARY"),
   (14,2,"Poster session: presentations and discussion; prize","PLENARY"),(16,1,"Open 360° feedback round: closes the poster session and opens the apéro","PLENARY")],
   "Exam papers, jury, prize, clean-up checklist. Apéro ordered [TODO: catering]; evaluation survey sent after the course.", F22+" Apéro room [TODO: catering].")]),
]

OVERVIEW = {
    "title": "Overview: the four weeks at a glance (default plan)",
    "rows": [  # (label, [(Mon..Fri text, kind or None)])
        ("Week 1", [None, None, None, ("Welcome and introductory lecture; lab and biosafety; supervisors and groups; the pathway drawing and the menu choices", "PLENARY"),
                    ("Hands-on cell culture; thaw and seed the group's stock flask; git and RStudio from scratch; plan committed", "EXP1")]),
        ("Week 2", [("Other lectures", "BUFFER"), ("Morning: other lectures. 13:00 plate with the polarizer; dry lab", "EXP1"),
                    ("Facility lecture; harvest, stain, fix", "EXP1"),
                    ("Flow acquisition; FlowJo session; journal club and debrief: stick or pivot", "FACILITY"), ("Good Friday", "BUFFER")]),
        ("Easter", [("Break 26 Mar - 4 Apr; staff carry the stock flasks", "BUFFER"), None, None, None, None]),
        ("Week 3", [("Other lectures", "BUFFER"),
                    ("Morning: other lectures. 13:00 plate with the chosen polarizer; passage the stock", "EXP3"),
                    ("Challenge (overnight IL-6 default, 6 h TNF alternative); lecture; coat ELISA plates", "EXP3"),
                    ("Harvest; ELISA with dry lab in the incubations", "EXP3"),
                    ("ELISA analysis; poster: what is missing; debrief", "EXP3")]),
        ("Week 4", [("Other lectures", "BUFFER"),
                    ("Morning: other lectures. 13:00 optional repeat, further experiment, or dry lab", "EXT"),
                    ("Optional harvest and ELISA; wrap up; publish or perish", "POSTER"),
                    ("Wrap up: code, figures, poster; print when ready", "POSTER"),
                    ("Lab cleaning; finish the branch; written exam 13:00; poster session; 360° feedback; Apéro", "PLENARY")]),
    ],
    "foot": ["Course days run 08:00 to 17:00, Tuesdays from 13:00; Monday and Tuesday morning are the students' other "
             "lectures. Every full day opens with a self-study hour. All four groups follow the same plan, each at its "
             "own hood; see the week sheets.",
             "Lectures and dry lab in conference room HPL F22, bench in HPL F27.2. Cutting Edge Immunology Seminar "
             "Tue 16:30-17:30 in weeks 3 and 4."],
}

LEGEND_TEXT = {
    "B7": "Wet lab Exp 1: polarize and characterize (plate with the polarizer, harvest, stain, acquire)",
    "B8": "Wet lab Exp 3: polarize and challenge (plate, stimulate, harvest, ELISA)",
    "A8": "EXP3",
    "A2": "Built by tools/schedule/gantt_build.py on {today}. Hand edits are fine, but a rebuild overwrites the "
          "Overview and the week sheets; lasting changes go into the script. After editing, run "
          "tools/schedule/gantt2readme.py.",
    "B14": "One sheet per week: one column per day, one row per hour, 08:00 to 17:00 (Tuesdays from 13:00; Monday and Tuesday morning are the students' other lectures). Every full day opens with a self-study hour. Below the hour grid: a staff row and a resources row, one cell per day.",
    "B15": "Lecture slots, the facility lecture, cytometer slots and the FlowJo session, journal club, the Tuesday Cutting Edge Immunology Seminar (16:30-17:30) in weeks 3 and 4, the publish-or-perish discussion, exam, poster session. Drawn by the teaching staff, dark cells, thick border, locked. Everything else is flexible.",
    "B16": "Plenary sessions (dark cells, bold) are mandatory. All four groups follow the same plan. Each group "
           "has its own laminar flow hood in HPL F27.2, reserved all day every day, so bench work may shift with "
           "the supervisors' agreement. Lectures and dry lab in conference room HPL F22. Nobody submits a "
           "timetable.",
    "B17": "No checkerboard: with four hoods, all four groups do the same thing at the same time, which keeps "
           "supervision simple. Where the cytometer forces a split (week 3 Thursday), two groups acquire while "
           "the other two run the ELISA, then swap.",
    "B18": "Exp 1 (week 2): polarize and characterize. Plate from the group's stock with the polarizer in the seeding suspension, vehicle and LPS controls beside it; harvest, stain, acquire; FlowJo; decide to stick or pivot before the break. Exp 2 (dry lab, weeks 2 to 4): comparison of in vitro versus in vivo polarization, see the Dry lab row. Exp 3 (week 3): polarize and challenge. Plate with the polarizer on Tuesday, challenge on Wednesday with the group's stimulus and optional inhibitor (LPS on M(-) shared by all), overnight with an IL-6 readout by default or 6 h with TNF; ELISA on Thursday. Week 4: repeat, add, or wrap up. Menus in P04 and P05. Protocol IDs (P01...) refer to protocols/ in the course repository.",
    "B19": "Week 1: environment and templates. Exp 2, the in silico comparison, runs through weeks 2 to 4. Week 2: scRNA-seq part 1 (QC) in the afternoon dry-lab slots, FlowJo on the own data. Week 3: scRNA-seq part 2 (signatures from the bulk RAW 264.7 dataset) during the challenge and the ELISA incubations, own ELISA data on Friday. Week 4: scRNA-seq part 3 (scoring of the tissue macrophages), wrap up of code, figures and poster.",
    "B20": "A group whose polarization or challenge failed repeats it in week 4, Tuesday 13:00 to Wednesday, as agreed with the supervisor on Friday 9 April; never at the cost of wrapping up.",
    "B24": "[TODO] Cytometer: two slots of 1.5 h on Thu 25 March 09:00-12:00 (two groups each); FlowJo teaching seats for the session on Thu 25 March 13:00 (Florian Mair). Week 3 and 4 slots only through the regular booking calendar.",
    "B25": "[TODO] Facility lecture: slot on Wed 24 March 09:00.",
    "B21": "Fri 26 March to Sun 4 April. No course. The staff carry the groups' stock flasks over the break (split every 2 to 3 days, backup vials frozen on Thu 25 March).",
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

    for d, (hdr, tuesday, blocks, staff, resources) in enumerate(spec["days"]):
        c = 2 + d
        put(ws, 3, c, hdr, bold=True, fill=HEADER_FILL, valign="center")
        if not tuesday:
            blocks = [SELF_STUDY] + list(blocks)
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
