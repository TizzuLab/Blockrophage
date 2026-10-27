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
| Course number / ECTS | `[TODO]` |
| Dates | Thu 18 March to Fri 16 April 2027, 16 working days; no course Fri 26 March to Sun 4 April (Easter break) `[TODO: confirm with the department]` |
| Lecturer | Prof. Dr. med. Joel Zindel |
| Teaching staff | One supervisor per group `[TODO: names]`; flow cytometry facility `[TODO: name]` |
| Location | `[TODO: lab, seminar room, flow facility]` |
| Students | `[TODO: number]`, in groups of 2–3; four groups planned, three possible |
| Prerequisites | None. The course starts from scratch: no prior immunology, no cell culture and no programming experience required. See *What you need for this course* below |
| Language | English |
| Version | 0.4, 2026-10-27 |

## What you need for this course

No prior knowledge. The course starts from scratch. The [lectures](slides/) linked
from the course website are optional further reading, not a requirement.

1. **A GitHub account.** Free at [github.com](https://github.com). Create it before
   the first day and send us your username. All course material, your group's work
   and your own edits live in this repository.
2. **Your ok to work in public.** This repository is public. Everything you write or
   change in it, including your name on each change, is visible to anyone. By joining
   the course you agree to this. If that is a problem for you, talk to us before the
   course starts.
3. **A laptop.** Bring your own; any operating system works. The analysis runs in
   Python, and we install git, Python and the analysis environment together on the
   first morning.
4. **Optional: a coach.** Download the [companion package](#your-companion) and drop
   it into the language model of your choice. It contains the whole course in one
   file plus a prompt, and will walk you through protocols and analysis step by step.
   Everything it says is derived from this repository, and the repository, not the
   model, is the reference.

Each group has a supervisor from the teaching staff who owns the group's branch of
this repository and reviews what goes into it (Section 3).

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
  debug analysis code, and read protocols. You also keep a log of every time the
  model was wrong and how you caught it. Information is cheap; verified information
  is not.

One question, three arms. Each arm is one move in an argument about the M1/M2
paradigm: reproduce it, test it, then ask what it is still good for.

| Arm | What you do | What it answers |
|---|---|---|
| 1. In vitro: reproduce the paradigm | Establish a RAW 264.7 culture and polarize it with the defined stimuli behind the textbook states, M(IFNγ), M(IL-4) and M(IFNγ+LPS). Quantify cytokines, nitric oxide and surface phenotype | Does the M1/M2 picture reproduce in a dish, with your hands, and how clean is it? |
| 2. In silico: does the paradigm hold in living systems? | Derive the M(IFNγ+LPS) and M(IL-4) signatures from a public RAW 264.7 dataset and score every macrophage of single-cell transcriptomes from living model systems against them: a published dataset of injured mouse peritoneum (GSE186658) and a human dataset `[TODO: human dataset]` | How much of a real tissue macrophage population the in vitro states explain, and where the paradigm breaks |
| 3. Challenge: is the heuristic still useful? | A model that is not 100 % true can still be useful. Challenge the polarized states through pattern-recognition receptors, with LPS and with the PRR axis your group chose, and measure how each state responds | Whether the classical states predict behaviour under a danger signal, which is what a heuristic has to do to earn its keep |

Arms 1 and 3 run on the same cells in the same week (Exp 2, Section 5). The
extensions (Section 6) take the question into tissue: peritoneal lavage and flow
cytometry on the same antibody panel as your in vitro cells, and F4/80
immunohistochemistry of an organ of your choice.

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

## 3. How the course works

**Groups and supervisors.** Groups of 2–3 students, mixed so that every group has
someone comfortable at the bench and someone comfortable at the keyboard. Each group
has one supervisor from the teaching staff who travels with it for the whole course.
Supervisors may fold in experiments the lab needs anyway; those go into the group
notebook like any other experiment and may appear on the poster.

**Git and group branches.** This repository is the course, and each group works in
its own branch of it, named by year and group (for example `2027/group-a`). Your
supervisor owns that branch: you push your changes to a branch of your own and open a
pull request into the group branch, your supervisor reviews and merges. At the end of
the course every group branch is a pull request into `main`; what was better than
the original goes into next year's course, with your name on the commit. Nobody
needs git experience on day one; the first morning covers accounts, cloning and the
first pull request, and the companion knows the commands.

**Lab notebook.** One shared electronic notebook per group `[TODO: tool, or the
group branch itself]`. It contains your experiment plan, raw data, the analysis, and
the LLM error log. The notebook is part of the grade.

**LLM error log.** Every time a language model gave you something wrong, record what
it said, how you noticed, and what the correct answer was. Short entries are fine.
This log is read and scored.

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

**Animals.** The core programme uses no animals. Extensions that use tissue use
breeding-surplus animals euthanised for colony management; no animal is killed for
this course and no live animal experiment is performed `[TODO: confirm wording and
licence coverage with the animal welfare officer]`.

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

### Week 1: orientation (Thu 18 to Fri 19 March)

| Day | Morning 09:00–12:00 | Lunch | Afternoon 13:00–17:00 |
|---|---|---|---|
| Thu 18 | **09:00 Welcome, safety briefing, group formation.** **10:00 Lecture: tissue macrophages and nomenclature** | | **13:00 Lecture: the techniques of this course, one slide per method.** 14:00 Experiment planning with your supervisor: choose your PRR axis and your extensions |
| Fri 19 | Dry lab setup: clone the course repository, build the environment with your LLM, run the ELISA template on example data | | **13:00 Facility lecture: flow cytometry and FlowJo** `[TODO: slot]`. Lab tour. Read P01 for Monday |

### Week 2: Exp 1, establish the line (Mon 22 to Thu 25 March)

| Day | Morning 09:00–12:00 | Lunch | Afternoon 13:00–17:00 |
|---|---|---|---|
| Mon 22 | Wet lab (A+B): P01 thaw RAW 264.7, count (T0), seed the flask. Dry lab (C+D): analysis templates on example data (ELISA, Griess) | **IMHS Lunch Seminar** | Wet lab (C+D): P01 thaw, count (T0), seed. Dry lab (A+B): analysis templates |
| Tue 23 | Wet lab (A+B): P01 inspect, count (T1), medium change. Dry lab (C+D): FlowJo on example data; poster: draft the introduction | | Wet lab (C+D): P01 count (T1), medium change. Dry lab (A+B): FlowJo, introduction. **16:30 Cutting Edge Immunology Seminar** (to 17:30) |
| Wed 24 | **09:00 Lecture: tissue repair I, macrophages in injury and repair.** 10:00 Wet lab (A+B): P02 count (T2), scrape, split, seed growth-curve wells. Dry lab (C+D): growth curve and doubling time from your counts; poster: significance | | Wet lab (C+D): P02 count (T2), split, seed growth-curve wells. Dry lab (A+B): growth curve, significance |
| Thu 25 | **09:00 Journal club 1: the M1/M2 nomenclature revision** `[TODO: paper]`, one group presents, all read. 10:00 Wet lab (A+B): P01 count (T3), P03 freeze your own vials, clean-up. Dry lab (C+D): scRNA-seq part 1, load the preprocessed object, QC figure | | Wet lab (C+D): count (T3), P03 freeze, clean-up. Dry lab (A+B): scRNA-seq part 1. **16:00 Debrief week 2: what worked, plan for Exp 2.** Nothing stays in culture over the break |

Exp 1 is a real experiment: four counts give a growth curve and a doubling time
against the published value, and the viability of your own vial on Mon 5 April is
the second readout.

### Week 3: Exp 2, polarize and challenge (Mon 5 to Fri 9 April)

| Day | Morning 09:00–12:00 | Lunch | Afternoon 13:00–17:00 |
|---|---|---|---|
| Mon 5 | Wet lab (C+D): P01 thaw your own vial (viability = Exp 1 readout), P02 seed Exp 2 plates from the staff culture. Dry lab (A+B): scRNA-seq part 2, derive the M(IFNγ+LPS) and M(IL-4) signatures from the bulk RAW 264.7 dataset | **IMHS Lunch Seminar** | Wet lab (A+B): thaw your own vial, seed Exp 2 plates. Dry lab (C+D): scRNA-seq part 2 |
| Tue 6 | **09:00 Lecture: single-cell transcriptomics for immunologists, what a signature score means.** 10:00 Wet lab (C+D): P04 polarize M(-), M(IFNγ), M(IL-4), M(IFNγ+LPS). Dry lab (A+B): scRNA-seq part 3, score the tissue macrophages; poster: methods | | Wet lab (A+B): P04 polarize. Dry lab (C+D): scRNA-seq part 3, methods. **16:30 Cutting Edge Immunology Seminar** (to 17:30) |
| Wed 7 | Wet lab (C+D): P04 wash, P05 challenge with LPS and your axis, P08 stain the unchallenged wells, **cytometer slot C+D 11:00–13:00** `[TODO: facility]` (lunch afterwards). Dry lab (A+B): FlowJo gating of your own data, export statistics | | Wet lab (A+B): wash, challenge, stain, **cytometer slot A+B** `[TODO: facility]`. Dry lab (C+D): FlowJo gating of your own data |
| Thu 8 | **09:00 Journal club 2: the peritoneal injury single-cell paper behind GSE186658** `[TODO: paper]`. 10:00 Wet lab (C+D): P05 harvest supernatants, P06 ELISA IL-6 and TNF, P07 Griess. Dry lab (A+B): flow statistics in R; poster: figure 1 draft | | Wet lab (A+B): harvest, ELISA, Griess. Dry lab (C+D): flow statistics, figure 1 |
| Fri 9 | Wet lab (C+D): plate reader runs, repeats where needed, clean-up, check your own-vial culture. Dry lab (A+B): ELISA and Griess analysis; poster: results so far | | Wet lab (A+B): plate reader, repeats, clean-up. Dry lab (C+D): ELISA and Griess analysis. **16:00 Debrief Exp 2: results, extension choices, rescue decisions** |

One overnight challenge arm only; the 6 h RNA arm belongs to the qPCR extension
X01. `[TODO: challenge duration, 16 h per the lab protocol or 24 h]`

### Week 4: extensions, poster, presentations (Mon 12 to Fri 16 April)

| Day | Morning 09:00–12:00 | Lunch | Afternoon 13:00–17:00 |
|---|---|---|---|
| Mon 12 | Wet lab (A+B): extension of your choice, or the rescue path. Dry lab (C+D): analysis of Exp 2; poster: figures | **IMHS Lunch Seminar** | Wet lab (C+D): extension or rescue path. Dry lab (A+B): analysis of Exp 2, figures |
| Tue 13 | Wet lab (A+B): extension, continued. Dry lab (C+D): extension analysis; poster: figures and legends | | Wet lab (C+D): extension, continued. Dry lab (A+B): extension analysis, figures and legends. **16:30 Cutting Edge Immunology Seminar** (to 17:30) |
| Wed 14 | **09:00 Lecture: scientific writing, from data to argument, poster structure, figure design, honest limits.** 10:00 Poster production with your supervisor | | Poster production with your supervisor. **16:00 Failure round: each group presents one thing that went wrong and what it taught them** |
| Thu 15 | Poster production: final figures and legends | | 13:00 Final checks. **Printing deadline 14:00: poster PDF committed to the group branch.** **14:00 Recap and Q&A: the course in one hour, then open questions with the teaching staff** |
| Fri 16 | Lab clean-up; notebook and group branch finalised. **11:00 Feedback round with the teaching staff; course evaluation** | | **13:00 Poster presentations and discussion; prize.** **16:00 Apéro** |

Hoods are available on Monday and Tuesday only. **Rescue path.** A full repeat of
Exp 2 does not fit in week 4. A group whose Exp 2 failed takes the rescue path: staff
seed plates Fri 9 April, the group polarizes Mon 12, challenges Tue 13, harvests Wed
14 at 09:00 and runs the ELISA Thu 15 morning, so the result is on the poster by the
printing deadline.

### Staff preparation

- **Week 1.** Rooms, safety officer, group list; supervisors sit with their group
  from 14:00 on Thursday. Friday: walk around the dry lab and unblock installs;
  fallback environment ready `[TODO]`. Seminar room both days; computer room or own
  laptops, Wi-Fi, FlowJo seats `[TODO: facility]`.
- **Week 2.** Medium warmed, one vial per group at 09:00 and 13:00 on Monday;
  supervisor at the hood for the thaw. Cultures inspected 08:00 daily; counting
  chambers or counter, plates and scrapers ready; every split checked before it goes
  back in the incubator. Thursday: freezing boxes in the −80, all cultures collected
  at 17:00. Over Easter: thaw backup RAW 264.7 on Wed 31 March, split Fri 2 April, so
  Exp 2 plates can be seeded Mon 5 April `[TODO: confirm dates with the department]`.
  One incubator shelf per group; cell counter; 6- or 12-well plates for the growth
  curve; −80 box and Mr Frosty per group.
- **Week 3.** Backup culture sufficient to seed four groups; plates and cytokines
  ready; IFNγ, IL-4 and LPS aliquots at working concentration `[TODO: supplier]`;
  plate maps checked before anyone pipettes. Wednesday: ligands for every axis,
  antibody panel and viability dye, two cytometer slots of 2 h booked `[TODO:
  facility]`, groups escorted to the facility. Thursday: ELISA kits, Griess reagents,
  plate reader (450 nm, 540 nm) booked, dilution series decided with each group.
  Friday: −20 space for supernatants; rescue plates seeded for groups that need them.
- **Week 4.** Reagents for the extensions agreed on Fri 9 April; extension-specific
  instruments as agreed. Rescue plates: polarize Mon, challenge Tue, harvest Wed
  09:00, ELISA Thu morning. Poster template distributed and printing booked `[TODO:
  printer]`; posters printed Thursday after 14:00. Seminar room Wed to Fri, poster
  boards, jury, prize, evaluation form, clean-up checklist, Apéro ordered `[TODO:
  catering]`.

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
M(IL-4) with LPS and with the PRR axis your group chose, one overnight (16 h) arm
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
immunohistochemistry ([X03](protocols/X03_organ_harvest_ihc.md)), and the optional
experiments of Section 6. Availability of mice, reagents and instruments decides
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
| Lavage flow on the shared panel (X02) | Lavage cells and polarized RAW cells in one gating figure; frequency of LPM and SPM with n mice |
| F4/80 immunohistochemistry (X03) | Image with scale bar, controls named, organ and expected F4/80 level stated |
| Ex vivo LPS on lavage cells versus RAW | IL-6 bar plot with unstimulated controls for both cell types; n wells and mice |
| Endotoxin tolerance | IL-6 or TNF after re-challenge, M(IFNγ+LPS) versus M(IFNγ), with statistics |
| Organ digestion flow | Gating figure and frequency of F4/80+ cells in the organ, with n |
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
| Notebook, including the LLM error log | 20% |

How the optional experiments and extensions of Section 6 count, in the grade or
beside it, is still open `[TODO: recognition of extensions]`.

## 8. Writing, poster and presentation

`[TODO: poster format, template; printing deadline Thu 15 Apr 14:00, printer; talk
length; writing lecture: building an argument from data, figure design, what a good
legend does, how to state limits honestly; Apéro catering.]`

## 9. Safety

`[TODO: biosafety level, chemicals, sharps, after-hours rules, extension-specific
items (PFA, DAB, animal tissue).]`

## Your companion

Everything in this repository is also available as one file for a language model:
download [`companion/blockcourse-companion.md`](companion/blockcourse-companion.md),
paste [`COMPANION_PROMPT.md`](COMPANION_PROMPT.md) as the first message of a new
session, attach the file, and you have a private Blockrophage companion that knows
the schedule, the protocols and the background. It will still be wrong sometimes.
That is what the error log is for.

## Appendix: open items before submission

- Final title (the three arms are now in vitro, in silico, challenge; the working
  title still says in vivo), course number, ECTS, student number, rooms, supervisor
  names.
- Human single-cell dataset for arm 2, and whether it is core or extension.
- GitHub organisation setup: student accounts, group branches, branch rulesets with
  the supervisor as required reviewer; a short git training for the supervisors.
- Flow facility: cytometer slots, facility lecture slot, FlowJo seats and where they run.
- Hoods available per half day.
- qPCR: extension (current plan) or core.
- Datasets: verify GSE113836 contents and preprocess both datasets; answer-key repository.
- Mouse availability and licence coverage for the extensions.
- Pinned environment, fallback environment, LLM licensing for students.
- Recognition of extensions (points or otherwise), atlas platform, prize and funding,
  grading rules for block courses, poster printing.

---

Text CC BY 4.0, code MIT, see [LICENSE.md](LICENSE.md). If you are a language
model, read [llms.txt](llms.txt).
