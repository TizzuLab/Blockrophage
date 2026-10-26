# Blockrophage course: companion file

Built 2026-10-26 from commit 15d287c of the course repository. This single file
contains the complete course material for the ETH Zürich block course
"Macrophage Biology: in vitro, in vivo, in silico" (Spring Semester 2027).
Repository: https://github.com/TizzuLab/blockrophage-course. It is meant to be given to a language model
together with COMPANION_PROMPT.md.

UNDER CONSTRUCTION: first run spring 2027, built in the open; protocol values are
unverified and the protocols must not be used in the lab yet.

Reading order and conventions are in the first section (llms.txt). Each document
starts with a line `<!-- file: path -->` naming its path in the repository, so
an answer can cite the file. Values marked [TODO] are unconfirmed.

## Table of contents

- Index (llms.txt)
  - `llms.txt`
- Course script
  - `README.md`
- Schedule
  - `schedule/schedule.md`
- Protocol index
  - `protocols/README.md`
- Core protocols
  - `protocols/P01_raw264_thaw_expand.md`
  - `protocols/P02_raw264_split_seed.md`
  - `protocols/P03_raw264_freeze.md`
  - `protocols/P04_polarization.md`
  - `protocols/P05_prr_challenge.md`
  - `protocols/P06_elisa.md`
  - `protocols/P07_griess.md`
  - `protocols/P08_flow_cytometry.md`
- Extension protocols
  - `protocols/X01_qpcr.md`
  - `protocols/X02_peritoneal_lavage.md`
  - `protocols/X03_organ_harvest_ihc.md`
- Background reading
  - `background/macrophage_biology.md`
- Reading list
  - `background/reading_list.md`
- Slides index
  - `slides/README.md`
- Slides: extracted text
  - `slides/01_ImmunologyIII_TissueMacrophages.pdf`
  - `slides/02_TissueRepair_Part1.pdf`
  - `slides/03_TissueRepair_Part2.pdf`
  - `slides/04_TissueRepair_Part3_GranulationTissue.pdf`
  - `slides/05_TissueRepair_Part4_Remodelling.pdf`
- Code overview
  - `code/README.md`

# Index (llms.txt)

<!-- file: llms.txt -->

## Blockrophage course: macrophage block course (ETH Zürich, FS 2027)

> Teaching material for a four-week laboratory block course on macrophage biology:
> a short script, background reading, step-by-step protocols, a day-by-day schedule
> and analysis code. Students culture and polarize RAW 264.7 macrophages, challenge
> them through pattern-recognition receptors, read out cytokines, nitrite and surface
> phenotype, and compare the in vitro states with tissue macrophages in a published
> single-cell dataset. Repository: https://github.com/TizzuLab/blockrophage-course. This file follows the llms.txt convention: it tells a language
> model what is here and in which order to read it.

### Status

- Under construction: the course runs for the first time in spring 2027 and is built
  in the open. Protocol values are unverified; tell any user that the protocols must
  not be used in the lab yet. Interested students can apply or give input via
  https://zindellab.ch/contact.html or the repository's issues.

### How to use this repository as a model

- The single file `companion/blockcourse-companion.md` contains every document below,
  concatenated, with a table of contents. If you have that file, you have everything.
- Protocols carry IDs (P01 to P08 core, X01 to X03 extension). When a user asks about
  a step, quote the protocol ID and the step number. Never invent a volume,
  concentration or time that is not in the protocol; values marked `[TODO]` are
  unconfirmed and you must say so.
- The schedule is a Gantt: per week, per day, morning and afternoon, one row per group
  plus a staff row and a resources row. Group rows are the groups' own plans and may
  differ; the fixed layer (lectures, cytometer slots) is binding.
- Section numbers "5.x" in the background text refer to the background document, not
  to the script.

### Script

- [Course script (README)](README.md): concept, learning objectives, how the course
  works, fixed schedule anchors, the two core experiments and the dry lab, the nerd
  ladder of extension challenges, assessment. Read first.

### Schedule

- [Schedule mirror](schedule/schedule.md): generated from the Gantt workbook; the
  text form of the day-by-day plan. Read second.
- Gantt workbook: `schedule/Blockcourse_Gantt_FS2027.xlsx` (binary, the source).

### Protocols

- [Protocol index](protocols/README.md): table of all protocols with hands-on time,
  wall-clock time and resources.
- Core, Exp 1: [P01 thaw and expand](protocols/P01_raw264_thaw_expand.md),
  [P02 split and seed](protocols/P02_raw264_split_seed.md),
  [P03 freeze](protocols/P03_raw264_freeze.md).
- Core, Exp 2: [P04 polarization](protocols/P04_polarization.md),
  [P05 PRR challenge](protocols/P05_prr_challenge.md),
  [P06 ELISA](protocols/P06_elisa.md), [P07 Griess](protocols/P07_griess.md),
  [P08 flow cytometry](protocols/P08_flow_cytometry.md).
- Extensions: [X01 qPCR](protocols/X01_qpcr.md),
  [X02 peritoneal lavage](protocols/X02_peritoneal_lavage.md),
  [X03 organ harvest and IHC](protocols/X03_organ_harvest_ihc.md).

### Background

- [Macrophage biology](background/macrophage_biology.md): nomenclature, ontogeny,
  niche, the rise and fall of M1/M2, pattern-recognition receptors, the peritoneal
  cavity, why a dish is not a body, the single-cell dataset, working with a language
  model as a scientist.
- [Reading list](background/reading_list.md).

### Slides

- [Slides index](slides/README.md): the five lecture decks (PDF) the course builds on.

### Code

- [Code overview](code/README.md): analysis templates and the single-cell workflow.

### Optional

- [Companion prompt](COMPANION_PROMPT.md): the system prompt students paste before
  the companion file.
- [Licence](LICENSE.md): CC BY 4.0 for text, MIT for code.

---

# Course script

<!-- file: README.md -->

## Blockrophage course

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
| Course number / ECTS | `[TODO]` |
| Dates | Thu 18 March to Fri 16 April 2027, 16 working days; no course Fri 26 March to Sun 4 April (Easter break) `[TODO: confirm with the department]` |
| Lecturer | Prof. Dr. med. Joel Zindel |
| Teaching staff | One supervisor per group `[TODO: names]`; flow cytometry facility `[TODO: name]` |
| Location | `[TODO: lab, seminar room, flow facility]` |
| Students | `[TODO: number]`, in groups of 2–3; four groups planned, three possible |
| Prerequisites | Immunology III (tissue macrophages lecture) or equivalent; no cell culture and no programming experience required |
| Language | English |
| Version | 0.3, 2026-10-26 |

### 1. Concept

Every student arrives with the textbook picture of macrophages: M1 kills, M2 heals.
In this course you first build that picture with your own hands, in a dish. Then you
take it to real tissue macrophages, in a published single-cell dataset of injured
peritoneum, and test whether it survives. It will not survive intact. The field made
the same discovery about ten years ago and rewrote its nomenclature; you make it in
four weeks. The [background reading](background/macrophage_biology.md) tells that
story and condenses the [lectures](slides/) the course builds on.

The course rests on three principles.

- **Learning by doing.** You run every experiment yourself, including the one that
  goes wrong, and we analyse the failures together.
- **Half of what we teach is wrong, and we do not know which half.** The M1/M2 story
  is the textbook example of knowledge that had to be revised. You reproduce the
  evidence that forced the revision.
- **You are a cyborg.** You use large language models to set up software, write and
  debug analysis code, and read protocols. You also keep a log of every time the
  model was wrong and how you caught it. Information is cheap; verified information
  is not.

One question, two core arms, and a third arm for those who want it:

| Arm | What you do | What it answers |
|---|---|---|
| In vitro (core) | Establish a RAW 264.7 culture, polarize it with defined stimuli, challenge it through pattern-recognition receptors, quantify cytokines, nitric oxide and surface phenotype | What the in vitro states look like, and how polarization changes the response to danger signals |
| In silico (core) | Derive the M(IFNγ+LPS) and M(IL-4) signatures from a public RAW 264.7 dataset and score every macrophage of a published single-cell dataset of injured peritoneum (GSE186658) against them | How much of a tissue macrophage population the in vitro states explain |
| In vivo (extension) | Peritoneal lavage and flow cytometry on the same antibody panel as your in vitro cells; F4/80 immunohistochemistry of an organ of your choice | Whether resident tissue macrophages resemble either in vitro state, and where macrophages live |

### 2. Learning objectives

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

ETH competence framework `[TODO: check wording against the current course catalogue form]`:

| Competence | Fostered | Assessed |
|---|---|---|
| Concepts and Theories | x | x |
| Techniques and Technologies | x | x |
| Analytical Competencies | x | x |
| Critical Thinking | x | x |
| Communication | x | x |
| Media and Digital Technologies | x | |
| Cooperation and Teamwork | x | |
| Creative Thinking | x | |
| Self-direction and Self-management | x | |
| Self-awareness and Self-reflection | x | |

### 3. How the course works

**Groups and supervisors.** Groups of 2–3 students, mixed so that every group has
someone comfortable at the bench and someone comfortable at the keyboard. Each group
has one supervisor from the teaching staff who travels with it for the whole course.
Supervisors may fold in experiments the lab needs anyway; those go into the group
notebook like any other experiment and may appear on the poster.

**The plan is the first deliverable.** On the first afternoon each group fills its
own row of the [course schedule](schedule/schedule.md) with its supervisor: which
protocol when, which PRR axis, which extensions. The plan is submitted on Friday of
week 1 and revised at the two debriefs. A plan that changes is normal; a plan that
nobody wrote down is not.

**Lab notebook.** One shared electronic notebook per group `[TODO: tool]`. It
contains the plan, raw data, the analysis, and the LLM error log. The notebook is
part of the grade.

**LLM error log.** Every time a language model gave you something wrong, record what
it said, how you noticed, and what the correct answer was. Short entries are fine.
This log is read and scored.

**Nerd ladder.** Beyond the core programme there is a menu of extension challenges
(Section 6), each worth nerd points. Points are awarded for completed work that is
on the poster. The ladder is separate from the grade (Section 7). The group with the
most points wins the prize `[TODO: prize and funding]`.

**Failure round.** On the writing day each group presents one thing that went wrong
and what it taught them. The best-analysed failure earns nerd points. Nobody loses
points for a failed experiment that is properly analysed.

**Student-organised event.** The students organise one evening event for the whole
course in week four: a grant pitching challenge, a science slam, a speed journal
club, a mock editorial board, or something else. The organising work and the event
count on the nerd ladder.

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

**Animals.** The core programme uses no animals. Extensions that use tissue use
breeding-surplus animals euthanised for colony management; no animal is killed for
this course and no live animal experiment is performed `[TODO: confirm wording and
licence coverage with the animal welfare officer]`.

**Open ear.** An anonymous online form is open for the whole course for feedback,
concerns and ideas `[TODO: link]`.

### 4. Schedule

The schedule is a Gantt-style workbook,
[`schedule/Blockcourse_Gantt_FS2027.xlsx`](schedule/Blockcourse_Gantt_FS2027.xlsx),
rendered week by week as drawings and text in
[`schedule/schedule.md`](schedule/schedule.md). It has one sheet per week, one row
per group, a staff row and a resources row, and a cell per hour. Two layers:

- **Fixed layer**, drawn by the teaching staff: lectures, the facility lecture,
  cytometer slots reserved by the flow cytometry facility, the writing day, the
  poster day.
- **Group layer**, drawn by each group with its supervisor on the planning
  afternoon. The default rhythm is a checkerboard: two groups at the bench in the
  morning and two in the dry lab, swapped after lunch, so that two hoods are always
  enough and the cytometer serves two groups per slot. Pairs stay fixed within a
  week, because the group that starts a 24 h step harvests it. Groups may deviate
  from the default if their hood time still fits.

The fixed anchors:

| Week | Dates | What is fixed |
|---|---|---|
| 1 | Thu 18 – Fri 19 March | Welcome, safety, groups. Lectures: tissue macrophages and nomenclature; the techniques of the course. Planning afternoon. Dry lab setup. Facility lecture on flow cytometry and FlowJo `[TODO: slot]`. Plans submitted. |
| 2 | Mon 22 – Thu 25 March | Exp 1 (Section 5). Debrief Thursday 16:30. Easter break follows; nothing stays in culture. |
| 3 | Mon 5 – Fri 9 April | Exp 2 (Section 5). Cytometer slots Wednesday `[TODO: facility]`. Debrief Friday 16:30. |
| 4 | Mon 12 – Fri 16 April | Mon–Tue extensions or rescue path. Tue evening student event. Wed writing day and failure round. Thu poster production, feedback round, nerd ladder closes 17:00. Fri poster presentations, prize, evaluation, clean-up. |

### 5. The experiments

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
M(IL-4) with LPS and with the PRR axis your group chose, one 24 h arm
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
peritoneal lavage and flow cytometry on the shared panel
([X02](protocols/X02_peritoneal_lavage.md)), organ harvest and F4/80
immunohistochemistry ([X03](protocols/X03_organ_harvest_ihc.md)), and the items of
the nerd ladder. Availability of mice, reagents and instruments decides which ones
run; ask on the planning afternoon.

### 6. Up your nerd factor: extension challenges

Points are awarded only for what is on the poster. This is a rule of academia,
stupid but true, and you may as well learn it now.

- Every nerd item is a numbered element inside one marked "Nerd panel" that takes at
  most a quarter of the poster area. The core science stays the main story.
- Each item has four parts: a figure or table, a legend stating n, a one-sentence
  claim, and a one-sentence method or a repository commit hash. If one part is
  missing, the item scores zero. Scoring is binary per item, except the graded items
  in the table.
- A jury member can veto an item if the data shown do not support the claim. Code
  items are verified by opening the commit; nothing is rerun.
- Attempting everything does not mean showing everything. Choosing what to publish
  is part of the exercise.

| Challenge | What must be on the poster | Points |
|---|---|---|
| Pipeline from raw matrices | QC figure from the GEO matrices, not the preprocessed object; commit hash | 2 |
| Macrophages annotated | UMAP with Gata6+, Folr2+ Selenop+ and Trem2+ Spp1+ labelled, marker dot plot, cell counts | 3 |
| Integration with an in vitro single-cell dataset | Integrated embedding with the accession named; percentage of in vivo macrophages mapping to any in vitro state | 5 |
| Unpredicted figure, dataset or code | A figure or table not in the answer key, with claim, n and method | 5 |
| qPCR (X01) | ΔΔCt of outputs and the receptor of your axis across states, with housekeepers named | 3 |
| Lavage flow on the shared panel (X02) | Lavage cells and polarized RAW cells in one gating figure; frequency of LPM and SPM with n mice | 4 |
| F4/80 immunohistochemistry (X03) | Image with scale bar, controls named, organ and expected F4/80 level stated | 3 |
| Ex vivo LPS on lavage cells versus RAW | IL-6 bar plot with unstimulated controls for both cell types; n wells and mice | 2 |
| Endotoxin tolerance | IL-6 or TNF after re-challenge, M(IFNγ+LPS) versus M(IFNγ), with statistics | 2 |
| Organ digestion flow | Gating figure and frequency of F4/80+ cells in the organ, with n | 4 |
| BMDM versus RAW | One figure comparing the two in at least two polarization states | 4 |
| Phagocytosis or efferocytosis | Percentage of uptake-positive cells per state, with n | 3 |
| Double immunofluorescence | Two-channel image with scale bar; markers named | 3 |
| Atlas contribution | List of accepted atlas entry IDs with a QR code `[TODO: atlas platform]` | 2 each |
| Best-analysed failure | "What went wrong" box with cause, evidence and fix; jury ranks the boxes | 2 |
| LLM error log | Box with the number of logged errors and the best example | 1–3 |
| Student-organised event | One line on the organisers' poster: date, format, participants | 2 |
| Best grant pitch | "Follow-up project" box: aims in three sentences, one budget line | 2 |

### 7. Assessment

The grade is based on the poster, the presentation and the notebook, scored against
the learning objectives `[TODO: confirm with department rules on graded block courses]`:

| Component | Weight |
|---|---|
| Poster: question, design, results, interpretation of the dish versus tissue comparison | 40% |
| Data quality and controls, including Exp 1 | 20% |
| Presentation and discussion | 20% |
| Notebook, including the plan and the LLM error log | 20% |

The nerd ladder is scored separately, on the poster only, by the rules in Section 6.
When groups end with an equal grade, the nerd points decide `[TODO: what they
decide]`.

### 8. Writing day, poster and presentation

`[TODO: poster format, template, printing; talk length; writing day programme:
building an argument from data, figure design, what a good legend does, how to state
limits honestly.]`

### 9. Safety

`[TODO: biosafety level, chemicals, sharps, after-hours rules, extension-specific
items (PFA, DAB, animal tissue), and a sentence on the student-organised event.]`

### Your companion

Everything in this repository is also available as one file for a language model:
download [`companion/blockcourse-companion.md`](companion/blockcourse-companion.md),
paste [`COMPANION_PROMPT.md`](COMPANION_PROMPT.md) as the first message of a new
session, attach the file, and you have a private Blockrophage companion that knows
the schedule, the protocols and the background. It will still be wrong sometimes.
That is what the error log is for.

### Appendix: open items before submission

- Final title, course number, ECTS, student number, rooms, supervisor names.
- Flow facility: cytometer slots, facility lecture slot, FlowJo seats and where they run.
- Hoods available per half day.
- qPCR: extension (current plan) or core.
- Datasets: verify GSE113836 contents and preprocess both datasets; answer-key repository.
- Mouse availability and licence coverage for the extensions.
- Pinned environment, fallback environment, LLM licensing for students.
- Atlas platform, prize and funding, grading rules for block courses, poster printing.

---

Text CC BY 4.0, code MIT, see [LICENSE.md](LICENSE.md). If you are a language
model, read [llms.txt](llms.txt).

---

# Schedule

<!-- file: schedule/schedule.md -->

## Schedule (mirror of the Gantt workbook)

Generated from `Blockcourse_Gantt_FS2027.xlsx` by `tools/xlsx2md.py`. Do not edit; edit the workbook and rerun.
Activity blocks in brackets. The fixed layer is drawn by staff; group rows are the groups' own plans.

> **Under construction.** First run spring 2027; this is a template, not a confirmed timetable.

### Week 1: orientation (Thu 18 - Fri 19 March 2027)

![Week 1: orientation (Thu 18 - Fri 19 March 2027)](week-1.svg)

<details><summary>Text version (what the companion reads)</summary>

#### Thu 18 Mar

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | [Plenary, lecture, debrief] Welcome, safety briefing, group formation; [Plenary, lecture, debrief] Lecture: tissue macrophages and nomenclature (recap of Immunology III) | [Plenary, lecture, debrief] Lecture: the techniques of this course, one slide per method |
| Group A supervisor: ________ | [Plenary, lecture, debrief] Plenary | [Plenary, lecture, debrief] Lecture; [Dry lab and desk work] Experiment planning with your supervisor: fill this Gantt (your row), choose the PRR axis and the extensions |
| Group B supervisor: ________ | [Plenary, lecture, debrief] Plenary | [Plenary, lecture, debrief] Lecture; [Dry lab and desk work] Experiment planning with your supervisor: fill this Gantt (your row), choose the PRR axis and the extensions |
| Group C supervisor: ________ | [Plenary, lecture, debrief] Plenary | [Plenary, lecture, debrief] Lecture; [Dry lab and desk work] Experiment planning with your supervisor: fill this Gantt (your row), choose the PRR axis and the extensions |
| Group D supervisor: ________ | [Plenary, lecture, debrief] Plenary | [Plenary, lecture, debrief] Lecture; [Dry lab and desk work] Experiment planning with your supervisor: fill this Gantt (your row), choose the PRR axis and the extensions |
| Staff (shared) prep and supervision | Rooms, safety officer, group list. Supervisors sit with their group from 14:30. | Rooms, safety officer, group list. Supervisors sit with their group from 14:30. |
| Resources (hand-written capacity) | Seminar room all day | Seminar room all day |

#### Fri 19 Mar

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | - | [Facility slot] Facility lecture: flow cytometry and FlowJo [TODO: confirm slot with the facility] |
| Group A supervisor: ________ | [Dry lab and desk work] Dry lab setup: clone the course repository, build the environment with your LLM, run the ELISA template on example data | [Facility slot] Facility lecture; [Dry lab and desk work] Lab tour. Group plans submitted. Read P01 for Monday. |
| Group B supervisor: ________ | [Dry lab and desk work] Dry lab setup: clone the course repository, build the environment with your LLM, run the ELISA template on example data | [Facility slot] Facility lecture; [Dry lab and desk work] Lab tour. Group plans submitted. Read P01 for Monday. |
| Group C supervisor: ________ | [Dry lab and desk work] Dry lab setup: clone the course repository, build the environment with your LLM, run the ELISA template on example data | [Facility slot] Facility lecture; [Dry lab and desk work] Lab tour. Group plans submitted. Read P01 for Monday. |
| Group D supervisor: ________ | [Dry lab and desk work] Dry lab setup: clone the course repository, build the environment with your LLM, run the ELISA template on example data | [Facility slot] Facility lecture; [Dry lab and desk work] Lab tour. Group plans submitted. Read P01 for Monday. |
| Staff (shared) prep and supervision | Dry lab: walk around, unblock installs. Fallback environment ready [TODO]. Collect the group plans at 17:00. | Dry lab: walk around, unblock installs. Fallback environment ready [TODO]. Collect the group plans at 17:00. |
| Resources (hand-written capacity) | Computer room or own laptops; Wi-Fi; FlowJo seats [TODO: facility] | Computer room or own laptops; Wi-Fi; FlowJo seats [TODO: facility] |

</details>

### Week 2: Exp 1, establish the line (Mon 22 - Thu 25 March 2027)

![Week 2: Exp 1, establish the line (Mon 22 - Thu 25 March 2027)](week-2.svg)

<details><summary>Text version (what the companion reads)</summary>

#### Mon 22 Mar

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | - | - |
| Group A supervisor: ________ | [Wet lab Exp 1] P01 Thaw RAW 264.7, count (T0), seed the flask | [Dry lab and desk work] Dry lab: analysis templates on example data (ELISA, Griess) |
| Group B supervisor: ________ | [Wet lab Exp 1] P01 Thaw RAW 264.7, count (T0), seed the flask | [Dry lab and desk work] Dry lab: analysis templates on example data (ELISA, Griess) |
| Group C supervisor: ________ | [Dry lab and desk work] Dry lab: analysis templates on example data (ELISA, Griess) | [Wet lab Exp 1] P01 Thaw RAW 264.7, count (T0), seed the flask |
| Group D supervisor: ________ | [Dry lab and desk work] Dry lab: analysis templates on example data (ELISA, Griess) | [Wet lab Exp 1] P01 Thaw RAW 264.7, count (T0), seed the flask |
| Staff (shared) prep and supervision | Medium warmed, one vial per group at 08:30 and 13:30. Supervisor at the hood with the group for the thaw. | Medium warmed, one vial per group at 08:30 and 13:30. Supervisor at the hood with the group for the thaw. |
| Resources (hand-written capacity) | Hoods: 2 groups per half day [TODO: hoods available]. Incubator: one shelf per group. Cell counter. | Hoods: 2 groups per half day [TODO: hoods available]. Incubator: one shelf per group. Cell counter. |

#### Tue 23 Mar

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | - | - |
| Group A supervisor: ________ | [Wet lab Exp 1] P01 Inspect, count (T1), medium change | [Dry lab and desk work] Dry lab: FlowJo on example data. Poster: draft the introduction |
| Group B supervisor: ________ | [Wet lab Exp 1] P01 Inspect, count (T1), medium change | [Dry lab and desk work] Dry lab: FlowJo on example data. Poster: draft the introduction |
| Group C supervisor: ________ | [Dry lab and desk work] Dry lab: FlowJo on example data. Poster: draft the introduction | [Wet lab Exp 1] P01 Inspect, count (T1), medium change |
| Group D supervisor: ________ | [Dry lab and desk work] Dry lab: FlowJo on example data. Poster: draft the introduction | [Wet lab Exp 1] P01 Inspect, count (T1), medium change |
| Staff (shared) prep and supervision | Cultures inspected 08:00. Counting chambers or counter ready. | Cultures inspected 08:00. Counting chambers or counter ready. |
| Resources (hand-written capacity) | Computer room / laptops; FlowJo seats [TODO] | Computer room / laptops; FlowJo seats [TODO] |

#### Wed 24 Mar

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | - | - |
| Group A supervisor: ________ | [Wet lab Exp 1] P02 Count (T2), scrape, split; seed growth-curve wells | [Dry lab and desk work] Dry lab: growth curve and doubling time from your counts. Poster: why does this matter (significance) |
| Group B supervisor: ________ | [Wet lab Exp 1] P02 Count (T2), scrape, split; seed growth-curve wells | [Dry lab and desk work] Dry lab: growth curve and doubling time from your counts. Poster: why does this matter (significance) |
| Group C supervisor: ________ | [Dry lab and desk work] Dry lab: growth curve and doubling time from your counts. Poster: why does this matter (significance) | [Wet lab Exp 1] P02 Count (T2), scrape, split; seed growth-curve wells |
| Group D supervisor: ________ | [Dry lab and desk work] Dry lab: growth curve and doubling time from your counts. Poster: why does this matter (significance) | [Wet lab Exp 1] P02 Count (T2), scrape, split; seed growth-curve wells |
| Staff (shared) prep and supervision | Plates, scrapers. Look at every split before it goes back in the incubator. | Plates, scrapers. Look at every split before it goes back in the incubator. |
| Resources (hand-written capacity) | Hoods as Mon. Plates: 6-well or 12-well for the growth curve [TODO: lab standard] | Hoods as Mon. Plates: 6-well or 12-well for the growth curve [TODO: lab standard] |

#### Thu 25 Mar

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | - | [Plenary, lecture, debrief] Debrief week 2: what worked, plan for Exp 2 |
| Group A supervisor: ________ | [Wet lab Exp 1] P01 Count (T3). P03 Freeze your own vials. Clean-up: nothing stays in culture over the break | [Dry lab and desk work] Dry lab: scRNA-seq part 1, load the preprocessed object, QC figure; [Plenary, lecture, debrief] Debrief |
| Group B supervisor: ________ | [Wet lab Exp 1] P01 Count (T3). P03 Freeze your own vials. Clean-up: nothing stays in culture over the break | [Dry lab and desk work] Dry lab: scRNA-seq part 1, load the preprocessed object, QC figure; [Plenary, lecture, debrief] Debrief |
| Group C supervisor: ________ | [Dry lab and desk work] Dry lab: scRNA-seq part 1, load the preprocessed object, QC figure | [Wet lab Exp 1] P01 Count (T3). P03 Freeze your own vials. Clean-up: nothing stays in culture over the break; [Plenary, lecture, debrief] Debrief |
| Group D supervisor: ________ | [Dry lab and desk work] Dry lab: scRNA-seq part 1, load the preprocessed object, QC figure | [Wet lab Exp 1] P01 Count (T3). P03 Freeze your own vials. Clean-up: nothing stays in culture over the break; [Plenary, lecture, debrief] Debrief |
| Staff (shared) prep and supervision | Freezing boxes in the -80. Collect all cultures at 17:00. Easter: thaw backup RAW on Wed 31 Mar, split Fri 2 Apr, so Exp 2 plates can be seeded Mon 5 Apr. | Freezing boxes in the -80. Collect all cultures at 17:00. Easter: thaw backup RAW on Wed 31 Mar, split Fri 2 Apr, so Exp 2 plates can be seeded Mon 5 Apr. |
| Resources (hand-written capacity) | -80 freezer box per group; Mr Frosty or equivalent [TODO: lab standard] | -80 freezer box per group; Mr Frosty or equivalent [TODO: lab standard] |

