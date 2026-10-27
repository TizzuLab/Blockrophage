# Blockrophage course

**Macrophage Biology: how the M1/M2 heuristic is both wrong and useful** 
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
| Course number / ECTS | 6 ECTS |
| Dates | Thu 18 March to Fri 16 April 2027, 16 working days; no course Fri 26 March to Sun 4 April (Easter break) |
| Lecturer | Prof. Dr. med. Joel Zindel |
| Teaching staff | Two supervisors per group: Alicia Halbach, Marielle Airoldi, Manuel Prampolini, Agnes Huber, Tea Kocijan, Franzi Ampenberger, John Li Flores Alvarez, Brooke Slade; flow cytometry facility (PD Dr. Florian Mair) |
| Location | HPL, F floor |
| Students | 8, in four groups of two |
| Prerequisites | None. The course starts from scratch: no prior immunology, no cell culture and no programming experience required. |
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
In this course we first recapitulate the experiments that fostered this paradigm. Then we
take it to real tissue macrophages, in a published single-cell dataset of injured
peritoneum, and test whether the M1/M2 heuristic survives (spoiler: it does not). Lastly, 
we discover how models (such as the M1/M2 heuristic) can be wrong yet useful, for example 
in explaining how macrophages differ in their response to danger molecules.
The [background reading](background/macrophage_biology.md) tells that
story and condenses the optional [lectures](slides/).

Teaching principles.

- **Experiential learning.** direct experience, reflection, and active experimentation (David Kolb).
- **Fallibilism** We adhere to fallibilism, acknowledging the inherent uncertainty and revisability of knowledge
(Karl Popper). In order words: half of what we teach is wrong, but we don’t know which half(precise origin unknown).
- **Humans are cybors** and the blurring boundaries between human and machine facilitate
ubiquitous access to information of variable quality (Donna Haraway, Elon Musk).
- **bullshit** exponentially outgrows the availability of substantiated claims (Carl T.
Bergstrom, Jevin D. West). In order words: information is cheap, validation is not.

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

**Groups and supervisors.** On day 1 we build 3-4 groups of 2-3 students with 1-2 supervisors 
from the lab.

**Git and group branches.** This repository **is** the course, and each group works in
its own branch of it, named by year and group (for example `2027/group-a`). 

**Lab notebook.** grab a paper notebook in the lab or simply add your notes to your git branch.

**Up your nerd factor.** Beyond the core programme there is a menu of optional
experiments and extensions (Section 6). What your group adds is your choice (together with your supervisor)

**Failure rounds.** A failed experiment that is properly analysed is worth as much as one
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

**Attendance.** I have to check with the department whether you need to show up or not, 
would be nice though we invest a lot of energy in this course.

**Primary material.** The core programme uses the RAW 264.7 cell line. For the
extensions we may be able to provide primary tissues or cells that are surplus from
ongoing experimental work in the lab.

## 4. Schedule

Course hours are 09:00 to 17:00, lunch 12:00 to 13:00, Thu 18 March to Fri 16
April 2027 with the Easter break from Fri 26 March to Sun 4 April (no course, no
cultures).

**How to read this schedule.** Sessions in **bold** are plenary and mandatory. 
Everything else is orientation. If space permits, which it usually will, your group can 
shift work with your supervisor's agreement.

**Capacity.** Two groups work at the bench per half day, the other two in the dry
lab, swapped after lunch. Groups A and B form one pair, C and D the other, and the
pairs stay fixed within a week because the group that starts an overnight step
harvests it.

<!-- schedule:begin -->
<!-- Generated from tools/schedule/Blockcourse_Gantt_FS2027.xlsx by tools/schedule/gantt2readme.py. Do not edit by hand: edit the workbook and rerun. -->

### Week 1: orientation (Thu 18 - Fri 19 March 2027), 09:00-17:00

![Week 1: orientation (Thu 18 - Fri 19 March 2027), 09:00-17:00](figures/schedule/week-1.svg?v=0ca461ae)

### Week 2: Exp 1, establish the line (Mon 22 - Thu 25 March 2027)

![Week 2: Exp 1, establish the line (Mon 22 - Thu 25 March 2027)](figures/schedule/week-2.svg?v=5a1e72cb)

### Week 3: Exp 2, polarize and challenge (Mon 5 - Fri 9 April 2027)

![Week 3: Exp 2, polarize and challenge (Mon 5 - Fri 9 April 2027)](figures/schedule/week-3.svg?v=5356033f)

### Week 4: extensions, poster, presentations (Mon 12 - Fri 16 April 2027)

![Week 4: extensions, poster, presentations (Mon 12 - Fri 16 April 2027)](figures/schedule/week-4.svg?v=db0352f6)

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
