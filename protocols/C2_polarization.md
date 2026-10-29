# C2 Polarization of RAW 264.7: the menu

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

## Purpose

Give your cells one defined signal and ask whether it changes what they are (week 2,
read by flow cytometry, C3) and how they answer danger (week 3, read by ELISA after
the challenge of C4). Your group picks one polarizer from the menu below. The
polarizer goes into the seeding suspension: plate and polarize in one step on Tuesday
afternoon, harvest or challenge on Wednesday morning. LPS is not a polarizer in this
course; it is the technical positive control on every plate, beside the vehicle
control, so that a polarizer that does nothing can be told from a staining or cell
problem.

## The menu

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

## Materials

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

## Before you start

- The plate map is drawn in the notebook before anything is pipetted. Week 2 (flow
  plate, 6- or 12-well): vehicle, M(pol), LPS control, one well each, a second set if
  you run intracellular Arg1. Week 3 (96-well, C4): the six conditions of the
  challenge in triplicate plus the inhibitor wells.
- Stimuli are added as 100× stocks to the seeding suspension, 1 part in 100, so
  every well gets the same volume of additive and no medium change is needed.
- Vortex the LPS vial before use and between every dilution step: LPS aggregates.
- Retinoic acid: keep the stock and the dilutions in the dark, make the 100× stock
  fresh on the day; serum contains retinoids, so M(-) is not retinoid-free.

## Procedure

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

## Controls

- M(-) or vehicle is the reference for every comparison.
- LPS control: must show CD86 and scatter up by flow (week 2) and cytokine in the
  supernatant (week 3); if it does not, the reagent, the cells or the staining is the
  problem, not your polarizer.
- Endotoxin tolerance: a cell that has already seen LPS answers the next LPS weakly;
  that is why LPS stays out of the polarization and why the LPS control wells are
  never challenged again.

## Checkpoints

- Wednesday 09:00: LPS wells look activated, cells spread and often larger; IFNγ
  wells spread; dexamethasone and IL-10 wells look like M(-) or calmer. If every
  condition looks identical, check the stock dilutions before you blame the biology.

## Known failure modes

- No difference between conditions: cytokine inactive (freeze-thawed aliquot,
  carrier-free protein diluted without BSA, wrong dilution) or the flask overgrown
  before plating. Check the photograph from the morning of the plating day.
- Suppression everywhere, including M(-): vehicle above 0.1%.
- LPS wells inconsistent: LPS not vortexed, aggregates pipetted unevenly.
- Cells not attached by Wednesday: plated too cold, or the suspension sat too long
  before plating.

## Output

Plate map with the plating time, lot numbers and dilution tubes of the stimuli, and
the photograph of each condition on Wednesday morning.
