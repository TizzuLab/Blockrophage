# Blockrophage course: companion file

Built from the course repository by tools/build_companion.py. This single file
contains the complete course material for the ETH Zürich block course
"Macrophage Biology: in vitro, in vivo, in silico" (Spring Semester 2027).
Repository: https://github.com/TizzuLab/Blockrophage. It is meant to be given to a language model
by pasting it into a new session; the instructions it then follows come next.

UNDER CONSTRUCTION: first run spring 2027, built in the open; protocol values are
unverified and the protocols must not be used in the lab yet.

Reading order and conventions are in the first section (llms.txt). Each document
starts with a line `<!-- file: path -->` naming its path in the repository, so
an answer can cite the file. Values marked [TODO] are unconfirmed.

## How to behave: the companion prompt

The instructions below are companion/prompt.md. A student pasted this file to
make you the course companion: follow them and open with the greeting.

You are reading the Blockrophage course companion for the ETH Zürich block course
"Macrophage Biology" (spring 2027). The student who pasted this file wants you to be
their Blockrophage Companion: take that role now, without asking for confirmation,
and treat this file as the only source of truth about the course.

Begin with exactly this message and nothing else: "Hi there! I'm going to be your
Blockrophage Companion! 🧱🦠🔬 Ready to explore macrophage biology, one block at a
time. Welcome to the course! Would you like to check your software setup, look at the
schedule, or start with some macrophage biology? Or is there something else on your
mind?"

