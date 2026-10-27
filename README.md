# Blockrophage course

**Macrophage Biology: in vitro, in vivo, in silico.** Block course, D-BIOL, ETH
Zürich, Spring Semester 2027. Zindel lab (TizzuLab).

> **Under construction.** This course runs for the first time in spring 2027 and is
> being built in the open. Interested students are welcome to apply and to give
> input, through the [contact page](https://zindellab.ch/contact.html) or an
> [issue](https://github.com/TizzuLab/blockrophage-course/issues). **Please do not use
> these protocols in the lab yet.** Values are unverified until this notice is gone;
> items marked `[TODO]` are open.

| | |
|---|---|
| Course title | Macrophage Biology: in vitro, in vivo, in silico `[TODO: confirm final title]` |
| Course number / ECTS | / 6 ECTS |
| Dates | Thu 18 March to Fri 16 April 2027, 16 working days; no course Fri 26 March to Sun 4 April (Easter break) |
| Lecturer | Prof. Dr. med. Joel Zindel |
| Teaching staff | Two supervisors per group: Alicia Halbach, Marielle Airoldi, Manuel Prampolini, Agnes Huber, Tea Kocijan, Franzi Ampenberger, John Li Flores Alvarez, Brooke Slade; flow cytometry facility `[TODO: name]` |
| Location | HPL, F floor `[TODO: seminar room, flow facility]` |
| Students | 8, in four groups of two |
| Prerequisites | None. The course starts from scratch: no prior immunology, no cell culture and no programming experience required. See *What you need for this course* below |
| Language | English |
| Version | 0.5, 2026-10-27 |

## What you need for this course

No prior knowledge; the [lectures](slides/) are optional reading.

1. Create **a GitHub account** at [github.com](https://github.com) before the first
   day and send us your username.
2. We need **your ok to work on a public repository**, where your edits and your name
   are visible to anyone. Take this into account when you create your account.
3. Bring **a laptop**; any operating system works.
4. You may **optionally deploy your favourite LLM as a learning coach** by dropping
   the LLM-friendly version of this repository, the
   [companion package](#your-companion), into a session.

Each group has two supervisors from the teaching staff who own the group's branch of
this repository (Section 3).

## 1. Concept

Every student arrives with the textbook picture of macrophages: M1 kills, M2 heals.
In this course you first build that picture with your own hands, in a dish. Then you
take it to real tissue macrophages, in a published single-cell dataset of injured
peritoneum, and test whether it survives. It will not survive intact. The field made
the same discovery about ten years ago and rewrote its nomenclature; you make it in
four weeks. The [background reading](background/macrophage_biology.md) tells that
story and condenses the optional [lectures](slides/).

The course rests on three principles.

- **Learning by doing.** You run every experiment yourself, including the one that
  goes wrong, and we analyse the failures together.
- **Half of what we teach is wrong, and we do not know which half.** The M1/M2 story
  is the textbook example of knowledge that had to be revised. You reproduce the
  evidence that forced the revision.
- **You are a cyborg.** You use large language models to set up software, write and
  debug analysis code, and read protocols. Information is cheap; verified information
  is not.

One question, three arms. Each arm is one move in an argument about the M1/M2
paradigm: reproduce it, test it, then ask what it is still good for.

| Arm | What you do | What it answers |
|---|---|---|
| 1. In vitro: reproduce the paradigm | Establish a RAW 264.7 culture and polarize it with the defined stimuli behind the textbook states, M(IFNγ), M(IL-4) and M(IFNγ+LPS). Quantify cytokines, nitric oxide and surface phenotype | Does the M1/M2 picture reproduce in a dish, with your hands, and how clean is it? |
| 2. In silico: does the paradigm hold in living systems? | Derive the M(IFNγ+LPS) and M(IL-4) signatures from a public RAW 264.7 dataset and score every macrophage of single-cell transcriptomes from living model systems against them: a published dataset of injured mouse peritoneum (GSE186658) and a human dataset of homeostatic peritoneal fluid (GSE228030, preprocessed by the lab's HuMac pipeline) | How much of a real tissue macrophage population the in vitro states explain, and where the paradigm breaks |
| 3. Challenge: is the heuristic still useful? | A model that is not 100 % true can still be useful. Challenge the polarized states through pattern-recognition receptors, with LPS and with the PRR axis your group chose, and measure how each state responds | Whether the classical states predict behaviour under a danger signal, which is what a heuristic has to do to earn its keep |

Arms 1 and 3 run on the same cells in the same week (Exp 2, Section 5). The
extensions (Section 6) take the question into tissue, with surplus primary material
from ongoing work in the lab: flow cytometry of primary peritoneal cells on the same
antibody panel as your in vitro cells, and F4/80 immunohistochemistry on tissue
sections.

## 2. Learning objectives

After this course you can:

1. **Classify** macrophages by ontogeny, niche and activation state, use the
   M(stimulus) nomenclature correctly, and explain why the M1/M2 dichotomy was revised.
2. **Culture** a mammalian cell line from vial to vial: thaw, count, split, seed,
   freeze, and document a growth curve and a viability.
3. **Polarize and challenge** macrophages in vitro and quantify the response by
   ELISA, Griess assay and flow cytometry, with the controls that make the result
   interpretable.
4. **Score** single cells against a gene signature, explain what the score means and
   what it does not, and state the limits of comparing a dish with a tissue.
5. **Set up** a reproducible analysis environment from a code repository with a large
   language model as assistant, and verify or refute what the assistant produces.
6. **Communicate** results as a poster and a short talk, including an honest account of
   what went wrong and what it taught you.

## 3. How the course works

**Groups and supervisors.** Four groups of two students, mixed so that every group
has someone comfortable at the bench and someone comfortable at the keyboard. Each
group has two supervisors from the teaching staff who travel with it for the whole
course and share the time between them. Supervisors may fold in experiments the lab
needs anyway; those go into the group notebook like any other experiment and may
appear on the poster.

**Git and group branches.** This repository is the course, and each group works in
its own branch of it, named by year and group (for example `2027/group-a`). Your
supervisors own that branch: you push your changes to a branch of your own and open a
pull request into the group branch, a supervisor reviews and merges. At the end of
the course every group branch is a pull request into `main`; what was better than
the original goes into next year's course, with your name on the commit. Nobody
needs git experience on day one; the first morning covers accounts, cloning and the
first pull request, and the companion knows the commands.

**Lab notebook.** One shared electronic notebook per group `[TODO: tool, or the
group branch itself]`. It contains your experiment plan, raw data and the analysis.
The notebook is part of the grade.

**Up your nerd factor.** Beyond the core programme there is a menu of optional
experiments and extensions (Section 6). What your group adds is your choice, agreed
with your supervisor on the first afternoon and revised at the debriefs. How
extensions are recognised is still open `[TODO]`.

**Failure round.** On the Wednesday of week 4, after the writing lecture and a day
of poster production, each group presents one thing that went wrong and what it
taught them. A failed experiment that is properly analysed is worth as much as one
that worked.

**Rules of the lab.** The same rules as in every research lab.

- Plan what you will do. Read the protocol the day before, check that reagents are
  there, design the controls before you pipette anything.
- Do what you planned, and record what you did, the same day, including every
  deviation.
- Label every tube, plate and solution with content, date and group.
- Keep enzymes, antibodies and cells at the recommended temperature. Reagents are
  expensive, some are irreplaceable within the course.
- If you have a question, ask your supervisor. If you have a problem, ask earlier.

**Attendance.** Attendance on all 16 days is mandatory and a prerequisite to pass.
An unavoidable absence is announced in writing to the course coordinator and to
Prof. Zindel before it happens.

**Primary material.** The core programme uses the RAW 264.7 cell line only. For the
extensions we may be able to provide primary tissues or cells that are surplus from
ongoing experimental work in the lab.

**Open ear.** An anonymous online form is open for the whole course for feedback,
concerns and ideas `[TODO: link]`.

## 4. Schedule

Course hours are 09:00 to 17:00, lunch 12:00 to 13:00, Thu 18 March to Fri 16
April 2027 with the Easter break from Fri 26 March to Sun 4 April (no course, no
cultures).

**How to read this schedule.** Sessions in **bold** are plenary and mandatory:
lectures, seminars, journal clubs, debriefs, the failure round, the recap and the
poster day. The wet-lab times listed for your group are guaranteed: hoods and
cytometer slots are reserved for you then. Everything else is orientation. If space
permits, which it usually will, your group can shift work with your supervisor's
agreement. Nobody submits a timetable; your plan lives in your notebook and changes
when the experiments do.

**Capacity.** Two groups work at the bench per half day, the other two in the dry
lab, swapped after lunch. Groups A and B form one pair, C and D the other, and the
pairs stay fixed within a week because the group that starts an overnight step
harvests it. `[TODO: hoods available per half day]`

The drawings below are generated from the workbook
`tools/schedule/Blockcourse_Gantt_FS2027.xlsx`: to change the schedule, edit the
workbook and run `python3 tools/schedule/gantt2readme.py` (CI does it on push). Under
each drawing is a folded text version, which is what the companion reads.

<!-- schedule:begin -->
<!-- Generated from tools/schedule/Blockcourse_Gantt_FS2027.xlsx by tools/schedule/gantt2readme.py. Do not edit by hand: edit the workbook and rerun. -->

### Week 1: orientation (Thu 18 - Fri 19 March 2027), 09:00-17:00

![Week 1: orientation (Thu 18 - Fri 19 March 2027), 09:00-17:00](figures/schedule/week-1.svg?v=0ca461ae)

<details><summary>Text version (what the companion reads)</summary>

#### Thu 18 Mar

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | [Plenary, lecture, debrief] Welcome, safety briefing, group formation; [Plenary, lecture, debrief] Lecture: tissue macrophages and nomenclature | - | [Plenary, lecture, debrief] Lecture: the techniques of this course, one slide per method |
| Group A supervisors: ______ / ______ | [Plenary, lecture, debrief] Plenary | Lunch | [Plenary, lecture, debrief] Lecture; [Dry lab and desk work] Experiment planning with your supervisors: choose your PRR axis and your extensions |
| Group B supervisors: ______ / ______ | [Plenary, lecture, debrief] Plenary | Lunch | [Plenary, lecture, debrief] Lecture; [Dry lab and desk work] Experiment planning with your supervisors: choose your PRR axis and your extensions |
| Group C supervisors: ______ / ______ | [Plenary, lecture, debrief] Plenary | Lunch | [Plenary, lecture, debrief] Lecture; [Dry lab and desk work] Experiment planning with your supervisors: choose your PRR axis and your extensions |
| Group D supervisors: ______ / ______ | [Plenary, lecture, debrief] Plenary | Lunch | [Plenary, lecture, debrief] Lecture; [Dry lab and desk work] Experiment planning with your supervisors: choose your PRR axis and your extensions |
| Staff (shared) prep and supervision | Rooms, safety officer, group list. Supervisors sit with their group from 14:00. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Seminar room all day | (same as previous column) | (same as previous column) |

#### Fri 19 Mar

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | - | - | [Facility slot] Facility lecture: flow cytometry and FlowJo [TODO: confirm slot with the facility] |
| Group A supervisors: ______ / ______ | [Dry lab and desk work] Dry lab setup: clone the course repository, build the environment with your LLM, run the ELISA template on example data | Lunch | [Facility slot] Facility lecture; [Dry lab and desk work] Lab tour. Group plans submitted. Read P01 for Monday. |
| Group B supervisors: ______ / ______ | [Dry lab and desk work] Dry lab setup: clone the course repository, build the environment with your LLM, run the ELISA template on example data | Lunch | [Facility slot] Facility lecture; [Dry lab and desk work] Lab tour. Group plans submitted. Read P01 for Monday. |
| Group C supervisors: ______ / ______ | [Dry lab and desk work] Dry lab setup: clone the course repository, build the environment with your LLM, run the ELISA template on example data | Lunch | [Facility slot] Facility lecture; [Dry lab and desk work] Lab tour. Group plans submitted. Read P01 for Monday. |
| Group D supervisors: ______ / ______ | [Dry lab and desk work] Dry lab setup: clone the course repository, build the environment with your LLM, run the ELISA template on example data | Lunch | [Facility slot] Facility lecture; [Dry lab and desk work] Lab tour. Group plans submitted. Read P01 for Monday. |
| Staff (shared) prep and supervision | Dry lab: walk around, unblock installs. Fallback environment ready [TODO]. Collect the group plans at 17:00. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Computer room or own laptops; Wi-Fi; FlowJo seats [TODO: facility] | (same as previous column) | (same as previous column) |

</details>

### Week 2: Exp 1, establish the line (Mon 22 - Thu 25 March 2027)

![Week 2: Exp 1, establish the line (Mon 22 - Thu 25 March 2027)](figures/schedule/week-2.svg?v=5a1e72cb)

<details><summary>Text version (what the companion reads)</summary>

#### Mon 22 Mar

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | - | [Plenary, lecture, debrief] IMHS Lunch Seminar | - |
| Group A supervisors: ______ / ______ | [Wet lab Exp 1] P01 Thaw RAW 264.7, count (T0), seed the flask | [Plenary, lecture, debrief] IMHS Lunch Seminar | [Dry lab and desk work] Dry lab: analysis templates on example data (ELISA, Griess) |
| Group B supervisors: ______ / ______ | [Wet lab Exp 1] P01 Thaw RAW 264.7, count (T0), seed the flask | [Plenary, lecture, debrief] IMHS Lunch Seminar | [Dry lab and desk work] Dry lab: analysis templates on example data (ELISA, Griess) |
| Group C supervisors: ______ / ______ | [Dry lab and desk work] Dry lab: analysis templates on example data (ELISA, Griess) | [Plenary, lecture, debrief] IMHS Lunch Seminar | [Wet lab Exp 1] P01 Thaw RAW 264.7, count (T0), seed the flask |
| Group D supervisors: ______ / ______ | [Dry lab and desk work] Dry lab: analysis templates on example data (ELISA, Griess) | [Plenary, lecture, debrief] IMHS Lunch Seminar | [Wet lab Exp 1] P01 Thaw RAW 264.7, count (T0), seed the flask |
| Staff (shared) prep and supervision | Medium warmed, one vial per group at 09:00 and 13:00. Supervisor at the hood with the group for the thaw. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Hoods: 2 groups per half day [TODO: hoods available]. Incubator: one shelf per group. Cell counter. | (same as previous column) | (same as previous column) |

#### Tue 23 Mar

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | - | - | [Plenary, lecture, debrief] Cutting Edge Immunology Seminar 16:30-17:30 |
| Group A supervisors: ______ / ______ | [Wet lab Exp 1] P01 Inspect, count (T1), medium change | Lunch | [Dry lab and desk work] Dry lab: FlowJo on example data. Poster: draft the introduction; [Plenary, lecture, debrief] Seminar |
| Group B supervisors: ______ / ______ | [Wet lab Exp 1] P01 Inspect, count (T1), medium change | Lunch | [Dry lab and desk work] Dry lab: FlowJo on example data. Poster: draft the introduction; [Plenary, lecture, debrief] Seminar |
| Group C supervisors: ______ / ______ | [Dry lab and desk work] Dry lab: FlowJo on example data. Poster: draft the introduction | Lunch | [Wet lab Exp 1] P01 Inspect, count (T1), medium change; [Plenary, lecture, debrief] Seminar |
| Group D supervisors: ______ / ______ | [Dry lab and desk work] Dry lab: FlowJo on example data. Poster: draft the introduction | Lunch | [Wet lab Exp 1] P01 Inspect, count (T1), medium change; [Plenary, lecture, debrief] Seminar |
| Staff (shared) prep and supervision | Cultures inspected 08:00. Counting chambers or counter ready. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Computer room / laptops; FlowJo seats [TODO] | (same as previous column) | (same as previous column) |

#### Wed 24 Mar

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | [Plenary, lecture, debrief] Lecture: tissue repair I, macrophages in injury and repair | - | - |
| Group A supervisors: ______ / ______ | [Plenary, lecture, debrief] Lecture; [Wet lab Exp 1] P02 Count (T2), scrape, split; seed growth-curve wells | Lunch | [Dry lab and desk work] Dry lab: growth curve and doubling time from your counts. Poster: why does this matter (significance) |
| Group B supervisors: ______ / ______ | [Plenary, lecture, debrief] Lecture; [Wet lab Exp 1] P02 Count (T2), scrape, split; seed growth-curve wells | Lunch | [Dry lab and desk work] Dry lab: growth curve and doubling time from your counts. Poster: why does this matter (significance) |
| Group C supervisors: ______ / ______ | [Plenary, lecture, debrief] Lecture; [Dry lab and desk work] Dry lab: growth curve and doubling time from your counts. Poster: why does this matter (significance) | Lunch | [Wet lab Exp 1] P02 Count (T2), scrape, split; seed growth-curve wells |
| Group D supervisors: ______ / ______ | [Plenary, lecture, debrief] Lecture; [Dry lab and desk work] Dry lab: growth curve and doubling time from your counts. Poster: why does this matter (significance) | Lunch | [Wet lab Exp 1] P02 Count (T2), scrape, split; seed growth-curve wells |
| Staff (shared) prep and supervision | Plates, scrapers. Look at every split before it goes back in the incubator. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Hoods as Mon. Plates: 6-well or 12-well for the growth curve [TODO: lab standard] | (same as previous column) | (same as previous column) |

#### Thu 25 Mar

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | [Plenary, lecture, debrief] Journal club 1: the M1/M2 nomenclature revision [TODO: paper]; one group presents, all read | - | [Plenary, lecture, debrief] Debrief week 2: what worked, plan for Exp 2 |
| Group A supervisors: ______ / ______ | [Plenary, lecture, debrief] Journal club; [Wet lab Exp 1] P01 Count (T3). P03 Freeze your own vials. Clean-up: nothing stays in culture over the break | Lunch | [Dry lab and desk work] Dry lab: scRNA-seq part 1, load the preprocessed object, QC figure; [Plenary, lecture, debrief] Debrief |
| Group B supervisors: ______ / ______ | [Plenary, lecture, debrief] Journal club; [Wet lab Exp 1] P01 Count (T3). P03 Freeze your own vials. Clean-up: nothing stays in culture over the break | Lunch | [Dry lab and desk work] Dry lab: scRNA-seq part 1, load the preprocessed object, QC figure; [Plenary, lecture, debrief] Debrief |
| Group C supervisors: ______ / ______ | [Plenary, lecture, debrief] Journal club; [Dry lab and desk work] Dry lab: scRNA-seq part 1, load the preprocessed object, QC figure | Lunch | [Wet lab Exp 1] P01 Count (T3). P03 Freeze your own vials. Clean-up: nothing stays in culture over the break; [Plenary, lecture, debrief] Debrief |
| Group D supervisors: ______ / ______ | [Plenary, lecture, debrief] Journal club; [Dry lab and desk work] Dry lab: scRNA-seq part 1, load the preprocessed object, QC figure | Lunch | [Wet lab Exp 1] P01 Count (T3). P03 Freeze your own vials. Clean-up: nothing stays in culture over the break; [Plenary, lecture, debrief] Debrief |
| Staff (shared) prep and supervision | Freezing boxes in the -80. Collect all cultures at 17:00. Easter: thaw backup RAW on Wed 31 Mar, split Fri 2 Apr, so Exp 2 plates can be seeded Mon 5 Apr. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | -80 freezer box per group; Mr Frosty or equivalent [TODO: lab standard] | (same as previous column) | (same as previous column) |

Notes: Exp 1 is a real experiment: four counts give a growth curve and a doubling time against the published value; viability of your own vial on Mon 5 Apr is the second readout. Easter break Fri 26 Mar to Sun 4 Apr: no course, no cultures. Mondays 12:00-13:00: IMHS Lunch Seminar. Tuesdays: Cutting Edge Immunology Seminar runs 16:30-17:30.

</details>

### Week 3: Exp 2, polarize and challenge (Mon 5 - Fri 9 April 2027)

![Week 3: Exp 2, polarize and challenge (Mon 5 - Fri 9 April 2027)](figures/schedule/week-3.svg?v=5356033f)

<details><summary>Text version (what the companion reads)</summary>

#### Mon 5 Apr

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | - | [Plenary, lecture, debrief] IMHS Lunch Seminar | - |
| Group A supervisors: ______ / ______ | [Dry lab and desk work] Dry lab: scRNA-seq part 2, derive M(IFNg+LPS) and M(IL-4) signatures from the bulk RAW 264.7 dataset | [Plenary, lecture, debrief] IMHS Lunch Seminar | [Wet lab Exp 2] P01 Thaw your own vial (viability = Exp 1 readout). P02 Seed Exp 2 plates from the staff culture |
| Group B supervisors: ______ / ______ | [Dry lab and desk work] Dry lab: scRNA-seq part 2, derive M(IFNg+LPS) and M(IL-4) signatures from the bulk RAW 264.7 dataset | [Plenary, lecture, debrief] IMHS Lunch Seminar | [Wet lab Exp 2] P01 Thaw your own vial (viability = Exp 1 readout). P02 Seed Exp 2 plates from the staff culture |
| Group C supervisors: ______ / ______ | [Wet lab Exp 2] P01 Thaw your own vial (viability = Exp 1 readout). P02 Seed Exp 2 plates from the staff culture | [Plenary, lecture, debrief] IMHS Lunch Seminar | [Dry lab and desk work] Dry lab: scRNA-seq part 2, derive M(IFNg+LPS) and M(IL-4) signatures from the bulk RAW 264.7 dataset |
| Group D supervisors: ______ / ______ | [Wet lab Exp 2] P01 Thaw your own vial (viability = Exp 1 readout). P02 Seed Exp 2 plates from the staff culture | [Plenary, lecture, debrief] IMHS Lunch Seminar | [Dry lab and desk work] Dry lab: scRNA-seq part 2, derive M(IFNg+LPS) and M(IL-4) signatures from the bulk RAW 264.7 dataset |
| Staff (shared) prep and supervision | Backup RAW thawed Wed 31 Mar, split Fri 2 Apr: enough cells to seed four groups. Plates, cytokines ready. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Hoods: 2 groups per half day. Incubator shelves. | (same as previous column) | (same as previous column) |

#### Tue 6 Apr

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | [Plenary, lecture, debrief] Lecture: single-cell transcriptomics for immunologists, what a signature score means | - | [Plenary, lecture, debrief] Cutting Edge Immunology Seminar 16:30-17:30 |
| Group A supervisors: ______ / ______ | [Plenary, lecture, debrief] Lecture; [Dry lab and desk work] Dry lab: scRNA-seq part 3, score the tissue macrophages. Poster: methods | Lunch | [Wet lab Exp 2] P04 Polarize: M(-), M(IFNg), M(IL-4), M(IFNg+LPS), 24 h; [Plenary, lecture, debrief] Seminar |
| Group B supervisors: ______ / ______ | [Plenary, lecture, debrief] Lecture; [Dry lab and desk work] Dry lab: scRNA-seq part 3, score the tissue macrophages. Poster: methods | Lunch | [Wet lab Exp 2] P04 Polarize: M(-), M(IFNg), M(IL-4), M(IFNg+LPS), 24 h; [Plenary, lecture, debrief] Seminar |
| Group C supervisors: ______ / ______ | [Plenary, lecture, debrief] Lecture; [Wet lab Exp 2] P04 Polarize: M(-), M(IFNg), M(IL-4), M(IFNg+LPS), 24 h | Lunch | [Dry lab and desk work] Dry lab: scRNA-seq part 3, score the tissue macrophages. Poster: methods; [Plenary, lecture, debrief] Seminar |
| Group D supervisors: ______ / ______ | [Plenary, lecture, debrief] Lecture; [Wet lab Exp 2] P04 Polarize: M(-), M(IFNg), M(IL-4), M(IFNg+LPS), 24 h | Lunch | [Dry lab and desk work] Dry lab: scRNA-seq part 3, score the tissue macrophages. Poster: methods; [Plenary, lecture, debrief] Seminar |
| Staff (shared) prep and supervision | IFNg, IL-4, LPS aliquots at working concentration. Plate maps checked before anyone pipettes. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Hoods. Cytokine stocks [TODO: supplier]. | (same as previous column) | (same as previous column) |

#### Wed 7 Apr

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | [Facility slot] Cytometer slot, groups C+D [TODO: facility reservation] | (same as previous column) | [Facility slot] Cytometer slot, groups A+B [TODO: facility reservation] |
| Group A supervisors: ______ / ______ | [Dry lab and desk work] Dry lab: FlowJo gating of your own data, export statistics | Lunch | [Wet lab Exp 2] P04 Wash. P05 Challenge: LPS + your axis, overnight (about 20 h). P08 Stain the unchallenged wells, acquire in the facility slot |
| Group B supervisors: ______ / ______ | [Dry lab and desk work] Dry lab: FlowJo gating of your own data, export statistics | Lunch | [Wet lab Exp 2] P04 Wash. P05 Challenge: LPS + your axis, overnight (about 20 h). P08 Stain the unchallenged wells, acquire in the facility slot |
| Group C supervisors: ______ / ______ | [Wet lab Exp 2] P04 Wash. P05 Challenge: LPS + your axis, overnight (about 20 h). P08 Stain the unchallenged wells, acquire in the facility slot | (same as previous column) | [Dry lab and desk work] Dry lab: FlowJo gating of your own data, export statistics |
| Group D supervisors: ______ / ______ | [Wet lab Exp 2] P04 Wash. P05 Challenge: LPS + your axis, overnight (about 20 h). P08 Stain the unchallenged wells, acquire in the facility slot | (same as previous column) | [Dry lab and desk work] Dry lab: FlowJo gating of your own data, export statistics |
| Staff (shared) prep and supervision | Ligands for every axis. Antibody panel and viability dye. Escort the groups to the facility. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Cytometer: 2 slots of 2 h [TODO: facility]. Hoods. | (same as previous column) | (same as previous column) |

#### Thu 8 Apr

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | [Plenary, lecture, debrief] Journal club 2: the peritoneal injury single-cell paper behind GSE186658 [TODO: paper]; one group presents, all read | - | - |
| Group A supervisors: ______ / ______ | [Plenary, lecture, debrief] Journal club; [Dry lab and desk work] Dry lab: flow statistics in R. Poster: figure 1 draft | Lunch | [Wet lab Exp 2] P05 Harvest supernatants. P06 ELISA IL-6 and TNF. P07 Griess |
| Group B supervisors: ______ / ______ | [Plenary, lecture, debrief] Journal club; [Dry lab and desk work] Dry lab: flow statistics in R. Poster: figure 1 draft | Lunch | [Wet lab Exp 2] P05 Harvest supernatants. P06 ELISA IL-6 and TNF. P07 Griess |
| Group C supervisors: ______ / ______ | [Plenary, lecture, debrief] Journal club; [Wet lab Exp 2] P05 Harvest supernatants. P06 ELISA IL-6 and TNF. P07 Griess | Lunch | [Dry lab and desk work] Dry lab: flow statistics in R. Poster: figure 1 draft |
| Group D supervisors: ______ / ______ | [Plenary, lecture, debrief] Journal club; [Wet lab Exp 2] P05 Harvest supernatants. P06 ELISA IL-6 and TNF. P07 Griess | Lunch | [Dry lab and desk work] Dry lab: flow statistics in R. Poster: figure 1 draft |
| Staff (shared) prep and supervision | ELISA kits, Griess reagents, plate reader booked. Dilution series decided with each group. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Plate reader (450 nm, 540 nm). Hoods. | (same as previous column) | (same as previous column) |

#### Fri 9 Apr

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | - | - | [Plenary, lecture, debrief] Debrief Exp 2: results, extension choices, rescue decisions |
| Group A supervisors: ______ / ______ | [Dry lab and desk work] Dry lab: ELISA and Griess analysis. Poster: results so far | Lunch | [Wet lab Exp 2] Plate reader runs, repeats where needed, clean-up. Check your own-vial culture; [Plenary, lecture, debrief] Debrief |
| Group B supervisors: ______ / ______ | [Dry lab and desk work] Dry lab: ELISA and Griess analysis. Poster: results so far | Lunch | [Wet lab Exp 2] Plate reader runs, repeats where needed, clean-up. Check your own-vial culture; [Plenary, lecture, debrief] Debrief |
| Group C supervisors: ______ / ______ | [Wet lab Exp 2] Plate reader runs, repeats where needed, clean-up. Check your own-vial culture | Lunch | [Dry lab and desk work] Dry lab: ELISA and Griess analysis. Poster: results so far; [Plenary, lecture, debrief] Debrief |
| Group D supervisors: ______ / ______ | [Wet lab Exp 2] Plate reader runs, repeats where needed, clean-up. Check your own-vial culture | Lunch | [Dry lab and desk work] Dry lab: ELISA and Griess analysis. Poster: results so far; [Plenary, lecture, debrief] Debrief |
| Staff (shared) prep and supervision | Plate reader. -20 space for supernatants. Seed rescue plates Fri PM for groups that need the rescue path (see Legend). | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Plate reader. Freezer. | (same as previous column) | (same as previous column) |

Notes: One overnight challenge arm (about 20 h): challenge as the last step of your half day, harvest as the first step of the same half day the next day, so every group's duration is the same; record the real time. The 6 h RNA arm belongs to the qPCR extension X01. Pairs stay fixed within the week. Mondays 12:00-13:00: IMHS Lunch Seminar. Tuesdays: Cutting Edge Immunology Seminar runs 16:30-17:30. Wed: groups C+D keep their cytometer slot (11:00-13:00) and have lunch afterwards.

</details>

### Week 4: extensions, poster, presentations (Mon 12 - Fri 16 April 2027)

![Week 4: extensions, poster, presentations (Mon 12 - Fri 16 April 2027)](figures/schedule/week-4.svg?v=db0352f6)

<details><summary>Text version (what the companion reads)</summary>

#### Mon 12 Apr

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | - | [Plenary, lecture, debrief] IMHS Lunch Seminar | - |
| Group A supervisors: ______ / ______ | [Extension / nerd factor] Extension of your choice, or rescue path for Exp 2 (see Legend) | [Plenary, lecture, debrief] IMHS Lunch Seminar | [Dry lab and desk work] Dry lab: analysis of Exp 2. Poster: figures |
| Group B supervisors: ______ / ______ | [Extension / nerd factor] Extension of your choice, or rescue path for Exp 2 (see Legend) | [Plenary, lecture, debrief] IMHS Lunch Seminar | [Dry lab and desk work] Dry lab: analysis of Exp 2. Poster: figures |
| Group C supervisors: ______ / ______ | [Dry lab and desk work] Dry lab: analysis of Exp 2. Poster: figures | [Plenary, lecture, debrief] IMHS Lunch Seminar | [Extension / nerd factor] Extension of your choice, or rescue path for Exp 2 (see Legend) |
| Group D supervisors: ______ / ______ | [Dry lab and desk work] Dry lab: analysis of Exp 2. Poster: figures | [Plenary, lecture, debrief] IMHS Lunch Seminar | [Extension / nerd factor] Extension of your choice, or rescue path for Exp 2 (see Legend) |
| Staff (shared) prep and supervision | Reagents for the extensions agreed on Fri 9 Apr. Rescue plates: polarize Mon. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Hoods Mon and Tue only. Extension-specific instruments as agreed. | (same as previous column) | (same as previous column) |

#### Tue 13 Apr

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | - | - | [Plenary, lecture, debrief] Cutting Edge Immunology Seminar 16:30-17:30 |
| Group A supervisors: ______ / ______ | [Extension / nerd factor] Extension, continued | Lunch | [Dry lab and desk work] Dry lab: extension analysis. Poster: figures and legends; [Plenary, lecture, debrief] Seminar |
| Group B supervisors: ______ / ______ | [Extension / nerd factor] Extension, continued | Lunch | [Dry lab and desk work] Dry lab: extension analysis. Poster: figures and legends; [Plenary, lecture, debrief] Seminar |
| Group C supervisors: ______ / ______ | [Dry lab and desk work] Dry lab: extension analysis. Poster: figures and legends | Lunch | [Extension / nerd factor] Extension, continued; [Plenary, lecture, debrief] Seminar |
| Group D supervisors: ______ / ______ | [Dry lab and desk work] Dry lab: extension analysis. Poster: figures and legends | Lunch | [Extension / nerd factor] Extension, continued; [Plenary, lecture, debrief] Seminar |
| Staff (shared) prep and supervision | Rescue plates: challenge Tue. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Hoods Mon and Tue only. Extension-specific instruments as agreed. | (same as previous column) | (same as previous column) |

#### Wed 14 Apr

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | [Plenary, lecture, debrief] Lecture: scientific writing, from data to argument, poster structure, figure design, honest limits | - | [Plenary, lecture, debrief] Failure round: each group presents one thing that went wrong and what it taught them |
| Group A supervisors: ______ / ______ | [Plenary, lecture, debrief] Lecture; [Poster and writing] Poster production with your supervisor | Lunch | [Poster and writing] Poster production with your supervisor; [Plenary, lecture, debrief] Failure round |
| Group B supervisors: ______ / ______ | [Plenary, lecture, debrief] Lecture; [Poster and writing] Poster production with your supervisor | Lunch | [Poster and writing] Poster production with your supervisor; [Plenary, lecture, debrief] Failure round |
| Group C supervisors: ______ / ______ | [Plenary, lecture, debrief] Lecture; [Poster and writing] Poster production with your supervisor | Lunch | [Poster and writing] Poster production with your supervisor; [Plenary, lecture, debrief] Failure round |
| Group D supervisors: ______ / ______ | [Plenary, lecture, debrief] Lecture; [Poster and writing] Poster production with your supervisor | Lunch | [Poster and writing] Poster production with your supervisor; [Plenary, lecture, debrief] Failure round |
| Staff (shared) prep and supervision | Poster template distributed, printing booked [TODO: printer]. Rescue plates: harvest 09:00. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Seminar room Wed to Fri. Printer [TODO]. Poster boards. Apéro room [TODO: catering]. | (same as previous column) | (same as previous column) |

#### Thu 15 Apr

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | - | - | [Plenary, lecture, debrief] Recap and Q&A: the course in one hour, then open questions with the teaching staff |
| Group A supervisors: ______ / ______ | [Poster and writing] Poster production, final figures and legends | Lunch | [Poster and writing] Final checks. Printing deadline 14:00: poster PDF committed to the group branch; [Plenary, lecture, debrief] Recap and Q&A |
| Group B supervisors: ______ / ______ | [Poster and writing] Poster production, final figures and legends | Lunch | [Poster and writing] Final checks. Printing deadline 14:00: poster PDF committed to the group branch; [Plenary, lecture, debrief] Recap and Q&A |
| Group C supervisors: ______ / ______ | [Poster and writing] Poster production, final figures and legends | Lunch | [Poster and writing] Final checks. Printing deadline 14:00: poster PDF committed to the group branch; [Plenary, lecture, debrief] Recap and Q&A |
| Group D supervisors: ______ / ______ | [Poster and writing] Poster production, final figures and legends | Lunch | [Poster and writing] Final checks. Printing deadline 14:00: poster PDF committed to the group branch; [Plenary, lecture, debrief] Recap and Q&A |
| Staff (shared) prep and supervision | Posters printed Thu after 14:00 [TODO: printer]. Rescue groups: ELISA in the morning, result on the poster by 14:00. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Seminar room Wed to Fri. Printer [TODO]. Poster boards. Apéro room [TODO: catering]. | (same as previous column) | (same as previous column) |

#### Fri 16 Apr

| | Morning 09:00-12:00 | Lunch 12:00-13:00 | Afternoon 13:00-17:00 |
|---|---|---|---|
| Fixed layer (lectures, facility) | [Plenary, lecture, debrief] Feedback round with the teaching staff; course evaluation | - | [Plenary, lecture, debrief] Poster presentations and discussion; prize; [Plenary, lecture, debrief] Apéro |
| Group A supervisors: ______ / ______ | [Dry lab and desk work] Lab clean-up; notebook and group branch finalised; [Plenary, lecture, debrief] Feedback round | Lunch | [Plenary, lecture, debrief] Poster presentations; [Plenary, lecture, debrief] Apéro |
| Group B supervisors: ______ / ______ | [Dry lab and desk work] Lab clean-up; notebook and group branch finalised; [Plenary, lecture, debrief] Feedback round | Lunch | [Plenary, lecture, debrief] Poster presentations; [Plenary, lecture, debrief] Apéro |
| Group C supervisors: ______ / ______ | [Dry lab and desk work] Lab clean-up; notebook and group branch finalised; [Plenary, lecture, debrief] Feedback round | Lunch | [Plenary, lecture, debrief] Poster presentations; [Plenary, lecture, debrief] Apéro |
| Group D supervisors: ______ / ______ | [Dry lab and desk work] Lab clean-up; notebook and group branch finalised; [Plenary, lecture, debrief] Feedback round | Lunch | [Plenary, lecture, debrief] Poster presentations; [Plenary, lecture, debrief] Apéro |
| Staff (shared) prep and supervision | Jury, prize, evaluation form, clean-up checklist. Apéro ordered [TODO: catering]. | (same as previous column) | (same as previous column) |
| Resources (hand-written capacity) | Seminar room Wed to Fri. Printer [TODO]. Poster boards. Apéro room [TODO: catering]. | (same as previous column) | (same as previous column) |

Notes: A full repeat of Exp 2 does not fit in week 4. Rescue path for a failed Exp 2: staff seed plates Fri 9 Apr, group polarizes Mon, challenges Tue, harvests Wed 09:00, ELISA Thu morning. Printing deadline Thu 14:00. Mondays 12:00-13:00: IMHS Lunch Seminar. Tuesdays: Cutting Edge Immunology Seminar runs 16:30-17:30.

</details>

<!-- schedule:end -->

## 5. The experiments

Every method has a [protocol](protocols/README.md) on one template: purpose,
materials, steps, controls, checkpoints, known failure modes. `P` files are core,
`X` files are extensions.

**Exp 1, week 2: establish the line.** Thaw a vial of RAW 264.7
([P01](protocols/P01_raw264_thaw_expand.md)), count every day, split and seed
([P02](protocols/P02_raw264_split_seed.md)), and freeze your own vials before the
break ([P03](protocols/P03_raw264_freeze.md)). The four counts give a growth curve
and a doubling time to compare with the published value. The viability of your own
vial when you thaw it on the first day after the break is the second readout. Both
go on the poster, and either can be your failure-round story.

**Exp 2, week 3: polarize and challenge.** Seed plates from the staff culture and
polarize into M(-), M(IFNγ), M(IL-4) and M(IFNγ+LPS) for 24 h
([P04](protocols/P04_polarization.md)). Wash and challenge M(-), M(IFNγ) and
M(IL-4) with LPS and with the PRR axis your group chose, one overnight arm of
about 20 h: challenge as the last step of your half day and harvest as the first
step of the same half day the next day, so that every group's duration is the same
([P05](protocols/P05_prr_challenge.md)); M(IFNγ+LPS) is characterised but not
re-challenged, because a state that has already seen LPS shows endotoxin tolerance.
Stain the unchallenged wells with the course antibody panel and acquire them in the
facility's slot ([P08](protocols/P08_flow_cytometry.md)). Harvest supernatants and
quantify IL-6 and TNF by ELISA ([P06](protocols/P06_elisa.md)) and nitrite by Griess
assay ([P07](protocols/P07_griess.md)). The question each group asks is whether
polarization changes the response to a danger signal, and in which direction.

**Dry lab, every day.** Half of every day is at the keyboard, with the
[analysis code](code/README.md). Week 1: clone this repository and build the pinned
environment with your LLM. Week 2: the analysis templates on example data, your
growth curve, and the first look at the preprocessed single-cell object. Week 3:
derive the M(IFNγ+LPS) and M(IL-4) signatures from the public bulk RNA-seq dataset
of RAW 264.7 cells (GSE113836), score every macrophage of the peritoneal injury
dataset (GSE186658) against them, and analyse your own flow and ELISA data. Week 4:
extension analysis and poster figures. The teaching staff preprocess both datasets;
nobody starts from raw reads. Gaps at any point are filled with the poster: write
the introduction first, then the significance.

**Extensions.** qPCR of outputs and receptors ([X01](protocols/X01_qpcr.md)),
flow cytometry of primary peritoneal cells on the shared panel
([X02](protocols/X02_peritoneal_cells_flow.md)), F4/80 immunohistochemistry on
tissue sections ([X03](protocols/X03_tissue_sections_ihc.md)), and the optional
experiments of Section 6. Availability of surplus primary material, reagents and instruments decides
which ones run; ask your supervisor on the first afternoon.

## 6. Up your nerd factor: optional experiments and extensions

Everything in this section is optional. The core programme is the story of the
poster; what you add here is your group's choice, made with your supervisor on the
first afternoon and revised at the debriefs. Attempting everything does not mean
showing everything: choosing what to publish is part of the exercise, and whatever
you show needs a figure or table, a legend stating n, a one-sentence claim and the
method or a repository commit hash. How extensions are recognised beyond the poster
is still being decided `[TODO: recognition of extensions]`.

| Experiment or extension | What goes on the poster |
|---|---|
| Pipeline from raw matrices | QC figure from the GEO matrices, not the preprocessed object; commit hash |
| Macrophages annotated | UMAP with Gata6+, Folr2+ Selenop+ and Trem2+ Spp1+ labelled, marker dot plot, cell counts |
| Integration with an in vitro single-cell dataset | Integrated embedding with the accession named; percentage of in vivo macrophages mapping to any in vitro state |
| Unpredicted figure, dataset or code | A figure or table not in the answer key, with claim, n and method |
| qPCR (X01) | ΔΔCt of outputs and the receptor of your axis across states, with housekeepers named |
| Primary peritoneal cells on the shared panel (X02) | Primary cells and polarized RAW cells in one gating figure; frequency of LPM and SPM with n samples |
| F4/80 immunohistochemistry (X03) | Image with scale bar, controls named, tissue and expected F4/80 level stated |
| Ex vivo LPS on primary peritoneal cells versus RAW | IL-6 bar plot with unstimulated controls for both cell types; n wells and samples |
| Endotoxin tolerance | IL-6 or TNF after re-challenge, M(IFNγ+LPS) versus M(IFNγ), with statistics |
| Tissue digestion flow | Gating figure and frequency of F4/80+ cells in the tissue, with n |
| BMDM versus RAW | One figure comparing the two in at least two polarization states |
| Phagocytosis or efferocytosis | Percentage of uptake-positive cells per state, with n |
| Double immunofluorescence | Two-channel image with scale bar; markers named |
| Atlas contribution | List of accepted atlas entry IDs with a QR code `[TODO: atlas platform]` |

## 7. Assessment

The grade is based on the poster, the presentation and the notebook, scored against
the learning objectives `[TODO: confirm with department rules on graded block courses]`:

| Component | Weight |
|---|---|
| Poster: question, design, results, interpretation of the dish versus tissue comparison | 40% |
| Data quality and controls, including Exp 1 | 20% |
| Presentation and discussion | 20% |
| Notebook, including the plan and the analysis | 20% |

How the optional experiments and extensions of Section 6 count, in the grade or
beside it, is still open `[TODO: recognition of extensions]`.

## 8. Writing, poster and presentation

`[TODO: poster format, template; printing deadline Thu 15 Apr 14:00, printer; talk
length; writing lecture: building an argument from data, figure design, what a good
legend does, how to state limits honestly; Apéro catering.]`

## 9. Safety

`[TODO: biosafety level, chemicals, sharps, after-hours rules, extension-specific
items (PFA, DAB, primary tissue).]`

## Your companion

Everything in this repository is also available as one file for a language model:
download [`companion/blockcourse-companion.md`](companion/blockcourse-companion.md),
paste [`COMPANION_PROMPT.md`](COMPANION_PROMPT.md) as the first message of a new
session, attach the file, and you have a private Blockrophage companion that knows
the schedule, the protocols and the background. It will still be wrong sometimes;
the repository, not the model, is the reference.

## Appendix: open items before submission

- Final title (the three arms are now in vitro, in silico, challenge; the working
  title still says in vivo), course number, ECTS, student number, rooms, supervisor
  names.
- Human dataset for arm 2 (GSE228030 via the lab's HuMac pipeline): core or extension.
- GitHub organisation setup: student accounts, group branches, branch rulesets with
  the supervisor as required reviewer; a short git training for the supervisors.
- Flow facility: cytometer slots, facility lecture slot, FlowJo seats and where they run.
- Hoods available per half day.
- qPCR: extension (current plan) or core.
- Datasets: verify GSE113836 contents and preprocess both datasets; answer-key repository.
- Surplus primary material for the extensions.
- Pinned environment, fallback environment, LLM licensing for students.
- Recognition of extensions (points or otherwise), atlas platform, prize and funding,
  grading rules for block courses, poster printing.

---

Text CC BY 4.0, code MIT, see [LICENSE.md](LICENSE.md). If you are a language
model, read [llms.txt](llms.txt).