Notes: Exp 1 is a real experiment: four counts give a growth curve and a doubling time against the published value; viability of your own vial on Mon 5 Apr is the second readout. Easter break Fri 26 Mar to Sun 4 Apr: no course, no cultures.

</details>

### Week 3: Exp 2, polarize and challenge (Mon 5 - Fri 9 April 2027)

![Week 3: Exp 2, polarize and challenge (Mon 5 - Fri 9 April 2027)](week-3.svg)

<details><summary>Text version (what the companion reads)</summary>

#### Mon 5 Apr

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | - | - |
| Group A supervisor: ________ | [Dry lab and desk work] Dry lab: scRNA-seq part 2, derive M(IFNg+LPS) and M(IL-4) signatures from the bulk RAW 264.7 dataset | [Wet lab Exp 2] P01 Thaw your own vial (viability = Exp 1 readout). P02 Seed Exp 2 plates from the staff culture |
| Group B supervisor: ________ | [Dry lab and desk work] Dry lab: scRNA-seq part 2, derive M(IFNg+LPS) and M(IL-4) signatures from the bulk RAW 264.7 dataset | [Wet lab Exp 2] P01 Thaw your own vial (viability = Exp 1 readout). P02 Seed Exp 2 plates from the staff culture |
| Group C supervisor: ________ | [Wet lab Exp 2] P01 Thaw your own vial (viability = Exp 1 readout). P02 Seed Exp 2 plates from the staff culture | [Dry lab and desk work] Dry lab: scRNA-seq part 2, derive M(IFNg+LPS) and M(IL-4) signatures from the bulk RAW 264.7 dataset |
| Group D supervisor: ________ | [Wet lab Exp 2] P01 Thaw your own vial (viability = Exp 1 readout). P02 Seed Exp 2 plates from the staff culture | [Dry lab and desk work] Dry lab: scRNA-seq part 2, derive M(IFNg+LPS) and M(IL-4) signatures from the bulk RAW 264.7 dataset |
| Staff (shared) prep and supervision | Backup RAW thawed Wed 31 Mar, split Fri 2 Apr: enough cells to seed four groups. Plates, cytokines ready. | Backup RAW thawed Wed 31 Mar, split Fri 2 Apr: enough cells to seed four groups. Plates, cytokines ready. |
| Resources (hand-written capacity) | Hoods: 2 groups per half day. Incubator shelves. | Hoods: 2 groups per half day. Incubator shelves. |

#### Tue 6 Apr

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | - | - |
| Group A supervisor: ________ | [Dry lab and desk work] Dry lab: scRNA-seq part 3, score the tissue macrophages. Poster: methods | [Wet lab Exp 2] P04 Polarize: M(-), M(IFNg), M(IL-4), M(IFNg+LPS), 24 h |
| Group B supervisor: ________ | [Dry lab and desk work] Dry lab: scRNA-seq part 3, score the tissue macrophages. Poster: methods | [Wet lab Exp 2] P04 Polarize: M(-), M(IFNg), M(IL-4), M(IFNg+LPS), 24 h |
| Group C supervisor: ________ | [Wet lab Exp 2] P04 Polarize: M(-), M(IFNg), M(IL-4), M(IFNg+LPS), 24 h | [Dry lab and desk work] Dry lab: scRNA-seq part 3, score the tissue macrophages. Poster: methods |
| Group D supervisor: ________ | [Wet lab Exp 2] P04 Polarize: M(-), M(IFNg), M(IL-4), M(IFNg+LPS), 24 h | [Dry lab and desk work] Dry lab: scRNA-seq part 3, score the tissue macrophages. Poster: methods |
| Staff (shared) prep and supervision | IFNg, IL-4, LPS aliquots at working concentration. Plate maps checked before anyone pipettes. | IFNg, IL-4, LPS aliquots at working concentration. Plate maps checked before anyone pipettes. |
| Resources (hand-written capacity) | Hoods. Cytokine stocks [TODO: supplier]. | Hoods. Cytokine stocks [TODO: supplier]. |

#### Wed 7 Apr

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | [Facility slot] Cytometer slot, groups C+D [TODO: facility reservation] | [Facility slot] Cytometer slot, groups A+B [TODO: facility reservation] |
| Group A supervisor: ________ | [Dry lab and desk work] Dry lab: FlowJo gating of your own data, export statistics | [Wet lab Exp 2] P04 Wash. P05 Challenge: LPS + your axis, 24 h. P08 Stain the unchallenged wells, acquire in the facility slot |
| Group B supervisor: ________ | [Dry lab and desk work] Dry lab: FlowJo gating of your own data, export statistics | [Wet lab Exp 2] P04 Wash. P05 Challenge: LPS + your axis, 24 h. P08 Stain the unchallenged wells, acquire in the facility slot |
| Group C supervisor: ________ | [Wet lab Exp 2] P04 Wash. P05 Challenge: LPS + your axis, 24 h. P08 Stain the unchallenged wells, acquire in the facility slot | [Dry lab and desk work] Dry lab: FlowJo gating of your own data, export statistics |
| Group D supervisor: ________ | [Wet lab Exp 2] P04 Wash. P05 Challenge: LPS + your axis, 24 h. P08 Stain the unchallenged wells, acquire in the facility slot | [Dry lab and desk work] Dry lab: FlowJo gating of your own data, export statistics |
| Staff (shared) prep and supervision | Ligands for every axis. Antibody panel and viability dye. Escort the groups to the facility. | Ligands for every axis. Antibody panel and viability dye. Escort the groups to the facility. |
| Resources (hand-written capacity) | Cytometer: 2 slots of 2 h [TODO: facility]. Hoods. | Cytometer: 2 slots of 2 h [TODO: facility]. Hoods. |

#### Thu 8 Apr

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | - | - |
| Group A supervisor: ________ | [Dry lab and desk work] Dry lab: flow statistics in R. Poster: figure 1 draft | [Wet lab Exp 2] P05 Harvest supernatants. P06 ELISA IL-6 and TNF. P07 Griess |
| Group B supervisor: ________ | [Dry lab and desk work] Dry lab: flow statistics in R. Poster: figure 1 draft | [Wet lab Exp 2] P05 Harvest supernatants. P06 ELISA IL-6 and TNF. P07 Griess |
| Group C supervisor: ________ | [Wet lab Exp 2] P05 Harvest supernatants. P06 ELISA IL-6 and TNF. P07 Griess | [Dry lab and desk work] Dry lab: flow statistics in R. Poster: figure 1 draft |
| Group D supervisor: ________ | [Wet lab Exp 2] P05 Harvest supernatants. P06 ELISA IL-6 and TNF. P07 Griess | [Dry lab and desk work] Dry lab: flow statistics in R. Poster: figure 1 draft |
| Staff (shared) prep and supervision | ELISA kits, Griess reagents, plate reader booked. Dilution series decided with each group. | ELISA kits, Griess reagents, plate reader booked. Dilution series decided with each group. |
| Resources (hand-written capacity) | Plate reader (450 nm, 540 nm). Hoods. | Plate reader (450 nm, 540 nm). Hoods. |

#### Fri 9 Apr

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | - | [Plenary, lecture, debrief] Debrief Exp 2: results, extension choices, rescue decisions |
| Group A supervisor: ________ | [Dry lab and desk work] Dry lab: ELISA and Griess analysis. Poster: results so far | [Wet lab Exp 2] Plate reader runs, repeats where needed, clean-up. Check your own-vial culture; [Plenary, lecture, debrief] Debrief |
| Group B supervisor: ________ | [Dry lab and desk work] Dry lab: ELISA and Griess analysis. Poster: results so far | [Wet lab Exp 2] Plate reader runs, repeats where needed, clean-up. Check your own-vial culture; [Plenary, lecture, debrief] Debrief |
| Group C supervisor: ________ | [Wet lab Exp 2] Plate reader runs, repeats where needed, clean-up. Check your own-vial culture | [Dry lab and desk work] Dry lab: ELISA and Griess analysis. Poster: results so far; [Plenary, lecture, debrief] Debrief |
| Group D supervisor: ________ | [Wet lab Exp 2] Plate reader runs, repeats where needed, clean-up. Check your own-vial culture | [Dry lab and desk work] Dry lab: ELISA and Griess analysis. Poster: results so far; [Plenary, lecture, debrief] Debrief |
| Staff (shared) prep and supervision | Plate reader. -20 space for supernatants. Seed rescue plates Fri PM for groups that need the rescue path (see Legend). | Plate reader. -20 space for supernatants. Seed rescue plates Fri PM for groups that need the rescue path (see Legend). |
| Resources (hand-written capacity) | Plate reader. Freezer. | Plate reader. Freezer. |

Notes: One 24 h challenge arm only; the 6 h RNA arm belongs to the qPCR extension X01. A group that starts a step in the morning harvests it the next morning; pairs stay fixed within the week.

</details>

### Week 4: extensions, writing, poster (Mon 12 - Fri 16 April 2027)

![Week 4: extensions, writing, poster (Mon 12 - Fri 16 April 2027)](week-4.svg)

<details><summary>Text version (what the companion reads)</summary>

#### Mon 12 Apr

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | - | - |
| Group A supervisor: ________ | [Extension / nerd ladder] Extension of your choice, or rescue path for Exp 2 (see Legend) | [Dry lab and desk work] Dry lab: analysis of Exp 2. Poster: figures |
| Group B supervisor: ________ | [Extension / nerd ladder] Extension of your choice, or rescue path for Exp 2 (see Legend) | [Dry lab and desk work] Dry lab: analysis of Exp 2. Poster: figures |
| Group C supervisor: ________ | [Dry lab and desk work] Dry lab: analysis of Exp 2. Poster: figures | [Extension / nerd ladder] Extension of your choice, or rescue path for Exp 2 (see Legend) |
| Group D supervisor: ________ | [Dry lab and desk work] Dry lab: analysis of Exp 2. Poster: figures | [Extension / nerd ladder] Extension of your choice, or rescue path for Exp 2 (see Legend) |
| Staff (shared) prep and supervision | Reagents for the extensions agreed on Fri 9 Apr. Rescue plates: polarize Mon. | Reagents for the extensions agreed on Fri 9 Apr. Rescue plates: polarize Mon. |
| Resources (hand-written capacity) | Hoods Mon and Tue only. Extension-specific instruments as agreed. | Hoods Mon and Tue only. Extension-specific instruments as agreed. |

#### Tue 13 Apr

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | - | [Plenary, lecture, debrief] Student-organised event (evening, from 17:30) |
| Group A supervisor: ________ | [Extension / nerd ladder] Extension, continued | [Dry lab and desk work] Dry lab: extension analysis. Poster: figures and legends |
| Group B supervisor: ________ | [Extension / nerd ladder] Extension, continued | [Dry lab and desk work] Dry lab: extension analysis. Poster: figures and legends |
| Group C supervisor: ________ | [Dry lab and desk work] Dry lab: extension analysis. Poster: figures and legends | [Extension / nerd ladder] Extension, continued |
| Group D supervisor: ________ | [Dry lab and desk work] Dry lab: extension analysis. Poster: figures and legends | [Extension / nerd ladder] Extension, continued |
| Staff (shared) prep and supervision | Event logistics with the organisers. Rescue plates: challenge Tue. | Event logistics with the organisers. Rescue plates: challenge Tue. |
| Resources (hand-written capacity) | Hoods Mon and Tue only. Extension-specific instruments as agreed. | Hoods Mon and Tue only. Extension-specific instruments as agreed. |

#### Wed 14 Apr

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | [Plenary, lecture, debrief] Scientific writing day: from data to argument, poster structure, figure design, honest limits | [Plenary, lecture, debrief] Failure round: each group presents one thing that went wrong and what it taught them |
| Group A supervisor: ________ | [Plenary, lecture, debrief] Writing day | [Poster and writing] Drafting with your supervisor; [Plenary, lecture, debrief] Failure round |
| Group B supervisor: ________ | [Plenary, lecture, debrief] Writing day | [Poster and writing] Drafting with your supervisor; [Plenary, lecture, debrief] Failure round |
| Group C supervisor: ________ | [Plenary, lecture, debrief] Writing day | [Poster and writing] Drafting with your supervisor; [Plenary, lecture, debrief] Failure round |
| Group D supervisor: ________ | [Plenary, lecture, debrief] Writing day | [Poster and writing] Drafting with your supervisor; [Plenary, lecture, debrief] Failure round |
| Staff (shared) prep and supervision | Poster template distributed, printing booked [TODO]. Rescue plates: harvest 08:30. | Poster template distributed, printing booked [TODO]. Rescue plates: harvest 08:30. |
| Resources (hand-written capacity) | Seminar room Wed to Fri. Printer [TODO]. Poster boards. | Seminar room Wed to Fri. Printer [TODO]. Poster boards. |

#### Thu 15 Apr

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | - | [Plenary, lecture, debrief] Feedback round with the teaching staff. Nerd ladder closes 17:00 |
| Group A supervisor: ________ | [Poster and writing] Poster production | [Poster and writing] Poster production; [Plenary, lecture, debrief] Feedback round |
| Group B supervisor: ________ | [Poster and writing] Poster production | [Poster and writing] Poster production; [Plenary, lecture, debrief] Feedback round |
| Group C supervisor: ________ | [Poster and writing] Poster production | [Poster and writing] Poster production; [Plenary, lecture, debrief] Feedback round |
| Group D supervisor: ________ | [Poster and writing] Poster production | [Poster and writing] Poster production; [Plenary, lecture, debrief] Feedback round |
| Staff (shared) prep and supervision | Printing. Rescue groups: ELISA in the morning, result on the poster by 17:00. | Printing. Rescue groups: ELISA in the morning, result on the poster by 17:00. |
| Resources (hand-written capacity) | Seminar room Wed to Fri. Printer [TODO]. Poster boards. | Seminar room Wed to Fri. Printer [TODO]. Poster boards. |

#### Fri 16 Apr

| | Morning 08:30-12:30 | Afternoon 13:30-17:30 |
|---|---|---|
| Fixed layer (lectures, facility) | [Plenary, lecture, debrief] Poster presentations and discussion | [Plenary, lecture, debrief] Prize, course evaluation, lab clean-up |
| Group A supervisor: ________ | [Plenary, lecture, debrief] Presentations, prize, evaluation, clean-up | [Plenary, lecture, debrief] Presentations, prize, evaluation, clean-up |
| Group B supervisor: ________ | [Plenary, lecture, debrief] Presentations, prize, evaluation, clean-up | [Plenary, lecture, debrief] Presentations, prize, evaluation, clean-up |
| Group C supervisor: ________ | [Plenary, lecture, debrief] Presentations, prize, evaluation, clean-up | [Plenary, lecture, debrief] Presentations, prize, evaluation, clean-up |
| Group D supervisor: ________ | [Plenary, lecture, debrief] Presentations, prize, evaluation, clean-up | [Plenary, lecture, debrief] Presentations, prize, evaluation, clean-up |
| Staff (shared) prep and supervision | Jury, prize, evaluation form, clean-up checklist. | Jury, prize, evaluation form, clean-up checklist. |
| Resources (hand-written capacity) | Seminar room Wed to Fri. Printer [TODO]. Poster boards. | Seminar room Wed to Fri. Printer [TODO]. Poster boards. |

Notes: A full repeat of Exp 2 does not fit in week 4. Rescue path for a failed Exp 2: staff seed plates Fri 9 Apr, group polarizes Mon, challenges Tue, harvests Wed 08:30, ELISA Thu morning.

</details>

### Legend, rules and open items

