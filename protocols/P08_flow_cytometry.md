# P08 Flow cytometry of polarized RAW 264.7

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P08 |
| Used in | Exp 2 (core: polarized RAW cells); X02 (extension: lavage cells on the same panel) |
| Hands-on time | 2 h staining, 1 h acquisition |
| Wall-clock time | half a day |
| Resources | hood, centrifuge, cytometer slot reserved by the facility `[TODO: instrument, slot dates]`, FlowJo seat |
| Depends on | P04 unchallenged well per state, 24 h after polarization |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

## Purpose

Phenotype the four in vitro states on the course antibody panel. The panel is shared
with the lavage extension (X02) so that in vitro and tissue cells can be compared
directly in the same session. In the core it is run on RAW cells only.

## Materials

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

## Before you start

- Cytometer slot confirmed; the facility reserves slots for the course, two groups
  per slot.
- Staining plan in the notebook: samples, single stains, FMOs, unstained.
- Cells harvested by scraping into cold FACS buffer, counted; `[TODO: 0.5–1 × 10^6
  cells per stain]`.

## Procedure

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

## Controls

- Unstained and single-stain controls for compensation.
- FMO for MHCII, CD86 and CD206: the markers that carry the result.
- M(-) as the reference state.

## Checkpoints

- Viability above 80% in M(-); M(IFNγ+LPS) may be lower.
- MHCII and CD86 higher in M(IFNγ) than M(-), CD206 higher in M(IL-4): if neither
  moves, check the stimulation before the staining.

## Known failure modes

- RAW cells clump after scraping: filter through a 40 µm strainer or pipette
  gently; EDTA in the buffer helps.
- Autofluorescence in activated cells: use the FMOs, not the unstained control, to
  set gates.
- Tim4 and ICAM2 negative on every RAW sample: expected. No in vitro cell falls into
  the large-peritoneal-macrophage gate; that is a result.

## Output

FCS files, compensation matrix, staining plan. Gating in FlowJo (licences from the
facility `[TODO: confirm seats and whether they run on student laptops]`); export
gated population statistics as CSV into the notebook. Do not try to gate in R.
