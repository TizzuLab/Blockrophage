# P04 Polarization of RAW 264.7

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P04 |
| Used in | Exp 2 |
| Hands-on time | 45 min to prepare the stimuli and stimulate, 30 min to wash |
| Wall-clock time | 24 h |
| Resources | hood, incubator shelf, vortex |
| Depends on | P02 plates seeded 24 h earlier (96-well for supernatants, 6-well for flow, 24-well for the RNA arm) |
| Lab SOP | Zindel lab "RAW 264.7 polarisation" (v1.0, 2025-12-08): 96-well format, 100× stimulus stocks, master mixes. The SOP wins over this page. |

## Purpose

Generate the four in vitro states that the course compares with tissue macrophages:
M(-), M(IFNγ), M(IL-4) and M(IFNγ+LPS), named after their stimulus as the field
agreed in 2014. The states are then challenged (P05), read by ELISA and Griess
(P06, P07) and phenotyped on the cytometer (P08).

The lab's own stimulation protocol uses an LPS dose ladder (0.1 to 100 ng/mL) on
RAW 264.7 in 96-well plates. This page keeps its format and its way of preparing
stimuli, and adds the cytokine states the course needs.

## Materials

- Recombinant mouse IFNγ, recombinant mouse IL-4 `[TODO: supplier, catalogue
  number, stock concentration, aliquot storage; the lab has not used these yet]`
- LPS, E. coli O111:B4, ultrapure, lab stock 2.5 mg/mL `[TODO: supplier and
  catalogue number of the lab's stock]`
- Complete medium, warm (recipe in P01); DPBS, warm
- 1.5 mL tubes for the 100× stocks, 5 mL or 15 mL tubes for the master mixes
- Vortex

## Before you start

- Plate map from P02 in front of you. Each state has its challenge wells (P05) and
  its unchallenged wells for flow cytometry (P08).
- Stimuli are added as 100× stocks in complete medium, 1 part in 100, so the medium
  on the cells is replaced once and every well gets the same volume of additive.
- Vortex the LPS vial before use and between every dilution step: LPS aggregates.

## Procedure

1. LPS 100× stock. Dilute the lab stock stepwise in complete medium, as the lab SOP
   does:

   | Tube | From | Add | Result | 100× for |
   |---|---|---|---|---|
   | L1 | LPS stock (2.5 mg/mL) | 2 µL + 498 µL medium | 10,000 ng/mL | 100 ng/mL |
   | L2 | L1 | 50 µL + 450 µL medium | 1,000 ng/mL | 10 ng/mL |

   L1 is the tube used here and in P05; the full ladder (L3, L4) is for the
   dose-response extension.

2. Cytokine 100× stocks: dilute IFNγ and IL-4 to 2 µg/mL in complete medium
   (100× of 20 ng/mL) `[TODO: check against the supplier's recommended working
   range]`.
3. Master mixes, one per state. Per 700 µL of mix add 7 µL of each 100× stock (or
   7 µL plain medium for M(-)). 700 µL feeds three 96-well wells at 200 µL; scale
   up for the 24-well (500 µL per well) and 6-well (2 mL per well) plates and add
   dead volume. Vortex briefly.

   | State | Additive per 700 µL | Final concentration | Time |
   |---|---|---|---|
   | M(-) | 7 µL medium | – | 24 h |
   | M(IFNγ) | 7 µL IFNγ 100× | 20 ng/mL | 24 h |
   | M(IL-4) | 7 µL IL-4 100× | 20 ng/mL | 24 h |
   | M(IFNγ+LPS) | 7 µL IFNγ 100× + 7 µL L1 | 20 ng/mL + 100 ng/mL | 24 h |

4. Remove the old medium from the cells and add the state mix according to the
   plate map: 200 µL per 96-well, 500 µL per 24-well, 2 mL per 6-well. Record the
   clock time.
5. Incubate 24 h at 37 °C, 5% CO2.

   > **To verify:** the lab's validated LPS stimulation runs 16 h, not 24 h. The
   > 24 h polarization follows the 2014 nomenclature paper; confirm in the first run
   > that 24 h of IFNγ or IL-4 gives a visible difference in P08.

6. Wash: aspirate, add warm DPBS gently along the well wall, aspirate; repeat once.
   Add fresh warm complete medium. Every state is washed, including M(-).
7. Hand the plates to P05 (challenge) and keep the unchallenged wells of every
   state for P08.

## Controls

- M(-) is the reference for every comparison.
- M(IFNγ+LPS) is characterised but not re-challenged with LPS: a state that has seen
  LPS shows endotoxin tolerance and would confuse the challenge experiment. Seeing
  tolerance on purpose is an extension (see Section 6 of the script).

## Checkpoints

- After 24 h: M(IFNγ+LPS) wells look different, cells spread and often larger; M(IL-4)
  wells look like M(-). If all four states look identical, check the stock
  dilutions.

## Known failure modes

- No difference between states: cytokine inactive (freeze-thawed aliquot, wrong
  dilution) or cells overgrown at stimulation. Check the plate photograph from P02.
- LPS wells inconsistent: LPS not vortexed, aggregates pipetted unevenly.
- Cells detached after washing: DPBS added onto the cells instead of along the
  wall.

## Output

Plate map with the stimulation and wash times, lot numbers and dilution tubes of the
stimuli, and the photograph of each state after 24 h.