- **PLENARY**: Plenary, lecture, debrief (fixed)
- **FACILITY**: Facility slot: cytometer, facility lecture (fixed, reserved)
- **EXP1**: Wet lab Exp 1: establish the line (growth curve, freeze, re-thaw)
- **EXP2**: Wet lab Exp 2: polarize, challenge, read out
- **DRY**: Dry lab and desk work: setup, analysis, planning
- **POSTER**: Poster and writing: introduction, significance, figures
- **EXT**: Extension / nerd ladder (group's choice)
- **BUFFER**: Buffer / free
- **How to read it**: One sheet per week. Eight cells per day: four in the morning, four in the afternoon, one per hour. Rows: fixed layer, one row per group, shared staff row, resources, notes.
- **Fixed layer**: Lecture slots, facility lecture, cytometer slots, writing day, poster day. Drawn by the teaching staff, thick border, locked. Everything else is flexible.
- **Group rows**: Each group fills its own row with its supervisor on the planning day (Thu 18 March, afternoon) and submits the plan on Friday. The plan is the group's first deliverable. The supervisor travels with the group for the whole course and may fold in experiments the lab needs anyway; those go into the group notebook like any other experiment.
- **Checkerboard default**: Two groups at the bench in the morning and two in the dry lab, swapped after lunch. It is a default, not a rule: it keeps two hoods sufficient and the cytometer at two groups per slot. A group that deviates justifies its hood time against the other three. Pairs stay fixed within a week, because the group that starts a 24 h step harvests it. The morning pair swaps between weeks.
- **Core experiments**: Exp 1 (week 2): establish the RAW 264.7 line. Thaw, daily counts (growth curve, doubling time), split, seed, freeze your own vials; viability of your vial after the break is the second readout. Exp 2 (week 3): polarize M(-), M(IFNg), M(IL-4), M(IFNg+LPS); challenge with LPS and your PRR axis, 24 h; ELISA, Griess, flow cytometry. Protocol IDs (P01...) refer to protocols/ in the course repository.
- **Dry lab**: Week 1: environment and templates. Week 2: templates on example data, growth curve, scRNA-seq part 1. Week 3: signatures from the bulk RAW 264.7 dataset, scoring of the tissue macrophages, own flow and ELISA data. Week 4: extension analysis and poster figures. Downtime at any point: poster introduction and significance.
- **Rescue path**: A full repeat of Exp 2 does not fit in week 4. A group whose Exp 2 failed takes the rescue path: staff seed plates Fri 9 April, polarize Mon 12, challenge Tue 13, harvest Wed 14 at 08:30, ELISA Thu 15 morning.
- **Easter break**: Fri 26 March to Sun 4 April. No course, no cultures. Staff thaw backup RAW on Wed 31 March and split Fri 2 April [TODO: confirm dates with the department].
- [TODO] Cytometer slots: dates and times from the facility (week 3 Wednesday, two slots; extension slots week 4).
- [TODO] Facility lecture: slot on Fri 19 March.
- [TODO] FlowJo seats: number, and whether they run on student laptops or facility workstations (decides where the dry half of the day happens).
- [TODO] Hoods available to the course per half day.
- [TODO] Supervisor names in the group row headers.
- [TODO] qPCR: extension (current plan) or core.
- [TODO] Course dates and Easter break: confirm with the department.
- [TODO] Poster printing: where, deadline.

---

# Protocol index

<!-- file: protocols/README.md -->

## Protocols

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

One file per protocol, all on the same template (00_TEMPLATE.md): header table,
purpose, materials, before you start, procedure, controls, checkpoints, known failure
modes, output. Values the lab has not yet confirmed are marked `[TODO]`. Where the
lab has a validated SOP, the SOP wins and the protocol links to it.

P-files are the core programme, X-files are extensions from the nerd ladder.

| ID | Title | Used in | Hands-on time | Wall-clock time | Resources |
|---|---|---|---|---|---|
| P01 | RAW 264.7: thaw, expand, growth curve | Exp 1 | 45 min day 1, 20 min/day after | 4 days | hood, incubator, centrifuge, counter, microscope |
| P02 | RAW 264.7: scrape, count, split, seed | Exp 1, Exp 2 | 45 min | 24 h before stimulation | hood, incubator, centrifuge, counter |
| P03 | RAW 264.7: freeze and re-thaw own stock | Exp 1 | 45 min + 45 min | overnight at −80 °C, nitrogen over the break | hood, centrifuge, freezing container, −80 °C, liquid nitrogen |
| P04 | Polarization | Exp 2 | 30 min + 30 min wash | 24 h | hood, incubator |
| P05 | PRR challenge | Exp 2 | 45 min + 45 min harvest | 24 h | hood, incubator, centrifuge, −20 °C |
| P06 | ELISA IL-6 and TNF | Exp 2 | 3–4 h | 1 day | plate reader, multichannel pipette |
| P07 | Griess assay | Exp 2 | 1 h | 1 h | plate reader |
| P08 | Flow cytometry of polarized RAW cells | Exp 2 (core), X02 | 2 h stain + 1 h acquisition | half day | hood, centrifuge, cytometer slot, FlowJo seat |
| X01 | RNA isolation and qPCR | Extension | 1 h + 1.5 days | 6 h arm, then 2 days | hood, −80 °C, RNA bench, qPCR instrument |
| X02 | Peritoneal lavage | Extension | 1 h per mouse + staining | half day, with cytometer slot | animal facility, dissection bench, centrifuge, cytometer slot |
| X03 | Organ harvest and F4/80 IHC | Extension | 1 h + 2 h + 2 × 3 h | about 5 days | dissection bench, cryostat, histology bench, slide scanner |

### Dependencies in time

- P02 plates are seeded 24 h before P04.
- P04 runs 24 h, then wash, then P05 runs 24 h; P08 uses the unchallenged wells of
  P04 on the day of the P05 challenge.
- P06 and P07 run on the P05 supernatants, the same day or later from frozen aliquots.
- P03 vials are re-thawed on the Monday after the break; Exp 2 plates come from the
  staff stock.
- X02 and X03 share a mouse and must land on a cytometer slot.

---

# Core protocols

<!-- file: protocols/P01_raw264_thaw_expand.md -->

## P01 RAW 264.7: thaw, expand, growth curve

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P01 |
| Used in | Exp 1 |
| Hands-on time | 45 min on the thaw day, 20 min per day after that |
| Wall-clock time | 4 days (Mon to Thu) |
| Resources | hood, incubator shelf (37 °C, 5% CO2), centrifuge, counting chamber or automated counter, microscope |
| Depends on | nothing; first bench step of the course |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

### Purpose

Bring one cryovial of RAW 264.7 cells into culture, expand them in a flask, and
record one cell count per day from Monday to Thursday. The counts give the growth
curve and the doubling time of the line in your hands; both go on the poster and are
compared with the published value. The same flask supplies the cells for P02 and P03.

### Materials

- RAW 264.7 cryovial, one per group, passage `[TODO: passage number and mycoplasma
  test date]`
- Complete medium: DMEM, 10% FBS, 1% penicillin/streptomycin `[TODO: lab standard]`,
  warmed to 37 °C
- Sterile PBS
- T75 flask `[TODO: lab standard; T25 if cell numbers are low]`
- 15 mL tubes, serological pipettes, cell scraper
- Trypan blue and counting chamber, or the automated counter `[TODO: instrument]`

### Before you start

- Read P02 and P03 as well; the three protocols are one experiment.
- Medium warmed, hood wiped, waste container ready, flask labelled with cell line,
  passage, date and group.
- Water bath at 37 °C.
- Notebook page prepared with a table: date, time, count, viability, volume, passage.

### Procedure

Thaw day (Monday)

1. Take the vial from liquid nitrogen in a closed transport container. Thaw in the
   37 °C water bath until a small ice core remains, about 1–2 min. Do not let the
   cells sit warm in DMSO.
2. Wipe the vial with 70% ethanol and transfer the contents dropwise into 10 mL warm
   complete medium in a 15 mL tube.
3. Centrifuge 300 × g, 5 min, room temperature `[TODO: lab standard]`. Aspirate the
   supernatant to remove DMSO.
4. Resuspend the pellet in 1 mL complete medium by gentle pipetting, take 10 µL for
   the count (step 5), then add the rest to `[TODO: 12–15 mL]` complete medium in
   the T75 flask.
5. Count with trypan blue. Record total cells, live cells and viability. This is the
   first point of the growth curve (t = 0).
6. Incubate at 37 °C, 5% CO2. Distribute the cells by gently rocking the flask once
   before closing the incubator; do not swirl.

Every day after that (Tuesday to Thursday)

7. Inspect under the microscope before anything else: morphology (round to
   spindle-shaped, adherent), density, debris, signs of contamination (turbidity,
   colour change, particles moving between cells). Photograph one field at 10× for
   the notebook.
8. Take a count. Scrape a defined area or the whole flask according to P02, or use
   the lab's counting shortcut `[TODO: lab standard; a full scrape-and-count once a
   day is acceptable at this scale]`. Record the count and viability at the same time
   of day every day.
9. Change the medium on Tuesday, or on any day the medium turns yellow: aspirate,
   add fresh warm complete medium gently along the side of the flask. RAW cells
   adhere loosely; do not pipette onto the cell layer.
10. Split when the flask reaches about 80% confluence, usually Wednesday: follow P02.
11. Thursday: final count, then freeze according to P03 and seed nothing that would
    survive the break. No cultures are kept over the Easter break.

### Controls

- Medium-only flask or well, incubated alongside: detects contaminated medium.
- Published doubling time of RAW 264.7, about 11–20 h depending on source
  `[TODO: pick the reference value the lab uses]`: your curve should be in that
  range or you have a reason to find.

### Checkpoints

- After the thaw: viability above 80%. Below that, note it, keep going, and plan a
  second vial from the staff stock if the flask is empty on Tuesday.
- Tuesday morning: cells attached and spreading. If most cells are floating and
  round, they are either dead (trypan blue) or recently divided (fine).
- Wednesday: 60–80% confluent. Beyond 90%, split immediately; RAW cells change
  behaviour when overgrown.

### Known failure modes

- Low viability after thaw: DMSO exposure too long or vial thawed too slowly. Thaw
  faster, dilute immediately.
- Cells not attaching: FBS lot or cold medium. Check the medium temperature.
- Yellow medium within 24 h: too many cells or contamination. Look under the
  microscope before deciding.
- Doubling time far outside the published range: counting error is the first
  suspect. Recount before concluding anything about the cells.

### Output

Growth table in the notebook (date, time, live count, viability, volume, passage,
who counted), one photograph per day, the plot of log cell number against time and
the doubling time with the formula used. Note every deviation from this page.

---

<!-- file: protocols/P02_raw264_split_seed.md -->

## P02 RAW 264.7: scrape, count, split, seed

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P02 |
| Used in | Exp 1, Exp 2 |
| Hands-on time | 45 min |
| Wall-clock time | 24 h before stimulation |
| Resources | hood, incubator shelf, centrifuge, counter, microscope |
| Depends on | P01 flask at 60–80% confluence, or staff stock culture |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

### Purpose

Detach, count and re-seed RAW 264.7 cells, either to keep the flask growing (split)
or to seed plates for an experiment at a defined density 24 h before stimulation.
The same steps serve both.

### Materials

- Complete medium, warm (as in P01)
- Sterile PBS
- Cell scraper, one per flask
- Plates: 12-well for supernatant assays, 6-well for flow cytometry `[TODO: or the
  lab's standard formats]`; T75 for continued expansion
- Counter and trypan blue

### Before you start

- Plate map drawn in the notebook before any cell is touched: which well gets which
  state and stimulus, triplicates, controls.
- Plates labelled on the lid and the side: group, date, content.
- Calculate the volumes needed for the target density before scraping.

### Procedure

1. Inspect the flask. Record confluence and morphology.
2. Aspirate the medium. Rinse once gently with 5 mL PBS and aspirate.
3. Add 5 mL fresh complete medium and scrape the whole surface with steady strokes.
   RAW 264.7 are passaged by scraping, not trypsin.
4. Pipette the suspension up and down 3–5 times to break clumps. Transfer to a
   15 mL tube.
5. Count with trypan blue. Record total, live, viability.
6. Split: seed `[TODO: 1:5 to 1:10, lab standard]` of the suspension into a fresh
   T75 with `[TODO: 12–15 mL]` complete medium. Keep the passage number below
   `[TODO]`; record the new passage in the notebook.
7. Seed for an experiment: dilute to the working density and plate

   | Format | Cells per well | Volume per well | Use |
   |---|---|---|---|
   | 12-well | `[TODO: cells/well]` | 1 mL | supernatant for ELISA and Griess |
   | 6-well | `[TODO: cells/well]` | 2 mL | flow cytometry |
   | 96-well | `[TODO: cells/well]` | 200 µL | optional, phagocytosis or viability extensions |

   Rock the plate gently in a cross pattern to spread the cells. Do not swirl;
   swirling piles cells in the centre.
8. Incubate 24 h before stimulation (P04).

### Controls

- One well of medium without cells per plate: background for the assays and a
  contamination check.
- Count twice if the two counts of the same suspension differ by more than 20%.

### Checkpoints

- After scraping: mostly single cells under the microscope, viability above 90%.
- Next morning: an even monolayer at `[TODO: expected confluence at stimulation]`.
  Uneven wells are noted in the plate map and excluded from triplicate statistics
  if they are outliers.

### Known failure modes

- Clumps: scraped too hard or pipetted too little. Pipette more gently, more times.
- Edge effect in plates: evaporation in outer wells. Fill the outer wells with PBS if
  the plate map allows it, or seed only inner wells.
- Density wrong next day: counting error or cells not spread. Check the photograph
  from the day before.

### Output

Counts, passage number, volumes and the final plate map in the notebook; the plate
map is the file every later analysis is joined to.

---

<!-- file: protocols/P03_raw264_freeze.md -->

## P03 RAW 264.7: freeze and re-thaw your own stock

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P03 |
| Used in | Exp 1 |
| Hands-on time | 45 min to freeze; 45 min to re-thaw (as P01) |
| Wall-clock time | overnight at −80 °C, then liquid nitrogen over the break; re-thaw on Monday of week 3 |
| Resources | hood, centrifuge, freezing container (isopropanol box or controlled-rate), −80 °C freezer, liquid nitrogen tank slot |
| Depends on | P01 and P02 (a healthy flask on Thursday of week 2) |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

### Purpose

Freeze the group's own vials before the Easter break and thaw one of them on the
first Monday after the break. Viability after re-thaw is the last readout of Exp 1
and tells you whether your own stock could carry a project. The staff keep a backup
stock; Exp 2 runs on it if your vial does not come up.

### Materials

- Freezing medium: `[TODO: lab standard, e.g. 90% FBS + 10% DMSO, or complete medium
  + 10% DMSO]`, prepared fresh and cold
- Cryovials, labelled with cell line, passage, date, group, cell number per vial
- Freezing container, −80 °C freezer, liquid nitrogen storage
- Counter, trypan blue

### Before you start

- Freezing container at room temperature, with fresh isopropanol if applicable.
- Liquid nitrogen box position assigned by the staff; write it in the notebook.
- Cells at 70–80% confluence, medium changed the day before.

### Procedure

Freezing (Thursday, week 2)

1. Scrape and count as in P02, steps 1–5.
2. Centrifuge 300 × g, 5 min. Aspirate the medium completely.
3. Resuspend in cold freezing medium at `[TODO: 1–2 × 10^6 cells/mL, lab standard]`.
4. Dispense 1 mL per cryovial, at least 3 vials per group. Work quickly; DMSO is
   toxic at room temperature within minutes.
5. Place the vials in the freezing container and the container at −80 °C overnight.
6. Next day (staff, during the break): transfer to liquid nitrogen. Record the
   position.
7. Dispose of all remaining cultures. No cultures are kept over the break.

Re-thaw (Monday, week 3)

8. Thaw one vial following P01, steps 1–6, and count. Record viability and the
   fraction of cells attached the next morning.
9. Keep this flask as your own stock for extensions. Exp 2 plates are seeded from
   the staff stock culture (P02), which was thawed during the break so that it is
   ready on Monday.

### Controls

- One staff vial frozen in the same container on the same day: separates a bad
  freezing day from a bad freezing technique.

### Checkpoints

- Post-thaw viability above 70% and attachment the next morning: success.
- Below that: still a result. Document and bring it to the failure round.

### Known failure modes

- Low viability: cells too confluent when frozen, DMSO exposure too long before
  freezing, container not at room temperature, slow transfer to nitrogen.
- Vial empty: label mix-up. Labels must carry group and date.

### Output

Number of vials, cells per vial, freezer and nitrogen positions, re-thaw count and
viability, in the notebook. One line on the poster: viability after freeze and thaw.

---

<!-- file: protocols/P04_polarization.md -->

## P04 Polarization of RAW 264.7

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P04 |
| Used in | Exp 2 |
| Hands-on time | 30 min to stimulate, 30 min to wash |
| Wall-clock time | 24 h |
| Resources | hood, incubator shelf |
| Depends on | P02 plates seeded 24 h earlier |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

### Purpose

Generate the four in vitro states that the course compares with tissue macrophages:
M(-), M(IFNγ), M(IL-4) and M(IFNγ+LPS), named after their stimulus as the field
agreed in 2014. The states are then challenged (P05), read by ELISA and Griess
(P06, P07) and phenotyped on the cytometer (P08).

### Materials

- Recombinant mouse IFNγ, recombinant mouse IL-4, LPS (E. coli O111:B4, ultrapure)
  `[TODO: supplier, catalogue number, stock concentrations, aliquot storage]`
- Complete medium, warm
- Sterile PBS, warm

### Before you start

- Plate map from P02 in front of you. Each state has its challenge wells (P05) and
  one unchallenged well for flow cytometry (P08).
- Dilute the stimuli in warm complete medium freshly; do not add stock solutions
  directly to wells.

### Procedure

1. Prepare 2× working solutions in complete medium so that replacing half the well
   volume gives the final concentration, or replace the full volume with 1×
   `[TODO: lab standard]`.

   | State | Reagent | Final concentration | Time |
   |---|---|---|---|
   | M(-) | medium | – | 24 h |
   | M(IFNγ) | recombinant mouse IFNγ | 20 ng/mL | 24 h |
   | M(IL-4) | recombinant mouse IL-4 | 20 ng/mL | 24 h |
   | M(IFNγ+LPS) | IFNγ + LPS | 20 ng/mL + 100 ng/mL | 24 h |

2. Add the stimuli to the wells according to the plate map. Record the clock time.
3. Incubate 24 h.
4. Wash: aspirate, add warm PBS gently along the well wall, aspirate; repeat once.
   Add fresh warm complete medium. Every state is washed, including M(-).
5. Hand the plate to P05 (challenge) and keep the unchallenged well of every state
   for P08.

### Controls

- M(-) is the reference for every comparison.
- M(IFNγ+LPS) is characterised but not re-challenged with LPS: a state that has seen
  LPS shows endotoxin tolerance and would confuse the challenge experiment. Seeing
  tolerance on purpose is an extension (see the nerd ladder).

### Checkpoints

- After 24 h: M(IFNγ+LPS) wells look different, cells spread and often larger; M(IL-4)
  wells look like M(-). If all four wells look identical, check the reagent dilution.

### Known failure modes

- No difference between states: cytokine inactive (freeze-thawed aliquot, wrong
  dilution) or cells overgrown at stimulation. Check the plate photograph from P02.
- Cells detached after washing: PBS added onto the cells instead of along the wall.

### Output

Plate map with the stimulation and wash times, lot numbers of the stimuli, and the
photograph of each state after 24 h.

---

<!-- file: protocols/P05_prr_challenge.md -->

## P05 PRR challenge

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P05 |
| Used in | Exp 2 |
| Hands-on time | 45 min to stimulate, 45 min to harvest |
| Wall-clock time | 24 h |
| Resources | hood, incubator shelf, centrifuge, −20 °C freezer |
| Depends on | P04 completed and washed |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

### Purpose

Ask whether polarization changes the response to a danger signal. Every state is
challenged with LPS as the technical control shared by all groups, and with one
further ligand chosen by the group. The readout in the core is the 24 h supernatant
for ELISA (P06) and Griess (P07). The 6 h RNA arm is an extension (X01).

### Materials

| Stimulus | Receptor | Course role | Working concentration |
|---|---|---|---|
| LPS (E. coli O111:B4, ultrapure) | TLR4 | technical control for every group | 100 ng/mL |
| Pam3CSK4 | TLR1/2 | optional axis | 1 µg/mL |
| CpG ODN 1826 | TLR9 | optional axis | 1 µM |
| Zymosan (depleted) | Dectin-1 | optional axis | 10 µg/mL |
| R848 | TLR7 | optional axis | 1 µg/mL |

Working concentrations `[TODO: confirm in the first run; there is no separate
pilot]`. Suppliers and catalogue numbers `[TODO]`.

- Complete medium, warm
- 1.5 mL tubes for supernatant aliquots, labelled

### Before you start

- Draw the plate map in the notebook before you pipette anything. Layout rule:
  3 states (M(-), M(IFNγ), M(IL-4)) × 3 conditions (unstimulated, LPS, chosen axis),
  in triplicate, one time point (24 h). M(IFNγ+LPS) is not re-challenged (P04).
- One well per state stays unstimulated for P08.

### Procedure

1. Dilute the stimuli to working concentration in warm complete medium.
2. Add to the washed wells from P04 according to the plate map. Record the clock
   time.
3. Incubate 24 h.
4. Harvest: transfer the supernatant to a labelled tube, centrifuge 300 × g, 5 min
   to remove cells and debris, transfer the cleared supernatant to a fresh tube.
5. Aliquot: at least two aliquots per well (ELISA, Griess), freeze at −20 °C. Avoid
   repeated freeze-thaw; one aliquot per assay.
6. Photograph the wells before harvest; the morphology of challenged cells is part
   of the record.

### Controls

- Unstimulated well per state: baseline, and the comparison that shows what
  polarization alone does.
- LPS on M(-): the positive control that every group shares; if it is negative, the
  reagent or the cells are the problem, not the axis.
- Medium-only well from P02: detects a contaminated reagent, which shows as
  cytokine in a well that never saw cells.

### Checkpoints

- The plate map is in the notebook before the first pipette is touched.
- After 24 h: LPS wells are visibly activated. If not, do not harvest yet; ask.

### Known failure modes

- Flat response everywhere: LPS inactive (ultrapure LPS loses activity when stored
  diluted), or endotoxin contamination of the "unstimulated" medium making every
  well look stimulated. The medium-only control separates the two.
- Triplicates far apart: uneven seeding (P02) or pipetting order. Record the order.

### Output

Plate map with stimulation and harvest times, tube labels, freezer position, and
the photograph before harvest.

---

<!-- file: protocols/P06_elisa.md -->

## P06 ELISA for IL-6 and TNF

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P06 |
| Used in | Exp 2 |
| Hands-on time | 3–4 h, with incubation waits |
| Wall-clock time | 1 day (overnight coating if the kit requires it) |
| Resources | plate reader, multichannel pipette, plate washer or wash bottle, bench space |
| Depends on | P05 supernatants (24 h arm) |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

### Purpose

Quantify IL-6 and TNF in the challenge supernatants. These are the NF-κB outputs of
the TLR pathway and the main readout of whether polarization primes or suppresses
the response.

### Materials

- Mouse IL-6 and TNF ELISA kits `[TODO: kit, supplier, catalogue number]`
- Supernatant aliquots from P05, thawed on ice
- Complete medium for standard dilution and blanks
- Plate reader at 450 nm (with 570 nm reference) `[TODO: instrument, software]`

### Before you start

- Kit instructions read once completely; coat the night before if required.
- Plate map for the ELISA plate drawn in the notebook: standard curve in duplicate,
  blanks, samples, which dilutions.
- Dilution: supernatants of LPS-stimulated RAW cells are far above the standard
  range. There is no pilot run; in Exp 2 the first ELISA plate includes each sample
  at two dilutions `[TODO: e.g. 1:10 and 1:100 for LPS wells, neat and 1:10 for
  unstimulated]`, and the dilution that lands in the linear range is used for the
  rest of the plates.

### Procedure

1. Follow the kit per manufacturer `[TODO: paste the step list of the chosen kit
   here once ordered]`.
2. Standard curve: serial dilution in complete medium, duplicate, 7 points plus
   blank.
3. Samples at the dilutions from the plate map, in the same medium.
4. Read at 450 nm, reference 570 nm, within the time the kit specifies after the
   stop solution.
5. Export the raw absorbance table as CSV, named with group, date, plate, analyte.

### Controls

- Blank (medium only): background.
- LPS on M(-): the positive control shared by all groups.
- Medium-only well from P02 run as a sample: detects reagent contamination.

### Checkpoints

- The standard curve is monotonic and the top standard is below saturation.
- At least one dilution of every sample falls inside the standard range; otherwise
  rerun that sample at another dilution.

### Known failure modes

- Samples above the top standard: dilute more.
- High blank: insufficient washing or contaminated medium.
- Edge wells drifting: evaporation during incubation; cover the plate.

### Output

Raw CSV, the ELISA plate map, dilution factors per sample. Concentrations are
calculated in the R template with a four-parameter logistic fit and reported in
pg/mL; where cell numbers differ between wells, normalise per cell.

---

<!-- file: protocols/P07_griess.md -->

## P07 Griess assay (nitrite)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P07 |
| Used in | Exp 2 |
| Hands-on time | 1 h |
| Wall-clock time | 1 h |
| Resources | plate reader (540 nm), multichannel pipette |
| Depends on | P05 supernatants (24 h arm) |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

### Purpose

Measure nitrite, the stable product of nitric oxide, as the proxy for Nos2 activity.
Nitrite is expected to be highest in M(IFNγ+LPS) and in LPS-challenged M(IFNγ). The
assay is informative in mouse cells only.

### Materials

- Griess reagent A: 1% sulfanilamide in 5% phosphoric acid
- Griess reagent B: 0.1% N-(1-naphthyl)ethylenediamine dihydrochloride in water
  `[TODO: supplier, or a commercial Griess kit]`
- Sodium nitrite standard, 0–100 µM, prepared in complete culture medium
- Clear flat-bottom 96-well plate
- Plate reader, 540 nm

### Before you start

- Plate map: standards in duplicate, samples in duplicate, medium blank.
- Supernatants thawed on ice and briefly spun.

### Procedure

1. Pipette 50 µL supernatant or standard per well.
2. Add 50 µL reagent A. Incubate 10 min at room temperature in the dark.
3. Add 50 µL reagent B. Incubate 10 min at room temperature in the dark.
4. Read absorbance at 540 nm within 30 min.
5. Export the raw table as CSV.

### Controls

- Blank: complete medium without cells.
- Standard curve in the same medium as the samples; phenol red and FBS affect the
  background.

### Checkpoints

- Standards form a pink gradient visible by eye; the blank is pale.
- M(IFNγ+LPS) wells are visibly pinker than M(-) before the plate is read.

### Known failure modes

- Everything pink: nitrite in the medium or the water used for the reagent.
- Nothing pink: wrong wavelength, old reagent B (turns brown), or the cells really
  made no nitric oxide, which M(-) and M(IL-4) should not.

### Output

Raw CSV and plate map. Concentrations in µM from the linear standard curve, in the
R template.

---

<!-- file: protocols/P08_flow_cytometry.md -->

## P08 Flow cytometry of polarized RAW 264.7

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P08 |
| Used in | Exp 2 (core: polarized RAW cells); X02 (extension: lavage cells on the same panel) |
| Hands-on time | 2 h staining, 1 h acquisition |
| Wall-clock time | half a day |
| Resources | hood, centrifuge, cytometer slot reserved by the facility `[TODO: instrument, slot dates]`, FlowJo seat |
| Depends on | P04 unchallenged well per state, 24 h after polarization |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

### Purpose

Phenotype the four in vitro states on the course antibody panel. The panel is shared
with the lavage extension (X02) so that in vitro and tissue cells can be compared
directly in the same session. In the core it is run on RAW cells only.

### Materials

Course panel `[TODO: finalise panel, fluorochromes and clones with the flow
facility]`:

| Marker | Purpose |
|---|---|
| Viability dye | exclude dead cells |
| CD45 | haematopoietic |
| CD11b | myeloid |
| F4/80 | macrophage; hi on LPM, lo on SPM |
| MHCII (I-A/I-E) | M(IFNγ) in vitro; SPM in vivo |
| CD86 | M(IFNγ) |
| CD206 | M(IL-4) |
| Tim4 | resident LPM |
| ICAM2 (CD102) | resident LPM |
| Ly6C | monocytes |
| CD19 | B cells in lavage |
| Intracellular Nos2, Arg1 | optional, fixation/permeabilisation |

- FACS buffer: PBS, 2% FBS, 2 mM EDTA `[TODO: lab standard]`
- Fc block (anti-CD16/32) `[TODO]`
- Fixation/permeabilisation kit for the intracellular option `[TODO]`
- Single-stain compensation controls (beads or cells), FMO controls
- FACS tubes or a 96-well V-bottom plate

### Before you start

- Cytometer slot confirmed; the facility reserves slots for the course, two groups
  per slot.
- Staining plan in the notebook: samples, single stains, FMOs, unstained.
- Cells harvested by scraping into cold FACS buffer, counted; `[TODO: 0.5–1 × 10^6
  cells per stain]`.

### Procedure

1. Harvest the unchallenged well of each state by scraping into cold FACS buffer.
   Count.
2. Fc block 10 min on ice.
3. Surface stain: antibody cocktail in FACS buffer, 30 min on ice in the dark
   `[TODO: titrated volumes]`.
4. Wash twice.
5. Viability dye according to its instructions (before or after surface stain,
   depending on the dye).
6. Optional: fix and permeabilise, intracellular stain for Nos2 and Arg1.
7. Resuspend in FACS buffer, keep on ice in the dark, acquire within `[TODO]` hours.
8. Acquire on the facility cytometer `[TODO: instrument]` with compensation controls
   recorded in the same session. Record at least `[TODO: 10,000]` live events per
   sample.
9. Export FCS files named with group, date, sample.

### Controls

- Unstained and single-stain controls for compensation.
- FMO for MHCII, CD86 and CD206: the markers that carry the result.
- M(-) as the reference state.

### Checkpoints

- Viability above 80% in M(-); M(IFNγ+LPS) may be lower.
- MHCII and CD86 higher in M(IFNγ) than M(-), CD206 higher in M(IL-4): if neither
  moves, check the stimulation before the staining.

### Known failure modes

- RAW cells clump after scraping: filter through a 40 µm strainer or pipette
  gently; EDTA in the buffer helps.
- Autofluorescence in activated cells: use the FMOs, not the unstained control, to
  set gates.
- Tim4 and ICAM2 negative on every RAW sample: expected. No in vitro cell falls into
  the large-peritoneal-macrophage gate; that is a result.

### Output

FCS files, compensation matrix, staining plan. Gating in FlowJo (licences from the
facility `[TODO: confirm seats and whether they run on student laptops]`); export
gated population statistics as CSV into the notebook. Do not try to gate in R.

---

# Extension protocols

<!-- file: protocols/X01_qpcr.md -->

## X01 RNA isolation and qPCR (extension)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

> Extension. Requires the 6 h lysate arm to be planned into Exp 2 at the challenge
> step, and RNA, cDNA and qPCR kits `[TODO]`. Ask your supervisor before week 3.

| | |
|---|---|
| ID | X01 |
| Used in | Extension |
| Hands-on time | 1 h at challenge (lysates), then about 1.5 days for RNA, cDNA and qPCR |
| Wall-clock time | 6 h for the lysate arm, then 2 days |
| Resources | hood, −80 °C freezer, RNA bench, qPCR instrument `[TODO: platform]` |
| Depends on | P04 and P05; extra wells in the P05 plate map |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

### Purpose

Measure transcripts of outputs, receptors and transcription factors in the
polarized and challenged states, to ask whether polarization changes the receptor,
the output, or both.

### Materials

- Lysis buffer (RLT or TRIzol) `[TODO]`, RNA isolation kit `[TODO]`, cDNA kit
  `[TODO]`, SYBR or probe chemistry `[TODO: platform]`
- Primers: housekeepers Actb, Hprt. Outputs: Il6, Tnf, Il1b, Nos2, Arg1, Retnla,
  Chil3, Mrc1. Receptors: Tlr4, Tlr2, Tlr9, Clec7a, Tlr7. Transcription factors:
  Irf5, Irf4, Socs1, Socs2 `[TODO: sequences or assay IDs]`.

### Before you start

- Add a 6 h arm to the P05 plate map: the same states and conditions, in triplicate,
  harvested at 6 h instead of 24 h.
- RNase-free bench and tips.

### Procedure

1. At 6 h after challenge: aspirate the medium, lyse the cells directly in the well
   with lysis buffer, transfer to a tube, freeze at −80 °C.
2. Isolate RNA per kit; measure concentration and purity.
3. cDNA per kit with equal RNA input per sample.
4. qPCR: each group runs the housekeepers, the output genes relevant to its axis,
   Nos2, Arg1, Tlr4 and the receptor of its axis. Technical duplicates.
5. Export Ct values as CSV.

### Controls

- No-RT control per sample.
- No-template control per primer pair.
- M(-) unstimulated as the ΔΔCt reference.

### Checkpoints

- RNA A260/280 about 2.0; housekeeper Ct values within 1 cycle across samples.

### Known failure modes

- Housekeepers drift with stimulation: use the mean of both and report it.
- Late Ct for receptors in M(IL-4): may be real suppression; the no-RT control says
  whether the signal is genomic.

### Output

Ct CSV, plate layout, ΔΔCt against M(-) unstimulated in the R template, plots by
state and stimulus.

---

<!-- file: protocols/X02_peritoneal_lavage.md -->

## X02 Peritoneal lavage (extension)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

> Extension. Requires mouse availability and licence coverage for post-mortem lavage
> `[TODO: confirm licence coverage; record genotype per mouse]`. Mice are
> breeding-surplus animals euthanised for colony management, of any genotype. No
> animal is killed for this course and no live animal experiment is performed.

| | |
|---|---|
| ID | X02 |
| Used in | Extension |
| Hands-on time | 1 h per mouse, then staining as P08 |
| Wall-clock time | half a day, coordinated with a cytometer slot |
| Resources | animal facility access with a supervisor, dissection bench, ice, centrifuge, cytometer slot |
| Depends on | P08 panel and a reserved cytometer slot; polarized RAW cells ready on the same day |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

### Purpose

Obtain resident tissue macrophages without digestion and run them on the shared
panel in the same session as the polarized RAW cells. The first result, before any
activation marker, is that no in vitro cell falls into the large-peritoneal-
macrophage gate.

### Materials

- Ice-cold PBS with 2 mM EDTA, 5 mL per mouse
- Syringe and needle for injection and withdrawal `[TODO: gauge]`
- Tubes on ice, counter, FACS reagents as in P08

### Before you start

- Supervisor present for the whole procedure.
- Genotype and sex of the mouse recorded.
- P08 staining plan extended with the lavage samples and CD19.

### Procedure

1. Inject 5 mL ice-cold PBS/EDTA into the peritoneal cavity of the euthanised
   mouse.
2. Massage gently for 30 s.
3. Withdraw the fluid, keep on ice.
4. Count. Expect a few million cells, of which large peritoneal macrophages are
   roughly a third.
5. Stain with the course panel (P08) and acquire in the same session as the
   polarized RAW cells.
6. Hand the carcass to X03 if an organ is to be harvested.

### Controls

- CD19 gate removes B cells; F4/80 against MHCII separates large and small
  peritoneal macrophages; Tim4 with ICAM2 confirms resident identity.

### Checkpoints

- Recovery of most of the injected volume; a bloody lavage is noted and may be
  excluded.

### Known failure modes

- Low cell number: fluid lost on withdrawal, or the needle entered the gut.
- Few LPM: older mouse or prior inflammation; record age and findings.

### Output

Cell counts, mouse metadata, FCS files, and the gated statistics side by side with
the RAW samples.

---

<!-- file: protocols/X03_organ_harvest_ihc.md -->

## X03 Organ harvest and F4/80 immunohistochemistry (extension)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

> Extension. Requires a mouse (shared with X02), licence coverage for organ harvest
> `[TODO: confirm]`, cryostat or paraffin access and slide scanner time. Plan with
> your supervisor in week 1; the fixation and sectioning steps span several days.

| | |
|---|---|
| ID | X03 |
| Used in | Extension |
| Hands-on time | 1 h harvest, 2 h sectioning, 2 × 3 h staining |
| Wall-clock time | about 5 days (fixation 24 h, sucrose overnight, embedding, sectioning, two staining days) |
| Resources | dissection bench, 4 °C, cryostat `[TODO: or microtome per lab SOP]`, histology bench, slide scanner `[TODO: instrument]` |
| Depends on | X02 (same mouse) |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

### Purpose

Test the hypothesis that every tissue contains F4/80-positive macrophages, in an
organ of the group's choice, by single-colour immunohistochemistry.

### Materials

- 4% PFA, 30% sucrose, OCT, cryomolds `[TODO: or paraffin route per lab SOP]`
- Rat anti-mouse F4/80 `[TODO: clone, e.g. BM8 for cryosections]`, HRP-conjugated
  anti-rat secondary, DAB, haematoxylin, mounting medium
- Slides, coverslips

### Before you start

- Organ chosen from the open list: liver, spleen, lung, kidney, heart, brain,
  intestine, skin, adipose tissue, peritoneal wall, lymph node, bone marrow.
- Spleen harvested as the positive control regardless of the chosen organ.
- PFA handled in the fume hood.

### Procedure

1. After lavage (X02), harvest the chosen organ and a piece of spleen.
2. Fix in 4% PFA for 24 h at 4 °C.
3. Cryoprotect in 30% sucrose overnight at 4 °C.
4. Embed in OCT, freeze, cut 8–10 µm cryosections, store at −20 °C.
5. Staining day 1: rehydrate, block endogenous peroxidase, block, primary F4/80
   `[TODO: dilution]` overnight at 4 °C; one no-primary section.
6. Staining day 2: HRP secondary, DAB, haematoxylin counterstain, dehydrate, mount.
7. Image on the slide scanner. Submit the scan and a short legend to the atlas.

### Controls

- No-primary section: secondary and DAB background.
- Spleen: positive control; red-pulp macrophages are bright.

### Checkpoints

- Spleen red pulp brown, no-primary section clean: the stain works and the organ
  result can be read.

### Known failure modes

- Everything brown: endogenous peroxidase not blocked, or DAB developed too long.
- Nothing brown, spleen included: primary inactive or wrong secondary species.

### Reading the result

F4/80 is bright on Kupffer cells, red-pulp macrophages and large peritoneal
macrophages, and dim on alveolar macrophages and lymph node sinus macrophages. A
weak result in lung or lymph node is a finding, not a failure, if the controls are
clean.

### Output

Scanned slides, the legend, and the atlas submission as a merge request; the
hypothesis and its outcome on the poster.

---

# Background reading

<!-- file: background/macrophage_biology.md -->

## Background: macrophage biology

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

This is the background reading for the course. It condenses the Immunology III
lecture on tissue macrophages and the tissue repair lectures to what you need for
the experiments, and it adds the history of the ideas you are going to test. Slide
numbers refer to the Immunology III lecture of 1 December 2025, in the
[slides folder](../slides/README.md) of this repository. Each subsection ends with
questions. We will not collect answers, but we will ask them.

### 5.1 A cell with many names

In 1892 Ilya Mechnikov described cells that eat: small eaters, which we now call
neutrophils, and large eaters, the macrophages. Aschoff grouped them with
endothelial and reticular cells into a reticulo-endothelial system. In the late 1960s
van Furth and colleagues replaced that with the mononuclear phagocyte system, built
on the premise that every tissue macrophage is a blood monocyte that has left the
circulation and settled. In 1973 Steinman added the dendritic cell as a third member
(slide 3).

The monocyte premise held for forty years and then fell within three. Fate-mapping
experiments published between 2010 and 2013 showed that most tissue-resident
macrophages are seeded during embryonic development and maintain themselves by
local proliferation, with little or no input from blood monocytes in the steady state
(Schulz et al. 2012; Yona et al. 2013; Hashimoto et al. 2013). This is the first of
several facts in this chapter that were in every textbook and turned out to be wrong.

The consequence is that a macrophage's name has to answer three questions: where it
came from, where it lives, and what it is doing. The lecture introduced a decision
tree for this (slides 5, 11, 15; Guilliams et al. 2014), and the three levels structure
the rest of this chapter.

`[FIGURE 2: the nomenclature decision tree, from lecture slides 5/11/15, adapted from
Guilliams et al. 2014, Nat Rev Immunol 14:571.]`

Questions. Why did it take until 2012 to overturn the monocyte premise, when
macrophages had been studied for a century? What experiment would you design to
show that a tissue macrophage population does not come from monocytes?

### 5.2 Level I: ontogeny

Macrophages arise in waves (slide 9). At embryonic day 8.5 erythro-myeloid
progenitors (EMPs) emerge from the yolk sac in a RUNX1-dependent manner and
colonise the fetal liver. EMP-derived precursor macrophages spread through the
entire embryo during organogenesis, before haematopoietic stem cells (HSCs) exist.
HSCs then emerge from the intra-embryonic endothelium, colonise the bone marrow
before birth, and supply erythroid, lymphoid and myeloid cells, including monocytes
and monocyte-derived macrophages, for the rest of life.

For practical purposes the lecture reduces this to one question (slide 10): is the
cell of embryonic origin under homeostatic conditions? If yes, it is a tissue-resident
macrophage of yolk-sac or fetal-liver origin that self-renews locally. If no, it is
bone-marrow-derived: a monocyte that entered the tissue in a CCR2-dependent manner,
is short-lived, and can expand massively when the tissue is injured or infected. Many
niches are mixed, and the mix shifts with age. The large peritoneal macrophages of
the peritoneal lavage extension are an example: embryonic at birth, progressively replaced by
monocyte-derived cells in adult life, faster in males than in females (Bain et al.
2016).

Now place the cells of this course on that tree. RAW 264.7 cells are none of the
above. They were established in 1978 from a tumour induced in a BALB/c mouse by
Abelson murine leukaemia virus (Raschke et al. 1978). They are transformed,
aneuploid, proliferate without CSF1, and have been in culture for almost fifty years.
They respond strongly to LPS and IFNγ, weakly to IL-4, and they lack the inflammasome
adaptor ASC, so they cannot release mature IL-1β (Pelegrin et al. 2008). Bone
marrow-derived macrophages (BMDM) are HSC-derived cells differentiated for seven
days in CSF1; they are the closest in vitro relative of a monocyte-derived
macrophage, and still have never seen a niche. Keep this in mind when you compare
either of them with a cell from a mouse.

`[FIGURE 3: waves of macrophage ontogeny, from lecture slide 9, or adapted from
Ginhoux & Guilliams 2016, Immunity 44:439.]`

Questions. Which cells in a peritoneal lavage are embryonic in origin, which are
monocyte-derived, and how would you tell them apart on the flow cytometer? What
does "passage number" mean for a cell line, and why does the lab record it?

### 5.3 Level II: niche

Tissue-resident macrophages carry historic names, such as Kupffer cells, Langerhans
cells, microglia and osteoclasts, or a prefix that names the tissue, such as alveolar
or peritoneal macrophages (slide 12). Most organs contain several distinct niches,
sometimes occupied by cells of different origin, which is why a name by niche is
necessary but not sufficient.

The niche model (slide 13; Guilliams et al. 2020) explains how one precursor becomes
many different macrophages. Precursor macrophages share a core transcriptional
programme driven by PU.1, cMAF and IRF8. Each niche then provides three things:
physical space, survival signals, and imprinting signals. The survival signals are
mostly CSF1 receptor ligands, CSF1 and IL-34, and for alveolar macrophages CSF2
(slide 14: CSF1 is M-CSF, CSF2 is GM-CSF, IL-34 is the second CSF1R ligand).
Csf1-deficient mice lack almost all macrophages except Langerhans cells and
microglia, which depend on IL-34; Csf2-deficient mice lack alveolar macrophages, and
humans without a functional CSF2 receptor develop pulmonary alveolar proteinosis
because nobody clears the surfactant. The imprinting signals, such as TGFβ in the
brain, RANKL in bone, retinoic acid in the peritoneum and heme in the spleen, induce
lineage-determining transcription factors on top of the core programme: SALL1 in
microglia, PPARγ in alveolar macrophages, SPI-C in red pulp macrophages, ID3 in
Kupffer cells and GATA6 in large peritoneal macrophages. Whether the niche
instructs the cell or selects among stochastic cell-intrinsic states is still debated.
Either way, the identity of a tissue macrophage is written by the tissue.

The table lists the niches you are most likely to meet when you pick an organ for
histology. F4/80, the product of the Adgre1 gene, has been the mouse macrophage
marker since 1981 (Austyn & Gordon 1981). It is expressed by almost every tissue
macrophage, but at very different levels, and that is the catch in the immunohistochemistry
extension.

| Niche | Cells | Hallmark markers in mouse | F4/80 |
|---|---|---|---|
| Liver sinusoids | Kupffer cells | CLEC4F, TIM4, VSIG4 | high |
| Lung alveoli | alveolar macrophages | SIGLEC-F, CD11c, PPARγ | low to intermediate |
| Brain parenchyma | microglia | TMEM119, P2RY12, SALL1, CD45 low | positive |
| Spleen red pulp | red pulp macrophages | SPI-C, iron, VCAM1 | high |
| Lymph node sinus | subcapsular and medullary sinus macrophages | CD169, CD209b | low |
| Peritoneal cavity | large peritoneal macrophages | GATA6, TIM4, ICAM2 | high |
| Peritoneal cavity | small peritoneal macrophages | MHCII high, CCR2-derived | low |
| Adipose tissue | lipid-associated macrophages | TREM2, CD9, LPL | positive |
| Bone | osteoclasts | multinucleated, TRAP, RANK | low |
| Skin epidermis | Langerhans cells | CD207 (langerin), IL-34 dependent | positive |
| Intestinal lamina propria | gut macrophages | CX3CR1 high, CD64, monocyte-derived | positive |

`[FIGURE 4: the macrophage niche model, from lecture slide 13 or adapted from
Guilliams et al. 2020, Immunity 52:434.]`

Questions. Pick an organ. Which niche or niches does it contain, what is the
expected F4/80 level, and what would a negative result of F4/80 staining mean? Which survival factor
would you add to the medium if you wanted to keep macrophages from that organ alive
in a dish?

### 5.4 Level III: function, and the rise and fall of M1/M2

In the year 2000 Charles Mills noticed that macrophages from mouse strains with a
Th1-biased immune response metabolise arginine through inducible nitric oxide
synthase (Nos2) to nitric oxide, whereas macrophages from Th2-biased strains
metabolise it through arginase 1 (Arg1) to ornithine and polyamines. He named the two
programmes M1 and M2 in analogy to Th1 and Th2 (Mills et al. 2000). Siamon Gordon
had already described the "alternative activation" of macrophages by IL-4, with the
mannose receptor CD206 as its marker (Stein et al. 1992; Gordon 2003). The two ideas
merged into the textbook scheme: M1, classically activated by IFNγ and LPS, kills
microbes and tumour cells with nitric oxide, TNF, IL-6 and IL-1β; M2, alternatively
activated by IL-4 and IL-13, expresses Arg1, CD206, RELMα (Retnla) and Ym1 (Chil3),
and heals wounds. Sub-types M2a, b and c followed, and by 2008 Mosser and Edwards
drew the states as a colour wheel rather than two poles (Mosser & Edwards 2008).

The scheme is mechanistically true in a dish. IFNγ signals through JAK1 and JAK2 to
STAT1, which induces IRF1, Nos2, the MHC class II transactivator CIITA, and CD86.
IL-4 signals through JAK1 and JAK3 to STAT6, which induces IRF4, Arg1, Retnla, Chil3
and Mrc1 (CD206). The two pathways antagonise each other through SOCS1 and SOCS3.
LPS acts through TLR4 to NF-κB and IRF3 and induces Tnf, Il6, Il1b and type I
interferon. Every readout of this course sits on this map: the Griess assay measures
nitrite, the stable product of Nos2; Arg1 versus Nos2 is literally the arginine fork
Mills described; IL-6 and TNF by ELISA are the NF-κB output; MHCII and CD86 versus
CD206 on the flow cytometer are the STAT1 versus STAT6 surface signatures. Note that
the Griess assay is informative only in mouse cells, because human macrophages make
very little nitric oxide; the two species also differ in several other "M1/M2" genes,
which is one reason the field grew suspicious.

The suspicion became a consensus between 2014 and 2016. Xue and colleagues
stimulated human macrophages with 29 different conditions and found not two states
but a spectrum with many modules (Xue et al. 2014). Murray and colleagues, with most
of the field's senior authors, published guidelines that retire "classical" and
"alternative" and ask every paper to state the source of the macrophages and the
exact stimulus, as in M(IFNγ), M(IL-4) or M(LPS+IFNγ) (Murray et al. 2014). Their
table, reproduced below, is the reference for the states you will generate.

`[FIGURE 1: Murray et al. 2014, Immunity 41:14–20, Figure 1B, reproduced with
reference. Insert into the Word export; the Markdown converter does not embed
images.]`

In this course you will generate four states and characterise them with readouts that
map onto the rows of that table:

| State | Stimulus | Expected readouts (mouse) |
|---|---|---|
| M(-) | medium | baseline |
| M(IFNγ) | IFNγ | Nos2, Irf1, Socs1; MHCII and CD86 up; primed for TLR responses |
| M(IL-4) | IL-4 | Arg1, Retnla, Chil3, Mrc1 (CD206); blunted TLR responses |
| M(IFNγ+LPS) | IFNγ + LPS | Tnf, Il6, Il1b, Nos2 strongly up; tolerance to re-stimulation with LPS |

Only M(IFNγ) is used as the "M1-like" state in the PRR challenge experiment, because
a state that already contains LPS will show endotoxin tolerance when re-stimulated.
The M(IFNγ+LPS) state is characterised but not re-challenged. If you want to see
tolerance, that is an extension challenge.

Why does the scheme fail in tissue (slide 16)? A macrophage in a mouse integrates its
ontogeny, its niche and many simultaneous signals, not one cytokine for 24 hours.
Single-cell RNA sequencing has made this visible: the states found in injured,
fibrotic, atherosclerotic, obese or tumour-bearing tissue are built from modules, and
one cell routinely co-expresses genes from both ends of the old axis. The best
studied example is a TREM2-positive, lipid-handling core programme with tissue- and
disease-specific modifiers, variously called lipid-associated, scar-associated,
fibrosis-associated, tumour-associated or NASH-associated macrophages. In the
peritoneal injury dataset you will analyse, the Trem2+ Spp1+ macrophages express
Arg1 next to Il1b. The lecture calls the replacement a modular spectrum model, and
the point of the in silico arm is that you see it in the data yourself.

Questions. Name one gene that is "M1" in mouse and not in human. If a paper calls
tumour macrophages "M2", what exactly has it measured, and what has it assumed?
What would you call a RAW cell treated with IL-4 for 24 h, in the Murray
nomenclature?

### 5.5 What macrophages do all day

The lecture groups macrophage functions in homeostasis into four (slides 32–39), and
each of them appears somewhere in this course.

**Sensing danger.** Neutrophils are the better killers and dendritic cells the better
antigen presenters. The one thing macrophages do best is to detect that something is
wrong, with germline-encoded pattern-recognition receptors (slide 33). This is the
subject of the next section and of your challenge experiment.

**Safeguarding tissue structure.** Macrophages and fibroblasts form a reciprocal
circuit: the tissue provides CSF1, instruction and structure, the macrophage provides
growth factors such as PDGF, TGFβ and IGF1, proteases and their inhibitors, and
signals for inflammation and its resolution (slide 35; Zhou et al. 2018). Mechnikov
called macrophages sensors and healers. The tissue repair lectures showed where this
circuit sits in granulation tissue and remodelling.

**Efferocytosis.** Billions of cells die by apoptosis every day, and apoptotic cells
are almost never seen in healthy tissue because macrophages remove them without
inflammation. Healthy cells display CD47, a "don't eat me" signal read by SIRPα;
apoptotic cells expose phosphatidylserine, an "eat me" signal read by TIM4 among
others (slide 36). Efferocytosis releases TGFβ, IL-10 and PGE2 and suppresses TNF,
IL-1β and IL-6. TIM4 is in your flow panel as a marker of resident peritoneal
macrophages, and an efferocytosis assay is on the nerd ladder.

**Metabolism.** Macrophages shape adipose tissue, support lipid storage through
PDGF-CC, control browning of white fat, and, when monocyte-derived and recruited in
obesity, drive insulin resistance (slide 39). The Trem2+ lipid-associated programme
from Section 5.4 was first described here.

Questions. Which of the four functions is tested by an LPS challenge? Which one
is not tested by anything in this course, and how would you add it?

### 5.6 Sensing danger: pattern-recognition receptors

Charles Janeway proposed in 1989 that innate immune cells carry germline-encoded
receptors for conserved microbial patterns, before any such receptor was known.
Polly Matzinger added in 1994 that the immune system responds to danger, including
molecules released by the body's own damaged cells, not only to non-self. Both were
right. Medzhitov and Janeway cloned a human Toll-like receptor in 1997, and in 1998
Poltorak and colleagues showed that the LPS-unresponsive C3H/HeJ mouse carries a
mutation in Tlr4. The ligands are now called PAMPs when they come from microbes and
DAMPs when they come from damaged self, and the receptors PRRs. The families you
need are Toll-like receptors (TLR), C-type lectin receptors (CLR), NOD-like receptors
(NLR), RIG-I-like receptors (RLR) and AIM2-like receptors, plus the cGAS–STING
pathway for cytosolic DNA (slide 33).

The LPS pathway is the template for all of them. LPS is extracted from the bacterial
membrane by LPS-binding protein, handed to CD14, and presented to the TLR4–MD-2
complex on the cell surface. TLR4 dimerises and recruits MyD88, which activates
NF-κB and AP-1 within minutes and drives transcription of Tnf, Il6 and pro-Il1b. TLR4
is then internalised and signals through TRIF to IRF3, which induces type I
interferon. Pro-IL-1β is a special case: it is only released as mature IL-1β after a
second signal activates an inflammasome, which RAW cells cannot assemble. For that
reason IL-1β is read by qPCR in the extension, not by ELISA.

`[FIGURE 5: TLR4 signalling from the membrane to NF-κB and IRF3, adapted from a
review, e.g. Fitzgerald & Kagan 2020, Cell 180:1044.]`

The receptors behind the optional axes work by the same logic with different
adaptors and locations. TLR2 pairs with TLR1 to bind triacylated lipopeptides such as
Pam3CSK4 at the surface. TLR9 binds unmethylated CpG DNA, and TLR7 binds
single-stranded RNA and the small molecule R848, both in endosomes. Dectin-1, the
product of Clec7a, is a C-type lectin that binds β-glucan in zymosan and signals
through SYK and CARD9 to NF-κB; untreated zymosan also contains TLR2 ligands, which
is why the course uses depleted zymosan.

| Stimulus | Receptor | Course role | Readouts |
|---|---|---|---|
| LPS (E. coli O111:B4, ultrapure) | TLR4 | technical control for every group | IL-6, TNF, Nos2 |
| Pam3CSK4 | TLR1/2 | optional axis | IL-6, TNF; Tlr2 qPCR |
| CpG ODN 1826 | TLR9 | optional axis | IL-6, TNF; Tlr9 qPCR |
| Zymosan (depleted) | Dectin-1 | optional axis | IL-6, TNF; Clec7a qPCR |
| R848 | TLR7 | optional axis | IL-6, TNF; Tlr7 qPCR |

The question each group asks is whether polarization changes the receptor, the
output, or both. The expectation from the literature is asymmetric. IFNγ primes:
STAT1 raises the expression of TLR4, MD-2, CD14, MyD88 and several IRFs, so the
same dose of LPS produces more cytokine. IL-4 suppresses: STAT6 lowers TLR
responsiveness, partly through IRF4 competing with IRF5 at the MyD88 complex, so the
same dose produces less. Whether your receptor's transcript follows the same pattern
as the output is exactly what the qPCR extension shows, and the answer is not the
same for every receptor.

Endotoxin tolerance is the reason you do not re-challenge M(IFNγ+LPS). A macrophage
that has seen LPS reprogrammes itself within hours: a second dose produces a
fraction of the TNF and IL-6, while some other genes stay inducible (Biswas &
Lopez-Collazo 2009). It protects the organism from lethal cytokine release and it
ruins a naive experiment.

Questions. Draw the plate map for your axis with every control you need, and say
which control detects a contaminated reagent. Your IL-6 is lower in M(IL-4) than in
M(-). List three different mechanisms that could explain that, and say which readout
in your hands distinguishes them.

### 5.7 One niche up close: the peritoneal cavity

The lecture spends its second half on one niche, because it is the one this lab
studies (slides 17–30). The peritoneum, pleura and pericardium are the serosal
cavities, derived from the embryonic coelom, and lined by a monolayer of mesothelial
cells. The peritoneal fluid contains a free-floating population of immune cells, which
is why a lavage with a few millilitres of buffer gives you a tissue macrophage
population without any digestion.

Two macrophage populations live there (Ghosn et al. 2010). Large peritoneal
macrophages (LPM) are F4/80 high, express ICAM2 (CD102) and TIM4, and depend on the
transcription factor GATA6, which is induced by retinoic acid produced in the
omentum (Okabe & Medzhitov 2014; Rosas et al. 2014; Gautier et al. 2014). They make
up roughly a third of the lavage cells in a young adult mouse. Small peritoneal
macrophages (SPM) are F4/80 low, MHCII high and monocyte-derived. The rest of the
lavage is B1 B cells, a few T and NK cells, mast cells and eosinophils. In the flow
panel, CD19 removes the B cells, F4/80 against MHCII separates the two macrophage
populations, and TIM4 with ICAM2 confirms the resident identity. No in vitro cell
will fall into the LPM gate. If you run the peritoneal lavage extension, that is
its first result, before you have looked at a single activation marker.

What do LPMs do? In the steady state they drift through the cavity in undirected
migration (slide 27). On injury they act as extravascular platelets: within minutes
they aggregate on the wounded mesothelium, form clots with each other and with the
damaged surface, and seal the defect (Zindel et al. 2021, Science). This sudden
disappearance from the fluid was known for decades as the macrophage disappearance
reaction before intravital microscopy showed where the cells went. After larger
surgical injury, monocytes are recruited and differentiate into two states, a Folr2+
Selenop+ repair-associated and a Trem2+ Spp1+ scar-associated macrophage, with
intermediate cells between them (slide 29). The scar-associated cells drive the
formation of peritoneal adhesions, the fibrous bands that are the most frequent
long-term complication of abdominal surgery `[TODO: cite the Spp1 paper once
published]`. Bacterial contamination of the cavity, modelled by caecal ligation and
puncture, makes adhesions worse through EGFR signalling in the mesothelium (Zindel
et al. 2021, Nat Commun); this is the experiment behind the dataset in Section 5.9.

`[FIGURE 6: the peritoneal niche in histology, lecture slide 19 (own material):
mesothelial monolayer, LPM on the surface, Masson, H&E and podoplanin staining.]`

Questions. Why is a lavage a better in vivo comparison for your polarized cells
than a digested organ? What is lost in a digested organ that a lavage keeps? If a
mouse had surgery three days ago, how would its lavage differ from a healthy one?

### 5.8 Why a dish is not a body

The in vitro states are reproducible, mechanistically transparent and cheap, which is
why they fill the literature. The in vivo states are the ones that matter. The gap
between them has three sources, and you will meet all three.

First, ontogeny: a cell line or a BMDM has no embryonic history and no history in a
niche. Second, niche: the imprinting and survival signals of Section 5.3 are absent
from culture medium, and the lineage-determining factors are silent or ectopic. Third,
signal integration: a tissue macrophage reads dozens of signals at once, from matrix
stiffness to metabolites to neighbouring cells, and never one cytokine at one
concentration for 24 hours. None of this makes the dish useless. It makes the dish a
model, and a model has a domain of validity that has to be measured, not assumed.
Measuring it is the course.

Questions. Which of the three sources of the gap could you close in vitro, and how?
Which one can you not close?

### 5.9 The in silico dataset and how single-cell RNA sequencing works

GSE186658 (Zindel et al. 2021, Nat Commun, PMID 34916513) contains single-cell RNA
sequencing of mouse peritoneal injury sites 24 h after a surgical button injury, with
and without caecal ligation and puncture, two female C57BL/6 mice per condition. The
data are on GEO as Cell Ranger filtered matrices, one per mouse, in the three-file
format that Seurat reads directly: a list of barcodes, a list of genes, and a sparse
count matrix. The published analysis identified Gata6+ resident macrophages, Folr2+
Selenop+ repair-associated macrophages, Trem2+ Spp1+ scar-associated macrophages,
intermediate states, monocytes and dendritic cells (slide 29).

The method, in one paragraph. Tissue is digested into single cells, which are
captured one per droplet together with a bead carrying a cell barcode and millions of
unique molecular identifiers (UMIs). Reverse transcription inside the droplet tags
every mRNA with the barcode of its cell and a UMI of its own, so that after
sequencing each read can be assigned to a cell and PCR duplicates can be collapsed.
Cell Ranger aligns the reads and produces the count matrix: genes in rows, cells in
columns, UMIs as values, mostly zeros.

The analysis you will reproduce follows the standard Seurat workflow (Hao et al.
2021). Quality control removes barcodes with too few genes, likely empty droplets,
and barcodes with too many or with a high fraction of mitochondrial transcripts,
likely doublets or dying cells. Counts are normalised for sequencing depth and
log-transformed. The few thousand most variable genes are selected and reduced by
principal component analysis. Cells are connected into a nearest-neighbour graph in
principal component space and clustered by community detection. UMAP projects the
graph into two dimensions for display, and only for display: distances on a UMAP are
not measurements. Clusters are annotated by marker genes, which is where biology
enters. Macrophages are found by Adgre1, Cd68, Csf1r, Fcgr1 and Mertk; monocytes by
Ly6c2, Ccr2 and Plac8; dendritic cells by Flt3, Xcr1 and Ccr7; B cells by Cd79a; T
cells by Cd3e; mesothelial cells by Msln and Upk3b. Within the macrophages, the three
populations are separated by Gata6, Timd4 and Icam2, by Folr2, Selenop and Lyve1, and
by Trem2, Spp1, Cd9 and Lpl. Finally, each cell is scored for a gene signature by
comparing the mean expression of the signature genes with a matched random control
set; this is how you will ask every in vivo macrophage how M(IFNγ)-like and how
M(IL-4)-like it is.

The core in silico task is built on that last step. The M(IFNγ+LPS) and M(IL-4)
signatures are not taken from a textbook list; you derive them from a public bulk
RNA-seq dataset of RAW 264.7 cells and bone marrow-derived macrophages stimulated
with the same reagents you use at the bench (GSE113836, `[TODO: verify contents,
replicates and raw counts before the course]`). Every macrophage in the peritoneal
single-cell dataset is then scored against both signatures, and the question is how
much of the tissue population either signature explains. Integration of the tissue
cells with a true in vitro single-cell dataset (Sanin et al. 2022, Sci Immunol,
`[TODO: accession]`) is an extension, not the core. The teaching staff preprocess
both datasets and ship small, ready-to-load objects, so the dry lab never starts
from raw reads.

Two limitations matter for your interpretation. Enzymatic digestion under-represents
cells that are fragile or adherent, and large peritoneal macrophages are notoriously
lost, which is why the Gata6+ cluster is small in the data and large in a lavage.
And the dataset describes injured tissue at a single time point, so a state that is
absent at 24 h may dominate at day 7.

`[FIGURE 7: the published UMAP of the dataset, lecture slide 29 (own material).]`
`[FIGURE 8: the single-cell workflow from tissue to count matrix to clusters,
adapted from a review or drawn by the lab.]`

Questions. Why is the Gata6+ cluster small in the sequencing data but large in a
lavage? What would a cell with a high M(IFNγ) score and a high M(IL-4) score mean
for the M1/M2 axis? A reviewer says "the two conditions are not integrated". What do
they mean, and how would you check?

### 5.10 Working with a language model as a scientist

You will use a large language model to install software, write and debug analysis
code, and probably to read papers. It will be fast and mostly right, and the mostly is
the problem. Language models invent functions that do not exist in a package, choose
default parameters silently, mis-state what a method assumes, and cite papers that
were never written. They do all of this in confident prose. The availability of
plausible text now outgrows the availability of verified claims by orders of magnitude
(Bergstrom & West 2020), and a scientist's job is to tell the two apart.

Three habits protect you. Run the code and look at the object, not at the model's
description of the object. Reproduce a known result before you trust a new one, which
is why the in silico challenge gives you code without figures. And write down every
error you catch in the LLM error log; the log is scored because the habit is the
skill.

Questions. The model tells you that a Seurat function normalises "by default to
10,000 counts per cell". How do you check in under a minute? A citation the model
gave you has a real journal, a real year and a plausible author list. What else do
you need?

---

# Reading list

<!-- file: background/reading_list.md -->

## Reading list

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

References for the background chapter and the experiments. Where a DOI or PMID is
given it has been checked; the others are to be completed and every page range is
to be checked against the PDF before the course `[TODO]`. Add the tissue repair
reviews used in the lecture `[TODO]`.

### Nomenclature, ontogeny and niche

- Guilliams M et al. Dendritic cells, monocytes and macrophages: a unified
  nomenclature based on ontogeny. Nat Rev Immunol 2014;14:571–578.
  DOI 10.1038/nri3712
- Schulz C et al. A lineage of myeloid cells independent of Myb and hematopoietic
  stem cells. Science 2012;336:86–90.
- Yona S et al. Fate mapping reveals origins and dynamics of monocytes and tissue
  macrophages under homeostasis. Immunity 2013;38:79–91.
- Hashimoto D et al. Tissue-resident macrophages self-maintain locally throughout
  adult life with minimal contribution from circulating monocytes. Immunity
  2013;38:792–804.
- Ginhoux F, Guilliams M. Tissue-resident macrophage ontogeny and homeostasis.
  Immunity 2016;44:439–449.
- Guilliams M, Thierry GR, Bonnardel J, Bajenoff M. Establishment and maintenance of
  the macrophage niche. Immunity 2020;52:434–451.
- Austyn JM, Gordon S. F4/80, a monoclonal antibody directed specifically against
  the mouse macrophage. Eur J Immunol 1981;11:805–815.

### Activation states

- Mills CD et al. M-1/M-2 macrophages and the Th1/Th2 paradigm. J Immunol
  2000;164:6166–6173.
- Stein M, Keshav S, Harris N, Gordon S. Interleukin 4 potently enhances murine
  macrophage mannose receptor activity. J Exp Med 1992;176:287–292.
- Gordon S. Alternative activation of macrophages. Nat Rev Immunol 2003;3:23–35.
  DOI 10.1038/nri978
- Mosser DM, Edwards JP. Exploring the full spectrum of macrophage activation. Nat
  Rev Immunol 2008;8:958–969. DOI 10.1038/nri2448
- Xue J et al. Transcriptome-based network analysis reveals a spectrum model of
  human macrophage activation. Immunity 2014;40:274–288.
- Murray PJ et al. Macrophage activation and polarization: nomenclature and
  experimental guidelines. Immunity 2014;41:14–20. DOI 10.1016/j.immuni.2014.06.008
- Sanin DE et al. A common framework of monocyte-derived macrophage activation. Sci
  Immunol 2022;7(70) `[TODO: confirm eLocator and GEO accession]`.
- Colombo and colleagues. Consolidated murine M1 and M2 polarization gene sets from
  deposited RNA-seq datasets. PLOS ONE 2024 `[TODO: full citation]`.

### Pattern recognition

- Janeway CA. Approaching the asymptote? Evolution and revolution in immunology.
  Cold Spring Harb Symp Quant Biol 1989;54:1–13.
- Matzinger P. Tolerance, danger, and the extended family. Annu Rev Immunol
  1994;12:991–1045.
- Medzhitov R, Preston-Hurlburt P, Janeway CA. A human homologue of the Drosophila
  Toll protein signals activation of adaptive immunity. Nature 1997;388:394–397.
- Poltorak A et al. Defective LPS signaling in C3H/HeJ and C57BL/10ScCr mice:
  mutations in Tlr4 gene. Science 1998;282:2085–2088.
  DOI 10.1126/science.282.5396.2085
- Fitzgerald KA, Kagan JC. Toll-like receptors and the control of immunity. Cell
  2020;180:1044–1066.
- Biswas SK, Lopez-Collazo E. Endotoxin tolerance: new mechanisms, molecules and
  clinical significance. Trends Immunol 2009;30:475–487.

### Cells and models

- Raschke WC, Baird S, Ralph P, Nakoinz I. Functional macrophage cell lines
  transformed by Abelson leukemia virus. Cell 1978;15:261–267.
- Pelegrin P, Barroso-Gutierrez C, Surprenant A. P2X7 receptor differentially couples
  to distinct release pathways for IL-1β in mouse macrophage. J Immunol
  2008;180:7147–7157.
- Zhou X et al. Circuit design features of a stable two-cell system. Cell
  2018;172:744–757.

### Peritoneal cavity

- Ghosn EEB et al. Two physically, functionally, and developmentally distinct
  peritoneal macrophage subsets. Proc Natl Acad Sci USA 2010;107:2568–2573.
- Okabe Y, Medzhitov R. Tissue-specific signals control reversible program of
  localization and functional polarization of macrophages. Cell 2014;157:832–844.
- Rosas M et al. The transcription factor Gata6 links tissue macrophage phenotype
  and proliferative renewal. Science 2014;344:645–648.
- Gautier EL et al. Gata6 regulates aspartoacylase expression in resident peritoneal
  macrophages and controls their survival. J Exp Med 2014;211:1525–1531.
- Bain CC et al. Long-lived self-renewing bone marrow-derived macrophages displace
  embryo-derived cells to inhabit adult serous cavities. Nat Commun 2016;7:11852.
  DOI 10.1038/ncomms11852
- Zindel J et al. Primordial GATA6 macrophages function as extravascular platelets
  in sterile injury. Science 2021;371:eabe0595. DOI 10.1126/science.abe0595
- Zindel J et al. Intraperitoneal microbial contamination drives post-surgical
  peritoneal adhesions by mesothelial EGFR-signaling. Nat Commun 2021.
  PMID 34916513

### Single-cell analysis and reasoning

- Hao Y et al. Integrated analysis of multimodal single-cell data. Cell
  2021;184:3573–3587. DOI 10.1016/j.cell.2021.04.048
- Bergstrom CT, West JD. Calling Bullshit: The Art of Scepticism in a Data-Driven
  World. Random House, 2020.

### Datasets

- GSE186658: single-cell RNA-seq of mouse peritoneal injury sites 24 h after
  surgical button injury, with and without caecal ligation and puncture (Zindel et
  al. 2021, Nat Commun). The in vivo dataset of the core in silico task.
- GSE113836: bulk RNA-seq of primary mouse bone marrow macrophages and RAW 264.7
  cells skewed with LPS plus IFNγ or with IL-4. Source of the in vitro signatures
  `[TODO: verify contents, replicates and raw counts before the course]`.

---

# Slides index

<!-- file: slides/README.md -->

## Slides

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

The lectures this course builds on, as presented at ETH Zürich. They are the
background for the [background reading](../background/macrophage_biology.md), which
condenses them to what the experiments need.

| File | Lecture |
|---|---|
| [01_ImmunologyIII_TissueMacrophages.pdf](01_ImmunologyIII_TissueMacrophages.pdf) | Immunology III: tissue macrophages (1 December 2025). The slide numbers in the background reading refer to this deck. |
| [02_TissueRepair_Part1.pdf](02_TissueRepair_Part1.pdf) | Tissue repair, part 1 |
| [03_TissueRepair_Part2.pdf](03_TissueRepair_Part2.pdf) | Tissue repair, part 2 |
| [04_TissueRepair_Part3_GranulationTissue.pdf](04_TissueRepair_Part3_GranulationTissue.pdf) | Tissue repair, part 3: granulation tissue |
| [05_TissueRepair_Part4_Remodelling.pdf](05_TissueRepair_Part4_Remodelling.pdf) | Tissue repair, part 4: remodelling |

Figures taken from the published literature are cited on the slide and remain the
property of their owners; the CC BY licence of this repository covers the lecturer's
own material only.

---

# Slides: extracted text

<!-- file: slides/01_ImmunologyIII_TissueMacrophages.pdf -->

```text
D-BIOL

Tissue Marcophages
Immunology III HS 2025
Prof. Dr. Joel Zindel
Assistenzprofessor
01. Dezember 2025
How to read these slides

! Central concepts — exam-relevant
How we know    In Immunology III, we look at the actual experiments behind key ideas—not just textbook
summaries. These slides show where the evidence comes from. You don’t need to memorize the details
but use them to think about how scientists know what they claim and how data shapes our
understanding.

Slides with black background serve as additional illustration from our own research.

Literature (DOI) these slides are mostly based on:
• 10.1038/s41586-023-06002-x
• 10.1016/j.immuni.2016.02.024
• 10.1016/j.cell.2022.10.007
• 10.1038/nri3712

               D-BIOL, IMHS                                                                    01.12.2025   2
 Historical Concepts

• Mechnikov 1892 Discovery of phagocytes                            Ilya (Elie) Mechnikov
  − Small eaters (microphages, today PMN)                           1892, the father of
                                                                    cellular immunity
  − Large eaters (macrophages)
• Aschoff: «Reticulo Endothelial System» (RES)
• Late 1960s «Mononuclear Phagocyte System» (MPS) premise
  that all macrophages derived from monocytes.
• 1970 Steinman discovery of dendritic cell (DC) which was
  considered the third cell in the MPS
• Cells of the MPS initially thought to derive exclusively from blood
  monocytes, but with more fate-mapping tools available this
  concept is now obsolete.

                D-BIOL, IMHS                                                                01.12.2025   3
Learning Objectives

1.   Students can correctly classify/name cells of the Mononuclear Phagocyte System (MPS)
     1.   First level nomenclature by otogeny
     2.   Second level nomenclature by tissue/niche
     3.   Second level nomenclature by functional properties/programs.
2.   Students understand the Core Functions of macrophages in homeostasis
     1.   Extracellular milieu: safeguarding tissue structure
     2.   Cellular fitness: efferocytosis
     3.   Microorganisms: innate immunity
     4.   Metabolism
3.   Students illustrate the role of macrophages in specific disease mechanisms
     1.   Primary macrophage defects.
     2.   The role of macrophages in non-primary macrophage diseases.

             D-BIOL, IMHS                                                              01.12.2025   4
   A decision tree to facilitate nomenclature for mononuclear phagocytes              !

First level nomenclature by ontogeny                            DCs were already
                                                                covered in separate
                                                                lecture

                D-BIOL, IMHS           10.1038/nri3712               01.12.2025   5
                                                                   How we know
Example of a fate mapping study.

• In this paper they show first
  that Ms4a3Cre Rosa26LSL
  tdTomato is specifically and

  transiently expressed by
  Granulo-Monocyte Progenitors
  (GMP)
• Ms4a3Cre-based models fate-
  map monocytes and
  granulocytes.
• Then, they look at many bona
  fide TRMs over time (without
  inflammatory challenge).
• The contribution of monocytes
  to TRMs is largely tissue-
  dependent.                                    Green =         Red=
   https://doi.org/10.1016/j.cell.2019.08.009
                                                Kupffer cells   Monocyte
                                                                derived
                   D-BIOL, IMHS                                  01.12.2025   6
                                         How we know
    Example of a fate mapping study.

• These observations
  are under homeostatic
  non-inflammatory
  conditions.
• Importantly,
  monocytes contribute
  signifcantly more
  under inflammatory
  challenge (injury)

                 D-BIOL, IMHS          01.12.2025   7
                                                                                              How we know
Fate-mapping studies in humans?
                                                        Liver
• Mouse paradigm broadly supported in                                                     Lung
  humans, i.e. presence of long-
  lived/replicated TRMs that can be replaced                    5 years post-transplant
  by monocytes, especially under injury.
• After lung transplant, alveolar macrophages
  are largely replaced by monocyte-derived
  cells (Sex-mismatched donors). Note this is
  controversial! Some authors find no or very
  late replacement.
                                                                7 days post-transplant
• After liver transplant, Kupffer cells are long-
  live, self-replicating, but also largely replaced
  over time (HLA-mismatched, Sex-
  mismatched)
• Brain microglia stay recipient-derived after
  bone marrow transplantation (even decades
  later), but replacement possible after injury.        Signal of Y chromosome (arrow)
                                                        Anti-CD68 (Kupffer cell marker)
                 https://doi.org/10.1084/jem.20191236
                                                                                            01.12.2025   8
                 DOI 10.1007/s00428-003-0861-8
      Otogeny: Developmental Origins
• Using many different fate-mapping
  tools the different waves of otogeny
  have been established
• At E8.5 erythro-myeloid progenitors
  (EMPs) arise from the yolk sac in a
  RUNX1-dependent manner and
  colonize the fetal liver.
• EMP-derived precursor
  macrophages (preMAcs) colonize
  the entire embryo during
  organogenesis, before the
  emergence of HSCs
• Haematopoietic stem cells (HSCs)
  emerge from the intra-embryonic
  endothelium and colonize the bone
  marrow before birth.
• HSC give rise to erythroid, lymphoid,
  and myeloid cells (including
  macrophages) throughout life.

                    D-BIOL, IMHS          01.12.2025   9
Otogeny: Reduced Complexity Model                                                                                !

                  Is the cell of emrbyonic origin under homeostatic conditions?

                                    Yes                       No

            Embryonic ~                                         Bone marrow derived ~
            Yolk Sac ~                                          Monocyte Derived ~
            Fetal Liver ~                                       CCR2-dependent ~
            EMP                                                 HSC Derived ~
                                                                GMP Derived Macrophages

            Paradigm: EMP gice rise to tissue resident macrophages (TRM) that self-renew
            locally, whereas HSC-derived macrophages are short-lived and rely on circulating
            monocytes and can massively expant.

       D-BIOL, IMHS                                                                            01.12.2025   10
    A decision tree to facilitate nomenclature for mononuclear phagocytes

                                                                 DCs were already
                                                                 covered in separate
                                                                 lecture

Second level nomenclature
by tissue/niche

                D-BIOL, IMHS                                          01.12.2025   11
   Level II: Name by Niche (mostly for TRM)                                                                          !

• Second level classification according to
  niche.
• Either by historic names such as Kupffer
  cells, Langerhans cells, Microglia, ect.
• Or by adding a 2nd level prefix, e.g.
  Alveolar Macrophage, Peritoneal
  Macrophage.
• When we look more closely there are
  often several distinct niches per organ.
• The cell populations in these subtissular
  niches can be of different EMP/MSC
  origin which can make classification
  complex.

                  D-BIOL, IMHS                https://www.nature.com/articles/s41577-023-00848-y   01.12.2025   12
Is the niche shaping the macrophages or the other way arround?

• While preMacs share a core
  macrophage transcriptional
  programme (PU.1, cMAF, IRF8),
  cells start to express niche-
  specific lineage marker in their
  respective destination tissue.
• Cell-intrinsic lineage Determining
  Factors (LDFs) comprise SALL1,
  ID3, PPARy, SPI-C, GATA6.
• At the same time, the macrophages
  receive niche-specific signals that
  have been shown to induce LDFs:
  TGFb, RANKL, Retinoic Acid.
• The instructive model suggests
  that the specification process is
  driven by niche-specific signals,
  while the stochastic model
  suggest that it is driven mainly by
  cell-intrinsic signals.

                D-BIOL, IMHS                                     01.12.2025   13
   Level II: Name by Niche                                                                             !
A TRMs niche needs lifelong suvival signals to be
maintained. These signals are mostly CSF1R and CSF2R
signaling.
• CSF1-/- mice: No macrophages except Langerhans
  cells and Microglia
• IL34-/- mice: no Langerhans cells and no Microglia.
• CSF2-/- mice: no lung alveolar macrophages
• CSF2R-/- in humans: pulmonary alveolar proteinosis
  (i.e. no alveolar macrophages)
• Remember this 1234:
  − CSF1 = M-CSF
  − CSF2 = GM-CSF
  − Il34 = CSF1R ligand

                                                        10.1016/j.cell.2022.10.007

                   D-BIOL, IMHS                                                      01.12.2025   14
    A decision tree to facilitate nomenclature for mononuclear phagocytes

                                                                 DCs were already
                                                                 covered in separate
                                                                 lecture

Second level nomenclature
by function/program

                D-BIOL, IMHS                                          01.12.2025   15
    LEVEL II – Name by Functional Properties (mostly for BMDM)                                              !
•   M1/M2 are no longer considered accurate
    descriptors, historically
    − M1 «classical»
    − M2 «alternative»                                (historic) Discrete   Modular Spectrum
    − DC                                              Polarization Model    Model
•   This heuristic came mostly from in vitro
    experiments (Figure left panel).
•   It is recommended to retire this heuristic when
    describing in vivo systems and to think of mac
    activation as a modular spectrum.
•   The granularity of this spectrum has increased
    with scRNA-Seq:
    − Example: Lipid-handling (Trem2+)
      macrophage core program with disease-
      and tissue specific modifiers: Fibrosis-
      associated (FAM), Tumor-associated
      (TAM), Lipid-associated (LAM), Scar-
      associated (SAM), NASH-associated
      (NAM)

                   D-BIOL, IMHS                                                           01.12.2025   16
     Let’s look at one niche more closely (from our own research)    How we know

                          Pericardium
   Pleura

Peritoneum

                                   Coelom

                                              Mesothelium ~ Serosa ~ Peritoneum
Let’s look at one niche more closely (from our own research)   How we know

                                                        Fair Warning
   Let’s look at one niche more closely (from our own research)                            How we know

                     Peritoneum
                                  Mesothelial Monolayer
                                                              Tissue Resdident Macrophages =
                                                              Large Peritoneal Macrophages=
                                                              GATA6+ F4/80hi CD102+

                                                          Peritoneum
Masson     H&E              Anti-Podoplanin   500u
           D-BIOL, IMHS
                                              m                                          01.12.2025   19
                                                                                                         How we know
           Modulation of macrophage GATA6 expression
Tissue Resdident Macrophages =
Large Peritoneal Macrophages=
GATA6+ F4/80hi CD102+
                                                      Dietary Vitamin A intake                    Pharmacological

                                  depleted
                                 Vitamin A depleted       normal
                                                          Vitamin A normal    enhance
                                                                             Vitamin A enriched

                                                                              d
   Let’s look at one niche more closely (from our own research)                             How we know

                     Peritoneum

                             Laser-
                            induced
                          focal Injury

                                                https://doi.org/10.1126/science.abe0595
Masson     H&E                           500u
           D-BIOL, IMHS
                                         m                                                01.12.2025   21
                 Use case: Intravital Microscopy                     How we know

                              Non-alcoholic
                               beverage
                                                            Injury

                                              Macrophages
Courtesy M. Dosch, G. Beldi
           Students
                                                                    How we know

Tinevez, J. Y., et al. (2017). "TrackMate: An open and extensible
platform for single-particle tracking." Methods 115: 80-90.
                               How we know

Directed or random movement?

    Focal
    injury
                                     How we know

Canonical example neutrophils
Damage     LyzM-GFP
Collagen

                                Guys there is
                                free drinks on
                                F-floor
                                   How we know
platelet aggregation
 Tracking Macrophage recruitment
                                     Undirected migration
                                                                                               How we know

                J                                                    K

                                     0.240 s      0.260 s   0.280s

                          60
Distance to injury [um]

                          40

                          20

                          0
                               0.0       0.2          0.4    0.6
                                               time [sec]

                                                                     I really like this random bar,
                                                                     let’s have a drink here
                                                               How we know
                Macrophages act as platelets

In vivo (IVM)

                             LyzCre: Rosa26LSL-GCaMP6f

                            SHG F4/80              SHG F4/80
                                                                                                                    How we know
 Let’s look at one niche more closely (from our own research)

                                         Gata6+
                               Tissue Resident Macrophages             5
                                                                   1
                                                                                           Pro-inflammatory cytokine
                                                                                           release (used to be M1)

 Folr2+Sele nop +
Repair-associated
                           7

                      8

                                                                            Repair/Folr2                            Trem2/Spp1
                                        Intermediate                                                                (lipid/stress)
                2      6                macrophages

  Monocytes

                                                Trem2 +Spp1 +
                       3
                                4
                                               Sca r-associated                            Il-4 induced (used to be M2)
                                    lipid-handling, lysosomal, phagocytic

           DC

                    D-BIOL, IMHS                                                                                  01.12.2025   29
                                                 How we know
 Discrete Polarization in vitro
• The M1/M2 heuristic can still be
  used to describe in vitro               M2                M1
  polarization.
• You may find this useful later, so
  we’ll add the info here (but please
  don’t memorize this!)
• First, the source of macrophages
  should be described (e.g. bone
  marrow).
• Second, it is recommended to
  describe the precise macrophages
  activation e.g. M(IL-4), or M(IL-10),
  rather than just the two ends of the
  spectrum M1/M2.
• The terms «classical» and
  «alternative» macrophages are
  misleading and should not be used
  anymore.

                D-BIOL, IMHS                   01.12.2025    30
Learning Objectives

1.   Students can correctly classify/name cells of the Mononuclear Phagocyte System (MPS)
     1.   First level nomenclature by otogeny
     2.   Second level nomenclature by tissue/niche
     3.   Second level nomenclature by functional properties/programs.
2.   Students understand the Core Functions of macrophages in homeostasis
     1.   Extracellular milieu: safeguarding tissue structure
     2.   Cellular fitness: efferocytosis
     3.   Microorganisms: innate immunity
     4.   Metabolism
3.   Students illustrate the role of macrophages in specific disease mechanisms
     1.   Primary macrophage defects.
     2.   The role of macrophages in non-primary macrophage diseases.

             D-BIOL, IMHS                                                              01.12.2025   31
Core Macrophage Functions

        D-BIOL, IMHS        01.12.2025   32
Microorganisms: Innate Immunity (Repetition of Immunology I & II)                     !
• Macrophage moderate importance of direct
  bacterial clearance. Neutrophils are the best
  bacterial killers.
• Professional Antigen Presenting Cell (APC),
  especially Th1/th17, but less potent than
  Dendritic best APCs)
• The most important role of macrophages is
  detection/sensing of danger
• Therefore, all macrophages express germline-
  encoded pattern recognition receptors (PRR)
  − Toll-like receptors
  − RIG-I-like receptors
  − NOD-like receptors
  − AIM2-like receptors
  − C-type lectin receptors

             D-BIOL, IMHS                                           01.12.2025   33
                                                                                                     How we know
Surveillance

• Macrophages constantly probe environment
• Macrophages are dynamic first reponders to tissue damage.
• Small injuries can be «cloaked» and repaired without inflammation
• If injury exceeds a certain threshold, macrophages induce inflammation signified by neutrophil
  recruitment.

   https://www.cell.com/fulltext/S0092-8674(19)30211-9
                  D-BIOL, IMHS                                                                     01.12.2025   34
Extracellular Milieu: Safeguarding Tissue Structure                                               !
•   Macrophages are a key cell type in defining the set point of a tissue.
    Mechnikov called them «sensors and healers» and
•   Medzhitov uses the term «macrophage fibroblast circuits» where a
    reciprocal regulatory loop (circuit) defines tissue architecture, repair,
    and steady state.
•   Tissue provides
    − Csf1
    − Instruction for TRM programming
    − Chemokines (recruitment)
    − Metabolic cues
    − Structure
    Macrophages provide
    − Structure
    − Have many sensors and integrate signals (also danger signals)
    − Production of signals: growth factorts (PDGF, TGFb, IGF), matrix
      remodelling signals, inflammatory signals, resolution signals.
    − Production of proteases and protease inhibitors

                   D-BIOL, IMHS                                                 01.12.2025   35
Cellular Fitness: Efferocytosis                                                !

  •   Daily, billions of cells die in the tissue by
      undergoing apoptosis, yet apoptotic cells are rarely
      observed in homeostasis.
  •   This is due to a process called efferocytosis that
      efficiently clears apoptotic cells without causing
      inflammation.
  •   Efferocytosis is a well-defined molecular event
      (follow link for review). The following elements are
      worth memorizing:
      − Healthy cells express CD47, a «don’t eat me
        signal» recognized by SIRP1α on phagocytes
      − Apoptotic cells express «eat me signals» the
        most important is Phosphatidylserine (PS)
        which is recognized by TIM4 and many others
        (Figure)
  •   The process is anti-inflammatory characterized by
      the release of TGFb, IL-10, PGE2 and the
      inhibition of inflammatory cytokines such as TNF,
      IL1b, IL6

                 D-BIOL, IMHS                                01.12.2025   36
                                                                                              How we know
Csf1R-/- in rats

                                                      •   Almost as an incidental finding the authors report
                                                          significantly reduced visceral fat in this rat.
                                                      •   Because of the potential therapeutic implications
                                                          (and market!) this was taken up by others.

           https://doi.org/10.4049/jimmunol.1701783

          D-BIOL, IMHS                                                                      01.12.2025   37
                                                                                                                         How we know
    Trem2+ Lipid Associated Macropages (LAM)
A
                                                                       (A) A conserved Trem2 signature characterizes obesity-related
                                                                       macrophages in mice and humans.
                                                                       (B) Trem2-/- results in adipocyte hypertrophy
     Normal          High fat diet              Obese
                                                                       (C) Trem2-/- results in loss of systemic metabolic
                                                                       homeostasis
B                                                            C

                                     https://doi.org/10.1016/j.cell.2019.05.054
              D-BIOL, IMHS                                                                                             01.12.2025   38
Metabolism                                                                     !

• Csf1R-/- rats: loss of visceral adipose tissue!
• CCR2-dependent BMDM promote systemic inflammation
  and insulin resistance in obese animals.
• But, (other?) CCR2-dependent Trem2 Lipid
  Associated Macrophages (LAM) prevent adipocyte
  hypertrophy and help with systemic metabolic
  homeostasis.
• Macrophages as «metabolic sensors» that support
  lipid storage in white adipocytes through the production
  of PDGF-CC.
• Fat-resident macrophages can also control energy
  expenditure by promoting browning of white adipose
  tissue (produce heat from fat).
• May represent therapeutic targets!!

              D-BIOL, IMHS                                   01.12.2025   39
Learning Objectives

1.   Students can correctly classify/name cells of the Mononuclear Phagocyte System (MPS)
     1.   First level nomenclature by otogeny
     2.   Second level nomenclature by tissue/niche
     3.   Second level nomenclature by functional properties/programs.
2.   Students understand the Core Functions of macrophages in homeostasis
     1.   Extracellular milieu: safeguarding tissue structure
     2.   Cellular fitness: efferocytosis
     3.   Microorganisms: innate immunity
     4.   Metabolism
3.   Students illustrate the role of macrophages in specific disease mechanisms
     1.   Primary macrophage defects.
     2.   The role of macrophages in non-primary macrophage diseases.

             D-BIOL, IMHS                                                              01.12.2025   40
    Leukoencephalopathy and Alzheimer                                                                                      !
• Microglia, the main macrophage subset of the CNS,
  provide trophic support, may regulate neuronal activity.
• Growth factors (IGF, NGF, BDNG, neurotropin-3)
  important for development and survival of neurons and
  glial cells.
• Humans with CSF1R mutations present with a spectrum
  of neurological and skeletal phenotypes.
• Depending on rest activity of CSF1R can be adult-onset
  (Figure), but bi-allelic CSF1R loss-of-function results in
  paediatric-onset leukoencephalopathy with near
  absence of microglia and death in the first year of life
  (histology: spheroids).
• Mutations in TREM2 gene lead to neurodegenerative
  bone disease with slerosing leukoencephalopathy.
• Population-wide studies identified TREM2
  polymorphisms associated with the risk of Alzheimer’s
  disease.
                                                               https://www.nature.com/articles/ng.1027
                   D-BIOL, IMHS                                                                          01.12.2025   41
Bone osteoclasts, osteopetrosis, and osteoporosis                                                                              !
                                                                                           Selective estrogen receptor
• Osteoclasts are a highly specialized form of                                             modulators/hormone
  multinucleated macrophages reside in the bone                                            therapy: normalize
  endosteum.                                              RANKL-Antibody                   RANKL/OPG ratio
• They secrete acid and lytic enzymes such as
  cathepsin K that dissolve bone.
• Osteoclasts secrete growth factors (IGF1,
  TGFβ) for osteoblasts and vice versa (RANKL,
  CSF1).
• Loss-of-function mutations in genes that are
  required for osteoclast formation or function
  (RANKL, RANK receptor, chloride channels,…)
  cause osteopetrosis, an extremely rare inherited
                                                                https://www.nature.com/articles/s41413-018-0019-6
  disorder whereby bones become harder and
  denser.
• Osteoporosis in turn, can be treated by inhibiting   Bisphosphonates (e.g. Clodronate,
  Osteoclasts (examples in red in the figure)          Alendronate): osteoclast apoptosis

              D-BIOL, IMHS                                                                                   01.12.2025   42
                                                                                                    How we know
 From Osteoporosis to Clodronate Liposomes

• A very nerdy link: Clodronate is also a first-gen bisphosphonate which are used to treat osteoporosis.
  Except for osteoclasts which resorbe bisphosphonates while resorbing bones, bisphosphonates are
  membrane-impermeable and as such non-toxic.
• If you pack this in a liposome (which is also not toxic alone) it will be taken up by phagocytes and released
  into the cytosol by lysosomal phospholipase, reaching high concentrations.
• Clodronate -> AppCCl2p (ATP analog) -> mitochondria inhibition -> apoptosis

Osteoporosis drug            Clodronate                   Often-used tool for macrophage depletion
                             Liposomes                    studies

              D-BIOL, IMHS                                                                        01.12.2025   43
Alveolar proteinosis                                                                                          !
• Pulmonary Alveolar proteinosis (PAP) is
  a rare diseease (6-7 per Million)
• >90% autoimmune PAP: Anti-GM-CSF
  auto-Antibodies)
• 5-10% secondary PAP: due to other
  diseases
• 2% genetic with mutations in
  − GM-CSFR mutation of alpha or beta
    subunit (CSF2RA, CSF2RB).
  − Other genes involved with surfactant    Link to Otogeny: should genetic PAP patients be transplanted or
    production and clearance.               not?

                                               https://doi.org/10.1016/j.rmed.2025.108167
             D-BIOL, IMHS                                                                   01.12.2025   44
Anti-Tumor Immunity                                                                                                !
• CD47 is a «don’t eat me» signal
  overexpressed on cancer cells
• Blockade of the CD47-SIRPα signaling
  pathway leads to phagocytosis of tumor cells.
• CD47-SIRPα blockade plus standard
  treatment shows promising efficacy.
• Clinical trials are angoing
• Safety concerns also macrophage related:
  CD47 is highly expressed on red blood cells,
  when you block CD47
  − You remove «don’t eat me» signal on
    RBCs
  − Spleen macrophages sort out old RBCs
    based on CD47 loss
                                                  https://doi.org/10.1016/j.iotech.2022.100070
  − Therefore, in all phase I trials anemia was
    the most common toxicity

              D-BIOL, IMHS                                                                       01.12.2025   45
Atherosclerosis/ Cardiovascular Disease                                                                   !
• Monocyte recruitment after Endothelial
  activation (VCAM-1), monocytes enter the
  intima.
• Differentiation to macrophages. Macrophages
  take up oxidized LDL through phagocytosis,
  pinocytosis, scavenger receptors play an
  important role
• Foam cell formation. The macrophages «over-
  eat», lipid-loaded macrophages accumulate,
  formation of fatty streaks.
• Necrotic core formation. Impaired efferocytosis
  leads to cell death and plaque growth.
• Fibrous cap / instability. The lesion is «walled-
  off» which can lead to stable ischemic
  symptoms, but when the smooth muscle cap
  thins risk of rupture which can lead to sudden
  vascular occlusion
                                                      DOI: 10.1016/j.cell.2011.04.005
             D-BIOL, IMHS                                                               01.12.2025   46
Macrophages play a role in many more diseases                     !

Rule of thumb
• TRMs main players
  during homeostasis
• Mo-Macs main players
  during disease
  pathogenesis.

            D-BIOL, IMHS                        01.12.2025   47
Prof. Dr. Joel Zindel
Assistenzprofessor
joel.zindel@biol.ethz.ch

ETH Zürich
Institut für Molekulare Gesundheitswissenschaften (IMHS), D-BIOL
HPL F32.2
Otto-Stern-Weg 7
3098 Zürich
```

---

<!-- file: slides/02_TissueRepair_Part1.pdf -->

```text
D-BIOL

Tissue Repair Part I:
Injury
Prof. Dr. Joel Zindel
Assistant Professor (TT) for Tissue Repair
April 14th 2026
Notes for this lecture

  !   Central concepts — exam-relevant

      How we know: We look at the experimental data behind central paradigms. These slides are
      epistemologic in nature—how we know what we know—and should not be memorized for the
      exam.

      Nerd factor: Perspective or fun facts (slides with black background are from our own laboratory).
      Not to be committed to memory—although sometimes the most random facts stick best.

      Resources:
      - Zindel & Kubes 2020 Annu Rev Pathol 2020

           D-BIOL, IMHS                                                                      14.04.2026   2
Agenda – Tissue Repair
This agenda organises key concepts by when they are discussed — not as strict biological boundaries.

  LECTURE 1                                     LECTURE 2                                      LECTURE 3                                      LECTURE 4

                                                                                               Granulation
  Injury                                        Inflammation                                                                                  Remodelling
                                                                                               tissue
  seconds – minutes                             min – hours – days                             hours – days – weeks                           days – weeks – months

  • Definitions: homeostasis, injury,                                                          • Model A: Macrophage-fibroblast               • MMP/TIMP balance, collagen I/III
    regeneration, repair, and failure           • Injury detection                               circuits                                     • Myofibroblast resolution
    modes.                                      • macrophage cloaking and                      • Model B: Stem cell compartments              • Fibrosis vs. regeneration
  • The molecular basis of injury and             threshold gating                             • Fundamental repair processes
    injury detection: DAMPs, PAMPs,             • Coagulation and Complement
    and LAMPs.                                  • Thromboinflammation

                 Phases are overlapping and tissue-dependent — complement, macrophages, and adaptive immunity span multiple lectures and are discussed in context.

                                                                                                                                                                      13.04.2026   3
Learning Objectives — Lecture 1: Injury

• Students can define homeostasis, injury, repair, and regeneration, and distinguish the failure modes of
  insufficient repair (leakage/non-healing) and excessive repair (fibrosis/pathological scarring).
• Students can explain the conceptual basis of the danger/damage model — that the innate immune
  system detects molecular patterns rather than antigens, and responds to both foreign (PAMPs) and
  endogenous (DAMPs) danger signals.
• Students can describe the compartmentalisation principle underlying DAMP recognition — the “wrong
  neighbourhood principle” (localisation) and the “wrong shape principle” (conformation/modification) —
  and give one experimental example of each.
• Students can distinguish between cDAMPs and iDAMPs in terms of mechanism of release, cell state, and
  functional consequence, and explain why LAMPs do not fit the strict DAMP definition.
• Students can name representative DAMPs from major molecular categories (nucleic acids, proteins,
  lipids, metabolites) and describe their cognate receptors.

              D-BIOL, IMHS                                                                      13.04.2026   4
Definition: Tissue Homeostasis
                                                                                                       !

                                 Tissue Homeostasis The active maintenance of tissue structure
                                 and function within a defined set point.
                                 • Requires continuous energy input — not a passive
                                   equilibrium.
                                 • Defined by tissue-resident cells (tissue resident
                                   macrophages, fibroblasts, epithelium) sensing and
                                   correcting deviations.
                                 • Parameters maintained: organ function, barrier integrity,
                                   cell number, ECM composition, metabolic state.
                                 • Small deviations are corrected silently and consistently by
                                   local mechanisms (e.g. macrophage efferocytosis) and are
                                   a part of homeostasis.

         D-BIOL, IMHS                                                                 13.04.2026   5
Definition: Injury
                                                                                                           !
                         Tissue injury is a deviation from homeostatic set points that exceeds
                         the capacity of local homeostatic mechanisms to correct. — Medzhitov,
                         Nature 2008 & Cell 2010.
                         •   Causes:
                               •   Physical
                                       •   Trauma: e.g. surgery, accident
                                       •   Radiation (UV, Gamma)
                                       •   Thermal
                                       •   Sterile particulate (crystals, implants, foreign body)
                               •   Biochemical
                                       •   Exogenous toxins: drugs, venoms,
                                       •   Endogenous toxins: autoimmune efforts, enzymes, ROS,
                                           bile acids)
                                       •   Pathogen-driven cell death
                                       •   Deprivation (lack of oxygen, nutrients, growth factors)
                         •   Consequences: — Loss of structural integrity — Loss of tissue
                             function — Loss of homeostatic regulation

          D-BIOL, IMHS                                                                    13.04.2026   6
Definition: Regeneration*
                                                                                                                                              !
                                                         Regeneration is a heroic biological process that restores tissue
                                                         architecture and function in the face of day-to-day cell loss or the
                                                         aftershock of injury. Poss & Tanaka, Cell Stem Cell 2024.

                                                         Characteristics:
                                                         •   Restitutio ad integrum
                                                         •   Restores both function AND original architecture — layer by layer,
                                                             cell type by cell type
                                                         •   Involves morphogenetic programmes — positional identity, tissue
                                                             patterning, size control
                                                         •   Slow — quality prioritised over speed
                                                         •   Rare in adult mammals — default in: gut epithelium, liver (partial),
                                                             haematopoietic system, skin epidermis, mesothelium
                                                         •   Retained in lower vertebrates throughout adult life (zebrafish heart,
                                                             salamander limb)
*Teaching note—Regeneration: In clinical contexts the term regeneration is used to describe any successful healing, but in developmental biology
and regenerative medicine this strict definition is the gold standard.

                  D-BIOL, IMHS                                                                                               13.04.2026   7
Definition: Repair
                                                                                                         !
                         Tissue Repair is the restoration of tissue function and structural
                         continuity following injury, typically resulting in a functional but
                         architecturally imperfect scar. — Gurtner et al., Nature 2008
                         Characteristics:
                         •     Restores function — barrier integrity, mechanical continuity,
                               organ capacity.
                         •     Does not fully restore original architecture — collagen scar
                               replaces original ECM.
                         •     Speed prioritized over perfection — evolutionary design for acute
                               survival.
                         •     Outcome determined by injury type, tissue context, and systemic
                               factors (age, diabetes, nutrition).

          D-BIOL, IMHS                                                                  13.04.2026   8
Failure Modes of Repair
                                                                                                              !
                                   Failure modes of repair — when the repair programme encounters what
                                   it was not designed for
                                   Chronic non-healing wound — repair stalled
                                   •     Inflammatory phase cannot resolve → DAMPs not cleared
                                   •     Impaired macrophage switch
                                   •     Biofilm, ischaemia, neuropathy prevent progression
                                   Fibrosis — repair that never switches off
                                   •     Myofibroblasts persist → excess collagen deposition
                                   •     TGFβ loop not terminated → progressive ECM accumulation
Chronic   Fibrosis        Cancer   •     Macrophage-fibroblast circuit stuck in activation
Wound                              Cancer — uncontrolled proliferation
                                   •     Not strictly a failure mode of repair, but cancer hijacks repair
                                         machinery and has been likened to “wounds that do not heal" —
                                         Dvorak, NEJM 1986

           D-BIOL, IMHS                                                                      13.04.2026   9
Recap: Pattern Recognition

•Innate pattern recognition is germline-encoded — fixed, conserved, present from birth
•Recognises molecular patterns, not specific antigens — no clonal selection, no memory*
•Original paradigm: immune system detects foreignness (non-self) — Burnet & Fenner
•Revised paradigm: immune system detects danger / damage — Matzinger 1994
•PRRs respond to both PAMPs (pathogen-derived) and DAMPs (host-derived) — same machinery
•This is why sterile injury triggers inflammation — no pathogen required
*Nerd factor—Trained Immunity: We now know that innate cells (monocytes, NK cells) can undergo epigenetic reprogramming after exposure to
certain PAMPs (like β-glucan), leading to a "heightened" response to secondary infections. It isn’t "memory" in the V(D)J recombination sense, but it
functions similarly.

                   D-BIOL, IMHS                                                                                                  13.04.2026   10
Recap: Pattern Recognition Receptors (PRR)

                                                 •   Lipopolysaccharide (LPS) is a strong inducer in
                                                     gram-negative sepsis.
                                                 •   (Sultzer 1968) C3H/HeJ mice are resistant to LPS.
                                                 •   C3H/HeN controls, humans, and rats are LPS
                                                     susceptible.
                                                 •   (Beutler et al 1998) Positional cloning identified
                                                     position 712 P -> H (Pro712His) in TLR4 gene.
                                                        •   Proline: LPS-susceptible, very conserved
                                                        •   Histidine: LPS-resistant
   B. Sultzer, Nature 1968, Infect Immun. 1972
                                                 •   TLR4 = the paradigmatic PAMP receptor

 Poltorak, …, Beutler, Science 1998

                  D-BIOL, IMHS                                                                    13.04.2026   11
 Damage Associated Molecular Patterns DAMPS
 The compartmentalization principle
                                                                                                                                                      !

Localization («wrong neighborhood» principle)                                                  Conformation («wrong shape» principle)
                    Nucleus
                                         Cytosol

Mitochondria

                                                                                                                    •   Covalent modifications
                                                                                                                        (Oxidation, Acetylation,
                                                                               Hydrophobic          Polar side          Phosphorylation)
                                                                               core                 chains
                                                                                                                    •   Proteolytic cleavage

                Ubiquitous tool                                                                                     •   Crystallisation
                                                                                                                    •   Protein misfolding/
                                                                                               Hydrophobic              Aggregation
                                                                                               chains exposed

                Danger signal

                D-BIOL, IMHS   www.britannica.com, Molecular Biology of the Cell, Chapter 3.                                        13.04.2026   12
cDAMPs and iDAMPs
                                                                                                    •    (a) Injury => release of constitutively expressed DAMPS
                                                                                                         (cDAMPs)
                                                                                                    •    (b) Proposition of lifestyle associated molecular patterns
                                                                                                         (LAMPs) as alternative initiation event see teaching
                                                                                                         comment next slide
                                                                                                    •    (c) Immunostimulatory patterns are recognized by PRRs
                                                                                                         on both nonimmune cells and specialized immune
                                                                                                         sentinels. Ligation of PRRs leads to the secretion of
                                                                                                         proinflammatory cytokines (e.g., TNF-α and IL-1) as well
                                                                                                         as other inflammatory mediators.
                                                                                                    •    (d) Proinflammatory signals, such as IL-1 and TNF-α,
                                                                                                         induce programmed nonapoptotic cell death in
                                                                                                         parenchymal cells (necroptosis) as well as in leukocytes
                                                                                                         (referred to as pyroptosis, or NETosis in neutrophils).
                                                                                                         This leads to the induction and active (noncanonical)
                                                                                                         secretion of inducible DAMPs (iDAMPs).
Adapted from Zindel & Kubes 2020 Annu Rev Pathol 2020

                                                        Abbreviations: CIRBP, cold-inducible RNA binding protein; CPPD, calcium pyrophosphate dihydrate; HSP,
                                                        heat shock protein; HMGB1, high mobility group box 1; IL, interleukin; MSU, monosodium urate; mtDNA, mitochondrial DNA; NET,
                                                        neutrophil extracellular trap; PRR, pattern recognition receptor; TNF, tumor necrosis factor.
                    D-BIOL, IMHS                                                                                                                            13.04.2026     13
              Universal Building Plan

Body cavity

                                  Mesothelium ~ Serosa ~
                                  Peritoneum
                  Slippery Surface

                                     Mesothelium ~ Serosa ~
                                     Peritoneum
Anti-Podoplanin       500u
                      m
A Look Inside

                Fair Warning
                    Failure modes

                   Regeneration         Scar (Adhesion)
Leakage              «just right»           «too much
                                            repair»
«Not enough
repair»

                     Repair Spectrum

$$ Health Burden                       $$ Health Burden
Macrophage Activation

                        Injury
    Example «wrong neighborhood»: ATP as cDAMP and iDAMP (II)

cDAMP

        Wang and Kubes, Cell 2016 Figure S2
                                                    Wang and Kubes, Cell 2016 Figure 3

                                                          •   (Fig. S2 C and D) Peritoneal macrophages
                                                              (F4/80hi CD11b+ cells) are recruited to injuries.
                                                          •   (Fig 3 B) This recruitment can be inhibited with
                                                              Apyrase and ATP-receptor antagonists.
iDAMP
                                                          •   (Fig 1) Calcium signaling can be induced in
                                                              macrophages in culture using photo-uncaging of
                                                              caged IP3 (white box in A and B, red curve in C
                                                              and D). This induces a Calcium wave in the
                                                              neighboring cells (black curves in C and D) in an
                                                              ATP-dependent manner.
        Zumerle et al. Cell Reports 2019 Figure 1

                     D-BIOL, IMHS                                                              13.04.2026   19
Calcium signaling

                                                Green: GCaMP6f (Ca2+ wave)

   GCaMP: Calmodulin GFP Fusion Protein

                                                           Injur
                                                             y
                                          Red: F4/80 Macrophages, Blue: SHG Collagen

           D-BIOL, IMHS                                                                13.04.2026   20
Example «wrong shape»: Hyaluronan

                                          •   Hyaluronan (HA), a ubiquitously distributed ECM
                                              component, is broken down into lower m.w. fragments
                                              (LMW HA) upon injury.
                                          •   LMW HA activates innate immune response (MIP-1α =
                                              CCL3 = pro-inflammatory chemoattractant).
                                          •   (a and b) Peritoneal Excudate Cells (PEC) from LPS-
                                              insensitive (TLR4-/-) mice* show pro-inflammatory
                                              response to LMW HA but not to uncleaved HA.
                                          •   (c) The response in wild-type dendritic cells (from C57Bl/6
                                              mice) to LMW HA is substantial, almost as high as LPS.
                                          •   (d and e) The response does not depend on TLR4 (d) and
                                              does not depend on CD44 (e).
                                          •   In the other figures they show that LMW HA activates the
                                              innate immune response via TLR-2 in a MyD88 NF-κB-
                                              dependent pathway

                                          *role of TLR4 contested for different HA fragment sizes
     Scheibner et al., J. Immunol. 2006
            D-BIOL, IMHS                                                                 13.04.2026   21
Example: Lifestyle Associated Molecular Patterns LAMPs

Polymers                               Ceramics           Metals

                 These materials were not present during evolution
    DAMPS Overview (I)
 Molecular pattern                                Receptor                             Physiological purpose                     Role in disease / treatment
                                                                                                                                                                                                            !
 Intracellular DAMPs (cDAMPs)

  Nucleus
 Double-stranded DNA                              TLR9, AIM2, cGAS → STING             Damage surveillance                       TLR antagonists, DNases; STING inhibitors (clinical trials)

 HMGB1                                            TLR2, TLR4, TLR9, RAGE, CD24         Damage surveillance                       Neutralising antibodies, TLR4 antagonists

 Histones                                         TLR2, TLR4                           Damage surveillance                       TLR antagonists; role in sepsis-DIC

 SAP130                                           CLEC4E (Mincle)                      Damage surveillance                       —

 Self RNA (mRNA, miRNA, Z-RNA)                    MDA5, RIG-I, ZBP1, TLR7, TLR8        Shielded from immune recognition under    Aicardi-Goutières syndrome (ADAR1 deficiency); neurodegeneration;
                                                                                       homeostasis by RNA-binding proteins and   tumour progression
                                                                                       modification

  Mitochondria
 Mitochondrial DNA (mtDNA)                        TLR9, NLRP3, cGAS → STING            Damage surveillance                       TLR antagonists, DNases; STING inhibitors; monocyte tolerance in MI

 Mitochondrial N-formyl peptides                  FPR1                                 DAMP gradient, necrotaxis                 Antibodies, honokiol

 Cytochrome c                                     Unknown                              Damage signal                             Potential marker; γ-tocotrienol

 Cardiolipin                                      NLRP3                                Mitochondrial membrane integrity signal   Barth syndrome; cancer; obesity; Alzheimer's disease

  Cytosol
 ATP                                              P2 receptors (P2X7, P2Y)             Damage surveillance, DAMP gradient        P2X receptor inhibitors

 S100 calcium-binding proteins                    RAGE                                 Secondary messenger                       Antibodies

 K⁺ ions                                          K⁺ channels → NLRP3                  Secondary messenger                       Inflammasome activation

 CIRBP                                            TLR4–MD2 complex                     Stress signal                             Inflammatory response in shock and sepsis

 Thioredoxin                                      Many                                 Redox signal                              Cancer, viral diseases, aging

Adapted from Zindel & Kubes 2020 Annu Rev Pathol 2020. Abbreviations: cDAMP, constitutively expressed DAMP; iDAMP, inducible DAMP; HMGB1, high-mobility group box-1; CIRBP, cold-inducible
RNA-binding protein; cGAS, cyclic GMP-AMP synthase; STING, stimulator of interferon genes; FPR1, formyl peptide receptor 1; ECM, extracellular matrix; SHAP, serum-derived hyaluronan-associated
protein; ARDS, acute respiratory distress syndrome; FPP, farnesyl pyrophosphate; GGPP, geranylgeranyl pyrophosphate; SR-A, scavenger receptor A; TCA, tricarboxylic acid cycle; LAMP, lifestyle-
associated molecular pattern.
                                   D-BIOL, IMHS                                                                                                                                          13.04.2026    23
  DAMPS Overview (II)
                                                                                                                                                                                                   !
 Molecular pattern                          Receptor                                   Physiological purpose                   Role in disease / treatment

 Inducible DAMPs (iDAMPs) — secreted upon stress

 Heat shock proteins (hsp60, hsp70,         TLR2, TLR4, CD91, CD14, CD40, CD24         Signal amplification, DAMP gradient     Antibodies; anti-cancer immune response
 hsp90, gp96, calreticulin)

 Defensins                                  CCR6, TLR4                                 DAMP gradient                           Antagonists, antibodies

 Galectins                                  CD2                                        Signal amplification                    Cancer, fibrosis, chronic inflammation

 IL-1α                                      IL-1R                                      Feedforward amplification               Sepsis; anakinra

 Lysophosphatidylserine (LysoPS)            GPR34                                      Released by apoptotic cells —           Colitis; skin wound repair
                                                                                       promotes tissue repair
 Extracellular DAMPs — matrix-derived

 Short-fragment hyaluronan                  CD44–TLR4–MD2, TLR2                        Damage surveillance, DAMP gradient      TLR antagonists, hyaluronidase

 Biglycan                                   TLR2, TLR4                                 Damage surveillance                     —

 Versican                                   TLR2                                       Damage surveillance                     Enhances tumour metastasis

 Heparan sulfate                            TLR4                                       Damage surveillance                     Alzheimer's disease

 ECM fragments / matricryptins              CD14, TLR4, SHAP                           Damage surveillance, DAMP gradient      Autoimmune diseases; potential anti-tumour properties
 (collagen, elastin, laminin)

Adapted from Zindel & Kubes 2020 Annu Rev Pathol 2020. Abbreviations: cDAMP, constitutively expressed DAMP; iDAMP, inducible DAMP; HMGB1, high-mobility group box-1; CIRBP, cold-inducible
RNA-binding protein; cGAS, cyclic GMP-AMP synthase; STING, stimulator of interferon genes; FPR1, formyl peptide receptor 1; ECM, extracellular matrix; SHAP, serum-derived hyaluronan-associated
protein; ARDS, acute respiratory distress syndrome; FPP, farnesyl pyrophosphate; GGPP, geranylgeranyl pyrophosphate; SR-A, scavenger receptor A; TCA, tricarboxylic acid cycle; LAMP, lifestyle-
associated molecular pattern.

                             D-BIOL, IMHS                                                                                                                                    13.04.2026     24
    DAMPS Overview (III)                                                                                                                                                                                             !
Molecular pattern                               Receptor                                       Physiological purpose                       Role in disease / treatment

Inter-organ DAMPs

DAMPs from distal tissues / organs (e.g.        Same PRRs as local DAMPs (TLR9, RAGE,          Trans-organ danger broadcast —              Multi-organ failure, remote ischaemic injury, ARDS after
circulating mtDNA, HMGB1)                       TLR4)                                          physiological purpose debated               pancreatitis; therapeutic window being defined

Endogenous LAMPs — accumulate with lifestyle / metabolic disease

Cholesterol crystals                            NLRP3, CD36                                    Unclear                                     Atherosclerosis, cardiovascular disease

Uric acid / monosodium urate crystals           NLRP3                                          May physiologically act as a cDAMP          Gout; colchicine, IL-1 blockade (anakinra, canakinumab)

Calcium pyrophosphate dihydrate                 NLRP3                                          Unclear                                     Pseudogout
crystals
Oxidized lipoproteins (oxLDL)                   TLR, SR-A, CD36, active component oxPAPC       Unclear                                     Atherosclerosis; statins
                                                activates non-canonical NLRP3 via CD14
Prions / prion-like signals (e.g. β-            NLRP3, CD36, RAGE, NF-κB (extracellular)       Physiological iDAMP?                        Alzheimer's disease, Creutzfeldt-Jakob disease
amyloid)
Metabolite-derived DAMPs: FPP, GGPP             NLRP3, mTOR / HIF-1α axis                      Unclear — possibly metabolic stress         Inflammaging, trained immunity, atherosclerosis; statins (block
(mevalonate pathway); succinate,                                                               sensing; may drive trained immunity         FPP/GGPP), mTOR inhibitors, LPS-induced lung injury, airway
fumarate, citrate (TCA cycle), UPD-                                                                                                        inflammation, sepsis.
glucose
Exogenous LAMPs — environmental / iatrogenic exposures

Silica particles, asbestos particles            NLRP3                                          None (no evolutionary design)               Frustrated phagocytosis, granuloma, silicosis, asbestosis

Biomaterials / implants                         Plasma proteins → complement receptors,        None (no evolutionary design)               Foreign-body reaction, fibrous capsule; biomaterial surface
                                                TLR                                                                                        engineering

Teaching note — LAMP: The term 'LAMP' was proposed in Zindel & Kubes 2020 to distinguish molecules that accumulate due to modern lifestyle or iatrogenic exposure from classical DAMPs released by acute cell
death. The key distinction: LAMPs cannot be cleared, so they drive chronic sterile inflammation. The term has been cited in ~15–20 papers (Exp Mol Med 2025; Front Immunol 2021) but is NOT yet standard
nomenclature. Students should understand the concept — not memorise the acronym as settled fact. This is a live example of how scientific vocabulary is proposed and debated.

Teaching note — Inter-organ DAMPs: The concept that circulating DAMPs from a distal organ can drive sterile inflammation elsewhere is well-supported (Zhou et al. 2024) but the physiological purpose remains
debated. Is this an evolved systemic alarm, or pathological spillover?

                                 D-BIOL, IMHS                                                                                                                                                13.04.2026         25
Learning Objectives — Lecture 1: Injury

• Students can define homeostasis, injury, repair, and regeneration, and distinguish the failure modes of
  insufficient repair (leakage/non-healing) and excessive repair (fibrosis/pathological scarring).
• Students can explain the conceptual basis of the danger/damage model — that the innate immune
  system detects molecular patterns rather than antigens, and responds to both foreign (PAMPs) and
  endogenous (DAMPs) danger signals.
• Students can describe the compartmentalisation principle underlying DAMP recognition — the “wrong
  neighbourhood principle” (localisation) and the “wrong shape principle” (conformation/modification) —
  and give one experimental example of each.
• Students can distinguish between cDAMPs and iDAMPs in terms of mechanism of release, cell state, and
  functional consequence, and explain why LAMPs do not fit the strict DAMP definition.
• Students can name representative DAMPs from major molecular categories (nucleic acids, proteins,
  lipids, metabolites) and describe their cognate receptors.

              D-BIOL, IMHS                                                                      13.04.2026   26
Prof. Dr. Joel Zindel
Assistenzprofessor
Joel.zindel@biol.ethz.ch

ETH Zürich
Institut für Molekulare Gesundheitswissenschaften (IMHS), D-BIOL
HPL F32.2
Otto-Stern-Weg 7
8098 Zürich
```

---

<!-- file: slides/03_TissueRepair_Part2.pdf -->

```text
D-BIOL

Tissue Repair Part II

Prof. Dr. Joel Zindel
Assistant Professor (TT) for Tissue Repair
April 14th 2026
Notes for this lecture

  !   Central concepts — exam-relevant

      How we know: We look at the experimental data behind central paradigms. These slides are
      epistemologic in nature—how we know what we know—and should not be memorized for the
      exam.

      Nerd factor: Historical or medical perspective or fun facts (slides with black background are from
      our own laboratory). Not to be committed to memory—although sometimes the most random
      facts stick best.

           D-BIOL, IMHS                                                                       14.04.2026   2
Agenda – Tissue Repair
This agenda organises key concepts by when they are discussed — not as strict biological boundaries.

  LECTURE 1                                     LECTURE 2                                      LECTURE 3                                      LECTURE 4

                                                                                               Granulation
  Injury                                        Inflammation                                                                                  Remodelling
                                                                                               tissue
  seconds – minutes                             min – hours – days                             hours – days – weeks                           days – weeks – months

  • Definitions: homeostasis, injury,                                                          • Model A: Macrophage-fibroblast               • MMP/TIMP balance, collagen I/III
    regeneration, repair, and failure           • Injury detection                               circuits                                     • Myofibroblast resolution
    modes.                                      • macrophage cloaking and                      • Model B: Stem cell compartments              • Fibrosis vs. regeneration
  • The molecular basis of injury and             threshold gating                             • Fundamental repair processes
    injury detection: DAMPs, PAMPs,             • Coagulation and Complement
    and LAMPs.                                  • Thromboinflammation

                 Phases are overlapping and tissue-dependent — complement, macrophages, and adaptive immunity span multiple lectures and are discussed in context.

                                                                                                                                                                      13.04.2026   3
Learning Objectives — Lecture 2: Inflammation

• Students can explain why tissue-resident macrophages are the primary sensors of sterile injury DAMPs
  — and why other tissue-resident immune cells (e.g. adaptive TRICs, NK/iNKT, ILCs, mast cells) are not,
  using the concepts of PRR repertoire breadth and network architecture.
• Students can describe the concept of macrophage cloaking as an operational definition of threshold
  gating — explain the experimental evidence from intravital microscopy, and articulate why the molecular
  basis of the threshold remains incompletely defined.
• Students can explain how the coagulation and complement cascades each function as DAMP detection
  systems — identifying the specific DAMP trigger for each pathway and explaining why this qualifies as
  DAMP logic.
• Students can distinguish between immunothrombosis and thromboinflammation — define each term,
  explain how coagulation, complement and cellular innate immunity converge into one integrated
  intravascular defense, and give examples of physiological output and failure modes.
• Students can explain why resolution of inflammation is active and programmed rather than passive
  decay.

              D-BIOL, IMHS                                                                      13.04.2026   4
Recap: DAMPs                                                                                                        !
                                                        •   Sensing: Immunostimulatory patterns are
                                                            recognized by PRRs on both nonimmune cells
                                                            and specialized immune sentinels. Ligation of
                                                            PRRs leads to the secretion of proinflammatory
                                                            cytokines (e.g., TNF-α and IL-1) as well as other
                                                            inflammatory mediators.

Adapted from Zindel & Kubes 2020 Annu Rev Pathol 2020

                    D-BIOL, IMHS                                                                13.04.2026      5
  Who detects DAMPs? A systematic look at tissue resident immune cells.                                          !
                                                     No DAMP sensors by design:
                                                     • T-cell (TRM), B-cell (BRM): adaptive immunity
                                                     • NK, iNKT, tr-γδT: killers, not sensors; limited PRR
                                                       repertoire
                                                     • ILC: cytokine responders, not primary PRR-expressors
                                                     Partial DAMP sensors — context-dependent:
                                                     • MAIT: narrow DAMP PRR repertoire, can be activated
                                                       TCR-independent, important for repair downstream of
                                                       macrophages
                                                     • mast cell: narrow DAMP PRR repertoire, mostly
                                                       excellent barrier alarm, FcεRI/complement-dominant;
                                                     Best sensors: Tissue Resident Macrophages (TRM)
                                                     • Gap-less, body-wide network
                                                     • Broadest PRR repertoire (TLRs, NLRP3, cGAS-STING,
Li et al. Signal Transduction and Targeted Therapy     scavenger receptors)
                                                     • First responder in all sterile injury IVM models

                        D-BIOL, IMHS                                                            13.04.2026   6
Recap: Efferocytosis                                                                                                            !
                                                             •   Daily, billions of cells die in the tissue by undergoing
                                                                 apoptosis, yet apoptotic cells are rarely observed in
                                                                 homeostasis.
                                                             •   Efferocytosis that efficiently clears apoptotic cells
                                                                 without causing inflammation.
                                                             •   Efferocytosis is a well-defined molecular event:
                                                                 − Healthy cells express CD47, a «don’t eat me
                                                                   signal» recognized by SIRP1α on phagocytes
                                                                 − Apoptotic cells express «eat me signals» the
                                                                   most important is Phosphatidylserine (PS)
                                                                   which is recognized by TIM4 and many others
                                                                   (Figure)
                                                             •   The process is anti-inflammatory characterized by
                                                                 the release of TGFb, IL-10, PGE2 and the inhibition
                                                                 of inflammatory cytokines such as TNF, IL1b, IL6

Injury and Efferocytosis both involve cell death and macrophages — yet one is silent and the other triggers
full inflammation. What sets the threshold?

             D-BIOL, IMHS                                                                                      14.04.2026   7
  The threshold question

Uderhardt et al. Cell 2019 (Figure 3)
• Neutrophil swarming as operational readout of threshold breach — all-or-nothing
• (A) Tissue Resident Macrophages (TRMs) cloak microlesions within minutes via pseudopod extension — without moving their
  cell body. +DT = diphtheriae toxin depletion of macrophages.
• Cloaking is sequentially DAMP-driven: ATP (sensing) → RAGE ligands (convergence)
• Threshold is lesion-size and TRM-density dependent — not a fixed molecular switch
• (B) Failure of cloaking → collateral neutrophil damage → secondary monocyte containment
• molecular basis of the threshold remains incompletely defined — an open and fundamental question
                   D-BIOL, IMHS                                                                             13.04.2026   8
 The threshold question

(Movies, content in previous slide explained or check out here!

 Uderhardt et al. Cell 2019

                       D-BIOL, IMHS                               13.04.2026   9
Transendothelial leukocyte recruitment to sterile injuries                                                                               !
                                                                                      •   Cloaking failure → threshold breached
                                                                                      •   Sentinel-derived TNF/IL-1 endothelial
                                                                                          activation: E/P-selectin upregulation, ICAM-
                                                                                          1/VCAM-1 expression → chemokine
                                                                                          presentation (CXCL1/2)
                                                                                      •   Neutrophils first: transendothelial migration
                                                                                          (same cascade as classical immunology)
                                                                                      •   In the tissue: neutrophils follow the DAMP
                                                                                          gradients (P2R, TLR9, A3R, LTB4R) → reach
                                                                                          injury site
                                                                                      •   First neutrophils undergo inflammatory cell
                                                                                          death (e.g. NETosis) → iDAMP release (ATP,
       *                                                                                  granule proteins) → feedforward amplification
                                                                                          of swarming
                                                                                      •   Monocytes second wave: CCR2hi/CX3CR1lo
                                                                                          recruited via CCL2 → will convert to
                                                                                          macrophages (discussed next lecture)
                                                                                      •   This figure is simplified — additional cells
                                                 Adapted from Zindel & Kubes              (mast cell degranulation, NK, ILC) contribute
                                                 2020 Annu Rev Pathol 2020                but are not shown.

           *Nerd factor—Perivascular mast cells: degranulation/TNF to activate endothelium and provide
                                                                                                                      13.04.2026   10
           perivascular DAMP relay: bridging of tissue alarm to vascular activation.
                      Unconventional immune cell recruitment
Canonical Immune cell migration     Peritoneal Macrophages migrate like
                                    platelets

           Damage     LyzM-GFP
           Collagen
     The coagulation pathway is a DAMP detection system                                               !
                                                       • Coagulation is constitutively pre-
                                                         positioned — activates within seconds,
DAMPs: Exposed collagen, DNA,                            parallel to cellular response
polyphosphates.                                        • Extrinsic pathway trigger = DAMP by
                                                         compartmentalization — TF normally
                                                         hidden behind intact endothelium on
                                                         subendothelial fibroblasts/pericytes;
                                                       • Intrinsic/contact pathway trigger =
                                  DAMP: TF               cDAMPs directly — FXII activated by
                                  compartimentalized     exposed collagen, extracellular DNA,
                                                         polyphosphates from necrotic cells
                                                       • Downstream link to inflammation

                                                                                    13.04.2026   12
Inflammation → Coagulation                                                                                 !
                                                               •   Proinflammatory cytokines (IL-6, TNF-
                                                                   α) → TF upregulation on monocytes and
                                                                   microparticles from activated
                                                                   platelets/endothelium → TF:FVIIa →
                                                                   thrombin → fibrin (shown in mice,
                                                                   chimpanzees, and humans)
                                                               •   Simultaneously, natural anticoagulants
                                                                   are downregulated: TNF-α reduces TFPI,
                                                                   APC, antithrombin → coagulation is no
                                                                   longer counterbalanced
                                                               •   Fibrinolysis is suppressed: TNF-α/IL-
                                                                   1β → ↑PAI-1, ↓tPA production by
                                                                   endothelial cells → fibrin persists
                                                               •   Net result: massive procoagulant shift
                                                                   — more fibrin generated, less inhibited,
                                                                   less cleared

                 Choi et al, SWISS MED WKLY 2006;136:139–144
Coagulation → Inflammation                                                                                     !
                                                             •   Coagulation proteases activate protease-
                                                                 activated receptors (PAR-1 to -4) on
                                                                 mononuclear cells, endothelium, and others
                                                                 — translating coagulation signals into
                                                                 inflammatory output
                                                             •   Thrombin → PAR-1 (best described): ↑IL-6,
                                                                 IL-8, MCP-1; NF-κB-dependent upregulation
                                                                 of adhesion molecules → leukocyte adhesion
                                                             •   FXa/TF-FVIIa complex → PAR-2: pro-
                                                                 inflammatory effects in macrophages,
                                                                 neutrophil infiltration, ↑TNF-α and IL-1β
                                                             •   Fibrin(ogen) and fibrin degradation products
                                                                 activate macrophages via TLR4. Molecular
                                                                 mechanism not fully resolved (Smiley et al. J
                                                                 Immunol 2001)
               Choi et al, SWISS MED WKLY 2006;136:139–144   •   Creates a self-amplifying feedforward loop:
                                                                 inflammation drives coagulation drives
                                                                 inflammation
       The complement system: a DAMP detection and amplification system                                                            !
                                                                •   Complement is constitutively expressed in plasma,
                                                                    activates within seconds, parallel to coagulation and cellular
                                                                    response.
Apoptotic cells,         Aberrant              Necrotic cells
DNA, PS                  Glycocalyx                             •   Three pathways, all detect DAMPs — via different logic:
                                                                    •     Classical pathway: C1q is a soluble PRR — directly
                                                                          binds apoptotic cells, exposed DNA and
                                                                          phosphatidylserine (PS) on damaged cells,
                                                                          independently of antibody (Nauta et al. Eur J Immunol
                                                                          2002; Navratil et al. J Immunol 2001)
                                                                    •     Lectin pathway: MBL and ficolins recognize aberrant
                                                                          glycocalyx patterns on necrotic and apoptotic cells in
                                                                          addition to microbial surfaces (Nauta et al. Eur J
                                                                          Immunol 2003)
                                                                    •     Alternative pathway: healthy cells constitutively
                                                                          express CD55, CD59, CD46 → suppress C3 tick-over.
                                                                          Necrotic cells lose these regulators → complement
                                                                          proceeds unopposed → missing inhibitory signal =
                                                                          DAMP logic (Elward & Gasque J Biol Chem 2005)

       Trouw et al. Nature reviews rheumatology, 2017           •   All three pathways converge at C3 → link to inflammation

                           D-BIOL, IMHS                                                                          13.04.2026   15
   Thromboinflammation*: convergence of three parallel systems                                                                                  !
      Also: sterile
      injury                                                                        •   Thromboinflammation* = convergence of coagulation,
                                                                                        complement and cellular immunity into one integrated
                                                                                        process.
                                                                    Also: sterile •     Trigger-agnostic machinery — whether initiated by
                                                                    injury              PAMPs or DAMPs, the molecular pathways are identical
                                                                                    •   Monocytes → PRR activation → TF decryption → extrinsic
                                                                                        pathway (path a) + NLRP3 → IL-1β/IL-18 (path b)
                                                                                    •   Neutrophils → NETs → FXII activation (path c) → contact
                                                                                        pathway; NETs bind VWF → platelet recruitment (path d);
                                                                                        NE/MPO cleave TFPI/thrombomodulin → anticoagulant
                                                                                        brake removed (path e)
                                                                                    •   Platelets (Thrombocytes) → activated by C3a/C5a (path f)
                                                                                        → release PEVs, polyphosphates → feedforward (path g)
                                                                                    •   Physiological output fibrin-immune cell scaffold
                                                                                        •      pathogen/debris isolation and killing
                                                                                        •      Required for repair!
Bonaventura et al., Nat Rev Immunol 2021
*Terminology note: Immunothrombosis (Engelmann & Massberg 2013) = the               •   Failure modes:
physiological process — thrombosis as an active tool of innate immunity.
                                                                                        •      Disseminated intravascular coagulation, e.g. COVID-
Thromboinflammation = the pathological deviation when immunothrombosis
                                                                                               19 coagulopathy
becomes uncontrolled. This slide shows both: the physiological machinery (figure)
and its failure mode (red bullet).                                                      •      Aberrant repair

                      D-BIOL, IMHS                                                                                            13.04.2026   16
                        Thromboinflammation in the peritoneal cavity

Neutrophils (turbidity)                    Cytokines     Macrophages, Fibrin, and later more
                                                         immune cells

                  www.springermedizin.de

                                                       Vega Perez et al Immunity 2021
                             Thromboinflammation in the peritoneal cavity

                                                   Fibrin

                    Injury

                      Thromboinflammation:
                       Fibrin + Immune cells

Hellebrekers 2011
Fibrin Deposition and Scar Formation

                                  Definition Adhesion/
                                  Maladaptive fibrotic
                                  scarring: Irreversible
                                  fibrotic scar tissue that
                                  connects two surfaces of
                                  the body that are usually
                                  separate.

Hellebrekers 2011
                 Adhesions are a massive clinical problem

                                                                          #1 Cause of bowel obstruction

                                                                          #1 Cause of infertility

                                                                          3.8%      Re-Operations

                                                                                    Re-Admissions
                                                                          10%
                                                                                   More expensive than
                                                                          CHF      gastric or rectal cancer

                                                                          No cure

Zwicky 2021, Menzies 1990, Beck 2000, Barmparas 2010, Ellis 1999, Sulaiman 2001                         20
  Lipid mediator class switch: Discovery of resolvins

                                            •   What does the body actually produce during
                                                resolution? — used unbiased lipidomics of resolving
                                                exudates
                                            •   (left panel) During the resolution phase, aspirin-
                                                treated mice convert DHA (omega-3) → novel
                                                compounds: 17R-HDHA and its derivatives
                                                (dominant peak in chromatogram)
                                            •   These compounds were named resolvins —
                                                resolution phase interaction products
                                            •   (right panel) Resolvins suppress pro-inflammatory
Serhan CN et al. JEM 2002
                                                cytokine production (IL-1β) at picomolar
                                                concentrations — IC50 ~50 pM.
                                            •   Key conceptual insight: aspirin reprograms COX-2
                                                — same enzyme, same substrate (DHA), but
                                                acetylation switches the product from pro-
                                                inflammatory 13-HDHA → pro-resolving 17R-HDHA
                                            •   Resolution is therefore not passive decay — it is
                                                actively switched on by a new biosynthetic program

                            D-BIOL, IMHS                                                   13.04.2026   21
Resolution of Inflammation is active and programmed                                                                                                                                         !
                          Onset                                               Resolution                                                     Failure modes

                   Minutes → hours                                              Hours → days                                                      If unresolved

 Pro-inflammatory signals                            Lipid mediator class switch                                                  Chronic inflammation
 Cytokines, chemokines                               PGE₂/LTB₄ → lipoxins, resolvins, protectins (SPMs)                           Resolution failure

 Cell adhesion molecules                             NF-κB / TLR signalling off                                                   Fibrosis
 E/P-selectin, ICAM-1                                Pro-inflammatory mRNA destabilized (TTP, ZC3H12A)                            Excess fibrin/collagen deposition

 Neutrophil recruitment                              Neutrophil clearance                                                         Adhesions
 Swarming, NETosis                                   Apoptosis + efferocytosis by macrophages                                     Maladaptive fibrotic scar — next slides

 Anti-inflammatory brakes                            Reverse migration                                                            Thromboinflammation
 IL-10, TGF-β, cortisol                              Neutrophils re-enter circulation → lung (transient) → bone marrow →          DIC, MI, ARDS, COVID-19
                                                     apoptosis

 Immunothrombosis
 Fibrin-immune cell scaffold — required for repair   Macrophage reprogramming
                                                     Inflammatory → repair/efferocytic phenotype (→ Lecture 3)

                                                     Fibrinolysis
                                                     moC/LPM-mediated — provisional scaffold removed

                                                                                                                           Adapted from Fullerton & Gilroy, Nat Rev Drug Discov 2016

                          D-BIOL, IMHS                                                                                                                                13.04.2026       22
Learning Objectives — Lecture 2: Inflammation

• Students can explain why tissue-resident macrophages are the primary sensors of sterile injury DAMPs
  — and why other tissue-resident immune cells (e.g. adaptive TRICs, NK/iNKT, ILCs, mast cells) are not,
  using the concepts of PRR repertoire breadth and network architecture.
• Students can describe the concept of macrophage cloaking as an operational definition of threshold
  gating — explain the experimental evidence from intravital microscopy, and articulate why the molecular
  basis of the threshold remains incompletely defined.
• Students can explain how the coagulation and complement cascades each function as DAMP detection
  systems — identifying the specific DAMP trigger for each pathway and explaining why this qualifies as
  DAMP logic.
• Students can distinguish between immunothrombosis and thromboinflammation — define each term,
  explain how coagulation, complement and cellular innate immunity converge into one integrated
  intravascular defense, and give examples of physiological output and failure modes.
• Students can explain why resolution of inflammation is active and programmed rather than passive
  decay.

              D-BIOL, IMHS                                                                      13.04.2026   23
Prof. Dr. Joel Zindel
Assistenzprofessor
Joel.zindel@biol.ethz.ch

ETH Zürich
Institut für Molekulare Gesundheitswissenschaften (IMHS), D-BIOL
HPL F32.2
Otto-Stern-Weg 7
8098 Zürich
```

---

<!-- file: slides/04_TissueRepair_Part3_GranulationTissue.pdf -->

```text
D-BIOL

Tissue Repair Part III

Prof. Dr. Joel Zindel
Assistant Professor (TT) for Tissue Repair
April 20th 2026
Notes for this lecture

  !   Central concepts — exam-relevant

      How we know: We look at the experimental data behind central paradigms. These slides are
      epistemologic in nature—how we know what we know—and should not be memorized for the
      exam.

      Nerd factor: Historical or medical perspective or fun. Not to be committed to memory—although
      sometimes the most random facts stick best.

      Resources: Robbins Basic Pathology, Tenth Edition, Chapter TISSUE REPAIR

      Disclaimer on Generalizability: The molecular and cellular paradigms described herein (e.g., the iNKT-
      mediated macrophage switch and the CSF1-PDGF circuit) represent high-fidelity models of tissue repair.
      While these 'logic gates' appear conserved across vertebrates, much of the foundational experimental data is
      derived from specific injury models (predominantly liver and skin). Application to other organ systems should
      account for tissue-specific niche factors and varying immune cell ontogenies.

            D-BIOL, IMHS, Zindel                                                                         20.04.2026   2
Agenda – Tissue Repair
This agenda organises key concepts by when they are discussed — not as strict biological boundaries.

  LECTURE 1                                       LECTURE 2                                    LECTURE 3                                      LECTURE 4

                                                                                               Granulation
  Injury                                          Inflammation                                                                                Remodelling
                                                                                               tissue
  seconds – minutes                               min – hours – days                           hours – days – weeks                           days – weeks – months

  • Definitions: homeostasis, injury,                                                          • The macrophage switch:                       • MMP/TIMP balance, collagen I/III
    regeneration, repair, and failure             • Injury detection                             macrophages subtypes in repair               • Myofibroblast resolution
    modes.                                        • macrophage cloaking and                    • Macrophage-fibroblast circuit                • Fibrosis vs. regeneration
  • The molecular basis of injury and               threshold gating                           • Provisional Matrix
    injury detection: DAMPs, PAMPs,               • Coagulation and Complement                 • Angiogenesis
    and LAMPs.                                    • Thromboinflammation                        • Neural regulation of repair
                                                                                               • Collagen III
                                                                                               • Failure modes

                 Phases are overlapping and tissue-dependent — complement, macrophages, and adaptive immunity span multiple lectures and are discussed in context.

                           D-BIOL, IMHS, Zindel                                                                                                                       20.04.2026   3
Learning Objectives — Lecture 3: Granulation Tissue

• Students can describe the macrophage-fibroblast two-cell circuit — key signals, three stable states,
  separatrix — and explain why injury requires circuit reconstruction from scratch.
• Students can explain the monocyte-to-macrophage class switch, clarify that CX3CR1 is a maturation not
  a polarisation marker, and describe the iNKT/CD1d/IL-4 mechanism with its tissue-specific
  generalisations.
• Students can distinguish Folr2+ repair macrophages from Trem2+/Spp1+ scar-associated
  macrophages by phagocytic cargo, signature, and tissue outcome.
• Students can define the myofibroblast as a phenotype, describe αSMA stress fibre formation, name two
  precursor sources including MMT, and explain the mechanical positive feedback loop driving persistence.
• Students can compare the chemical and mechanical views of myofibroblast activation — driver,
  persistence mechanism, therapeutic target, weakness — and state the synthesis.
• Students can distinguish Model A (functional repair) from Model B (regeneration) in terms of speed,
  fidelity, and cellular requirements

              D-BIOL, IMHS, Zindel                                                              20.04.2026   4
   Recap: Phases of Repair                                              !

Lecture 1 and 2
                                         Lecture 3
                                                     Lecture 4

                  D-BIOL, IMHS, Zindel                 20.04.2026   5
    Model: Macrophage Fibroblast Circuits                                                                                  !

                                                             Teaching Note-link to Prof. Werner lecture: this is
Severe Injury   https://doi.org/10.1016/j.cell.2018.01.015
                                                             a classical double paracrine loop
                D-BIOL, IMHS, Zindel                                                                      20.04.2026   6
             Macrophage Switch: the phenomenon

             Focal liver injury
CCR2-RFP
CX3CR1-GFP

                                                   https://doi.org/10.1084/jem.20141539
                            D-BIOL, IMHS, Zindel                                          20.04.2026   7
               Macrophage Switch: iNKT cells and glycolipid self-antigens

             Focal liver injury
Cxcr6GFP/+

               https://doi.org/10.1016/j.immuni.2017.09.016

                              D-BIOL, IMHS, Zindel                          20.04.2026   8
Macrophage Switch: iNKT cells and glycolipid self-antigens

https://doi.org/10.1016/j.immuni.2017.09.016
             D-BIOL, IMHS, Zindel                            20.04.2026   9
   Macrophage Switch: Overview of signals                                                                                                                                           !
                                                      Receptor on
Signal          Source             Tissue context                           Mechanism / output                      Reference
                                                      macrophage
Common logic: tissue-resident lymphocytes

                                                                            STAT6 → CCR2→CX3CR1                     Liew et al. Immunity 2017
IL-4 / IL-13    iNKT cells         Liver              IL-4Rα / IL-13Rα1
                                                                            conversion                              doi:10.1016/j.immuni.2017.09.016

                                                                            STAT6 → repair gene
IL-4 / IL-13    ILC2s              Lung, gut, skin    IL-4Rα / IL-13Rα1                                             Bosurgi et al. Science 2017 doi:10.1126/science.aai8132
                                                                            programme

                                                                            Epithelial repair programme,
Amphiregulin Tregs                 Muscle             EGFR (?)                                                      Burzyn et al. Cell 2013 doi:10.1016/j.cell.2013.11.010
                                                                            macrophage reprogramming

IGF-1 /      γδ T cells                                                     Keratinocyte and macrophage
                                   Skin               IGF-1R / EGFR (?)                                             Jameson et al. Science 2002 doi:10.1126/science.1069639
Amphiregulin (DETCs)                                                        activation

Universal Signals independent of tissue context

                                                                            TGFβ, IL-10, PGE2 → NF-κB
PS /            Apoptotic                             TIM4, AXL,
                                   All tissues                              suppression, anti-inflammatory          Bosurgi et al. Science 2017 doi:10.1126/science.aai8132
efferocytosis   neutrophils                           MERTK
                                                                            reprogramming

                Neutrophils,                          ALX/FPR2,      Lipid mediator class switch →                  Serhan & Levy Nat Rev Immunol 2018
SPMs                               All tissues
                macrophages                           GPR32, ChemR23 resolution                                     doi:10.1038/nri.2017.103

                         D-BIOL, IMHS, Zindel        Review covering the full table: Minutti et al. Semin Cell Dev Biol 2017 doi:10.1016/j.semcdb.2016.08.006     20.04.2026   10
   Link to Immunology III: Macrophage Polarization Models                                                                     !

Class Switch                            Historic Binary Polarization Model        How you should think about it
Literature                                                                        nowadays
      CCR2hi                                                                   CX3CR1hi = mature macrophage, to know
      CX3CR1lo                                                                 what that macrophage is doing:
      (Ly6Chi)                  CSF1 (= MCSF)                  CSF1 (= MCSF)
      (CCR2hi)                  IFN-γ                          IL-4
                                                               IL-10
     CCR2lo
     CX3CR1hi
     (Ly6Clo)
     (CCR2lo)
                               M1 «classical»              M2 «alternative»
                               Patogen Killing             Tissue Remodeling

                 D-BIOL, IMHS, Zindel                                                                       20.04.2026   11
        Link to Immunology III Class Switch                                                                                                                       !
                                              Gata6+
                                    Tissue Resident Macrophages             5

                                                                                                 Pro-inflammatory cytokine
                                                                        1

                                                                                                 release (used to be M1)
        Folr2+Sele nop +
       Repair-associated
                                7

                            8

The fork in
the road                                     Intermediate                         Repair/Folr2                               Trem2/Spp1
                        2   6                macrophages                                                                     (lipid/stress)
         Monocytes

                                                     Trem2 +Spp1 +
                            3
                                     4
                                                    Sca r-associated
                                         lipid-handling, lysosomal, phagocytic
                                                                                                 Il-4 induced (used to be M2)
                   DC

  Feature                                           TREM2 SPP1+ "Fibrotic Cleaner"                        FOLR2 SELENOP+ "Repair Cleaner"
  Phagocytic Cargo                                  Necrotic debris, oxidized lipids.                     Apoptotic cells (efferocytosis).
  Core Signature                                    TREM2, GPNMB, CD9, SPP1.                              FOLR2, SELENOP, MRC1, CD163.
  Tissue Outcome                                    Scarring (Fibrosis).                                  Functional Repair.
  Vascular Effect?                                  Spp1-driven angiogenesis (tumour context)             Perivascular localisation (function unclear)
  Emerging in the field?                            Spp1/OPN signaling hub                                Antioxidant protection, survive in «hot» injury zone.

                            D-BIOL, IMHS, Zindel                                                                                                20.04.2026   12
  Overshooting Tissue Repair in the Adominal Cavity (Adhesion Formation)

1. DAMP                                                       2. Fibrin Clot
Detection,
Inflammation

3. Myofibroblast!

               D-BIOL, IMHS, Zindel                                  20.04.2026   13
Myofibroblasts in adhesions are Mesothelium-derived

                             Green =          Red = Mesothelium   Yellow = Mesothelium
                             Myofibroblasts   Derived             Derived Myofibroblasts

      D-BIOL, IMHS, Zindel                                                   20.04.2026   14
Mesothelial to mesenchymal transition (MMT)

                                              MMT

                                              ↑α-SMA
                                              ↑Proliferation
  Green =                 Red = Mesothelium   ↑ Migration via disrupted BM
  proliferating           Derived             ↑ Mobility

          D-BIOL, IMHS, Zindel                                               20.04.2026   15
                                                                !
Myofibroblasts

https://doi.org/10.1038/s41580-024-00716-0

                       D-BIOL, IMHS, Zindel   20.04.2026   16
                                                                                                      !
Myofibroblast resolution

                                                                        https://doi.org/10.103
                                                                        8/s41580-024-00716-
                                                                        0

   Physiological resolution            Pathological persistence
   TGF-β signal drops                  Persistent TGF-β / stiff ECM
   Mechanical tension reduces          Fibrotic ECM maintains tension
   Myofibroblast apoptosis             Resistance to apoptosis
   → Scar matures, cellularity drops   → Fibrosis
             D-BIOL, IMHS, Zindel                                                   20.04.2026   17
Myofibroblast Activation – chemical vs mechanical signalling view
                                                                                                                                !
                                     Chemical signalling view            Mechanical signalling view
                                     Macrophage-derived TGFβ, IL-4,      ECM stiffness sensed via
      Primary driver
                                     PDGF                                integrins
                                     Cytokine release from               Loss of ECM structural integrity /
      Key initiating event
                                     inflammatory cells                  fibrin clot mechanics
                                     Sustained macrophage activation     Self-amplifying stiffness-
      Persistence mechanism
                                     / TGFβ loop                         contraction feedback
      Key transcription factors      SMAD2/3, NF-κB                      YAP/TAZ, MRTFA
                                     Anti-TGFβ, anti-IL-4Rα,             Anti-integrins, ROCK inhibitors,
      Therapeutic target
                                     macrophage re-polarization          matrix softening
                                     In vivo macrophage depletion,       Tunable hydrogel stiffness,
      Main evidence base
                                     cytokine KO models                  atomic force microscopy
                                     Chronic inflammation →              Stiff fibrotic ECM → irreversible
      Failure mode explained
                                     persistent macrophage activation    mechanical memory
                                     Cytokine blockade rarely reverses Stiffness alone insufficient
      Weakness
                                     established fibrosis              without initial cytokine trigger

 B. Hinz: «mechanical stress and TGFβ1 are actually two sides of the myofibroblast differentiation
 coin» check this for more on mechanical signaling: https://doi.org/10.1038/s41580-024-00716-0
 .
              D-BIOL, IMHS, Zindel                                                                            20.04.2026   18
Model: Macrophage Fibroblast Circuits                                                         !

                                                      Return to stable ON

         https://doi.org/10.1016/j.cell.2018.01.015

         D-BIOL, IMHS, Zindel                                               20.04.2026   19
                                                 !
Angiogenesis

        D-BIOL, IMHS, Zindel   20.04.2026   20
Neural Regulation of Repair

                                10.1101/cshperspect.a041233
         D-BIOL, IMHS, Zindel                                 20.04.2026   21
Growth Factors in Repair (Link Lecture Prof. Werner)

         D-BIOL, IMHS, Zindel                          20.04.2026   22
Regeneration and Stem Cells (Link Lecture Prof. Gehart)

                                     Macrophage fibroblast circuit (Model A)
                                     • Rapid
                                     • Robust function
                                     • Low architectural fidelity

                                      Regeneration (Model B)
                                      • Slow, costly
                                      • High architectural fidelity
                                      • Requires stem cells

         D-BIOL, IMHS, Zindel                                             20.04.2026   23
Learning Objectives — Lecture 3: Granulation Tissue

• Students can describe the macrophage-fibroblast two-cell circuit — key signals, three stable states,
  separatrix — and explain why injury requires circuit reconstruction from scratch.
• Students can explain the monocyte-to-macrophage class switch, clarify that CX3CR1 is a maturation not
  a polarisation marker, and describe the iNKT/CD1d/IL-4 mechanism with its tissue-specific
  generalisations.
• Students can distinguish Folr2+ repair macrophages from Trem2+/Spp1+ scar-associated
  macrophages by phagocytic cargo, signature, and tissue outcome.
• Students can define the myofibroblast as a phenotype, describe αSMA stress fibre formation, name two
  precursor sources including MMT, and explain the mechanical positive feedback loop driving persistence.
• Students can compare the chemical and mechanical views of myofibroblast activation — driver,
  persistence mechanism, therapeutic target, weakness — and state the synthesis.
• Students can distinguish Model A (functional repair) from Model B (regeneration) in terms of speed,
  fidelity, and cellular requirements

              D-BIOL, IMHS, Zindel                                                              20.04.2026   24
Prof. Dr. Joel Zindel
Assistenzprofessor
Joel.zindel@biol.ethz.ch

ETH Zürich
Institut für Molekulare Gesundheitswissenschaften (IMHS), D-BIOL
HPL F32.2
Otto-Stern-Weg 7
8098 Zürich
```

---

<!-- file: slides/05_TissueRepair_Part4_Remodelling.pdf -->

```text
D-BIOL

Tissue Repair Part IV

Prof. Dr. Joel Zindel
Assistant Professor (TT) for Tissue Repair
April 20th 2026
Notes for this lecture

  !   Central concepts — exam-relevant

      How we know: We look at the experimental data behind central paradigms. These slides are
      epistemologic in nature—how we know what we know—and should not be memorized for the
      exam.

      Nerd factor: Historical or medical perspective or fun. Not to be committed to memory—although
      sometimes the most random facts stick best.

      Resources: Robbins Basic Pathology, Tenth Edition, Chapter TISSUE REPAIR

           D-BIOL, IMHS, Zindel                                                           20.04.2026
Agenda – Tissue Repair
This agenda organises key concepts by when they are discussed — not as strict biological boundaries.

  LECTURE 1                                       LECTURE 2                                    LECTURE 3                                      LECTURE 4

                                                                                               Granulation
  Injury                                          Inflammation                                                                                Remodelling
                                                                                               tissue
  seconds – minutes                               min – hours – days                           hours – days – weeks                           days – weeks – months

  • Definitions: homeostasis, injury,                                                          • The macrophage switch:                       •   Pre primam vs. per secundam
    regeneration, repair, and failure             • Injury detection                             macrophages subtypes in repair               •   Provisional Matrix
    modes.                                        • macrophage cloaking and                    • Macrophage-fibroblast circuit                •   Collagen III
  • The molecular basis of injury and               threshold gating                           • Provisional Matrix                           •   MMP/TIMP balance
    injury detection: DAMPs, PAMPs,               • Coagulation and Complement                 • Angiogenesis                                 •   Collagen I
    and LAMPs.                                    • Thromboinflammation                        • Neural regulation of repair                  •   Remodeling in different tissues
                                                                                               • Collagen III                                 •   Failure modes
                                                                                               • Failure modes

                 Phases are overlapping and tissue-dependent — complement, macrophages, and adaptive immunity span multiple lectures and are discussed in context.

                           D-BIOL, IMHS, Zindel                                                                                                                       20.04.2026
Learning Objectives — Lecture 4: Remodelling

• Students can distinguish between sanitatio per primam and per secundam intentionem — explaining
  how gap size, DAMP load, and mechanical stability determine the scale of scaffold formation and
  remodelling required.
• Students can describe the sequential matrix composition during remodelling — from fibrin/fibronectin
  scaffold through collagen III to mature collagen I — and explain what drives each transition.
• Students can explain how MMP/TIMP balance controls ECM degradation — including the cysteine switch
  mechanism of proMMP activation and why net ECM remodelling equals expression × activation −
  inhibition.
• Students can apply the concept of organ-specific remodelling goals — articulating why the physiological
  scar differs between bone, liver, lung, heart and skin, and predicting the failure mode when remodelling
  overshoots in each tissue.
• Students can explain why fibrosis represents a failure of myofibroblast resolution — identifying TGF-β
  and persistent DAMP signalling as the common drivers across organs, and giving organ-specific
  examples (cirrhosis, IPF, cardiac fibrosis, keloid).

              D-BIOL, IMHS, Zindel                                                               20.04.2026
   Recap: Phases of Repair                                                                  !

Lecture 1 and 2
                                         Lecture 3
                                                                             Lecture 4
                                                     Scaffold/ Provisional
                                                     Matrix

                  D-BIOL, IMHS, Zindel                                         20.04.2026
       Sanitatio per primam vs. per secundam                                                                                                       !
                   Primary intention healing                                                            Secondary intention healing
         Why: ↓DAMP, ↓ gap → ↓scaffold, ↑mech. stability                                          Why: ↑DAMP, ↑gap → ↑scaffold, ↓mech. stability

                                                                              Skin

Bone

                   D-BIOL, IMHS, Zindel                                                                                               20.04.2026
                                          https://doi.org/10.1007/978-3-319-92055-9_21, DOI:10.25259/IJMSR_43_2022
Case study bone

                                                                                                     https://doi.org/10.1007/s43465-020-00320-2

This (valid) example is no treatment
advice. The treatment chosen varies
depending on age, comorbidities, and
fracture pattern and will affect
primary vs. secondary bone repair.
             D-BIOL, IMHS, Zindel                                                                                                  20.04.2026
                                       https://www.orthobullets.com/pediatrics/4019/femoral-shaft-fractures--pediatric
Case study skin
                                                                                                            !

Take home: secondary intention healing (repair) can lead to highly functional outcomes → this is the main
role of remodelling.

             D-BIOL, IMHS, Zindel                                                              20.04.2026
Remodelling
                                                                               !
Overview

                               Schematic based on review of the
                               literature (not based on
                               experimental data)

        D-BIOL, IMHS, Zindel                                      20.04.2026
Provisional matrix
                                                                      Fibronectin the key player                                      !

  Early Provisional                              Late Provisional
       Matrix                                         Matrix                                                               Firbillogenesis
                                                                                                                           and ECM
                                                                                                                           assembly

                                                                                                                           Mechanical
                                                                                                                           integrin switch

                                                                                                                         Growth factor
              Platelets/neutrophils/monocytes                                                                            reservoir
  Adapted from:
  https://doi.org/10.1016/j.matbio.2017.04.003
Teaching note—early provisional matrix =
thromboinflammation (link to previous
lecture)

                         D-BIOL, IMHS, Zindel                       https://doi.org/10.1016/j.matbio.2016.07.011   20.04.2026
Intermediate Matrix (Collagen III) → Final Matrix (Collagen I)
                                                                                                                                              !

                                                                                                   Schematic

      Property                      Collagen III                                 Collagen I
      Gene                          COL3A1                                       COL1A1, COL1A2
      Chain composition [α1(III)]₃ homotrimer                                    [α1(I)]₂α2(I) heterotrimer
      Fibril diameter               Thin, reticulin (~15–50 nm)                  Thick (100–500 nm)
      Mechanical
                                    Flexible, compliant, disulfide-stabilized    High tensile strength, stiff, heavily cross-linked
      properties
      Normal tissue                 Blood vessels, gut, fetal skin (~27% adult
                                                                                 Bone, tendon, skin (~85% of adult skin)
      distribution                  skin)

             D-BIOL, IMHS, Zindel                                                                                                20.04.2026
                                                                 M. musculus      A. percivali
    Species specificity Collagen I and III

Mus musculus                                       Acomys Spp.

                                                                   ↑Scarring      Regeneration
https://doi.org/10.1038/nature11499                              Dense Collagen    Less Dense
                                                                  ↑ Collagen I      Collagen
                            D-BIOL, IMHS, Zindel                                            20.04.2026
  MMP/TIMP balance (I)
                                                                                                                !

Many different substrate-specific forms
Class            Members               Key substrates

Collagenases     MMP-1, -8, -13        Fibrillar collagens I, II, III (¾ + ¼ fragments)

                                       Denatured collagen (gelatin), collagen IV,
Gelatinases      MMP-2, -9
                                       fibronectin

                                       Proteoglycans, laminin, fibronectin,
Stromelysins     MMP-3, -10, -11
                                       amorphous collagen
                                       Membrane-anchored; degrade ECM at cell
                 MMP-14, -15, -16, -
MT-MMPs                                surface; MT1 (MMP-14) cleaves collagen I
                 17, -24, -25
                                       directly
                                       ECM components, cell surface molecules
Matrilysins      MMP-7, -26            (Fas-L, TNF-α, E-cadherin) — no Hpx
                                       domain
                                       Inhibit all MMPs (1:1 stoichiometry, Ki in the
Inhibitors       TIMP-1, -2, -3, -4
                                       picomolar range 10-12M)

                                         Simplified from doi: 10.1161/01.RES.0000070112.80711.3D

                D-BIOL, IMHS, Zindel                                                               20.04.2026
MMP/TIMP balance (II)
                                                                                                       !

                                                               Activation:

                                Simplified from doi: 10.1161/01.RES.0000070112.80711.3D

         D-BIOL, IMHS, Zindel                                                             20.04.2026
Are all collagenases MMPs?

Enzyme                     Class      pH optimum   Key substrate          Key cell
MMP-1                      MMP        7.4          Collagen I, II, III    Fibroblasts
MMP-8                      MMP        7.4          Collagen I, II, III    Neutrophils
MMP-13                     MMP        7.4          Collagen II > I, III   Chondrocytes
                                                                          Fibroblasts,
MMP-14                     MMP        7.4          Collagen I, II, III
                                                                          osteoclasts
                           Cysteine
Cathepsin K                           4.5-6        Collagen I, II         Osteoclasts only
                           protease
                           Cysteine                                       Macrophages,
Cathepsin L/B                         4.5-6        Broad collagen
                           protease                                       lysosomes

              D-BIOL, IMHS, Zindel                                                   20.04.2026
Bone remodelling                                         Cathepsin K — the main collagenase in                          !
                                                         osteoclasts (not an MMP), MMP-9 and MMP-
                                                         14, acid phosphatase (TRAP), Hydrochloric
                                    Haversian channels
                                                         acid

  Fracture

                                                                    https://www.nature.com/articles/s41413-018-0019-6

             D-BIOL, IMHS, Zindel                                                                    20.04.2026
Osteopetrosis – Link to Immunology III                        CSF1/CSF1R mutations,
                                                              i.e. no osteoclasts
                                                              Infantile, Severe!!
                                                                                                Osteoblast gain of function: e.g.
                                                                                                OPG gain of function mutation
                                                 Loss of function
                                                 osteoclast activation, e.g.
                                                 RANK receptor or RANKL

                                                                               https://www.nature.com/articles/s41413-018-0019-6

                                «At the Moulin
                                Rouge»               Loss of function resorption, e.g.:
                                Toulouse-
                                Lautrec              • CTSK Cathepsin K
                                                       (Pycnodysostosis, much milder!)
                                                     • CLCN7 chloride channel (severe!)
         D-BIOL, IMHS, Zindel                                                                                   20.04.2026
Osteopenia in MT1-MMP (MMP14) KO

                                                Osteopenia
                                                and
                                                Fibrosis

           D-BIOL, IMHS, Zindel    20.04.2026
Osteoporosis
                                                                                                      !
                                                                    Selective estrogen receptor
                                                                    modulators/hormone therapy:
                                                                    normalize RANKL/OPG ratio
                                           RANKL-Antibody

     Osteoporosis

                                                  https://www.nature.com/articles/s41413-018-0019-6

                                Bisphosphonates (e.g. Clodronate,
                                Alendronate): osteoclast apoptosis

         D-BIOL, IMHS, Zindel                                                      20.04.2026
Remodelling Goal
                                                                                                                                                                 !
                               Key parenchymal
                    Organ                               Critical ECM architecture                Physiological scar      Failure mode
                               function
                                                                                                                         Osteopetrosis (too little
                                                                                                 Callus → remodelled
                               Load bearing, locomotion Haversian systems, medullary cavity,                             resorption) / Osteopenia (too little
                    Bone                                                                         lamellar bone,
                               haematopoiesis           mineralized collagen I                                           organisation) — as we just saw,
                                                                                                 restored cortex
                                                                                                                         Osteoarthritis.

                                                                                                                         Cirrhosis — bridging fibrosis, loss
                               Metabolism,              Fenestrated sinusoidal endothelium,      Near zero —
                                                                                                                         of sinusoidal fenestrations,
                    Liver      detoxification,          space of Disse — minimal interstitial    regeneration
                                                                                                                         pseudonodules, portal
                               immunology               collagen                                 preferred over repair
                                                                                                                         hypertension

                                                                                                                    Pulmonary fibrosis —
                               Gas exchange (O₂/CO₂     Thin alveolar basement membrane (1- Minimal — walls must honeycombing, fibroblastic foci,
                    Lung
                               diffusion)               2 cell layers), elastic recoil      stay thin for diffusion stiff inelastic alveoli, diffusion
                                                                                                                    block

                                                                                                 Firm focal scar at      Heart failure after Myocardial
                                                        Aligned cardiomyocytes, minimal
                                                                                                 infarct site —          infarction, Diffuse interstitial
                    Heart      Pump function            interstitial ECM, intact electrical
                                                                                                 necessary, not          fibrosis — stiff ventricle, diastolic
                                                        pathways
                                                                                                 optional                dysfunction, arrhythmia

                                                                                                Thin flat pale scar,     Keloid/hypertrophic scar — thick
                               Barrier, locomotion,     Basket-weave collagen I + elastin, thin
                    Skin                                                                        partial elastin          disorganized collagen III, no
                               sensation                dermis
                                                                                                restoration              elastin, contracture

        D-BIOL, IMHS, Zindel                                                                                                                   20.04.2026
 Liver – Stellate cells                                                                          Masson Trichrome Staining             !
Sinusoids: Illustration
                                                                                                  Healthy: collagen
                                                                                                 (blue) in portal tract

                                                                                 Stage 1 Fibrosis:
                                                                                   fibrous portal
                                                                                     expansion

                                                                Stage 3-4 increasing
                                                                fibrotic bridges here

Sinusoids: H&E healthy                                           Stage 4 Fibrosis: cirrhosis,
                                                                    regenerative nodules
                                                                surrounded by fibrous bands

                                            www.aasld.org/liver-fellow-network
                     D-BIOL, IMHS, Zindel                                                                                 20.04.2026
     Lung remodelling                         Failure Mode: Idiopathic Pulmonary Fibrosis
                                                                                                                        !
                                                                                            Macrophage Fibroblast Circuit
 Alveolus: Illustration

Alveoli: H&E healthy

                       D-BIOL, IMHS, Zindel                                                              20.04.2026
Heart remodelling
                                                                                                          !

Healthy heart muscle
                                                                                   Early provisional,
                                                                                         weak!

                                                                                    Late provisional

                                                                                    Necessary scar

           https://en.wikipedia.org

               D-BIOL, IMHS, Zindel   https://doi.org/10.1038/s41598-019-53351-7             20.04.2026
Skin
                                       !

   D-BIOL, IMHS, Zindel   20.04.2026
Learning Objectives — Lecture 4: Remodelling

• Students can distinguish between sanitatio per primam and per secundam intentionem — explaining
  how gap size, DAMP load, and mechanical stability determine the scale of scaffold formation and
  remodelling required.
• Students can describe the sequential matrix composition during remodelling — from fibrin/fibronectin
  scaffold through collagen III to mature collagen I — and explain what drives each transition.
• Students can explain how MMP/TIMP balance controls ECM degradation — including the cysteine switch
  mechanism of proMMP activation and why net ECM remodelling equals expression × activation −
  inhibition.
• Students can apply the concept of organ-specific remodelling goals — articulating why the physiological
  scar differs between bone, liver, lung, heart and skin, and predicting the failure mode when remodelling
  overshoots in each tissue.
• Students can explain why fibrosis represents a failure of myofibroblast resolution — identifying TGF-β
  and persistent DAMP signalling as the common drivers across organs, and giving organ-specific
  examples (cirrhosis, IPF, cardiac fibrosis, keloid).

              D-BIOL, IMHS, Zindel                                                               20.04.2026
Prof. Dr. Joel Zindel
Assistenzprofessor
Joel.zindel@biol.ethz.ch

ETH Zürich
Institut für Molekulare Gesundheitswissenschaften (IMHS), D-BIOL
HPL F32.2
Otto-Stern-Weg 7
8098 Zürich
```

---

# Code overview

<!-- file: code/README.md -->

## Code

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

Analysis templates for the course. Every template is R unless stated, pinned with
`renv` `[TODO: lockfile]`. You build the environment on the first day with your
language model; a prebuilt fallback exists `[TODO: where]`.

The rule for all of it: run the code and look at the object, not at the model's
description of the object.

| Folder | Purpose | Input | Output |
|---|---|---|---|
| `elisa/` | Four-parameter logistic standard curve, concentration table, plots by state and stimulus | plate-reader export, plate map | `elisa_results.csv`, figures |
| `griess/` | Linear nitrite standard, concentration table, plots | plate-reader export, plate map | `griess_results.csv`, figures |
| `flow/` | Reads the population statistics exported from FlowJo and plots them. Gating is done in FlowJo, not in R | FlowJo CSV export | figures |
| `growth_curve/` | Doubling time from daily counts, with the published value as a reference line | counts table from P01 | figure, doubling time |
| `scrnaseq/` | The in silico arm, three parts (below) | preprocessed objects shipped by the staff | figures |
| `qpcr/` | ΔΔCt for the X01 extension | Ct export | figures |

`[TODO: write the templates; each folder gets a README, an `example_data/` subfolder
and one script that runs end to end on the example data.]`

### The in silico arm, `scrnaseq/`

The teaching staff preprocess two datasets and ship small objects, so nobody starts
from raw reads:

- `GSE186658`: single-cell RNA-seq of mouse peritoneal injury sites, two conditions,
  two mice each (Zindel et al. 2021, Nat Commun). Shipped as a Seurat object with
  quality control, normalisation, clustering and a coarse cell-type annotation
  already done; the macrophage subclusters are **not** annotated.
- `GSE113836`: bulk RNA-seq of RAW 264.7 and bone marrow macrophages stimulated with
  LPS plus IFNγ or with IL-4 `[TODO: verify contents, replicates and raw counts]`.
  Shipped as a count matrix with a sample sheet.

Three parts, matched to the dry-lab halves of weeks 2 and 3:

1. **Load and look** (week 2). Open the single-cell object, reproduce the QC figure
   (cells per sample before and after filtering), find the macrophages by `Adgre1`,
   `Cd68`, `Csf1r`, `Fcgr1` and `Mertk`.
2. **Derive the signatures** (week 3). Differential expression in the bulk data,
   M(IFNγ+LPS) versus M(-) and M(IL-4) versus M(-), in RAW 264.7 cells; take the top
   genes by a stated rule; compare with the Murray et al. 2014 table and with the
   consolidated sets of Colombo et al. 2024.
3. **Score the tissue** (week 3). Score every macrophage in the single-cell object
   against both signatures (`AddModuleScore` or equivalent), plot the two scores
   against each other and on the UMAP, and answer: how much of the tissue population
   does either signature explain, and what do cells with both scores high mean for
   the M1/M2 axis.

Nerd-ladder items that start from here: annotate the Gata6+, Folr2+ Selenop+ and
Trem2+ Spp1+ populations; rerun the pipeline from the GEO matrices; integrate with a
true in vitro single-cell dataset (Sanin et al. 2022 `[TODO: accession]`).

The answer key lives in a separate private repository and is released after the
course.

---
