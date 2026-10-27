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
| Prerequisites | Immunology III (tissue macrophages lecture) or equivalent; no cell culture and no programming experience required |
| Language | English |
| Version | 0.3, 2026-10-26 |

## 1. Concept

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

**Failure round.** On the Wednesday of week 4, after the writing lecture and a day
of poster production, each group presents one thing that went wrong and what it
taught them. The best-analysed failure earns nerd points. Nobody loses
points for a failed experiment that is properly analysed.

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

The schedule is a Gantt-style workbook,
[`schedule/Blockcourse_Gantt_FS2027.xlsx`](schedule/Blockcourse_Gantt_FS2027.xlsx),
rendered week by week as drawings and text in
[`schedule/schedule.md`](schedule/schedule.md). It has one sheet per week, one row
per group, a staff row and a resources row, and a cell per hour. Course hours are
09:00 to 17:00 with lunch from 12:00 to 13:00. Two layers:

- **Fixed layer**, drawn by the teaching staff: lectures and journal clubs, the
  facility lecture, cytometer slots reserved by the flow cytometry facility, the
  IMHS Lunch Seminar every Monday 12:00–13:00 and the Cutting Edge Immunology
  Seminar every Tuesday 16:30–17:30 (weeks 2 to 4), the writing lecture, the recap,
  the poster presentations.
- **Group layer**, drawn by each group with its supervisor on the planning
  afternoon. The default rhythm is a checkerboard: two groups at the bench in the
  morning and two in the dry lab, swapped after lunch, so that two hoods are always
  enough and the cytometer serves two groups per slot. Pairs stay fixed within a
  week, because the group that starts a 24 h step harvests it. Groups may deviate
  from the default if their hood time still fits.

The fixed anchors:

| Week | Dates | What is fixed |
|---|---|---|
| 1 | Thu 18 – Fri 19 March | Thu: welcome, safety, groups 09:00; lecture on tissue macrophages and nomenclature 10:00–12:00; lecture on the techniques of the course 13:00; planning afternoon. Fri: dry lab setup; facility lecture on flow cytometry and FlowJo 13:00 `[TODO: slot]`; lab tour; plans submitted. |
| 2 | Mon 22 – Thu 25 March | Exp 1 (Section 5). Mon 12:00 IMHS Lunch Seminar. Tue 16:30 Cutting Edge Immunology Seminar. Wed 09:00 lecture: tissue repair I, macrophages in injury and repair. Thu 09:00 journal club 1: the M1/M2 nomenclature revision `[TODO: paper]`. Debrief Thursday 16:00. Easter break follows; nothing stays in culture. |
| 3 | Mon 5 – Fri 9 April | Exp 2 (Section 5). Mon 12:00 IMHS Lunch Seminar. Tue 09:00 lecture: single-cell transcriptomics for immunologists; Tue 16:30 Cutting Edge Immunology Seminar. Cytometer slots Wednesday `[TODO: facility]`. Thu 09:00 journal club 2: the peritoneal injury single-cell paper behind GSE186658 `[TODO: paper]`. Debrief Friday 16:00. |
| 4 | Mon 12 – Fri 16 April | Mon–Tue extensions or rescue path; Mon 12:00 IMHS Lunch Seminar; Tue 16:30 Cutting Edge Immunology Seminar. Wed 09:00 lecture on scientific writing, then poster production with your supervisor; 16:00 failure round. Thu poster production; **printing deadline 14:00**: poster PDF committed to the group branch, nerd ladder closes; 14:00–17:00 recap and Q&A with the teaching staff. Fri lab clean-up, notebook and group branch finalised; 11:00 feedback round and course evaluation; 13:00–16:00 poster presentations and prize; 16:00 Apéro. |

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

## 6. Up your nerd factor: extension challenges

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
| Best grant pitch | "Follow-up project" box: aims in three sentences, one budget line | 2 |

## 7. Assessment

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
