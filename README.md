# Blockrophage course

**The block course about macrophage polarization and their response to danger molecules**\
Zürich, Spring Semester 2027. Zindel lab (TizzuLab).

> **Under construction.** This course runs for the first time in spring 2027 and is
> being built in the open. Interested students are welcome to apply and to give
> input, through the [contact page](https://zindellab.ch/contact.html) or an
> [issue](https://github.com/TizzuLab/blockrophage-course/issues). **Please do not use
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
| Version | 0.5, 2026-10-27 |

## What you need for this course

1. **A GitHub account**, created at [github.com](https://github.com) before the first
   day; the username is sent to us.
2. **Your ok to work on a public repository**, where your edits and your name are
   visible to anyone. This is worth keeping in mind when the account is created.
3. **A laptop**; any operating system works.
4. Optionally, **your favourite LLM as a learning coach**: the LLM-friendly version of
   this repository, the [companion package](#your-companion), is dropped into a
   session.

No prior knowledge; the [lectures](slides/) are optional reading.

## 1. Concept

Every student arrives with the textbook picture of macrophages (which we will refresh in case
you forgot): M1 kills, M2 heals.
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

After this course you will be able to:

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

- Work is planned: the protocol is read the day before, reagents are checked, and the
  controls are designed before anything is pipetted.
- What was planned is done, and what was done is recorded the same day, including
  every deviation.
- Every tube, plate and solution is labelled with content, date and group.
- Enzymes, antibodies and cells are kept at the recommended temperature. Reagents are
  expensive, some are irreplaceable within the course.
- Questions go to your supervisor. Problems go there earlier.

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

## 5. Core experiments

**Experiment 1: can we culture macrophages in vitro?** (week 2) Primary macrophages
do not divide in a dish and die within days, so the field works with a model.
RAW 264.7 is a line established in 1978 from a tumour induced in a BALB/c mouse by
Abelson leukaemia virus: it divides without growth factor, adheres, responds strongly
to LPS and IFNγ, and has been in culture for almost fifty years. What that does and
does not make it is in the
[background](background/macrophage_biology.md#52-level-i-ontogeny). The question is
answered with the simplest readouts there are: the microscope, for morphology and
confluence, and a growth curve from daily counts and an MTT assay, from which a
doubling time is derived and compared with the published value. A culture that doubles at the expected rate, looks right and
survives its own freeze and thaw is fit for Experiment 2. By the end of week 2 you
will have taken this line from vial to vial yourselves. Protocols
[P01](protocols/P01_raw264_thaw_expand.md), [P02](protocols/P02_raw264_split_seed.md),
[P03](protocols/P03_raw264_freeze.md), [P09](protocols/P09_mtt.md).

**Experiment 2: can we polarize them?** (week 3) The textbook states were defined by
what is added: IFNγ, IL-4, or IFNγ with LPS, named M(IFNγ), M(IL-4) and M(IFNγ+LPS)
after the stimulus since the 2014 nomenclature
([background](background/macrophage_biology.md#54-level-iii-function-and-activation-state)).
Exactly that is added to wells of the same culture, with M(-) as the unstimulated
reference, and the question is whether the states separate on the three readouts the
field used to define them: cytokines in the supernatant (IL-6 and TNF by ELISA),
nitric oxide (Griess assay) and surface markers (flow cytometry). If they separate,
the paradigm has been built with your own hands. If they do not, that is a result
too, and the first thing analysed is which readout failed. Protocols
[P04](protocols/P04_polarization.md), [P06](protocols/P06_elisa.md),
[P07](protocols/P07_griess.md), [P08](protocols/P08_flow_cytometry.md).

**Experiment 3: does the profile hold true in vivo?** (dry lab, weeks 2 and 3) A
dish has two states because two were created; a tissue did not read the textbook.
From a public bulk RNA-seq dataset of RAW 264.7 cells under the same stimuli
(GSE113836) the M(IFNγ+LPS) and M(IL-4) gene signatures are derived, then every
macrophage of two single-cell datasets from living systems is scored against them:
injured mouse peritoneum (GSE186658) and homeostatic human peritoneal fluid
(GSE228030). The question is descriptive: do tissue macrophages fall into the two
states, onto a line between them, or somewhere the two axes do not reach? Both
datasets are preprocessed by the teaching staff; nobody starts from raw reads. What
the picture means is something we will work out together at the debriefs. Background
sections on
[why a dish is not a body](background/macrophage_biology.md#58-why-a-dish-is-not-a-body)
and [the dataset](background/macrophage_biology.md#59-the-in-silico-dataset-and-how-single-cell-rna-sequencing-works);
[analysis code](code/README.md).

**Experiment 4: is the heuristic still useful?** (week 3, on the cells of
Experiment 2) A model that fails the test of Experiment 3 may still predict
something. The prediction built into M1/M2 is that the state a macrophage is in
decides how it responds to the next danger signal. Exactly that is tested: M(-),
M(IFNγ) and M(IL-4) are challenged through a pattern-recognition receptor, with LPS
and with the PRR axis your group chose
([background](background/macrophage_biology.md#56-sensing-danger-pattern-recognition-receptors)),
one overnight arm, and the response is measured with the readouts of Experiment 2.
M(IFNγ+LPS) is characterised but not re-challenged, because a cell that has already
seen LPS shows endotoxin tolerance, itself a hint that the states are not fixed.
Whatever is found, one fact is worth keeping in mind: after twenty years of the
paradigm there is no approved therapy that targets macrophage polarization. A
heuristic can be useful at the bench and still have limits in the body. Where those
limits are is something we will think about together, with your data on the table.
Protocols
[P05](protocols/P05_prr_challenge.md), [P06](protocols/P06_elisa.md),
[P07](protocols/P07_griess.md).

**Dry lab, every day.** Half of every day is spent at the keyboard, with the
[analysis code](code/README.md): week 1 the environment, week 2 the templates on
example data and your growth curve, week 3 Experiment 3 and your own flow and ELISA
data, week 4 the poster figures. Gaps are filled with the poster: the introduction is
written first, then the significance.

## 6. Optional experiments

The core programme is composed of mainly established experiments, but students are encouraged
to experiment on their own to complete their story/poster. The availability of surplus primary material, reagents and instruments 
will be made available on day 1 and each group can define additional experiments they would like to attempt.

Some protocols are made available (prefix X... in protocol catalogue), others your group supervisor
may have established, yet others you may need to establish from the literature. Here are some examples of 
what you could do, but the list is non-exhaustive.

| Experiment or extension | What would  |
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
| Data quality and controls, including Experiment 1 | 20% |
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
[`companion/blockcourse-companion.md`](companion/blockcourse-companion.md) is
downloaded, [`COMPANION_PROMPT.md`](COMPANION_PROMPT.md) is pasted as the first
message of a new session, the file is attached, and the result is a private
Blockrophage companion that knows the schedule, the protocols and the background. It
will still be wrong sometimes; the repository, not the model, is the reference.

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