Then coach rather than lecture: short answers that cite the file (protocol and step,
or week and day, with the link https://github.com/TizzuLab/Blockrophage/blob/main/PATH),
one question back when the student is reasoning, and after every protocol answer say
where to check it. Never invent a value; [TODO] means unconfirmed, ask the
supervisor. The course is under construction and the protocols are not validated.
If a question needs more depth than this file gives, say that the full companion
with the background reading, the lecture text and the analysis code is at
https://raw.githubusercontent.com/TizzuLab/Blockrophage/main/stuff/companion/blockcourse-companion.md
and can be pasted in the same way.

This is the core companion: the script, the schedule, the protocols, the notebook
rules, the admission sheet and the poster guide. The full companion adds the
background reading, the lecture text and the analysis code:
https://raw.githubusercontent.com/TizzuLab/Blockrophage/main/companion/blockcourse-companion.md . When a question needs that depth, tell the student to download the
full file from the repository and attach it to the session.

## Table of contents

- Index (llms.txt)
  - `llms.txt`
- Course script, including the schedule
  - `README.md`
- Schedule, text version of the drawings
  - `stuff/tools/schedule/schedule_text.md`
- Protocol index
  - `protocols/README.md`
- Core protocols
  - `protocols/C1_raw264_culture.md`
  - `protocols/C2_polarization.md`
  - `protocols/C3_flow_cytometry.md`
  - `protocols/C4_prr_challenge.md`
  - `protocols/C5_elisa.md`
- Extension protocols
  - `protocols/X01_qpcr.md`
  - `protocols/X02_peritoneal_cells_flow.md`
  - `protocols/X03_tissue_sections_ihc.md`
  - `protocols/X04_griess.md`
  - `protocols/X05_mtt.md`
- Notebooks: the lab notebook rules
  - `notebooks/README.md`
- Admission sheet: safety and data
  - `safety/README.md`
- Poster guide
  - `poster/README.md`
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
> single-cell dataset. Repository: https://github.com/TizzuLab/Blockrophage. This file follows the llms.txt convention: it tells a language
> model what is here and in which order to read it.

### Status

- Under construction: the course runs for the first time in spring 2027 and is built
  in the open. Protocol values are unverified; tell any user that the protocols must
  not be used in the lab yet. Interested students can apply or give input via
  https://zindellab.ch/contact.html or the repository's issues.

### How to use this repository as a model

- The single file `stuff/companion/blockcourse-companion.md` contains every document below,
  concatenated, with a table of contents. If you have that file, you have everything.
- Protocols carry IDs (C1 to C5 core, X01 to X05 extension, S01 staff). When a user asks about
  a step, quote the protocol ID and the step number. Never invent a volume,
  concentration or time that is not in the protocol; values marked `[TODO]` are
  unconfirmed and you must say so.
- The schedule is Section 4 of the script: one drawing per week (SVG in stuff/figures/schedule/) with a folded text table per day underneath, generated from the workbook in stuff/tools/schedule/.
  Sessions in bold are plenary and mandatory; the wet-lab times listed for a group
  are guaranteed; everything else is orientation and a group may shift work with
  its supervisor's agreement.
- Section numbers "5.x" in the background text refer to the background document, not
  to the script.

### Script

- [Course script (README)](README.md): concept, learning objectives, how the course
  works, the schedule (Section 4, week by week), the three experiments (Section 5:
  polarization, the in vitro versus in vivo comparison in silico, the danger-signal
  challenge) with the extensions (nerd factor), assessment. Read first.

### Protocols

- [Protocol index](protocols/README.md): table of all protocols with hands-on time,
  wall-clock time and resources.
- Core, cell culture for Exp 1 and Exp 3:
  [C1 RAW 264.7 culture: thaw, split, seed](protocols/C1_raw264_culture.md).
- Core, Exp 1 (polarization): [C2 polarization](protocols/C2_polarization.md),
  [C3 flow cytometry](protocols/C3_flow_cytometry.md).
- Core, Exp 3 (challenge): [C4 PRR challenge](protocols/C4_prr_challenge.md),
  [C5 ELISA](protocols/C5_elisa.md).
- Exp 2 (in vitro versus in vivo comparison) is dry lab: see Code below.
- Extensions: [X01 qPCR](protocols/X01_qpcr.md),
  [X02 peritoneal cells on the shared flow panel](protocols/X02_peritoneal_cells_flow.md),
  [X03 F4/80 IHC on tissue sections](protocols/X03_tissue_sections_ihc.md),
  [X04 Griess](protocols/X04_griess.md), [X05 MTT assay](protocols/X05_mtt.md).
- Staff: [S01 backup vials and the stock over the break](protocols/S01_raw264_freeze.md).

### Background

- [Macrophage biology](background/README.md): nomenclature, ontogeny,
  niche, function and activation state, pattern-recognition receptors, the peritoneal
  cavity, why a dish is not a body, the single-cell dataset, working with a language
  model as a scientist.
- [Reading list](background/reading_list.md).

### Slides

- [Lecture slides](background/slides/): five lecture decks (PDF), optional further reading, listed in the background chapter; the course has no prerequisites.

### Code

- [Admission sheet](safety/README.md): safety and data. The whole safety instruction for the course, and the data terms students sign (data belong to the lab, published open access under CC BY 4.0); rules sourced from the ETH and IMHS biosafety concepts; chemicals table, waste, incidents; confirmation signed after the day-1 briefing.
- [Poster guide](poster/README.md): ETH scientific poster template (link, not hosted), A3 scaled to A0, what the course expects on the poster.
- [Code overview](code/README.md): analysis templates and the single-cell workflow.

### Optional

- [Companion prompt](stuff/companion/prompt.md): the instructions at the top of the
  companion files. The student copies the core companion from the collapsible block
  in the README and pastes it into a new session of their AI tool.
- [Companion file](https://raw.githubusercontent.com/TizzuLab/Blockrophage/main/stuff/companion/blockcourse-companion.md): the whole repository as one file.
- [Core companion](https://raw.githubusercontent.com/TizzuLab/Blockrophage/main/stuff/companion/blockcourse-companion-core.md): script, schedule and protocols only, for sessions that
  have to start from a link.
- [Licence](LICENSE.md): CC BY 4.0 for text, MIT for code.

---

# Course script, including the schedule

<!-- file: README.md -->

## Blockrophage

**The block course about macrophage polarization and their response to danger molecules**\
Zürich, Spring Semester 2027. Zindel lab (TizzuLab).

> **Under construction.** This course runs for the first time in spring 2027 and is
> being built in the open. Interested students are welcome to apply and to give
> input, through the [contact page](https://zindellab.ch/contact.html) or an
> [issue](https://github.com/TizzuLab/Blockrophage/issues). **Please do not use
> these protocols in the lab yet.** Values are unverified until this notice is gone;
> items marked `[TODO]` are open.

| | |
|---|---|
| Course title | Blockrophage course: the block course about macrophage polarization and their response to danger molecules |
| Course number / ECTS | 6 ECTS |
| Dates | Thu 18 March to Fri 16 April 2027, 16 working days; no course Fri 26 March to Sun 4 April (Easter break) |
| Lecturer | Prof. Dr. med. Joel Zindel |
| Teaching staff | Two supervisors per group: Alicia Halbach, Marielle Airoldi, Manuel Prampolini, Agnes Huber, Tea Kocijan, Franzi Ampenberger, John Li Flores Alvarez, Brooke Slade; flow cytometry facility (PD Dr. Florian Mair) |
| Location | HPL, F floor |
| Students | 8, in four groups of two |
| Prerequisites | None. The course starts from scratch: no prior immunology, no cell culture and no programming experience required. |
| Language | English |
| Version | 0.6, 2026-10-28 |

### What you need for this course

1. **A laptop**, any operating system, and **a GitHub account**, created at
   [github.com](https://github.com) before the first day; the username is sent to
   us. You will work in a public repository, where your edits and your name are
   visible to anyone, which is worth keeping in mind when the account is created.
2. **The admission sheet**, please read before the first day and signed after the
   briefing on the first morning ([safety and data](safety/README.md)). It holds the
   safety rules and the data terms: what you produce belongs to the lab and may be
   published open access. The signed sheet is your admission to the bench.
> [!TIP]
> **Your AI companion for the course.** Copy this prompt to your AI tool.
>
> <details>
> <summary>The prompt (open, press the copy button at the top right of the box, close again)</summary>
>
> (On GitHub this spot holds the core companion itself, in a collapsible block with a copy button.)
>
> </details>

No prior knowledge; the [lectures](background/slides/) are optional reading.

### 1. Concept

Every student arrives with the textbook picture of macrophages (which we will refresh in case
you forgot): M1 kills, M2 heals.
In this course we first recapitulate the experiments that fostered this paradigm. Then we
take it to real tissue macrophages, in a published single-cell dataset of injured
peritoneum, and test whether the M1/M2 heuristic survives (spoiler: it does not). Lastly, 
we discover how models (such as the M1/M2 heuristic) can be wrong yet useful, for example 
in explaining how macrophages differ in their response to danger molecules.
The [background reading](background/README.md) tells that
story and condenses the optional [lectures](background/slides/).

Teaching principles.

- **Experiential learning.** direct experience, reflection, and active experimentation (David Kolb).
- **Fallibilism** We adhere to fallibilism, acknowledging the inherent uncertainty and revisability of knowledge
(Karl Popper). In order words: half of what we teach is wrong, but we don’t know which half(precise origin unknown).
- **Humans are cybors** and the blurring boundaries between human and machine facilitate
ubiquitous access to information of variable quality (Donna Haraway, Elon Musk).
- **bullshit** exponentially outgrows the availability of substantiated claims (Carl T.
Bergstrom, Jevin D. West). In order words: information is cheap, validation is not.

### 2. Learning objectives

After this course, students will be able to:

1. **Classify** macrophages by ontogeny, niche and activation state, use the
   M(stimulus) nomenclature correctly, and explain why the M1/M2 dichotomy was revised.
2. **Culture** a mammalian cell line: thaw, count, seed at a defined density,
   stimulate and harvest adherent cells, and keep a stock going.
3. **Set up** a reproducible analysis environment from a code repository with an AI tool
   as assistant, and verify or refute what the AI tool produces.
4. **Establish** a scRNA-Seq analysis workflow for a published data set from an
   example, and score the identified myeloid populations against an in-vitro-derived
   M1/M2 gene signature.
5. **Polarize** macrophages in vitro and validate the resulting cellular phenotype.
6. **Explain** canonical LPS–TLR4 danger signaling, or another danger signaling
   pathway, in depth and validate it experimentally.
7. **Communicate** results as a poster and a short talk, including an honest account of
   what went wrong and what it taught you.

### 3. How the course works

**Git and group branches.** This repository **is** the course, and each group works in
its own branch of it, named by year and group (for example `2027/group-a`). 

**Groups and supervisors.** On day 1 we build 3-4 groups of 2-3 students with 1-2 supervisors 
from the lab.

**Lab notebook.** One text file per person in [`notebooks/`](notebooks/README.md) on
your group's branch, started with a "hello world" commit on the Friday of week 1 and
pushed at least once a day; paper notes are photographed into it.

**Up your nerd factor.** Beyond the core programme there is a menu of optional
experiments and extensions (Section 5, Extensions). What your group adds is your choice (together with your supervisor).

**Failure rounds.** A failed experiment that is properly analysed is worth as much as one
that worked.

**Safety and data.** The [admission sheet](safety/README.md), with the safety rules and the
data terms, needs to be read and signed before experimental work can start.

**Attendance.** We have to check with the department whether you need to show up all the time, 
would be nice though we invest a lot of energy in this course.


### 4. Schedule

Course days run from 08:00 to 17:00, Tuesdays from 13:00; Monday and Tuesday
morning belong to your other lectures, and every full day opens with a self-study
hour. Lunch is 12:00 to 13:00. The course runs Thu 18 March to Fri 16 April 2027 with
the Easter break from Fri 26 March to Sun 4 April, during which the staff look after
your stock flasks.

**How to read this schedule.** Days are columns, hours are rows. Dark sessions in
**bold** are plenary and mandatory. Everything else is the default plan, the same for
all four groups; if space permits, which it usually will, your group can shift work
with your supervisor's agreement.

**Where.** Lectures and dry lab are in conference room HPL F22. Bench work is in HPL
F27.2, where each group has its own laminar flow hood reserved all day, every day.

<!-- schedule:begin -->
<!-- Generated from tools/schedule/Blockcourse_Gantt_FS2027.xlsx by tools/schedule/gantt2readme.py. Do not edit by hand: edit the workbook and rerun. -->

#### Week 1: orientation (Thu 18 - Fri 19 March 2027)

![Week 1: orientation (Thu 18 - Fri 19 March 2027)](figures/schedule/week-1.svg?v=4be57bd7)

#### Week 2: polarize and characterize (Tue 23 - Thu 25 March 2027)

![Week 2: polarize and characterize (Tue 23 - Thu 25 March 2027)](figures/schedule/week-2.svg?v=5c993004)

#### Week 3: polarize and challenge (Tue 6 - Fri 9 April 2027)

![Week 3: polarize and challenge (Tue 6 - Fri 9 April 2027)](figures/schedule/week-3.svg?v=aab2d8c0)

#### Week 4: close the story (Tue 13 - Fri 16 April 2027)

![Week 4: close the story (Tue 13 - Fri 16 April 2027)](figures/schedule/week-4.svg?v=abda94d4)

<!-- schedule:end -->

### 5. Experiments

The course has three experiments, two at the bench and one at the computer, and every
group does all three. Experiment 1 polarizes the cells and reads the phenotype,
Experiment 2 asks whether the dish states exist in tissue macrophages of published
single-cell datasets, and Experiment 3 challenges the polarized cells with danger
signals. The dry-lab experiment runs alongside the bench work from week 2 to week 4.
A menu of extensions closes this section.

**Experiment 1: Polarization** (wet lab, week 2) Primary macrophages do not divide
in a dish and die within days, so the field works with a model. RAW 264.7 is a line
established in 1978 from a tumour induced in a BALB/c mouse by Abelson leukaemia
virus: it divides without growth factor, adheres, responds strongly to LPS and IFNγ,
and has been in culture for almost fifty years. What that does and does not make it
is in the [background](background/README.md#52-level-i-ontogeny). On the Friday of
week 1 your group thaws its own stock flask from a provided vial, and that flask
carries the whole course: the staff look after it over the weekend and the Easter
break, and after the break passaging it is your background task
([C1](protocols/C1_raw264_culture.md); staff: [S01](protocols/S01_raw264_freeze.md)). The textbook states were defined by what is
added: IFNγ, IL-4, or IFNγ with LPS, named M(IFNγ), M(IL-4) and M(IFNγ+LPS) after
the stimulus since the 2014 nomenclature
([background](background/README.md#54-level-iii-function-and-activation-state)).
Every group runs the same two controls, vehicle as the negative control and LPS as
the positive control, the technical positive that tells a silent polarizer from a
failed staining, and picks one polarizer from the menu
([C2](protocols/C2_polarization.md)): IFNγ, IL-10, dexamethasone, IL-4, PGE2, or,
as the lab's wild card, retinoic acid, the signal that gives peritoneal macrophages
their identity. On Tuesday of week 2 you plate from your stock with the polarizer
already in the suspension, beside the two controls. The readouts are the same for
everyone: flow cytometry ([C3](protocols/C3_flow_cytometry.md)), which belongs to
the polarization week, and an IL-6 ELISA ([C5](protocols/C5_elisa.md)), which
belongs to the challenge week and is run on the supernatants of Experiment 3. A
group may read TNF instead of IL-6, and a group that prefers another readout, a
western blot or qPCR ([X01](protocols/X01_qpcr.md)) for example, brainstorms it with
its supervisor. On Wednesday the cells are harvested, stained and fixed (C3), on
Thursday acquired at the facility and gated in a FlowJo session, with intracellular
Arg1 as a high-risk option for a group that wants to learn permeabilization. By
Thursday 16:00 you know whether your polarizer did what the menu says on this
readout, and you decide to stick with it or to pivot to one that worked, before the
break. For the dampeners IL-10, dexamethasone and PGE2, "no change and good
viability" is the expected result, because their test is the suppressed cytokine
response of Experiment 3. If the state separates from the vehicle control, the
paradigm has been built with your own hands. If it does not, that is a result too,
and the first thing analysed is which readout failed. Only LPS has been validated in
the lab, on this very stock; every other arm extends the data for the next iteration
of the course, and the poster says so.

**Experiment 2: Comparison in vitro versus in vivo polarization** (dry lab, weeks 2
to 4) A dish has two states because two were created; a tissue did not read the
textbook. M1 and M2 were defined in a dish, with a handful of markers. In Seurat,
you work through a published single-cell dataset of injured mouse peritoneum
(GSE186658): find the macrophages, look at what distinguishes their clusters, and
decide which one is M1 and which M2 before you see any score. Then you score every
cell with the classic markers and with a consensus of the published in vitro
RNA-seq experiments for IFNγ and IL-4 (Colombo et al. 2024), the two polarizers of
your bench work. The question is descriptive: does the dichotomy hold in tissue,
and for which readout? Finally you choose a signature from the single-cell
literature that describes your macrophages better, and that goes on the poster.
The data run from the GEO count matrices on your laptop in a few minutes, with the
scripts in [`code/scrnaseq`](code/scrnaseq/README.md); nobody starts from raw
reads. As an extension, a group can take the same workflow to an organ or a disease
of its own choice, mouse or human, from a published dataset: macrophages are
everywhere. Choose it together with your supervisor. What the picture means is something we will work out together
at the debriefs. Background sections on
[why a dish is not a body](background/README.md#58-why-a-dish-is-not-a-body)
and [the dataset](background/README.md#59-the-in-silico-dataset-and-how-single-cell-rna-sequencing-works);
[analysis code](code/README.md).

**Experiment 3: Challenge with danger signals** (wet lab, week 3) A model that fails
the test of Experiment 2 may still predict something. The prediction built into
M1/M2 is that the state a macrophage is in decides how it responds to the next
danger signal. So on the first afternoon your group hand-draws the pathway it is
going to test: which ligand, which receptor, which adaptor and output, how an
inhibitor could prove that it is this receptor and not endotoxin in the tube, and
where your polarizer should act on the pathway
([background](background/README.md#56-sensing-danger-pattern-recognition-receptors)).
The drawing is your group plan; it goes into the group branch and comes back on the
poster, redrawn in the light of your data. In week 3 you polarize again on Tuesday,
with your own approach or the standard that worked, and challenge on Wednesday from
the menu of [C4](protocols/C4_prr_challenge.md): PAMPs for TLR2, TLR3, TLR4, TLR7,
TLR9 and Dectin-1, heat-killed bacteria, one DAMP (a necrotic lysate of your own
cells), and two inhibitors, TAK-242 against TLR4 and polymyxin B against LPS itself,
with LPS on M(-) as the control every group shares. The readout is IL-6 after an
overnight challenge by default, or TNF after 6 h ([C5](protocols/C5_elisa.md)); the
cells go to the freezer as lysates for the extensions. By Friday 9 April every group
knows what its story still lacks. Every group ends up with a different combination
and the same schedule. Whatever is found, one fact is worth keeping in mind: after
twenty years of the paradigm there is no approved therapy that targets macrophage
polarization. A heuristic can be useful at the bench and still have limits in the
body. Where those limits are is something we will think about together, with your
data on the table.

**Week 4: close the story.** Bench work in the last week is optional and never at
the cost of wrapping up: repeat the polarization or the challenge, add a further
experiment if both worked, or use the days to finish Experiment 2 and the poster, as
agreed with your supervisor on Friday 9 April. Wednesday ends with "publish or
perish", a critical discussion on scientific integrity and output metrics; Friday
holds the written exam, the poster session with a 360° feedback round, and the
apéro.

**Dry lab, around the bench.** Every full day opens with a self-study hour, and the
dry-lab slots sit around the bench work, with the [analysis code](code/README.md):
week 1 the environment, week 2 scRNA-seq part 1 (Experiment 2) from the GEO
matrices and your own flow data in FlowJo, week 3 part 2 during the challenge and the
ELISA incubations and your ELISA data on Friday, week 4 part 3 and the figures. Gaps
are filled with the poster: the introduction is written first, then the
significance.

#### Extensions

The three experiments are composed of mainly established methods, but students are
encouraged to experiment on their own to complete their story/poster. The
availability of surplus primary material, reagents and instruments will be made
available on day 1 and each group can define additional experiments they would like
to attempt.

Some protocols are made available (prefix X... in protocol catalogue), others your
group supervisor may have established, yet others you may need to establish from the
literature. Here are some examples of what you could do, but the list is
non-exhaustive.

| Experiment or extension | What it adds to the story |
|---|---|
| Macrophages annotated | UMAP with Gata6+, Folr2+ Selenop+ and Trem2+ Spp1+ labelled, marker dot plot, cell counts |
| Macrophages in your field ([extensions](code/scrnaseq/README.md#potential-extensions)) | A published single-cell dataset of an organ or disease of your choice through the same workflow; its macrophages, their M1/M2 scores and a signature from that field |
| Unpredicted figure, dataset or code | A figure or table not in the answer key, with claim, n and method |
| qPCR (X01) | ΔΔCt of outputs and the receptor of your pathway across states, with housekeepers named |
| Primary peritoneal cells on the shared panel (X02) | Primary cells and polarized RAW cells in one gating figure; frequency of LPM and SPM with n samples |
| F4/80 immunohistochemistry (X03) | Image with scale bar, controls named, tissue and expected F4/80 level stated |
| Ex vivo LPS on primary peritoneal cells versus RAW | IL-6 bar plot with unstimulated controls for both cell types; n wells and samples |
| Endotoxin tolerance | IL-6 or TNF after re-challenge, M(IFNγ+LPS) versus M(IFNγ), with statistics |
| Tissue digestion flow | Gating figure and frequency of F4/80+ cells in the tissue, with n |
| BMDM versus RAW | One figure comparing the two in at least two polarization states |
| Phagocytosis or efferocytosis | Percentage of uptake-positive cells per state, with n |
| Double immunofluorescence | Two-channel image with scale bar; markers named |
| Atlas contribution | List of accepted atlas entry IDs with a QR code `[TODO: atlas platform]` |

### 6. Assessment

The grade has two parts of equal weight. A written exam on the last Friday at 13:00,
individual, gives 50% of the points. The other 50% is a group grade from the group
branch: the poster as a document, scored without the students present, and the way
there as recorded in the git history, which counts as much as the poster itself.
Details are announced in the welcome session on the first day.

### 7. Writing, poster and presentation

The poster is made with the ETH scientific poster template, laid out in A3 and
printed at A0; the [poster guide](poster/README.md) links the template on the ETH
Corporate Design page and lists what the course expects on the poster.

### 8. Safety

The [admission sheet](safety/README.md) is the whole safety instruction for this
course: where the rules come from, and what you need to know here: biosafety level,
protection and conduct, the cabinet, the chemicals of this course with one rule
each, sharps, waste, incidents and emergency numbers. It also holds the data terms
(Section 9). It ends with the confirmation you sign after the briefing on the first
morning, which is the written record the ETH biosafety concept asks for.

### 9. Data

The course keeps its data where each kind lasts best, so that the repository stays
small and the whole course can be rerun anywhere, at ETH or at another university.

| Data | Where |
|---|---|
| Plate reader exports (ELISA, Griess, MTT), counts, plate maps, processed tables such as FlowJo statistics or ΔCt values | in this repository, next to the code that reads them |
| FCS files, the prepared single-cell object and any other large file | [Zenodo](https://zenodo.org), one record with a DOI per course year |
| Sequencing raw data | GEO |

GitHub rejects files above 100 MB and slows down well before that, so nothing
larger than a few MB goes into git. The code fetches the large files from their DOI,
so a clone of this repository plus the download is the complete course.

The data you produce belong to the lab and are published open access under CC BY
4.0 in the record of your year, with your name as a contributor unless you opt out.
You agree to this with the [admission sheet](safety/README.md) (section 3).

### Appendix: open items before submission

- Final title (the three arms are now in vitro, in silico, challenge; the working
  title still says in vivo), course number, ECTS, student number, rooms, supervisor
  names.
- Human data: no fixed human dataset; groups may choose one for the "your field" extension.
- GitHub organisation setup: student accounts, group branches, branch rulesets with
  the supervisor as required reviewer; a short git training for the supervisors.
- Flow facility: cytometer slots, facility lecture slot, FlowJo seats and where they run.
- qPCR: extension (current plan) or core.
- Datasets: core and extension run from GEO (done); answer-key repository.
- Surplus primary material for the extensions.
- Pinned environment, fallback environment, AI tool licensing for students.
- Recognition of extensions (points or otherwise), atlas platform, prize and funding,
  grading rules for block courses; exam duration and room.
- Cytometer slots and FlowJo teaching seats for Thu 25 March, facility lecture slot
  Wed 24 March 09:00 (Florian Mair).
- Plate-and-polarize in one step and the polarizer doses: run once on the course
  stock before March.
- February email to the enrolled students: install R, RStudio and Git, create a
  GitHub account and send the username, read the admission sheet (safety and data
  terms), confirm the public repository. Assume some will not have done it; Friday afternoon of week 1 starts
  from scratch.
- Data: the ETH Legal Office checks the data terms of the admission sheet; set up
  the Zenodo record for FS2027 and a download script in `code/` that fetches the
  large files by DOI and checks them.

---

Text CC BY 4.0, code MIT, see [LICENSE.md](LICENSE.md). If you are a language
model, read [llms.txt](llms.txt).

---

# Schedule, text version of the drawings

<!-- file: stuff/tools/schedule/schedule_text.md -->

## Schedule, text version

Generated from `stuff/tools/schedule/Blockcourse_Gantt_FS2027.xlsx` by `stuff/tools/schedule/gantt2readme.py` for the
companion; the drawings in README Section 4 are the same content. Activity blocks in brackets;
dark (plenary) blocks are mandatory, everything else is the default plan for all four groups.

#### Week 1: orientation (Thu 18 - Fri 19 March 2027)

##### Thu 18 Mar

- 08:00-09:00: Self-study: reading for the day, notebook, group branch
- 09:00-11:00: [Plenary, lecture, debrief] Welcome address and introductory lecture: macrophages, why they matter, why we do what we do (Joel Zindel), 09:00-10:15
- 11:00-12:00: [Plenary, lecture, debrief] Working in the lab and biosafety (Tea Kocijan), 10:30-12:00: Q&A, then the admission sheet (safety and data) is signed
- 12:00-13:00: Lunch
- 13:00-14:00: [Plenary, lecture, debrief] Introduction of the supervisors (what they do and why) and group formation
- 14:00-17:00: [Dry lab and desk work] Experiment planning with your supervisors: hand-draw the pathway you will test (ligand, receptor, output, how an inhibitor proves it, where the polarizer acts), pick your polarizer, stimulus and cytokine (C2, C4, C5) and your extension. Read C1 and C3 for Friday and Tuesday.
- Staff: Rooms, safety officer. Signed admission sheets collected at 12:00. Supervisors sit with their group from 14:00.
- Resources: Conference room HPL F22 for lectures and dry lab.

##### Fri 19 Mar

- 08:00-09:00: Self-study: reading for the day, notebook, group branch
- 09:00-12:00: [Wet lab Exp 1] Hands-on cell culture with the staff culture: hood and sterile technique, microscope, C1 scrape, count, split and seed, cell counter. Then C1: thaw and seed your group's stock flask (course passage 0). Lab tour.
- 12:00-13:00: Lunch
- 13:00-17:00: [Dry lab and desk work] Working with git and RStudio, step by step with the supervisors: GitHub account, install R, RStudio and Git if you did not at home, token, clone the course repository from RStudio, switch to your group's branch, open the ELISA script and run it. Then the first commit: a new text file in notebooks/ with your first notes, saved under a name you like, committed as "hello world" and pushed to your branch. Then the rest of the environment with your AI tool. Group plan (the drawing and your menu choices) committed to the group branch at 17:00.
- Staff: One low-passage vial per group. Supervisors carry the stock flasks over the weekend and the break: split every 2 to 3 days, course passage counted from this thaw. Afternoon: one supervisor per two laptops; the 08:00 slot is the installation help desk for latecomers. Collect the plans at 17:00.
- Resources: 4 hoods HPL F27.2, one per group, available at all times. Cell counter. Conference room HPL F22 for lectures and dry lab. Own laptops, Wi-Fi.

#### Week 2: polarize and characterize (Tue 23 - Thu 25 March 2027)

##### Tue 23 Mar

- 08:00-12:00: Your other lectures (not course time)
- 12:00-13:00: Lunch
- 13:00-15:00: [Wet lab Exp 1] C1 and C2: plate cells from your stock with the polarizer already in the seeding suspension. Vehicle control, M(pol) and LPS control on the flow plate (6- or 12-well). Plate-and-polarize in one step, about 19 h. Wet-lab goal: plate at a defined density with a stimulus.
- 15:00-17:00: [Dry lab and desk work] Dry lab: scRNA-seq part 1, download and load the data, QC figure. If the bench runs over, the dry lab moves home.
- Staff: Stock flasks counted per group at 12:30. Polarizers, vehicle and LPS at working concentration; plate maps checked before anyone pipettes.
- Resources: 4 hoods HPL F27.2, one per group, available at all times. Cell counter.

##### Wed 24 Mar

- 08:00-09:00: Self-study: reading for the day, notebook, group branch
- 09:00-10:00: [Facility slot] Facility lecture: flow cytometry and FlowJo (Florian Mair) [TODO: confirm slot]
- 10:00-12:00: [Wet lab Exp 1] C3 Harvest the adherent cells, count, viability dye, Fc block, surface stain
- 12:00-13:00: Lunch
- 13:00-15:00: [Wet lab Exp 1] C3 continued: optional Arg1 fix and perm, fix, store at 4 °C until acquisition. Wet-lab goal: harvest, staining, fixation. Staining plan and FMOs in the notebook.
- 15:00-17:00: [Dry lab and desk work] Dry lab: scRNA-seq part 1 continued; poster: draft the introduction. If the bench runs over, the dry lab moves home.
- Staff: Antibody panel, viability dye, fix/perm buffers, compensation beads. Nothing in the incubator but the stock flasks.
- Resources: 4 hoods HPL F27.2, one per group, available at all times. Cooled centrifuge. Fridge. Conference room HPL F22 for lectures and dry lab.

##### Thu 25 Mar

- 08:00-09:00: Self-study: reading for the day, notebook, group branch
- 09:00-12:00: [Facility slot] C3 Acquisition at the facility, two batches of 1.5 h, two groups each [TODO: reservation]
- 12:00-13:00: Lunch
- 13:00-16:00: [Facility slot] FlowJo session: gating, FMOs, export statistics; the first figure [TODO: check with Florian Mair the available teaching seats]. Wet-lab goal: acquisition and gating.
- 16:00-17:00: [Plenary, lecture, debrief] Journal club 1 and debrief in one session: did the polarizer do what the menu says on this readout? Stick or pivot; decision in the group branch
- Staff: Escort the groups to the facility. Stock flasks: split, two or three backup vials to -80 per group, carried over the break by the staff. Easter: no course.
- Resources: Cytometer: 2 slots of 1.5 h [TODO: facility]. Conference room HPL F22 for lectures and dry lab. FlowJo seats [TODO].

#### Week 3: polarize and challenge (Tue 6 - Fri 9 April 2027)

##### Tue 6 Apr

- 08:00-12:00: Your other lectures (not course time)
- 12:00-13:00: Lunch
- 13:00-16:00: [Wet lab Exp 3] C1 and C2: plate from your stock (carried over the break) with the chosen polarizer, own approach or the standard that worked. 96-well for supernatants, extra wells for lysates. Passage the stock.
- 16:00-17:00: [Plenary, lecture, debrief] Cutting Edge Immunology Seminar 16:30-17:30 (tbd)
- Staff: Stock flasks counted at 12:30. Polarizers, stimuli, inhibitors, LPS at working concentration. Plate maps checked.
- Resources: 4 hoods HPL F27.2, one per group, available at all times. Plate centrifuge.

##### Wed 7 Apr

- 08:00-09:00: Self-study: reading for the day, notebook, group branch
- 09:00-12:00: [Wet lab Exp 3] C4 Challenge: your stimulus, optional inhibitor (TAK-242 1 h before, polymyxin B premixed), LPS on M(-) as everyone's control. Default: overnight, IL-6. Alternative: 6 h, TNF, harvest 15:00. Wet-lab goal: stimulate with inhibitor logic.
- 12:00-13:00: Lunch
- 13:00-14:00: [Plenary, lecture, debrief] Lecture: single-cell transcriptomics for immunologists, what a signature score means (tbd)
- 14:00-16:00: [Dry lab and desk work] Dry lab during the challenge: scRNA-seq part 2, markers of the macrophage clusters and the M1/M2 scores. TNF groups: harvest at 15:00, supernatants and lysates to the freezer.
- 16:00-17:00: [Wet lab Exp 3] 16:30: coat the ELISA plates with capture antibody, overnight at 4 °C (C5), 30 min at the bench
- Staff: Ligands, inhibitors and vehicle ready; -20 space and labelled tubes. Lysis buffers for RNA and protein.
- Resources: 4 hoods HPL F27.2, one per group, available at all times. Conference room HPL F22 for lectures and dry lab.

##### Thu 8 Apr

- 08:00-09:00: Self-study: reading for the day, notebook, group branch
- 09:00-10:00: [Wet lab Exp 3] C4 Harvest (overnight groups): supernatants in aliquots, cells as RNA or protein lysate to the freezer
- 10:00-12:00: [Wet lab Exp 3] C5 ELISA: blocking, standards, samples; dry lab in the incubations
- 12:00-13:00: Lunch
- 13:00-15:00: [Dry lab and desk work] Dry lab during the ELISA incubations: the assay waits for 3.5 h in total, which is used to prepare the next steps and for dry lab (scRNA-seq part 2). The split of wet and dry lab may shift a little.
- 15:00-17:00: [Wet lab Exp 3] C5 ELISA: detection and read-out; first look at the numbers. Passage the stock. Wet-lab goal: an ELISA from coating to concentration.
- Staff: ELISA reagents, plate reader booked. Flow on challenged cells only if a group found a slot in the regular booking.
- Resources: Plate reader (450 nm). 4 hoods HPL F27.2, one per group, available at all times. Conference room HPL F22 for lectures and dry lab.

##### Fri 9 Apr

- 08:00-09:00: Self-study: reading for the day, notebook, group branch
- 09:00-12:00: [Dry lab and desk work] ELISA analysis: standard curve, concentrations. Flow statistics from week 2 in R. scRNA-seq part 2 continued.
- 12:00-13:00: Lunch
- 13:00-16:00: [Poster and writing] Poster: what the story has and what it is missing; week 4 plan agreed with your supervisor (repeat, add, or wrap up)
- 16:00-17:00: [Plenary, lecture, debrief] Debrief Exp 3: results and week 4 decisions
- Staff: Stock flasks: keep or freeze according to each group's week 4 plan.
- Resources: Conference room HPL F22 for lectures and dry lab. 4 hoods HPL F27.2, one per group, available at all times.

#### Week 4: close the story (Tue 13 - Fri 16 April 2027)

##### Tue 13 Apr

- 08:00-12:00: Your other lectures (not course time)
- 12:00-13:00: Lunch
- 13:00-16:00: [Extension / nerd factor] Optional, as agreed on 9 April: repeat the polarization or the challenge, or a further experiment. Or dry lab: finish the in silico part and the poster. Never at the cost of wrapping up.
- 16:00-17:00: [Plenary, lecture, debrief] Cutting Edge Immunology Seminar 16:30-17:30 (tbd)
- Staff: Reagents for the agreed repeats or extensions. Stock flasks for the groups that plate.
- Resources: 4 hoods HPL F27.2, one per group, available at all times. Extension-specific instruments as agreed. Conference room HPL F22 for lectures and dry lab.

##### Wed 14 Apr

- 08:00-09:00: Self-study: reading for the day, notebook, group branch
- 09:00-12:00: [Extension / nerd factor] Optional harvest and ELISA for groups at the bench; otherwise poster: figures and legends
- 12:00-13:00: Lunch
- 13:00-16:00: [Poster and writing] Wrap up: code, figures and poster; scRNA-seq part 3, your own signature for the poster
- 16:00-17:00: [Plenary, lecture, debrief] Publish or perish: a critical discussion on scientific integrity and output metrics
- Staff: Poster template distributed. Plate reader for the groups that ran an ELISA.
- Resources: 4 hoods HPL F27.2, one per group, available at all times. Conference room HPL F22 for lectures and dry lab.

##### Thu 15 Apr

- 08:00-09:00: Self-study: reading for the day, notebook, group branch
- 09:00-12:00: [Poster and writing] Wrap up: code, figures and poster, with your supervisor. Print when ready (signprint.ch); the PDF goes to the group branch first
- 12:00-13:00: Lunch
- 13:00-17:00: [Poster and writing] Wrap up, continued: code, figures, poster, group branch. Stock flask frozen or discarded.
- Staff: Poster boards ready. Exam papers printed. Course evaluation goes out as a written survey.
- Resources: Conference room HPL F22 for lectures and dry lab. Poster boards.

##### Fri 16 Apr

- 08:00-09:00: Self-study: reading for the day, notebook, group branch
- 09:00-10:00: [Dry lab and desk work] Lab cleaning
- 10:00-12:00: [Dry lab and desk work] Finish the group branch; poster pickup, self-service
- 12:00-13:00: Lunch
- 13:00-14:00: [Plenary, lecture, debrief] Written exam, individual [TODO: duration and room]
- 14:00-16:00: [Plenary, lecture, debrief] Poster session: presentations and discussion; prize
- 16:00-17:00: [Plenary, lecture, debrief] Open 360° feedback round: closes the poster session and opens the apéro
- Staff: Exam papers, jury, prize, clean-up checklist. Apéro ordered [TODO: catering]; evaluation survey sent after the course.
- Resources: Conference room HPL F22 for lectures and dry lab. Apéro room [TODO: catering].

---

# Protocol index

<!-- file: protocols/README.md -->

## Protocols

← Back to the [course script](../README.md#readme)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

One file per protocol, all on the same template (00_TEMPLATE.md): header table,
purpose, materials, before you start, procedure, controls, checkpoints, known failure
modes, output. Values the lab has not yet confirmed are marked `[TODO]`; things
the lab has a protocol for but has not run in the course format carry a
`> [!IMPORTANT] **To verify:**` callout. Where the lab has a validated SOP, the SOP wins and the
protocol names it (lab SOP number, version and date; the SOPs themselves are
internal documents). Figures live in `figures/`. Every incubation and centrifugation
you set or time is bold and boxed, like **`37 °C, 5% CO2, 16 h`**; the formatting
rules are at the top of the template.

Five core protocols (C) carry the course, in the order you meet them: cells,
polarization, phenotype, challenge, readout. X-files are optional extensions
(Section 5 of the script, Extensions). The S-file is for the staff.

**Core**

| ID | Title | Used in | Hands-on time | Wall-clock time | Resources |
|---|---|---|---|---|---|
| [C1](C1_raw264_culture.md) | RAW 264.7 culture: thaw, split, seed | week 1 Friday (thaw the stock flask); Exp 1 and 3 plating; passaging | 45 min for the thaw, 45 min per split or seeding | the flask lives the whole course; a seeded plate is used the next morning | hood, incubator, centrifuge, counter, microscope |
| [C2](C2_polarization.md) | Polarization: the menu | Exp 1, Exp 3 | 30 min, at seeding | about 19 h, Tue to Wed | hood, incubator, vortex |
| [C3](C3_flow_cytometry.md) | Flow cytometry of polarized RAW cells | Exp 1 (week 2), X02 | 2 h stain + 1 h acquisition | half day | hood, cooled plate centrifuge, heating block, cytometer slot, FlowJo seat |
| [C4](C4_prr_challenge.md) | Danger-signal challenge: PAMPs, DAMPs, inhibitors | Exp 3 (week 3 Wed) | 45 min + 45 min harvest | 16 h overnight (default) or 6 h | hood, incubator, plate centrifuge, −20 °C, −80 °C |
| [C5](C5_elisa.md) | ELISA IL-6 (default) or TNF | Exp 3 (week 3 Thu) | 3–4 h + coating the day before | 2 days | plate reader (450 nm), multichannel pipette |

**Extensions**

| ID | Title | Used in | Hands-on time | Wall-clock time | Resources |
|---|---|---|---|---|---|
| [X01](X01_qpcr.md) | RNA isolation and qPCR | Extension | 1 h + 1.5 days | 6 h arm, then 2 days | hood, −80 °C, RNA bench, NanoDrop, thermal cycler, LightCycler 480 II |
| [X02](X02_peritoneal_cells_flow.md) | Peritoneal cells on the shared flow panel | Extension | 30 min + staining | half day, with cytometer slot | surplus peritoneal cell suspension provided by staff, ice, cooled centrifuge, cytometer slot |
| [X03](X03_tissue_sections_ihc.md) | F4/80 IHC on tissue sections | Extension | 1 h + 2 × 3 h | about 5 days | surplus fixed tissue or blocks provided by staff, histology facility (paraffin), pressure cooker, histology bench, slide scanner |
| [X04](X04_griess.md) | Griess assay | Extension, on the Exp 3 supernatants | 1 h | 1 h | plate reader |
| [X05](X05_mtt.md) | MTT assay: metabolic activity as a proxy for cell number | Extension | 40 min + 20 min per read day | 3.5 h per read, same day | hood, incubator, plate reader (560 or 570 nm plus reference), multichannel pipette |

**Staff**

| ID | Title | Used in | Hands-on time | Wall-clock time | Resources |
|---|---|---|---|---|---|
| [S01](S01_raw264_freeze.md) | RAW 264.7: backup vials and the stock over the break | Thu of week 2, Easter break | 45 min + 20 min per split | overnight at −80 °C, then −140 °C | hood, centrifuge, freezing container, −80 °C, −140 °C |

### Dependencies in time

- C1: the group's stock flask is thawed on Friday of week 1 and lives until the
  end of the course; the staff carry it over the weekend and the break (S01).
- Exp 1 (week 2): C1 plates on Tuesday 13:00 with the polarizer in the suspension
  (C2); C3 harvests, stains and fixes on Wednesday, acquires on Thursday morning.
- Exp 3 (week 3): C1 plates on Tuesday 13:00 with the polarizer (C2); C4
  challenges on Wednesday 09:00, overnight (default) or 6 h; C5 plates are coated
  on Wednesday 16:30 and run on Thursday. X04 (extension) runs on the same
  supernatants.
- X02 needs a cytometer slot on the day the peritoneal cells are available; X03
  tissue must reach the facility in week 1. Both depend on surplus primary material
  from ongoing work in the lab; ask on the first afternoon.

### Plate formats

One seeding density, scaled by growth area (C1): 96-well plates (2 × 10^4 cells,
200 µL) for everything that ends in a supernatant assay, 6-well plates for flow
cytometry, 24-well plates for the RNA extension.

### Buffers (lab recipes)

| Buffer | Recipe | Notes |
|---|---|---|
| Complete medium (50 mL) | 44.5 mL DMEM high glucose GlutaMAX (Gibco 31966021), 5 mL heat-inactivated FCS (Gibco A5256801), 0.5 mL penicillin-streptomycin (Gibco 15140122) | warm to 37 °C |
| FACS buffer (500 mL) | 478 mL 1× PBS, 15 mL FCS, 2 mL 0.5 M EDTA, 5 mL 1 M HEPES | 3% FCS, 2 mM EDTA, 10 mM HEPES; the lab calls it MACS buffer |
| PBS 10× (1 L) | 80 g NaCl, 2 g KCl, 11.5 g Na2HPO4, 2 g KH2PO4, water to 800 mL, pH 7.2–7.4 with HCl, to 1 L | autoclave, 4 °C |
| EDTA 0.5 M (1 L) | 146.13 g EDTA in 800 mL water, pH 8 with NaOH, to 1 L | autoclave, 4 °C, 1 year |
| HEPES 1 M (1 L) | 238.3 g HEPES in 800 mL water, pH 8 with NaOH, to 1 L | autoclave, 4 °C, dark |
| ACK lysis buffer (1 L) | 8.29 g NH4Cl (155 mM), 1 g KHCO3 (10 mM), 200 µL 0.5 M EDTA (0.1 mM), water to 800 mL, pH 7.4, to 1 L | autoclave, room temperature |

---

# Core protocols

<!-- file: protocols/C1_raw264_culture.md -->

## C1 RAW 264.7 culture: thaw, split, seed

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | C1 |
| Used in | Week 1 Friday (hands-on on the staff culture, then thaw your stock flask); Exp 1 and Exp 3 plating; passaging the stock |
| Hands-on time | 45 min for the thaw; 45 min per split or seeding |
| Wall-clock time | the flask lives until the end of the course; the staff carry it when you are away. A seeded plate is polarized at seeding (C2) and harvested or challenged the next morning |
| Resources | hood, incubator shelf (37 °C, 5% CO2), centrifuge, Neubauer chamber or Countess III, microscope |
| Depends on | Part A: the hands-on introduction of the same morning. Part B: the group's stock flask at 60–80% confluence |
| Lab SOP | Zindel lab 0203 "RAW 264.7 – adherent cells" (v1.0, 2025-12-01), and the lab's RAW 264.7 polarisation protocol (v1.0, 2025-12-08), seeding section. The SOP wins over this page. |

### Purpose

Bring one cryovial of RAW 264.7 cells into culture as your group's stock flask for the
whole course (Part A), then keep it growing and seed plates from it at a defined
density (Part B). From this flask you plate the polarization experiment on Tuesday of
week 2 and the challenge experiment on Tuesday of week 3, with the polarizer already
in the seeding suspension (C2). The first time you scrape, count and split is on the 
Friday morning of week 1.

Splits are counted from the thaw as course passage 0; the absolute passage of the lab
stock should be noted and can vary slight, so the course passage count goes on the poster. 
The stock is tested for mycoplasma by the staff before the course.

**Who looks after the flask:** you, on course days; the staff over the
Easter break, weekends are to negotiated (split every two to three days, backup vials frozen before the break, S01). After the break, passaging your stock is a background task with your supervisor
at the next hood, on Tuesdays when you plate and once more on Thursday or Friday.

### Materials

- RAW 264.7 cryovial, one per group, from the staff stock `[TODO: mycoplasma test
  date]`
- Complete medium, 50 mL: 44.5 mL DMEM high glucose with GlutaMAX (Gibco 31966021),
  5 mL heat-inactivated FCS (Gibco A5256801), 0.5 mL penicillin-streptomycin
  (Gibco 15140122). Final 10% FCS, 1% P/S. Warm to 37 °C before use.
- DPBS without calcium and magnesium (Gibco 14190144), warm
- Cell scraper, one per flask
- T25 flask for the thaw, T75 for expansion
- Plates: 6-well or 12-well for flow cytometry (week 2), 96-well flat-bottom for the
  supernatants (week 3), 24-well for the RNA extension
- Trypan blue, Neubauer chamber or Countess III

### Before you start

- Seeding days: plate map drawn in the notebook before any cell is touched: which
  well gets which state and stimulus, triplicates, controls.
- Plates labelled on the lid and the side: group, date, content.
- Calculate the volumes needed for the target density before scraping.

### Procedure

#### Part A: thaw your stock flask (Friday 19 March, after the hands-on introduction)

1. Prepare a 15 mL tube with 10 mL warm complete medium.
2. Take the vial from the staff tank in a closed transport container. Spray it with
   70% ethanol before it goes into the hood.
3. Thaw by dilution, not in the water bath: add 1 mL warm complete medium to the
   frozen vial with a 1 mL pipette, take the medium that has thawed off the ice back
   into the 15 mL tube, and repeat until the vial is empty.

> [!WARNING]
> Work fast: viability drops with every minute the cells sit in DMSO.

4. Centrifuge **`300 × g, 5 min, room temperature`** to remove the DMSO. Aspirate the
   supernatant.
5. Resuspend the pellet in 5 mL warm complete medium. If the cells are sticky, break
   clumps with a 1 mL pipette until you have a single-cell suspension. Take 10 µL for
   the count.
6. Count with trypan blue. Record total cells, live cells and viability: this is
   course passage 0 in the notebook.
7. Transfer the suspension to a T25 flask and incubate at **`37 °C, 5% CO2`**.

> [!TIP]
> Distribute the cells by gently rocking the flask once before closing the
> incubator; do not swirl.

#### Part B: scrape, count, split, seed (every visit from then on)

8. Every visit starts at the microscope: morphology (round to spindle-shaped,
   adherent), density, debris, signs of contamination (turbidity, colour change,
   particles moving between cells). Record the confluence and photograph one field at
   10× for the notebook. The lab splits at about 80% confluence; change the medium
   whenever it turns yellow.
9. Aspirate the medium. Wash once gently with 5 mL warm DPBS and aspirate.
10. Add 3 mL (T25) or 10 mL (T75) fresh complete medium and scrape the whole surface
    with steady strokes, including the edges.

> [!NOTE]
> RAW 264.7 are passaged by scraping, not trypsin.

11. With a serological pipette, wash the walls of the flask with the medium so that
    every cell is in suspension, then pipette up and down 3–5 times to break clumps.
    Transfer to a 15 mL tube.
12. Count with trypan blue. Record total, live, viability.
13. Split: seed 1:3 to 1:5 of the suspension into a fresh flask (3 mL final in a T25,
    10 mL in a T75); move from the T25 to a T75 at the first split. RAW 264.7 double
    every 15–24 h (lab SOP). Record the split with the date and the course passage
    count, counted from the Friday thaw.
14. Seed for an experiment: centrifuge the needed cells **`300 × g, 5 min`**,
    resuspend in fresh medium at the working density and plate

    | Format | Cells per well | Volume per well | Use |
    |---|---|---|---|
    | 96-well | 2 × 10^4 | 200 µL | supernatant for ELISA (lab-validated) |
    | 24-well | 1.2 × 10^5 | 500 µL | RNA arm, X01 |
    | 6-well | 6 × 10^5 | 2 mL | flow cytometry, C3 |


> [!IMPORTANT]
> **To verify:** the 24- and 6-well densities are derived, not tested. Check in
> the first run that a 6-well seeded this way yields at least 1 × 10^6 cells per
> well 48 h later for C3.

> [!TIP]
> Rock the plate gently in a cross pattern to spread the cells. Do not swirl;
> swirling piles cells in the centre.

15. Incubate overnight **`37 °C, 5% CO2, about 19 h`**; the polarizer went in with
    the suspension (C2). Harvest (C3) or challenge (C4) the next morning.
16. Before the Easter break the staff freeze two or three backup vials from your
    flask (S01) and carry the flask through the break; after the break the splits
    are done by you again.

### Controls

- Medium-only flask or well, incubated alongside: detects contaminated medium.
- One well of medium without cells per plate: background for the assays and a
  contamination check.
- Count twice if the two counts of the same suspension differ by more than 20%.
- The lab's LPS ladder on this stock (C5, worked example): the stock responds.

### Checkpoints

- After the thaw: viability above 80%. Below that, note it, keep going, and ask for
  a second vial if the flask is empty on Tuesday morning.
- After scraping: mostly single cells under the microscope, viability above 90%.
- Tuesday of week 2, before plating: cells attached, spreading, 60 to 80% confluent.

> [!WARNING]
> Beyond 90% confluence, split first: RAW cells change behaviour when overgrown.

- Next morning after seeding: an even monolayer, about 40–60% confluent in the
  96-well `[TODO: confirm expected confluence at stimulation in the first run]`.
  Uneven wells are noted in the plate map and excluded from triplicate statistics if
  they are outliers.

### Known failure modes

- Low viability after thaw: DMSO exposure too long or vial thawed too slowly. Thaw
  by dilution as in step 3, work faster.
- Cells not attaching: cold medium or an FCS lot problem. Check the medium
  temperature first.
- Clumps: scraped too hard or pipetted too little. Pipette more gently, more times.
- Edge effect in plates: evaporation in outer wells. Fill the outer wells of a
  96-well plate with 200 µL DPBS if the plate map allows it, or seed only inner
  wells.
- Density wrong next day: counting error or cells not spread. Check the photograph
  from the day before.
- Flask lost over a weekend or the break: the staff restart from a backup vial or
  the freezer stock; your plan does not change, the course passage count restarts
  and the notebook says so.

### Output

Thaw count and viability, the split log with course passage counts, one photograph
per visit; on seeding days the counts, volumes and the final plate map. The plate map
is the file every later analysis is joined to.

---

<!-- file: protocols/C2_polarization.md -->

## C2 Polarization of RAW 264.7: the menu

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | C2 |
| Used in | Exp 1 (week 2, polarize and characterize) and Exp 3 (week 3, polarize and challenge) |
| Hands-on time | 30 min to prepare the stimuli; the plating itself is C1 |
| Wall-clock time | about 19 h, Tuesday 14:00 to Wednesday 09:00, in both weeks |
| Resources | hood, incubator shelf, vortex |
| Depends on | the group's stock flask (C1) at 60 to 80% confluence, counted |
| Lab SOP | Zindel lab "RAW 264.7 polarisation" (v1.0, 2025-12-08): 96-well format, 100× stimulus stocks, master mixes. The SOP wins over this page. |

### Purpose

Give your cells one defined signal and ask whether it changes what they are (week 2,
read by flow cytometry, C3) and how they answer danger (week 3, read by ELISA after
the challenge of C4). Your group picks one polarizer from the menu below. The
polarizer goes into the seeding suspension: plate and polarize in one step on Tuesday
afternoon, harvest or challenge on Wednesday morning. LPS is not a polarizer in this
course; it is the technical positive control on every plate, beside the vehicle
control, so that a polarizer that does nothing can be told from a staining or cell
problem.

### The menu

| Polarizer | Working concentration | What it does in RAW 264.7 | Safe readout | Risk |
|---|---|---|---|---|
| IFNγ | 20 ng/mL | MHC-II and CD86 up, iNOS primed, TNF and IL-6 amplified with LPS. This is M(IFNγ) | flow (MHC-II, CD86) and ELISA | low |
| IL-10 | 20 ng/mL | TNF and IL-6 suppressed through STAT3 and SOCS3 | ELISA (suppression, week 3) | low; nothing to see by flow, by design |
| Dexamethasone | 100 nM | TNF, IL-6 and NO suppressed through the glucocorticoid receptor; the drug every patient on steroids gets | ELISA (suppression, week 3) | low; cheap and stable; needs a vehicle control |
| IL-4 | 20 ng/mL | Arg1, Chil3, Retnla and Mrc1 mRNA up, LPS response dampened. This is M(IL-4) | qPCR Arg1 (X01); ELISA (suppression) | medium: CD206 by flow is weak in this line; intracellular Arg1 (C3) is the high-risk flow option |
| PGE2 | 1 µM | IL-10 up and TNF down through cAMP | ELISA | medium; less canonical; vehicle control |
| ATRA, all-trans retinoic acid | 1 µM, from a DMSO stock, in the dark | In vivo the signal that induces GATA6 and the peritoneal macrophage identity; in vitro it dampens TNF and NO and helps IL-4 induce Arg1. Whether it induces Gata6 in RAW 264.7 is not known | qPCR Gata6, Arg1, Icam2 (X01) | high: the lab's wild card, outcome unknown; for a group that takes the qPCR extension |

What to expect in week 2, by flow: IFNγ shows, IL-4 shows weakly at best, ATRA is
unknown, and IL-10, dexamethasone and PGE2 show nothing by design, because their
readout is the suppressed cytokine response in week 3. "No change and good viability"
is the expected week 2 result for a dampener, not a reason to pivot.

> [!IMPORTANT]
> **To verify:** LPS is the only stimulus validated in the lab (100 ng/mL, 16 h, on
> the current stock, see C5). Every row above is a literature dose; working
> concentrations, suppliers and catalogue numbers `[TODO]`. A group that wants
> robust data takes IFNγ. Everything else extends the data for the next iteration of
> the course, and that is said on the poster.

### Materials

- Your polarizer `[TODO: supplier, catalogue number, stock concentration, aliquot
  storage; the lab has not used these yet]`. Recombinant mouse IFNγ, IL-4 and IL-10
  carrier-free, stocks at 100 µg/mL in PBS with 0.1% BSA, aliquoted at −80 °C; a
  carrier-free cytokine diluted without BSA sticks to the plastic. Dexamethasone and
  ATRA as 1 mM stocks in DMSO, PGE2 as 10 mM in ethanol; the vehicle control is the
  same solvent at the same final dilution (0.1%). For the cytokines, vehicle and M(-)
  are the same well.
- LPS, E. coli O111:B4, ultrapure, lab stock 2.5 mg/mL `[TODO: supplier and
  catalogue number of the lab's stock]`
- Complete medium, warm (recipe in C1); DPBS, warm
- 1.5 mL tubes for the 100× stocks, 5 mL or 15 mL tubes for the master mixes
- Vortex

### Before you start

- The plate map is drawn in the notebook before anything is pipetted. Week 2 (flow
  plate, 6- or 12-well): vehicle, M(pol), LPS control, one well each, a second set if
  you run intracellular Arg1. Week 3 (96-well, C4): the six conditions of the
  challenge in triplicate plus the inhibitor wells.
- Stimuli are added as 100× stocks to the seeding suspension, 1 part in 100, so
  every well gets the same volume of additive and no medium change is needed.
- Vortex the LPS vial before use and between every dilution step: LPS aggregates.
- Retinoic acid: keep the stock and the dilutions in the dark, make the 100× stock
  fresh on the day; serum contains retinoids, so M(-) is not retinoid-free.

### Procedure

1. LPS 100× stock. Dilute the lab stock stepwise in complete medium, as the lab SOP
   does:

   | Tube | From | Add | Result | 100× for |
   |---|---|---|---|---|
   | L1 | LPS stock (2.5 mg/mL) | 2 µL + 498 µL medium | 10,000 ng/mL | 100 ng/mL |
   | L2 | L1 | 50 µL + 450 µL medium | 1,000 ng/mL | 10 ng/mL |

   L1 is the tube used here and in C4; the full ladder (L3, L4) is for the
   dose-response extension.
2. Polarizer 100× stock in complete medium: IFNγ, IL-4 or IL-10 at 2 µg/mL (100× of
   20 ng/mL); dexamethasone at 10 µM; PGE2 at 100 µM; ATRA at 100 µM. Vehicle 100×:
   10% DMSO or ethanol in medium, for a final 0.1% `[TODO: check against the
   supplier's recommended range]`.
3. Seeding suspensions, one per condition: count the stock flask (C1, steps 1 to
   5), dilute to the working density of the plate format (C1, step 7), and add
   10 µL of 100× stock per mL of suspension (polarizer, LPS, or vehicle). Mix by
   inverting; do not vortex cells.
4. Plate according to the map (C1, step 7). Record the clock time: this is the start
   of the polarization.

> [!TIP]
> Rock the plate in a cross pattern; do not swirl.

5. Incubate overnight at **`37 °C, 5% CO2, about 19 h`**.
6. Wednesday 09:00, week 2: harvest for flow cytometry (C3). Week 3: the challenge
   goes onto the polarized cells (C4); the polarizer stays in the well.

### Controls

- M(-) or vehicle is the reference for every comparison.
- LPS control: must show CD86 and scatter up by flow (week 2) and cytokine in the
  supernatant (week 3); if it does not, the reagent, the cells or the staining is the
  problem, not your polarizer.
- Endotoxin tolerance: a cell that has already seen LPS answers the next LPS weakly;
  that is why LPS stays out of the polarization and why the LPS control wells are
  never challenged again.

### Checkpoints

- Wednesday 09:00: LPS wells look activated, cells spread and often larger; IFNγ
  wells spread; dexamethasone and IL-10 wells look like M(-) or calmer. If every
  condition looks identical, check the stock dilutions before you blame the biology.

### Known failure modes

- No difference between conditions: cytokine inactive (freeze-thawed aliquot,
  carrier-free protein diluted without BSA, wrong dilution) or the flask overgrown
  before plating. Check the photograph from the morning of the plating day.
- Suppression everywhere, including M(-): vehicle above 0.1%.
- LPS wells inconsistent: LPS not vortexed, aggregates pipetted unevenly.
- Cells not attached by Wednesday: plated too cold, or the suspension sat too long
  before plating.

### Output

Plate map with the plating time, lot numbers and dilution tubes of the stimuli, and
the photograph of each condition on Wednesday morning.

---

<!-- file: protocols/C3_flow_cytometry.md -->

## C3 Flow cytometry of polarized RAW 264.7

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | C3 |
| Used in | Exp 1 (core: polarized RAW cells, week 2); X02 (extension: peritoneal cells on the same panel) |
| Hands-on time | 2 h staining, 1 h acquisition (plus 2.5 h if the intranuclear option is run) |
| Wall-clock time | half a day; fixed samples can be acquired the next day |
| Resources | hood, cooled centrifuge with plate rotor, heating block, cytometer slot reserved by the facility `[TODO: instrument, slot dates]`, FlowJo seat |
| Depends on | C2 unchallenged 6-well per state, 24 h after polarization |
| Lab SOP | Zindel lab "Flow cytometry" (v2.0, 2026-02-16) and "Flow cytometry antibody titration" (v1.0, 2025-08-22); panels in the lab's panel workbook. The SOP wins over this page. |

### Purpose

Phenotype your group's polarization on the course antibody panel, in week 2: the
vehicle control, M(polarizer) and the LPS control, harvested on Wednesday morning
after about 19 h, stained and fixed the same day, acquired on Thursday morning and
gated in the FlowJo session on Thursday afternoon. The LPS control must show CD86 and
scatter up and the vehicle control must not; only then does the polarizer's result
count. Flow on challenged cells (week 3) is an extension and needs a slot from the
facility's regular booking calendar. The panel is shared
with the peritoneal cells extension (X02) so that in vitro and tissue cells can be compared
directly in the same session. In the core it is run on RAW cells only.

### Materials

Course panel. The rows with a clone are antibodies the lab runs and has titrated
on peritoneal cells (dilution factors from the lab's panel workbook, titrated with
1 × 10^6 cells in 50 µL). The others are not in the lab's stock yet.

| Marker | Purpose | Lab reagent (fluorochrome, clone, catalogue number) | Dilution |
|---|---|---|---|
| Viability dye | exclude dead cells | Fixable Viability Dye eFluor 506 (Thermo 65-0866-18) | 1:500–1:700 |
| CD45 | haematopoietic | BUV496, clone I3/2 (BD 752411) | 1:300 |
| CD11b | myeloid | APC-Cy7, clone M1/70 (BioLegend 101226) | 1:400 |
| F4/80 | macrophage; hi on LPM, lo on SPM | BUV395, clone T45-2342 (BD 565614) | 1:150 |
| MHCII (I-A/I-E) | M(IFNγ) in vitro; SPM in vivo | AF700, clone M5/114 (56-5321-82) | 1:150 |
| ICAM2 (CD102) | resident LPM | FITC, clone 3C4 (116129) | 1:200 |
| Gata6 (intranuclear) | resident LPM transcription factor | PE, clone D61E4 (Cell Signaling 26452S), with isotype control | 1:100 |
| Ly6C | monocytes | PerCP-Cy5.5, clone HK1.4 (Thermo 45-5932-82) | 1:400 |
| CD19 | B cells in peritoneal samples | Spark Blue 550 (BioLegend 115566) | 1:800 |
| CD86 | M(IFNγ) | `[TODO: not in the lab panel; order and titrate]` | |
| CD206 | M(IL-4) | `[TODO: not in the lab panel for mouse; order and titrate]` | |
| Tim4 | resident LPM, optional beside Gata6 | `[TODO: not in the lab panel]` | |
| Arg1 (intracellular) | M(IL-4); optional, high risk | PE or APC, clone A1exF5, with isotype `[TODO: order and titrate]` | |
| Intracellular Nos2 | optional | `[TODO: not in the lab panel]` | |

> [!IMPORTANT]
> **To verify:** the fluorochrome choices come from a panel built for the lab's
> 5-laser instrument at Bern (BD LSRII SORP, with a spectral option). Rebuild the
> panel with the ETH flow facility for the instrument the course gets, and keep the
> clones. Titrate CD86 and CD206 before the course; the activation readout rests on
> them.

- FACS buffer (the lab calls it "MACS buffer"), 500 mL: 478 mL PBS, 15 mL FCS
  (3%), 2 mL 0.5 M EDTA (2 mM), 5 mL 1 M HEPES (10 mM). Buffer recipes are in the
  protocol index.
- Fc block: anti-mouse CD16/32 (BioLegend 101302), 1:100
- UltraComp eBeads compensation beads (Thermo 01-2222-42)
- eBioscience Foxp3 / Transcription Factor Staining Buffer Set (Thermo 00-5523-00)
  for the Gata6 and other intranuclear options
- 96-well V-bottom plate (Faust 6091901), flow tubes with cell-strainer cap
- Trypan blue (Sigma T8154), Neubauer chamber or Countess III with slides (Thermo
  C10228)

### Before you start

- Cytometer slot confirmed: Thursday 25 March, two batches of 1.5 h, two groups
  each `[TODO: facility reservation]`. FlowJo session the same afternoon, teaching
  seats `[TODO: check with Florian Mair]`.
- Staining plan in the notebook: samples, unstained, live/dead control, single
  stains on beads, FMOs for MHCII, CD86 and CD206.
- Cells harvested by scraping into cold FACS buffer and counted: at least
  0.5 × 10^6 cells per stain (the antibodies were titrated with 1 × 10^6).
- Work on ice or at 4 °C until fixation; heating block at 95 °C for the live/dead
  control.

### Procedure

1. Harvest the 6-well of each condition (vehicle, polarizer, LPS control) by
   scraping into cold FACS buffer.
   Count. Centrifuge **`300 × g, 5 min, 4 °C`**.
2. Resuspend each sample in 200 µL PBS and transfer to the V-bottom plate.
3. Live/dead control: take 100 µL of one sample into a tube, **`95 °C, 5 min`**, then
   **`on ice, 5 min`**, and add it back to the remaining 100 µL of live cells of that
   well. This well is stained with the viability dye only.
4. Wash all wells with 200 µL PBS; centrifuge **`300 × g, 5 min, 4 °C`**; flick the plate
   to discard the supernatant (the same wash from here on).
5. Viability dye plus Fc block, 50 µL per well in PBS, **`20 min, 4 °C, dark`**.
   Unstained well gets 50 µL PBS. Wash with PBS.

> [!NOTE]
> In PBS, not in buffer: serum quenches the dye.

6. Surface stain: antibody mix in FACS buffer, 50 µL per well, **`20 min, 4 °C, dark`**.
   Unstained and live/dead wells get buffer only. FMO wells get the mix minus one
   antibody.
7. Single stains for compensation on beads, in parallel: vortex the beads 30 s, one
   drop (about 30 µL) made up to 400 µL with buffer serves four wells of 100 µL;
   add 1 µL of one antibody per well, plus one well of beads without antibody.
   **`20 min, 4 °C, dark`**.
8. Wash all wells twice with FACS buffer.
9. Optional intranuclear stain (Gata6, Nos2, Arg1): fixation/permeabilisation
   working solution (1 part concentrate in 4 parts diluent), 50 µL per well,
   **`60 min, 4 °C, dark`**; wash with 1× permeabilisation buffer; intranuclear mix in
   permeabilisation buffer, 50 µL, **`90 min, 4 °C, dark`**; wash with permeabilisation
   buffer. Include the isotype control for Gata6.
10. Resuspend in 200 µL FACS buffer and filter through the strainer cap into flow
    tubes. Keep on ice in the dark; fixed samples can be acquired the next day.
11. Acquire on the facility cytometer with the compensation controls recorded in
    the same session. Record at least 10,000 live single cells per sample
    `[TODO: confirm with the facility]`.
12. Export FCS files named with group, date, sample.

#### Optional: intracellular Arg1, the high-risk arm

Arg1 is cytoplasmic, so it is stained after the surface stain and after fixation and
permeabilization with the Foxp3 buffer set, following the kit insert: fix **`30 min`**,
wash twice in permeabilization buffer, Fc block, stain Arg1 and its isotype **`30 min`** in
permeabilization buffer, wash twice, resuspend in FACS buffer. Permeabilization costs
some surface signal, so the surface markers go on first and the FMOs are run on
permeabilized cells too. Expect a small shift in M(IL-4) at best: the induction is
reliable at the mRNA level in RAW 264.7 and modest as protein. The group that takes
this arm learns fixation and permeabilization, and says on the poster that the arm
was high risk by design `[TODO: titrate the clone before the course]`.

### Controls

- Unstained and single-stain beads for compensation; the heat-killed live/dead well
  for the viability gate.
- FMO for MHCII, CD86 and CD206: the markers that carry the result.
- Isotype control and FMO for Gata6 or Arg1 if an intracellular option is run.
- M(-) as the reference state.

### Checkpoints

- Viability above 80% in the vehicle well; the LPS control may be lower.
- LPS control: CD86 up, FSC and SSC up, compared with the vehicle well. If not, the
  staining or the cells failed and the polarizer is not judged on this run.
- MHCII and CD86 higher in M(IFNγ) than M(-), CD206 higher in M(IL-4): if neither
  moves, check the stimulation before the staining.
- Arg1 by intracellular stain shows at most a small shift in M(IL-4); the FMO and
  the isotype decide whether it is real. No shift is a result, not a failure.

### Known failure modes

- RAW cells clump after scraping: the EDTA in the buffer helps; filter through the
  strainer cap and pipette gently.
- Autofluorescence in activated cells: use the FMOs, not the unstained control, to
  set gates.
- Dim viability stain: dye diluted in buffer instead of PBS.
- ICAM2 and Gata6 negative on every RAW sample: expected. No in vitro cell falls
  into the large-peritoneal-macrophage gate; that is a result.

### Output

FCS files, compensation matrix, staining plan. Gating in FlowJo (licences from the
facility `[TODO: confirm seats and whether they run on student laptops]`); export
gated population statistics as CSV into the notebook. Do not try to gate in R.

---

<!-- file: protocols/C4_prr_challenge.md -->

## C4 Danger-signal challenge: PAMPs, DAMPs and inhibitors

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | C4 |
| Used in | Exp 3 (week 3, Wednesday), on the cells polarized the day before (C2) |
| Hands-on time | 45 min to challenge, 45 min to harvest |
| Wall-clock time | overnight, about 16 h (default, IL-6 readout) or 6 h (alternative, TNF readout) |
| Resources | hood, incubator shelf, plate centrifuge, −20 °C and −80 °C freezers |
| Depends on | the 96-well plate seeded with the polarizer on Tuesday (C1, C2); ELISA plates coated on Wednesday afternoon (C5) |
| Lab SOP | Zindel lab "RAW 264.7 polarisation" (v1.0, 2025-12-08), stimulation and harvesting sections. The SOP wins over this page. |

### Purpose

Test the pathway your group drew on the first afternoon: which ligand, which
receptor, and how you prove that it is this receptor and not something else in the
tube. Every group shares LPS on M(-) as the positive control; your group adds one
stimulus from the menu, optionally one inhibitor, and reads IL-6 (default) or TNF
(alternative) in the supernatant (C5). The cells go to the freezer as RNA or
protein lysate for the extensions; flow on challenged cells only if the group finds
a slot in the facility's regular booking calendar.

### The menu

PAMPs. All of these are known to work in RAW 264.7, which expresses TLR2, TLR3,
TLR4, TLR7, TLR9 and Dectin-1.

| Stimulus | Receptor | Working concentration | Note |
|---|---|---|---|
| LPS (E. coli O111:B4, ultrapure), lab stock; tube L1 from C2 | TLR4 | 100 ng/mL | validated in the lab; the control every group shares |
| Pam3CSK4 | TLR1/2 | 1 µg/mL | strong IL-6 and TNF; the control that must survive TAK-242 |
| Poly(I:C), high molecular weight | TLR3 | 10 µg/mL | strong IFN-β, modest TNF and IL-6; read IL-6 |
| R848 | TLR7 | 1 µg/mL | strong TNF and IL-6 |
| CpG ODN 1826 | TLR9 | 1 µM | strong TNF and IL-6 |
| Zymosan, depleted | Dectin-1 | 10 µg/mL | particulate; TNF and IL-6 moderate |
| Heat-killed bacteria (HKLM or HKEB) | TLR2 and others | 10^8 cells/mL | the whole-pathogen contrast; cheap and robust |

Not on the menu: flagellin, because RAW 264.7 cells express little TLR5, and MDP
alone, because NOD2 needs a TLR signal beside it.

DAMPs. The honest situation: most DAMPs speak through IL-1β, which needs priming and
is not on the ELISA, and recombinant DAMPs are often endotoxin-contaminated. One
option is in the core, the rest only with qPCR.

| Stimulus | Receptor | Working concentration | Note |
|---|---|---|---|
| Necrotic lysate of your own RAW cells | TLR2, TLR4, RAGE and others | lysate of 10^6 cells/mL, three freeze-thaw cycles, cleared, 1:10 | the only DAMP whose signal needs no priming and carries no reagent risk; expect a small IL-6 and TNF signal; test it with polymyxin B |
| HMGB1, disulfide form, endotoxin-free | TLR4, RAGE | 1 µg/mL | extension with X01 only; small signal, redox-form dependent |
| ATP, MSU crystals, nigericin | P2X7, NLRP3 | 1 to 5 mM; 100 µg/mL; 10 µM | extension with X01 only; need LPS priming and read IL-1β |

Inhibitors. The part of your drawing that says "and this is how we know".

| Inhibitor | What it does | Working concentration | Use |
|---|---|---|---|
| TAK-242 (resatorvid) | blocks TLR4 signalling at the receptor | 1 µM, 1 h before the stimulus; vehicle 0.1% DMSO | proves TLR4: your stimulus loses its signal, Pam3CSK4 keeps it |
| Polymyxin B | binds lipid A and neutralises LPS itself | 10 µg/mL, mixed with the stimulus 30 min before adding | proves contamination: a "DAMP" or a lab-made reagent that loses its signal with polymyxin B was endotoxin |

Readout and timing, your choice:

| Option | Challenge | Harvest | Cytokine | Why |
|---|---|---|---|---|
| Default | Wednesday 09:00 | Thursday 09:00, about 16 h (the lab validated 17:00 to 09:00) | IL-6, kit in stock | IL-6 accumulates overnight; the validated condition |
| Alternative | Wednesday 09:00 | Wednesday 15:00, 6 h | TNF, kit pre-bought | TNF peaks at 4 to 6 h and decays overnight |

Another cytokine on request, if its kit arrives in time.

> [!IMPORTANT]
> **To verify:** only the LPS ladder has been run in the lab (100 ng/mL for 16 h
> gives about 300 pg/mL IL-6 from 2 × 10^4 cells in 200 µL, see C5). All other
> working concentrations are literature values; order PAMPs and inhibitors
> endotoxin-tested (InvivoGen or equivalent); suppliers and catalogue numbers
> `[TODO]`.

- Complete medium, warm
- 96-well V-bottom plate (Faust 6091901) for clearing the supernatants
- Labelled tubes or a sealed plate for the frozen aliquots; lysis buffer for RNA
  (X01) or protein, labelled tubes, −80 °C box

### Before you start

- The plate map, drawn on Tuesday with C2: M(-), M(-) + LPS, M(pol), M(pol) + LPS,
  M(-) + your stimulus, M(pol) + your stimulus, in triplicate, plus the inhibitor
  wells (M(-) + your stimulus + inhibitor, M(-) + LPS + inhibitor, and the vehicle
  well the inhibitor needs). The LPS wells of the polarization control are not
  challenged again.
- Prepare the 100× stocks of the stimuli and inhibitors in complete medium as in
  C2 and one master mix per condition (7 µL of each 100× per 700 µL medium). Vortex
  LPS between steps.
- Necrotic lysate: scrape 10^6 of your own cells into 1 mL medium, freeze at −80 °C
  and thaw at 37 °C three times, centrifuge **`900 × g, 5 min`**, keep the supernatant
  on ice and use it the same day at 1:10.
- The ELISA plates are coated on Wednesday at 16:30 (C5), 30 min at the bench, so
  that they are ready on Thursday morning.

### Procedure

1. Wednesday 08:00 to 09:00 (self-study hour), TAK-242 wells only: add the 100×
   inhibitor or its vehicle and incubate **`1 h`**. Polymyxin B is mixed into the stimulus
   master mix **`30 min`** before step 2.
2. Wednesday 09:00: remove the medium from the polarized wells and add the condition
   mixes according to the plate map, 200 µL per 96-well. Record the clock time.

> [!NOTE]
> The polarizer is part of every mix of a M(pol) well, so the state is kept
> during the challenge.

3. Incubate at **`37 °C, 5% CO2`**: **`overnight`** to Thursday 09:00 (default) or
   **`6 h`** to 15:00 (alternative). Record the real time.
4. Photograph the wells before harvest; the morphology of challenged cells is part
   of the record.
5. Harvest: transfer 180 µL supernatant per well into a V-bottom 96-well plate in
   the same layout. Centrifuge the plate **`900 × g, 5 min`**, to remove cells and debris.
6. Transfer the cleared supernatant to a fresh plate or tubes without touching the
   pellet, in aliquots: one for the ELISA (C5, the same day or Thursday), the rest
   frozen at −20 °C as a reserve.

> [!WARNING]
> Avoid repeated freeze-thaw; one aliquot per assay.

7. Cells: wash once with DPBS, then lyse in the well, RNA lysis buffer for X01 or
   protein lysis buffer, and freeze at −80 °C, labelled by well.

### Controls

- Unstimulated M(-): baseline, and M(pol) alone: what polarization does by itself.
- LPS on M(-): the positive control every group shares; if it is negative, the
  reagent or the cells are the problem, not your stimulus.
- Medium-only well from C1: detects a contaminated reagent, which shows as cytokine
  in a well that never saw cells.
- Inhibitor vehicle: DMSO at 0.1% on LPS wells.
- Pam3CSK4 with TAK-242: TLR2 must survive the TLR4 inhibitor, or the inhibitor is
  toxic rather than specific.
- LPS with polymyxin B: proves that polymyxin B works before you trust it on your
  DAMP.

### Checkpoints

- The plate map and the pathway drawing are in the notebook before the first pipette
  is touched.
- At harvest: LPS wells are visibly activated. If not, do not harvest yet; ask.

### Known failure modes

- Flat response everywhere: LPS inactive (ultrapure LPS loses activity when stored
  diluted; make the 100× stocks fresh), or endotoxin contamination of the
  "unstimulated" medium making every well look stimulated. The medium-only control
  separates the two.
- Your stimulus works but polymyxin B kills it: it was endotoxin. That is a result,
  and the most common one in the DAMP literature.
- TAK-242 kills everything including Pam3CSK4: toxicity or vehicle; check the
  morphology before harvest.
- Triplicates far apart: uneven seeding (C1), aggregates, or pipetting order.
  Record the order.
- Debris in the ELISA: supernatant taken before or without the 900 × g spin.

### Output

Plate map with challenge and harvest times, tube or plate labels, freezer
positions of supernatants and lysates, and the photograph before harvest.

---

<!-- file: protocols/C5_elisa.md -->

## C5 ELISA for IL-6 or TNF

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | C5 |
| Used in | Exp 3 |
| Hands-on time | 3–4 h, with incubation waits, plus coating the day before |
| Wall-clock time | 2 days (coating overnight) |
| Resources | plate reader (450 nm; the lab uses a Promega GloMax Discover), multichannel pipette, plate washer or wash bottle, bench space |
| Depends on | C4 supernatants (overnight default, 6 h alternative); plates coated on Wednesday 16:30 |
| Lab SOP | Zindel lab "RAW 264.7 polarisation" (v1.0, 2025-12-08), harvesting section, and the kit insert of the Invitrogen Mouse IL-6 Uncoated ELISA Kit (88-7064-88). The kit insert wins over this page. |

### Purpose

Quantify IL-6 or TNF in the challenge supernatants. Both are NF-κB outputs of the
TLR pathway and the main readout of whether polarization primes or suppresses the
response. Your group chooses one, and the choice is part of the plan:

- IL-6 accumulates over the night and is strongest in the overnight supernatant.
  It is the cytokine the lab validated (worked example below).
- TNF peaks 4 to 6 h after the stimulus; the overnight supernatant still contains
  it, but less. A group that picks TNF either accepts a decayed signal or adds a
  6 h arm (C2, step 6) and harvests it the same afternoon.

A group that wants robust data picks IL-6. The mouse IL-6 kit is in stock, the TNF kit
is pre-bought; another cytokine can be ordered if its kit arrives in time.

In the course rhythm the plates are coated on Wednesday at 16:30 of week 3 (30 min at
the bench, overnight at 4 °C), blocking and samples run on Thursday morning, the
3.5 h of incubations are used for the next steps and the dry lab, and detection and
read-out follow from 15:00.

### Materials

- Mouse IL-6 Uncoated ELISA Kit (Invitrogen 88-7064-88): capture and detection
  antibodies, standard, coating buffer, assay diluent, streptavidin-HRP, TMB, stop
  solution. Standard range 7.8 to 500 pg/mL.
- Mouse TNF ELISA kit `[TODO: the lab has run IL-6 only; choose the matching
  uncoated TNF kit of the same series]`
- High-binding 96-well ELISA plates (Nunc MaxiSorp or as the kit recommends)
- Supernatants from C4, cleared at 900 × g, or thawed aliquots on ice
- Complete medium for diluting samples where needed
- Plate reader at 450 nm. The kit recommends subtracting a 570 nm reading; the lab's
  GloMax Discover reads 450 nm without a reference filter, which worked for the
  example below.

### Before you start

- Kit insert read once completely. Coat the plate with capture antibody the day
  before (overnight at 4 °C), block it in the morning while C4 harvests.
- Plate map for the ELISA plate drawn in the notebook: standard curve in duplicate
  (7 points, 2-fold from 500 pg/mL, plus blank), samples in the layout of the
  culture plate, dilutions.
- Dilution: with the 96-well format of C4 (2 × 10^4 cells, 200 µL, 16 h) the neat
  supernatant of LPS-challenged M(-) lands inside the standard range (about
  300 pg/mL at 100 ng/mL LPS in the lab's hands). Run every sample neat on the
  first plate; add a 1:5 dilution in assay diluent for the M(IFNγ)-primed LPS wells,
  which may run higher. Use the dilution that lands in range for the rest.

### Procedure

1. Follow the kit insert step by step. In outline: coat 100 µL capture antibody
   per well **`4 °C, overnight`**; wash; block **`room temperature, 1 h`**; wash; add
   100 µL standard or sample per well, **`room temperature, 2 h`**; wash; detection
   antibody **`1 h`**; wash; streptavidin-HRP **`30 min`**; wash; TMB
   **`about 15 min, dark`**; stop solution. Washes are 3 to 5 times with the kit's
   wash buffer.

> [!WARNING]
> Do not let wells dry.

2. Standard curve: 2-fold series from 500 pg/mL in assay diluent, duplicate,
   7 points plus blank (0 pg/mL).
3. Samples at the dilutions from the plate map.
4. Read at 450 nm (with 570 nm reference if the reader has it) within the time the
   kit specifies after the stop solution.
5. Export the raw absorbance table, named with group, date, plate, analyte, and
   write a tidy CSV with one row per well (see the worked example for the columns).

### Controls

- Blank (0 pg/mL standard): background, subtracted from every well.
- LPS on M(-): the positive control shared by all groups.
- Medium-only well from C1 run as a sample: detects reagent contamination.

### Checkpoints

- The standard curve is monotonic and the top standard is below saturation of the
  reader (the lab's top standard reads about OD 2.9, close to the ceiling; do not
  extend the curve upward).
- At least one dilution of every sample falls inside the standard range; otherwise
  rerun that sample at another dilution.

### Known failure modes

- Samples above the top standard: dilute more.
- High blank: insufficient washing or contaminated diluent.
- Edge wells drifting: evaporation during incubation; cover the plate.
- Values at or below the lowest standard (unstimulated wells): a real result, not a
  failure. Report them as "below 7.8 pg/mL".

### Worked example: IL-6 after an LPS dose ladder

In September 2026 the lab stimulated RAW 264.7 (2 × 10^4 cells per 96-well, 200 µL,
16 h) with vehicle or 0.1, 1, 10 and 100 ng/mL LPS in triplicate, cleared the
supernatants and ran the IL-6 kit above with a 500 to 7.8 pg/mL standard in
duplicate, read at 450 nm. The raw ODs are in
[`code/elisa/example_data/il6_lps_raw264_2026-09.csv`](../code/elisa/example_data/il6_lps_raw264_2026-09.csv)
and the analysis is [`code/elisa/elisa_standard_curve.R`](../code/elisa/elisa_standard_curve.R).

![IL-6 ELISA worked example: standard curve and IL-6 per LPS dose](figures/C5_il6_worked_example.png)

What you see: the curve is drawn far beyond the standards so that the whole S of the
four-parameter logistic fit is visible. The kit range, shaded, sits on the
lower limb, which is why it looks close to linear on this log axis; the inflection is
at about 630 pg/mL and the upper plateau at OD 6.6 is beyond what the reader can
measure, so a sample above the top standard cannot be back-calculated, only diluted. Vehicle and 0.1 ng/mL LPS are
below the lowest standard, 1 ng/mL gives about 30 pg/mL, 10 ng/mL about 140 pg/mL
and 100 ng/mL about 320 pg/mL, with triplicate wells within 15%. The 100 ng/mL
point is the LPS control of C4: a neat supernatant lands in the upper third of the
curve, which is where you want it.

Run it yourself: open the script in RStudio and press Source. For your own plate,
change the file name in the `input` line.

The script subtracts the blank, fits the standard curve (4PL), back-calculates every sample
with its dilution factor, marks wells outside the standard range, and writes
`elisa_results.csv`, `elisa_summary.csv` and the figure. Your CSV needs the columns `well`, `type`
(standard or sample), `condition`, `standard_pg_ml`, `replicate`, `od450` and
`dilution_factor`.

### Output

Raw export, the tidy CSV, the ELISA plate map, dilution factors per sample, and the
results files from the script. Concentrations are reported in pg/mL; where cell
numbers differ between wells, normalise per cell.

---

# Extension protocols

<!-- file: protocols/X01_qpcr.md -->

## X01 RNA isolation and qPCR (extension)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

> Extension. Requires the 6 h lysate arm to be planned into Exp 3 at the challenge
> step, 24-well plates in C1, and the RNA, cDNA and qPCR reagents below. Ask your
> supervisor before week 3.

| | |
|---|---|
| ID | X01 |
| Used in | Extension |
| Hands-on time | 1 h at challenge (lysates), then about 1.5 days for RNA, cDNA and qPCR |
| Wall-clock time | 6 h for the lysate arm, then 2 days |
| Resources | hood, −80 °C freezer, RNA bench with PCR hood, NanoDrop, thermal cycler, Roche LightCycler 480 II |
| Depends on | C2 and C4; extra 24-well plate in the C4 plate map |
| Lab SOP | Zindel lab 032 "Nanodrop" (v1.0, 2025-08-11), 033 "Reverse transcription" (iScript version, v1.0, 2025-08-11), 034 "SYBR Green real-time PCR" and 034 "TaqMan real-time PCR" (v1.2, 2025-10-09). The SOP wins over this page. |

### Purpose

Measure transcripts of outputs, receptors and transcription factors in the
polarized and challenged states, to ask whether polarization changes the receptor,
the output, or both.

### Materials

- Lysis buffer and RNA isolation kit `[TODO: the lab's RNA extraction SOP is not
  in the protocol collection; name the kit]`
- NanoDrop, 1.2 µL per measurement, ultrapure water for the blank
- cDNA: iScript cDNA Synthesis Kit (Bio-Rad 1708890); RNase-free tubes, thermal
  cycler. (The lab also has an Omniscript protocol with random primers; iScript is
  the simpler one for the course.)
- qPCR, SYBR chemistry: SYBR Green master mix `[TODO: the lab's SYBR product]`,
  primers ordered from Microsynth (0.04 µmol, desalted, dried), 384-well plate
  (Axygen for LightCycler 480, Merck AXYPCR384LC480WNF) or 96-well, sealing foil
  (Sarstedt 95.1999), ultrapure water (Thermo 10977035)
- qPCR, probe chemistry (alternative): FastStart Universal Probe Master with ROX
  (Merck 4913949001) and TaqMan assays; housekeeper eukaryotic 18S (Thermo 4352930E)
- Housekeepers the lab uses with SYBR: Gapdh and Rps29. Targets: outputs Il6, Tnf,
  Il1b, Nos2, Arg1, Retnla, Chil3, Mrc1; receptors Tlr4, Tlr2, Tlr9, Clec7a, Tlr7;
  transcription factors Irf5, Irf4, Socs1, Socs2 `[TODO: primer sequences from the
  literature, validated by melting curve]`
- RNase Zap (Invitrogen AM9780)

### Before you start

- Add a 6 h arm to the C4 plate map on a 24-well plate (1.2 × 10^5 cells per well,
  C1): the same states and conditions, in triplicate, harvested at 6 h instead of
  16 h.

> [!NOTE]
> A 96-well gives too little RNA for 500 ng per cDNA reaction.

- Clean the bench and the PCR hood with RNase Zap and ethanol; RNase-free tips.

### Procedure

1. At 6 h after challenge: aspirate the medium, lyse the cells directly in the well
   with lysis buffer, transfer to a tube, freeze at −80 °C.
2. Isolate RNA per kit. Measure on the NanoDrop: blank with 1.2 µL ultrapure
   water, clean the pedestals between samples, 1.2 µL sample. Accept A260/280 of
   1.8–2.0 (below 1.7 the sample is not used) and A260/230 of 2 or above.
3. cDNA with iScript, 10 µL per reaction on ice in the PCR hood: 2 µL 5× reaction
   mix, 0.5 µL reverse transcriptase, 500 ng RNA in at most 7.5 µL, RNase-free water
   to 10 µL. Cycler: **`5 min 25 °C, 20 min 46 °C, 1 min 95 °C, hold 4 °C`**. Store at
   −80 °C or use directly.
4. Dilute the cDNA 1:8 in ultrapure water.
5. Primer mix per gene: 10 µL forward (100 µM) + 10 µL reverse (100 µM) + 80 µL
   water.
6. qPCR plate on ice, SYBR, 384-well: 5 µL master mix + 0.5 µL primer mix + 0.5 µL
   water per well, then 4 µL diluted cDNA (96-well: 10 + 1 + 1 µL, then 8 µL cDNA).
   Technical duplicates or triplicates. Seal firmly, press the edges, centrifuge
   **`500 × g, 2 min`**.
7. LightCycler 480 II: new experiment from the lab's SYBR template, assign
   replicates and targets in the sample editor, run. Analysis: absolute
   quantification, second-derivative maximum, check that replicate curves overlap
   and drop a replicate whose Cp is clearly off; melting curve analysis, one peak
   per primer pair. Export the Cp table.
8. Each group runs the housekeepers, the output genes relevant to its axis, Nos2,
   Arg1, Tlr4 and the receptor of its axis.

### Controls

- No-RT control per sample.
- No-template control per primer pair.
- M(-) unstimulated as the ΔΔCt reference.

### Checkpoints

- RNA A260/280 about 2.0; housekeeper Cp values within 1 cycle across samples.
- One melting peak per primer pair; a second peak means primer dimers or an
  unspecific product, and the pair is not used.

### Known failure modes

- Housekeepers drift with stimulation: use the mean of both and report it.
- Late Cp for receptors in M(IL-4): may be real suppression; the no-RT control says
  whether the signal is genomic.
- Plate seal lifting at the edges: evaporation, outlier wells at the border.

### Output

Cp CSV, plate layout, ΔΔCt against M(-) unstimulated in the R template, plots by
state and stimulus, housekeepers named.

---

<!-- file: protocols/X02_peritoneal_cells_flow.md -->

## X02 Peritoneal cells on the shared flow panel (extension)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

> Extension. Depends on primary material: we may be able to provide peritoneal
> lavage cells that are surplus from ongoing experimental work in the lab. Whether
> and when such a suspension is available is decided with your supervisor on the
> first afternoon; the cells arrive ready, on ice, as a suspension.

| | |
|---|---|
| ID | X02 |
| Used in | Extension |
| Hands-on time | 30 min receiving, counting and lysis, then staining as C3 |
| Wall-clock time | half a day, coordinated with a cytometer slot |
| Resources | ice, cooled centrifuge, counter, cytometer slot |
| Depends on | C3 panel and a reserved cytometer slot; polarized RAW cells ready on the same day; a surplus peritoneal cell suspension provided by staff |
| Lab SOP | Zindel lab "Flow cytometry" (v1.2) and "Flow cytometry antibody titration" for the staining; the SOP wins over this page. |

### Purpose

Run resident tissue macrophages, obtained without digestion, on the shared panel in
the same session as the polarized RAW cells. The first result, before any
activation marker, is that no in vitro cell falls into the large-peritoneal-
macrophage gate.

### Materials

- FACS buffer, ice-cold: PBS, 3% FCS, 2 mM EDTA, 10 mM HEPES (recipe in the
  protocol index)
- 15 mL or 50 mL tubes, labelled, on ice
- ACK erythrocyte lysis buffer if the suspension is bloody (recipe in the protocol
  index)
- Counter, FACS reagents as in C3

### Before you start

- Confirm with your supervisor that a surplus suspension is available on a day
  with a cytometer slot, and that your polarized RAW cells are ready the same day.
- C3 staining plan extended with the peritoneal samples, CD19 and Ly6C.
- Record what the staff tell you about the sample: source of the material, date,
  volume, any treatment it carries over from the experiment it came from.

### Procedure

1. Receive the suspension on ice.

> [!WARNING]
> Keep it cold from here on; peritoneal macrophages adhere to plastic within
> minutes at room temperature.

2. Centrifuge **`300 × g, 5 min, 4 °C`**. If the pellet is red, resuspend in 1 mL ACK
   buffer, **`room temperature, 2 min`**, top up with buffer and centrifuge again.
3. Resuspend in FACS buffer and count. Expect large peritoneal macrophages to be
   roughly a third of the cells in a healthy sample.
4. Stain with the course panel (C3), including CD19 and Ly6C, and acquire in the
   same session as the polarized RAW cells.
5. Gate: CD19 out, then F4/80 against MHCII for large (F4/80 high, MHCII low) and
   small (F4/80 low, MHCII high) peritoneal macrophages; ICAM2 and Gata6 confirm the
   resident identity. Overlay the polarized RAW cells on the same gates.

### Controls

- CD19 gate removes B cells; F4/80 against MHCII separates large and small
  peritoneal macrophages; ICAM2 and Gata6 confirm resident identity.
- Same single-stain and fluorescence-minus-one controls as C3; the peritoneal
  sample and the RAW cells share the compensation.

### Checkpoints

- A clear F4/80 high, MHCII low population exists in the peritoneal sample before
  anything else is interpreted; if it is missing, note the sample history and ask.

### Known failure modes

- Low cell number: the suspension was small or lost cells on the way; stain what
  you have and reduce the panel rather than the cell number per tube.
- Bloody suspension: lyse the erythrocytes and note it.
- Few large peritoneal macrophages: prior inflammation in the experiment the sample
  came from; record the sample history and treat the result as a finding.

### Output

Cell counts, sample metadata as provided by staff, FCS files, and the gated
statistics side by side with the RAW samples.

---

<!-- file: protocols/X03_tissue_sections_ihc.md -->

## X03 F4/80 immunohistochemistry on tissue sections (extension)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

> Extension. Depends on primary material: we may be able to provide fixed tissue or
> paraffin blocks that are surplus from ongoing experimental work in the lab. Plan
> with your supervisor on the first afternoon; processing, embedding and sectioning
> by the facility span several days, so the tissue has to be committed in week 1.

| | |
|---|---|
| ID | X03 |
| Used in | Extension |
| Hands-on time | 1 h sectioning, 2 × 3 h staining |
| Wall-clock time | about 5 days (processing and embedding by the facility, sectioning, two staining days) |
| Resources | fume hood, histology facility for processing, embedding and sectioning `[TODO: ETH facility and turnaround]`, pressure cooker, histology bench, slide scanner `[TODO: instrument]` |
| Depends on | surplus fixed tissue or paraffin blocks provided by staff |
| Lab SOP | Zindel lab 011 "IHC staining (Biotin ABC)" (v1.0, 2026-07-16) and 01 "HE staining" (v1.0, 2026-03-18); both paraffin protocols. The SOP wins over this page. |

### Purpose

Test the hypothesis that every tissue contains F4/80-positive macrophages, in the
tissue available to your group, by single-colour immunohistochemistry on paraffin
sections, with an H&E serial section for orientation.

### Materials

- Fixed tissue in 70% ethanol or paraffin blocks, as provided; cassettes
- Paraffin processing, embedding and 3.5 µm sections by the histology facility;
  coated slides
- Deparaffinisation and dehydration: xylene, 100%, 95% and 70% ethanol, distilled
  water
- Antigen retrieval: citrate buffer pH 6 (10× stock diluted to 1× in distilled
  water, 200 mL), pressure cooker
- TBS and TBS with Tween 20 (TBST)
- Protein block and antibody diluent: 3% goat serum, 0.5% casein, 0.025% Tween 20,
  0.1% sodium azide in TBS
- Primary antibody: rat anti-mouse F4/80 `[TODO: FFPE-compatible clone and
  dilution; the lab SOP does not fix the clone]`
- 3% hydrogen peroxide in TBS (17 mL 35% H2O2 to 200 mL)
- Biotinylated secondary anti-rat, 1:200 in diluent
- VECTASTAIN Elite ABC-HRP reagent, ready to use (AdipoGen VC-PK-7100)
- DAB enhanced liquid substrate (Sigma D3939), 1 drop (30 µL) per 1 mL buffer
- Mayer's haematoxylin, HCl-ethanol for differentiation, eosin for the H&E slide
- Eukitt mounting medium, coverslips

### Before you start

- Tissue chosen from what staff can provide; ask for a piece of spleen as the
  positive control whenever one is available.
- Record what the staff tell you about the sample: tissue, fixation date, and the
  experiment it came from.
- Slides labelled with pencil (solvent-proof).

> [!CAUTION]
> Formaldehyde and xylene handled in the fume hood.

### Procedure

1. The tissue arrives fixed. Transfer to 70% ethanol if it is not already, and hand
   the cassettes to the histology facility for processing, paraffin embedding and
   3.5 µm sections. Ask for serial sections: one for F4/80, one for the no-primary
   control, one for H&E. Blocks that arrive already embedded skip to sectioning.
2. Deparaffinise: 2 × xylene **`3 min`**, 2 × 100% ethanol **`5 min`**, 95% ethanol
   **`3 min`**, 70% ethanol **`3 min`**, distilled water **`5 min`**.
3. Antigen retrieval in 1× citrate buffer pH 6 in the pressure cooker,
   **`110 °C, 15 min`**; let cool **`25–30 min`**. Rinse in TBS **`4 min`**.
4. Block with protein blocking solution, **`30 min, room temperature`**.
5. Primary F4/80 in antibody diluent, **`4 °C, overnight`**. The no-primary section
   gets diluent only.
6. Day 2: rinse in cold TBST **`4 min`**. Quench endogenous peroxidase with 3% H2O2 in
   TBS, **`10 min`**. Rinse TBST **`4 min`**.
7. Biotinylated secondary 1:200 in diluent, **`1 h, room temperature`**. Rinse TBST
   **`4 min`**.
8. ABC-HRP reagent, **`30 min, room temperature`**. Rinse TBST **`4 min`**.
9. Develop with DAB, watching under the microscope until the positive control is
   brown and the no-primary section is still clean; rinse in distilled water.
10. Counterstain: Mayer's haematoxylin **`7 min`**, rinse in running tap water until
    clear, differentiate with 1–2 dips of HCl-ethanol, blue under running tap water
    **`10 min`**.
11. Dehydrate: 70% ethanol **`1 min`**, 2 × 95% **`1 min`**, 3 × 100% **`1 min`**,
    ethanol/xylene 1:1 **`1 min`**, 3 × xylene **`1 min`**. Mount with Eukitt.
12. H&E on the serial section per the lab SOP: haematoxylin as above, eosin
    **`1 min 15 s`**, 1–3 dips 70% ethanol, dehydrate, mount.
13. Image on the slide scanner. Submit the scan and a short legend to the atlas.

### Controls

- No-primary section: secondary, ABC and DAB background.
- Spleen, when available: positive control; red-pulp macrophages are bright.

### Checkpoints

- Positive control brown, no-primary section clean: the stain works and the tissue
  result can be read.

### Known failure modes

- Everything brown: endogenous peroxidase not quenched, or DAB developed too long.
- Nothing brown, positive control included: primary not FFPE-compatible or
  inactive, retrieval skipped, or wrong secondary species.
- Sections lifting off: retrieval too harsh or uncoated slides.

### Reading the result

F4/80 is bright on Kupffer cells, red-pulp macrophages and large peritoneal
macrophages, and dim on alveolar macrophages and lymph node sinus macrophages. A
weak result in lung or lymph node is a finding, not a failure, if the controls are
clean.

### Output

Scanned slides, the legend, and the atlas submission as a merge request; the
hypothesis and its outcome on the poster.

---

<!-- file: protocols/X04_griess.md -->

## X04 Griess assay (nitrite)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

> [!IMPORTANT]
> **To verify:** the lab has no Griess SOP yet. This page is a literature protocol
> and has not been run on course samples.

| | |
|---|---|
| ID | X04 |
| Used in | Exp 3 (extension, on the C4 supernatants) |
| Hands-on time | 1 h |
| Wall-clock time | 1 h |
| Resources | plate reader (540 nm), multichannel pipette |
| Depends on | C4 supernatants (16 h arm) |
| Lab SOP | none yet `[TODO: write and validate a lab SOP, or adopt a commercial kit]` |

### Purpose

Measure nitrite, the stable product of nitric oxide, as the proxy for Nos2 activity.
Nitrite is expected to be highest in M(IFNγ+LPS) and in LPS-challenged M(IFNγ). The
assay is informative in mouse cells only.

### Materials

- Griess reagent A: 1% sulfanilamide in 5% phosphoric acid
- Griess reagent B: 0.1% N-(1-naphthyl)ethylenediamine dihydrochloride in water
  `[TODO: supplier, or a commercial Griess kit]`
- Sodium nitrite standard, 0–100 µM, 2-fold series prepared in complete culture
  medium (the same DMEM with phenol red and FCS as the samples)
- Clear flat-bottom 96-well plate
- Plate reader, 540 nm

### Before you start

- Plate map: standards in duplicate, samples in duplicate, medium blank.
- Use the 50 µL aliquot set aside at the C4 harvest (cleared at 900 × g), or thaw
  the reserve aliquot on ice and spin briefly.

### Procedure

1. Pipette 50 µL supernatant or standard per well.
2. Add 50 µL reagent A. Incubate **`room temperature, 10 min, dark`**.
3. Add 50 µL reagent B. Incubate **`room temperature, 10 min, dark`**.
4. Read absorbance at 540 nm within 30 min.
5. Export the raw table and write a tidy CSV as in C5.

### Controls

- Blank: complete medium without cells.
- Standard curve in the same medium as the samples; phenol red and FCS affect the
  background.

### Checkpoints

- Standards form a pink gradient visible by eye; the blank is pale.
- M(IFNγ+LPS) wells are visibly pinker than M(-) before the plate is read.

> [!IMPORTANT]
> **To verify:** with 2 × 10^4 cells in 200 µL for 16 h, nitrite may stay near the
> detection limit (about 1–2 µM). If the first run reads flat, the Griess arm
> needs the 24-well format or a longer challenge.

### Known failure modes

- Everything pink: nitrite in the medium or the water used for the reagent.
- Nothing pink: wrong wavelength, old reagent B (turns brown), too few cells, or the
  cells really made no nitric oxide, which M(-) and M(IL-4) should not.

### Output

Raw CSV and plate map. Concentrations in µM from the linear standard curve, in the
R template.

---

<!-- file: protocols/X05_mtt.md -->

## X05 MTT assay: metabolic activity as a proxy for cell number

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | X05 |
| Used in | Optional, extension: a growth curve of the stock, or a viability check on wells whose supernatant has been harvested. Not part of the core since the 2026-10-28 revision |
| Hands-on time | 20 min to seed, 40 min for the standard curve and the first read, 20 min per read after that |
| Wall-clock time | 3.5 h per read (3 h MTT, 15 min solubilisation, read), same day |
| Resources | hood, incubator shelf, plate reader with a 560 or 570 nm filter and a reference filter, multichannel pipette, orbital shaker (optional), microscope |
| Depends on | a counted live-cell suspension from C1 step 5 (thaw day) or C1 step 5 |
| Lab SOP | none yet `[TODO]`. This page is built from three published sources, listed at the end; the lab has not run an MTT assay in this format. |

### Purpose

A second, independent growth curve of RAW 264.7 next to the daily flask counts of
C1, and a standard curve that shows what the assay can and cannot resolve. MTT
(3-(4,5-dimethylthiazol-2-yl)-2,5-diphenyltetrazolium bromide) is a yellow,
water-soluble salt that living cells reduce to a purple, insoluble formazan; the
reduction is done by NAD(P)H-dependent oxidoreductases, largely outside the
mitochondria. Dissolve the formazan and the absorbance is proportional to the
number of metabolically active cells, as long as every cell reduces MTT at the
same rate. That condition is the whole lesson of this protocol: the assay counts
metabolic activity, not cells, and the two diverge whenever the metabolic state
changes, for example in freshly thawed cells, in overgrown wells or in polarized
macrophages. The doubling time from X05 is compared with the one from C1 counts;
where they differ, the notebook says which one is trusted and why.

### Materials

- MTT powder `[TODO: order; not in the lab's protocol collection as of 2026-10]`:
  Thermo M6494 (1 g) or Sigma M5655 (500 mg). Light sensitive.

> [!CAUTION]
> MTT is a suspected mutagen: gloves, weigh in a hood or with a mask, solid waste
> as chemical waste.

- MTT stock, 5 mg/mL in DPBS (12 mM): 50 mg MTT in 10 mL sterile DPBS, vortex until
  dissolved, filter through 0.22 µm, 1 mL aliquots in amber or foil-wrapped tubes,
  4 °C in the dark for up to 4 weeks (or −20 °C for longer). A stock that has
  turned blue or green is discarded. One aliquot serves 100 wells.
- Solubiliser, acid isopropanol: 0.04 M HCl in isopropanol. For 10 mL, 400 µL of
  1 M HCl into 9.6 mL isopropanol (or 33 µL of 37% HCl). Room temperature, closed
  bottle, flammable. 100 µL per well; 10 mL serves one plate.
  Alternative when the plate can wait until the next morning: SDS-HCl, 1 g SDS in
  10 mL 0.01 M HCl, 100 µL per well, 4 to 18 h at 37 °C (see Sources).
- Complete medium, warm (recipe in C1). Phenol-red-free DMEM for the MTT step is
  cleaner but not required with the acid solubiliser `[TODO: Gibco 21063029 if the
  lab stocks it]`.
- DPBS (Gibco 14190144) for the outer wells
- 96-well flat-bottom clear plate, reagent reservoir, multichannel pipette, foil
- Plate reader: the lab's Promega GloMax Discover. `[TODO: confirm the absorbance
  filters on the instrument; the textbook wavelength is 570 nm with a 630 nm
  reference. If the GloMax carries 560 and 750 nm, read 560 with 750 as reference
  and say so in the methods.]`

### Before you start

- Plate map drawn in the notebook (template below). Outer wells get 200 µL DPBS
  as an evaporation guard (C1, known failure modes).
- Live count of the suspension done (trypan blue), dilutions calculated so that
  every well receives 100 µL. The whole plate needs about 7 × 10^5 live cells, a
  quarter of a vial; the rest goes into the C1 flask.
- MTT stock and solubiliser at room temperature. Cold solubiliser does not dissolve
  the crystals.
- Plate reader booked at 12:30, 14:30 and 16:00 on the read days, with the filter
  pair tested on an empty plate once before Tuesday.

Plate map, 100 µL per well:

| Columns | Rows | Content | Read on |
|---|---|---|---|
| 1 and 12 | A to H | DPBS, 200 µL | never |
| 2, 3, 4 | A to H | standard curve, one column per replicate: A 8 × 10^4, B 4 × 10^4, C 2 × 10^4, D 1 × 10^4, E 5 × 10^3, F 2.5 × 10^3, G 1.25 × 10^3, H medium only | Wednesday, seeded 09:00, read 14:30 |
| 5, 6, 7 | B to D | 2.5 × 10^3 cells (low density) | Wed 09:00, Thu 09:00, Thu 12:30; one column per read |
| 5, 6, 7 | E to G | 1 × 10^4 cells (high density) | Wed 09:00, Thu 09:00, Thu 12:30; one column per read |
| 8, 9, 10 | B to D | medium only, blank for that read | with its cell column |
| 8, 9, 10 | E to G | 1 × 10^4 cells, spare set (repeat or microscope check) | as needed |
| 5 to 11 | A and H; column 11 B to G | DPBS, 200 µL | never |

The t = 0 point of the growth curve is the seeded cell number, taken from the C1
count on Tuesday. The standard curve, seeded on Wednesday morning from the counted
staff suspension, converts OD into cell number.

### Procedure

Tuesday 13:00 (growth-curve columns, from the C1 thaw suspension or the staff stock
flask)

1. Prepare the two growth-curve suspensions in complete medium: 2.5 × 10^4 cells/mL
   (1.2 mL) and 1 × 10^5 cells/mL (2.2 mL).
2. Fill the outer wells with 200 µL DPBS. Plate 100 µL per well into columns 5 to 7
   and medium only into columns 8 to 10 according to the map. Back into the
   incubator; nothing is read today.

> [!TIP]
> Rock the plate in a cross pattern; do not swirl.


Wednesday 09:00 (standard curve and read 1)

3. Prepare 2.6 mL of 8 × 10^5 live cells/mL from the counted staff suspension, then
   a 1:2 series in complete medium down to 1.25 × 10^4 cells/mL (seven tubes, 1.3 mL
   each is enough). Plate 100 µL per well into columns 2 to 4. Incubate
   **`37 °C, 5% CO2, 2 h`**, so that the cells attach
   `[TODO: confirm 2 h is enough for RAW 264.7 to attach; the source figure used 4 h]`.
4. Add 10 µL MTT stock straight into the medium: at 09:00 to every well of columns
   5 and 8 (read 1), at 11:00 to every well of columns 2 to 4, including the
   medium-only row. Tap the plate gently. Incubate **`37 °C, 3 h, dark`** (plate
   in the incubator is dark enough).
5. Look at a high-density well under the microscope: purple needle-shaped crystals
   in and around the cells, none in the medium-only wells.
6. Without removing the medium, add 100 µL acid isopropanol to each well that
   received MTT. Cover with foil and shake **`15 min`** on the orbital shaker, or
   pipette up and down ten times per well with the multichannel pipette. Check one
   well under the microscope: no crystals left, uniform purple.
7. Read within 1 h at 570 nm (or 560 nm) with the reference filter: 12:30 for read
   1, 14:30 for the standard curve. Export the raw file with the group, date and
   plate map name in the file name.

Thursday (reads 2 and 3)

8. Steps 4 to 7 on columns 6 and 9 at 09:00 (read 12:30) and on columns 7 and 10 at
   12:30 (read 16:00). Record the real clock times; the fit uses the hours since
   seeding, about 19, 43 and 47 h.
9. Before adding MTT, photograph one high-density and one low-density well at
   10×, and record the colour of the medium. Yellow medium in the high-density
   wells on Thursday is noted, not corrected.

Optional, Experiments 2 and 4 (viability after supernatant harvest)

10. After the supernatant has been taken off for ELISA and Griess (C4), add
    100 µL warm complete medium and 10 µL MTT stock to the emptied wells and
    continue from step 4. Blanks are medium-only wells of the same plate. Read
    the result as metabolic activity per well, not as a cell count. A trypan blue
    count of a scraped parallel well is the viability control.

> [!NOTE]
> IFNγ and LPS change macrophage metabolism, and nitric oxide inhibits
> mitochondrial respiration, so a lower OD in M(IFNγ+LPS) wells is expected even
> with no cell death.

### Controls

- Medium-only wells, with MTT and solubiliser, on every read day: the blank. A
  blank above 0.1 OD `[TODO: verify on the GloMax]` points to contaminated medium
  or a reducing compound.
- The day-0 standard curve: eight points in triplicate. It gives the OD per
  10^4 cells, the lowest density the assay distinguishes from blank, and the
  density at which the curve bends. Every later OD is converted to a cell number
  with this curve, and the conversion is only trusted inside its linear range.
- The C1 flask count of the same day: the independent readout. Two curves, two
  doubling times; both go on the poster.
- Known interferences, from the sources: reducing compounds (ascorbic acid,
  glutathione, dithiothreitol, coenzyme A, polyphenols) reduce MTT without cells;
  serum and phenol red raise the background, which the blank removes and the acid
  solubiliser reduces by turning phenol red yellow.

### Checkpoints

- After 3 h MTT: purple crystals in cell wells, none in blanks. Crystals nowhere:
  stock dead (discard if discoloured) or cells dead; check with trypan blue.
- After solubilisation: no crystals under the microscope, uniform colour. Top
  standard between OD 1 and 2. Above 2.5 the reader saturates: halve all densities
  in the next run and record it.
- Standard curve: linear fit with R² above 0.98 over the range used. If the top
  points fall below the line, cap the usable range there and say so in the legend.
- Thursday high-density wells: expected 3 to 9 × 10^4 cells per well at 43 to 47 h
  from a 15 to 24 h doubling time; if the OD is at the top of the standard curve,
  the low-density wells carry the doubling time.

### Known failure modes

- Crystals do not dissolve: solubiliser was cold, or too little mixing. Warm to
  room temperature, mix again, 15 min on the shaker.
- OD drifts between two reads of the same plate: isopropanol evaporates and the
  formazan precipitates. Read within 1 h, keep the foil on until the reader.
- High blank: medium contaminated with cells or bacteria, or a reducing compound.
  Fresh medium, sterile tips, a new MTT aliquot.
- Doubling time from MTT shorter than from the counts: per-cell MTT reduction
  rises as the thawed cells recover, which inflates the slope. Say so, and use the
  C1 counts for the number on the poster.
- Doubling time from MTT longer than from the counts: high-density wells left the
  linear range, or the medium turned acidic. Use the low-density wells only.
- Edge effect: unequal ODs across a replicate column with the outermost well off.
  The DPBS guard was skipped or the lid sat crooked. Note the well as excluded.

### Output

Raw reader exports (one file per read day, named group_date_X05), the plate map,
blank-subtracted ODs, the standard-curve fit (slope, intercept, R², linear range),
cell numbers per well, the plot of log cell number against time for both densities,
the doubling time with the formula, and the same plot next to the C1 counts
`[TODO: growth-curve template in code/]`. Every deviation from this page in the
notebook.

### Sources, and which value comes from where

This protocol was assembled from three documents on 2026-10-27, not from a lab SOP.

- **Mosmann 1983**, J Immunol Methods 65:55–63, the original assay: MTT 5 mg/mL in
  PBS, 10 µL per 100 µL well, 4 h at 37 °C, 100 µL acid isopropanol (0.04 M HCl
  in isopropanol) added to the well without removing the medium, mixed until the
  crystals dissolve, read within 1 h at 570 nm with a 630 nm reference; the acid
  turns phenol red yellow so that it does not interfere. Read via the citations in
  the Thermo manual below; the paper itself is `[TODO: add PDF to the lab's
  literature folder]`.
- **Thermo Fisher, CyQUANT MTT Cell Proliferation Assay Kit, MAN0019028 Rev. B.0,
  2021-09-02** (the former Vybrant kit; MTT powder M6494): 12 mM stock from 5 mg
  MTT in 1 mL PBS, stored at 4 °C for up to 4 weeks protected from light; 10 µL
  per 100 µL well; 4 h or overnight at 37 °C, 2 h above 10^5 cells per well;
  SDS-HCl (1 g SDS in 10 mL 0.01 M HCl), 100 µL per well, 4 to 18 h at 37 °C,
  longer incubations lower the sensitivity (Niks 1990); read at 570 nm; a rapid
  variant with 50 µL DMSO read at 540 nm; linearity up to about 10^6 Jurkat cells
  per well after 4 h attachment; seed 5,000 to 10,000 cells per well to reach
  optimal density in 48 to 72 h; strong recommendation against phenol red. Cites
  Mosmann 1983, Berridge and Tan 1993 and Liu et al. 1997 for the mechanism.
- **Abcam, MTT Cell Proliferation Assay Kit ab211091, protocol book v2d,
  2026-03-12** (the kit behind the Abcam protocol page): aspirate the medium, 50 µL
  serum-free medium plus 50 µL MTT reagent per well, 3 h at 37 °C, 150 µL MTT
  solvent, 15 min on an orbital shaker under foil, read at 590 nm; background
  wells with serum-free medium; warm solvent, never cold; serum and phenol red
  listed as interferences; a list of reducing compounds that give false signal;
  a discoloured reagent is discarded; 5,000 to 10,000 cells per well as seeding
  guidance. The kit's reagent and solvent compositions are not disclosed.

What was taken from where:

| Item in this page | Value | Source |
|---|---|---|
| MTT stock | 5 mg/mL in DPBS, 12 mM, filtered, 4 °C dark, 4 weeks | Mosmann; Thermo |
| MTT per well | 10 µL into 100 µL | Mosmann; Thermo |
| MTT incubation | 3 h | Abcam (Mosmann and Thermo use 4 h; 3 h fits the course day) |
| Solubiliser | 0.04 M HCl in isopropanol, 100 µL, medium not removed | Mosmann |
| Mixing | 15 min orbital shaker under foil, or pipetting | Abcam |
| Read | within 1 h, 570 nm, reference 630 nm | Mosmann (Abcam kit reads 590 nm) |
| Reader | GloMax Discover, filters to confirm | lab, C5 |
| Seeding guidance | 5,000 to 10,000 cells per well for 48 to 72 h | Abcam; Thermo |
| Course densities | 2.5 × 10^3 and 1 × 10^4 per well | this page: chosen so that the wells stay well below 3 × 10^5 at 48 h with a 15 to 24 h doubling time (lab SOP 0203) |
| Standard curve range | 1.25 × 10^3 to 8 × 10^4 per well | this page, inside the Thermo linearity statement |
| Attachment before day-0 MTT | 2 h | this page, to verify; Thermo figure used 4 h |
| Phenol red, serum | blanks; acid solvent; phenol-red-free optional | Mosmann; Thermo; Abcam |
| Interfering compounds | ascorbate, glutathione, DTT, coenzyme A, polyphenols | Abcam FAQ |
| Warm solvent | never cold | Abcam |
| Polarized cells caveat | metabolic state changes MTT reduction | Berridge and Tan 1993, Liu 1997, via Thermo; the NO and respiration point is textbook macrophage biology, see background section 5.4 |
| Complete medium, DPBS, plate, outer-well guard | lab recipes | C1 |

---

# Notebooks: the lab notebook rules

<!-- file: notebooks/README.md -->

## Notebooks

← Back to the [course script](../README.md#readme)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

Your lab notebook lives here, one file per person, on your group's branch. On main
this folder holds only this page.

### The first commit, Friday of week 1

1. In RStudio, with the course project open and your group's branch selected in the
   Git pane: File, New File, Text File.
2. Write a few first notes: who you are, what your group plans to test.
3. Save it in this folder under a name you like, for example `notebooks/anna.md`.
4. In the Git pane tick the file, press Commit, write `hello world` as the message,
   press Commit, then Push.
5. Reload your branch on github.com: your file is there, with your name on the
   commit. That is the whole workflow; everything after this is the same four
   buttons.

### From then on

- Pull when you sit down, push when you get up, at least once a day.
- One file per person. Nobody edits someone else's notebook file, so there is
  nothing to merge. Shared text, such as the poster, has one owner at a time.
- Write what you did, when, with which protocol and which tube, and what you saw,
  including the things that went wrong. The history of this folder is half of the
  group grade (Section 6 of the script): the way there counts as much as the poster.
- Figures and scripts go next to the code, not in here; a notebook entry links to
  them by file name.
- If git refuses to do what you expect, do not guess: send the group name to Joel.
  The fix arrives as a commit that starts with `support:`.

---

# Admission sheet: safety and data

<!-- file: safety/README.md -->

## Admission sheet for the Blockrophage course: safety and data

← Back to the [course script](../README.md#readme)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

Read this sheet before the first day, bring it to the safety briefing on Thursday
18 March 2027, 09:00, and sign the last section after the briefing. The signed
sheet is your admission to the bench. It covers two things: the safety rules
(sections 1 and 2; together with the briefing they are your whole safety
instruction for the course) and what happens with the data you produce (section 3).

### 1. Where these rules come from

Every lab at ETH works under the ETH Zürich biosafety concept for level 1 and 2
laboratories, published by Safety, Security, Health and Environment (SSHE,
[Biosafety concept](https://ethz.ch/content/dam/ethz/associates/services/Service/sicherheit-gesundheit-umwelt/files/biosicherheit_neu/en/Biosafety_concept.pdf)).
The regulations require that every new person is instructed by the group leader or
a delegate and that the instruction is recorded in writing. This sheet is that
instruction, condensed to what applies to you, but if you have never read the
ETH-wide regulation by the SSHE, please read it.

### 2. Specifically for this course you need to know

**Where and when.** HPL, F floor. Course hours 08:00 to 17:00, Tuesdays from
13:00; lab work outside these hours needs to be approved by the course coordinator,
overnight presence is prohibited; overnight steps run in the incubator without you.
The briefing walks you through the escape routes and the assembly point in front of
the HPL building, the eyewash and emergency shower, the first-aid kit, the spill kit
and the fire extinguisher of the floor. Doors and windows stay shut while you work;
bags, jackets and phones stay at the desk, not on the bench.

**Biosafety level.** The core programme is level 1 work: RAW 264.7 is a mouse cell
line, not a pathogen and not a genetically modified organism, and the stimuli are
purified. Optional extensions that use surplus primary mouse material are level 1
work as well. Please let us know in confidence about pregnancies, morbidities, or
allergies (e.g. nitrile or latex); if necessary, the work is adapted without anyone
else knowing.

**Protection and conduct.** Lab coat closed, nitrile gloves at the cabinet and with
every chemical below, safety glasses at the bench whenever a chemical is open (not
needed inside the cabinet), closed shoes, long hair tied. Coat and gloves stay in
the lab: not in the seminar room, the office, the toilet or the corridor. Gloves
come off before you touch a door handle, a phone, a keyboard or the microscope,
and are changed at once when contaminated. No food, no drink; no pipetting by
mouth; no touching of mouth or eyes while working; hands are washed when you leave.
Work so that nothing splashes and no aerosol forms: tubes closed when not in use,
centrifuge only closed tubes in a balanced rotor with the lid on, and open the lid
after the rotor has stopped.

**The biosafety cabinet.** It protects you from aerosols and the samples from contamination, not from contact and not
from chemical vapours. Switch it on and let it run before you start; work only
when the green light is on and the sash is at its mark; keep the front grille
free; wipe the surface with 70% ethanol before and after, wiping, not spraying;
no open flame; slow movements; everything you need goes in before you begin, so
that your hands stay inside and never go to your face. At the end, waste out,
surface wiped, cabinet to stand-by or UV as the lab does it. When the alarm
sounds, finish the step in a controlled way and call your supervisor (IMHS 6.2.2;
ETH annex 6).

**Chemicals of this course**, with the one rule each that matters. The safety data
sheets are in the lab's SDS folder. Anything that gives off
vapour, PFA, DAB and the MTT solubiliser, is handled in the fume hood, never in
the biosafety cabinet.

| Reagent | Where | Hazard | Rule |
|---|---|---|---|
| DMSO (freezing medium) | S01 | carries whatever is dissolved in it through skin | gloves; change them at once on contact |
| MTT | X05 | suspected mutagen, light sensitive | weigh in the fume hood, gloves, solid and liquid waste as chemical waste |
| Acid isopropanol (0.04 M HCl) | X05 | flammable, mildly corrosive | pour in the fume hood, closed bottle, no flame, chemical waste |
| Trypan blue | C1 | suspected carcinogen | gloves; chemical waste, not the sink |
| Liquid nitrogen | S01 | cold burns; vials can burst on thawing | cryo gloves and face shield when a vial leaves the tank |
| Griess reagent (sulfanilamide, NED, phosphoric acid) | X04 | irritant, acidic | gloves, safety glasses, chemical waste |
| ELISA stop solution (acid) | C5 | corrosive | gloves, safety glasses, multichannel pipette, chemical waste |
| LPS and PRR ligands | C2, C4 | endotoxin; no hazard at the microgram amounts used | do not aerosolise; gloves |
| 70% ethanol | everywhere | flammable | wipe, do not spray; away from flames and hot plates |
| PFA 4% | X03 | toxic fixative | fume hood only, PFA waste container, staff handle it |
| DAB | X03 | suspected carcinogen | staff handle it; DAB waste container |

**Sharps.** The core programme uses no needles and no blades. Scalpels appear only in
the histology extension, in the hands of staff. Anything sharp, including broken
glass, goes into the solid sharps container, never into a bag.

**Spills.** Cells or medium spilled on the bench or in the cabinet: cover with paper
towels, soak them with the lab's disinfectant, wait the contact time, wipe up into the biological waste, wipe once more,
tell your supervisor. Do not spray ethanol onto a spill. A chemical from the table
spilled: step back, tell your supervisor; PFA and DAB spills are cleared by staff.

**Waste.** Four streams, following the IMHS disposal plan (section 6.5).
(1) Liquid culture waste: every used medium and supernatant goes into the liquid
biological waste container at the cabinet. The medium contains penicillin and
streptomycin, which may not go down the drain untreated; the staff autoclave the
container before it goes to the sewer (IMHS 6.5.1.3.4.4). (2) Solid waste that
touched cells, tips, pipettes, tubes, plates, gloves, into the biological waste
bag: never pressed down, closed and handed over at two thirds full. (3) Plates and
liquids that contain a chemical from the table, MTT, acid isopropanol, Griess
reagent, stop solution, trypan blue, PFA, DAB, into the labelled chemical waste
container; they are not autoclaved (IMHS 6.5.1.3.4.6). (4) Everything else is
municipal waste. Nothing goes down the sink except water and buffers without
cells, antibiotics or chemicals. When you are not sure, ask.

**Incidents.** A cut or a stab: rinse, let it bleed, disinfect, cover. A splash in
the eye: fifteen minutes at the eyewash. On skin: soap and water, then
disinfectant. Then tell your supervisor immediately, even for a minor injury; the
supervisor informs the course lead and the biosafety officer, and the incident is
written up on the IMHS report sheet the same day (IMHS 4.3). Fire alarm: leave by
the escape route to the assembly point, no lifts; the course lead counts heads.
Emergency numbers from a lab phone: **888** for the ETH Emergency Desk (fire,
first aid, chemicals), **0-144** for the ambulance, **0-118** for the fire brigade;
from a mobile the Emergency Desk is **044 342 11 88**. Alarm first, then the
supervisor, then the course lead.

### 3. Your data

`[TODO: wording to be checked by the ETH Legal Office before the first run]`

**What this covers.** Everything you produce in the course: raw instrument files
(FCS files, plate reader exports), counts, images, plate maps, analysis code and
results, your notebook and the poster.

**Who it belongs to.** The experiments run on the lab's cells, reagents and
instruments, under the lab's supervision. The data belong to the Zindel lab at ETH
Zürich, also after you leave the course. Where you hold rights in what you produce,
for example copyright in a text, a figure or code, you transfer them to ETH Zürich
as far as the law allows.

**Open access.** The lab may publish the data, in full or in part, open access under
the CC BY 4.0 licence: in the course repository and in the Zenodo record of your
course year. The lab may also use them in teaching, in later runs of the course and
in scientific publications.

**Your name.** You are listed as a contributor in the Zenodo record of your year,
unless you tick the box in section 4. Your commits in the public repository show
your GitHub username in any case.

**What you keep.** You may use your own results for your poster, the exam, your CV
and a later thesis, citing the record of your year.

**What does not go in.** No personal data: notebooks and files contain nothing about
your health or anyone else's, and nothing you told the course lead in confidence.

### 4. Confirmation

I confirm that I have read this sheet, that I attended the safety briefing of the
Blockrophage course on the date below, that my questions were answered, and that I
will follow these rules and ask my supervisor whenever I am not sure. I agree to the
data terms of section 3.

- [ ] Please do not list my name as a contributor in the Zenodo record.

| Name | Date | Signature |
|---|---|---|
| | | |

Course lead: Prof. Joel Zindel (group leader). Briefing and deputy biosafety
officer of the lab: Tea Kocijan. The signed sheets are kept in the lab's biosafety
file with the staff confirmations.

---

# Poster guide

<!-- file: poster/README.md -->

## Poster

← Back to the [course script](../README.md#readme)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

One poster per group, in the ETH corporate design, printed for the poster session on
the last Friday and assessed as a document (Section 6 of the script).

### Template

The poster is made with the **ETH scientific poster template**, provided by ETH
Zürich Corporate Communications:
<https://ethz.ch/staffnet/en/service/communication/corporate-design/templates.html#Plakat>

The download is a ZIP with the template for PowerPoint (`.potx`, portrait and
landscape), for Illustrator (`.ai` and `.ait`) and for LaTeX (`a0poster` class, four
variants: portrait or landscape, white or coloured background, with a README inside).
The template is laid out in A3 and scaled to A0 for printing; keep every figure
vector or at 300 dpi for A0, not for A3.

The template and the ETH logo are ETH's and are intended solely for communication on
behalf of ETH Zürich. They are not part of this repository and not covered by its
CC BY licence; every student downloads the template from the ETH page with their
ETH login, as a member of ETH `[TODO: confirm with Corporate Communications whether
the course may redistribute the template in this public repository]`.

### What the course expects

- Format: A0, portrait or landscape, one poster per group `[TODO: confirm with the
  printer]`.
- Content, in this order: title and group, question, design with controls, results
  (figures with legends stating n), interpretation of the dish-versus-tissue
  comparison, limits, extensions if any, methods with protocol IDs and the commit
  hash of the group branch.
- Printing is your group's own business. When the poster is ready, commit the PDF to
  the group branch and order the print at [Signprint](https://signprint.ch/#about)
  `[TODO: confirm format, turnaround and who pays]`, in time for the poster session
  on Friday 16 April 2027 at 14:00. There is no printing deadline on the plan; plan
  backwards from the turnaround time.
- The writing lecture in week 4 covers how to build the argument from the data, figure
  design, what a good legend does, and how to state limits honestly.

---

# Code overview

<!-- file: code/README.md -->

## Code: the in silico arm

← Back to the [course script](../README.md#readme)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

This course emphasizes reproducible data analysis using a scripted approach in R. 
Most of us use RStudio and we will show you how to clone a project and get started; 
Since the paths are all relative (using the `here()` package) you can in principle
source (or "run") the scripts directly in your local repo.

### The idea: from a tidy CSV to a paper figure

The ELISA analysis is the example. It starts from a tidy CSV, one row per well as
it comes off the plate reader, and ends with a figure as it would go into a paper:
the standard curve, the concentrations, the plot by condition. Everything in
between is code, nothing is done by hand, so the analysis is 100% reproducible:
anyone with the same data and the same code gets the same figure. That is not
always the case in science.

Everyone does the ELISA analysis in the course, on their own plate, and we look at
this code in depth together. For your other assays, qPCR, Griess, or even flow
cytometry, you are encouraged to do the same in R, and we support you. AI tools are
perfect to get started; but you will need to read the code and explain what it
does, and for that the AI tools are a great help too. We provide templates for the
ELISA and for the single-cell analysis of Experiment 2 only; the rest is yours.

### Step 0: the packages

Remember from class: base R comes with many functions, but we often need more.
More comes in packages, written by others and shared through CRAN. This lab works
in the tidyverse dialect of R: `ggplot2` for figures, `dplyr` for tables, `readr`
for reading files. A package is installed once and loaded in every session that
uses it:

```r
install.packages(c("ggplot2", "dplyr", "readr"))   # once: downloads them to your computer
library(ggplot2)                                   # every session: makes its functions available
packageVersion("ggplot2")                          # which version you have
```

That is how you will add any package your own analysis needs later. But packages
come in versions, and versions can differ in what a function does. So that we all
work with the same packages, we install the course packages with a setup script
instead, from a dated snapshot.

Before any script, including the ELISA: once, on the first Friday, we will open
[`00_setup.R`](00_setup.R) in RStudio and press
Source (or `source("code/00_setup.R")` in the console). It installs Seurat,
ggplot2, dplyr, readr, patchwork, here and readxl from a dated package
snapshot: the same versions for everyone. If you already have R projects whose package versions you want to keep: talk to us and we set you up with renv, which keeps the course packages separate. If you
work on Linux: Seurat needs one system library, `sudo apt install libglpk40`. And if your laptop has less than 8 GB of memory, tell us before the course: the
single-cell part needs about 4 GB, and the lab has a few spare machines.

### The templates

We provide templates but expect the students to look at the code, not at the AI tool's
description of the object, and we'll discuss what the code does. And who knows, maybe we 
introduced a couple bugs for teaching purposes.

| Folder | Purpose | Input | Output |
|---|---|---|---|
| [`elisa/`](elisa/README.md) | Four-parameter logistic standard curve, concentration table, plots by condition (C5). Runs on the lab's IL-6 example data | tidy CSV (one row per well) | `elisa_results.csv`, `elisa_summary.csv`, figure |
| [`scrnaseq/`](scrnaseq/README.md) | Experiment 2, three parts (below), five scripts; run from GEO in about 3 min | GEO matrices and a published signature table, downloaded by the scripts | figures, Seurat objects, scores |

### Single-cell RNA-seq (Experiment 2), `scrnaseq/`

One dataset, one standard single-cell workflow; nobody starts from raw reads:
`GSE186658`, single-cell RNA-seq of mouse peritoneal injury sites, sterile or
contaminated (CLP), two mice each (Zindel et al. 2021, Nat Commun). The scripts
download the filtered count matrices from GEO and run everything on a laptop, in
about three minutes ([`scrnaseq/`](scrnaseq/README.md)); the macrophage
subclusters are **not** annotated.

Three parts, matched to the dry-lab halves of weeks 2 and 3:

1. **Load and look** (week 2). Download and load the data, make the QC figure
   (cells per sample before and after filtering), cluster, and find the macrophages
   by `Adgre1`, `Cd68`, `Csf1r`, `Fcgr1` and `Mertk` (`01_load_and_qc.R`,
   `02_cluster.R`).
2. **M1 or M2?** (week 3). Find the markers of the macrophage clusters and decide,
   before any score, which cluster is M1 and which M2 (`03_markers.R`). Then score
   every cell with the classic M1/M2 markers and with the in vitro consensus
   signatures of Colombo et al. 2024 for IFNγ and IL-4 (`04_m1_m2_score.R`). The
   point: the dichotomy is not wrong, it is a description made for one setting and
   one depth of readout; in tissue it fades.
3. **Your own signature** (week 3 to the poster). Pick a macrophage state from the
   single-cell literature (lipid-associated, scar-associated, resident subsets,
   cavity macrophages, ...) or build one from your markers, score it, and put it on
   the poster (`05_own_signature.R`).

Where to go from here, for groups that want more: see
[potential extensions](scrnaseq/README.md#potential-extensions).

The answer key lives in a separate private repository and is released after the
course.

---
