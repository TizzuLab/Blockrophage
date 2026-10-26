# P04 Polarization of RAW 264.7

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

## Purpose

Generate the four in vitro states that the course compares with tissue macrophages:
M(-), M(IFNγ), M(IL-4) and M(IFNγ+LPS), named after their stimulus as the field
agreed in 2014. The states are then challenged (P05), read by ELISA and Griess
(P06, P07) and phenotyped on the cytometer (P08).

## Materials

- Recombinant mouse IFNγ, recombinant mouse IL-4, LPS (E. coli O111:B4, ultrapure)
  `[TODO: supplier, catalogue number, stock concentrations, aliquot storage]`
- Complete medium, warm
- Sterile PBS, warm

## Before you start

- Plate map from P02 in front of you. Each state has its challenge wells (P05) and
  one unchallenged well for flow cytometry (P08).
- Dilute the stimuli in warm complete medium freshly; do not add stock solutions
  directly to wells.

## Procedure

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

## Controls

- M(-) is the reference for every comparison.
- M(IFNγ+LPS) is characterised but not re-challenged with LPS: a state that has seen
  LPS shows endotoxin tolerance and would confuse the challenge experiment. Seeing
  tolerance on purpose is an extension (see the nerd ladder).

## Checkpoints

- After 24 h: M(IFNγ+LPS) wells look different, cells spread and often larger; M(IL-4)
  wells look like M(-). If all four wells look identical, check the reagent dilution.

## Known failure modes

- No difference between states: cytokine inactive (freeze-thawed aliquot, wrong
  dilution) or cells overgrown at stimulation. Check the plate photograph from P02.
- Cells detached after washing: PBS added onto the cells instead of along the wall.

## Output

Plate map with the stimulation and wash times, lot numbers of the stimuli, and the
photograph of each state after 24 h.
