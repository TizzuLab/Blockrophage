# P04 Polarization of RAW 264.7: the menu

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P04 |
| Used in | Exp 2 and Exp 4, on one plate with P05 |
| Hands-on time | 45 min to prepare the stimuli and stimulate |
| Wall-clock time | overnight, about 18 h, together with the P05 challenge |
| Resources | hood, incubator shelf, vortex |
| Depends on | P02 plates seeded, spun down and left 2 h to adhere on the same afternoon |
| Lab SOP | Zindel lab "RAW 264.7 polarisation" (v1.0, 2025-12-08): 96-well format, 100× stimulus stocks, master mixes. The SOP wins over this page. |

## Purpose

Give your cells one defined signal and ask whether it changes what they are and how
they answer danger. Your group picks one polarizer from the menu below; M(-), the
unstimulated culture, is the reference for everything. The polarizer and the challenge
(P05) go onto the plate together on Tuesday afternoon, one overnight step, which is
how M(IFNγ+LPS) of the 2014 nomenclature is made and how the suppression by IL-10 or
glucocorticoids was described. The textbook alternative, 18 h of polarizer first and
a 6 h challenge on Wednesday, is possible if your supervisor agrees and you accept a
late Wednesday (step 6).

## The menu

| Polarizer | Working concentration | What it does in RAW 264.7 | Safe readout | Risk |
|---|---|---|---|---|
| IFNγ | 20 ng/mL | MHC-II and CD86 up, iNOS primed, TNF and IL-6 amplified with LPS. This is M(IFNγ) and, with LPS, M(IFNγ+LPS) | flow (MHC-II, CD86) and ELISA | low |
| IL-10 | 20 ng/mL | TNF and IL-6 suppressed through STAT3 and SOCS3 | ELISA (suppression) | low; no positive surface marker on the panel |
| Dexamethasone | 100 nM | TNF, IL-6 and NO suppressed through the glucocorticoid receptor; the drug every patient on steroids gets | ELISA (suppression) | low; cheap and stable; needs a vehicle control |
| IL-4 | 20 ng/mL | Arg1, Chil3, Retnla and Mrc1 mRNA up, LPS response dampened. This is M(IL-4) | qPCR Arg1 (X01); ELISA (suppression) | medium: CD206 by flow is weak in this line; intracellular Arg1 (P08) is the high-risk flow option |
| PGE2 | 1 µM | IL-10 up and TNF down through cAMP | ELISA | medium; less canonical; vehicle control |
| ATRA, all-trans retinoic acid | 1 µM, from a DMSO stock, in the dark | In vivo the signal that induces GATA6 and the peritoneal macrophage identity; in vitro it dampens TNF and NO and helps IL-4 induce Arg1. Whether it induces Gata6 in RAW 264.7 is not known | qPCR Gata6, Arg1, Icam2 (X01) | high: the lab's wild card, outcome unknown; for a group that takes the qPCR extension |

> **To verify:** LPS is the only stimulus validated in the lab (100 ng/mL, 16 h,
> see P06). Every row above is a literature dose; working concentrations, suppliers
> and catalogue numbers `[TODO]`. A group that wants robust data stays with LPS on
> M(-) and adds IFNγ. Everything else extends the data for the next iteration of the
> course, and that is said on the poster.

## Materials

- Your polarizer `[TODO: supplier, catalogue number, stock concentration, aliquot
  storage; the lab has not used these yet]`. Recombinant mouse IFNγ, IL-4 and IL-10
  carrier-free, stocks at 100 µg/mL in PBS with 0.1% BSA, aliquoted at −80 °C; a
  carrier-free cytokine diluted without BSA sticks to the plastic. Dexamethasone and
  ATRA as 1 mM stocks in DMSO, PGE2 as 10 mM in ethanol; the vehicle control is the
  same solvent at the same final dilution (0.1%).
- LPS, E. coli O111:B4, ultrapure, lab stock 2.5 mg/mL `[TODO: supplier and
  catalogue number of the lab's stock]`
- Complete medium, warm (recipe in P01); DPBS, warm
- 1.5 mL tubes for the 100× stocks, 5 mL or 15 mL tubes for the master mixes
- Vortex

## Before you start

- The plate map is shared with P05 and is drawn in the notebook before anything is
  pipetted: the six conditions below in triplicate, plus the inhibitor wells of P05,
  plus one set of unstimulated and polarized wells on the flow plate for P08.
- Stimuli are added as 100× stocks in complete medium, 1 part in 100, so the medium
  on the cells is replaced once and every well gets the same volume of additive.
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
   L1 is the tube used here and in P05; the full ladder (L3, L4) is for the
   dose-response extension.
2. Polarizer 100× stock in complete medium: IFNγ, IL-4 or IL-10 at 2 µg/mL (100× of
   20 ng/mL); dexamethasone at 10 µM; PGE2 at 100 µM; ATRA at 100 µM. Vehicle 100×:
   10% DMSO or ethanol in medium, for a final 0.1% `[TODO: check against the
   supplier's recommended range]`.
3. Master mixes, one per condition. Per 700 µL of medium add 7 µL of every 100×
   stock the condition contains and 7 µL plain medium or vehicle where it does not.
   700 µL feeds three 96-well wells at 200 µL; scale up for the flow plate (2 mL per
   6-well) and add dead volume. Vortex briefly.
   | Condition | Additives | Why |
   |---|---|---|
   | M(-) | medium (vehicle) | the reference |
   | M(-) + LPS | L1 | the control every group shares |
   | M(pol) | your polarizer | what the polarizer does alone: flow and baseline cytokine |
   | M(pol) + LPS | polarizer + L1 | does the state change the LPS answer |
   | M(-) + your stimulus | P05 stimulus | your pathway |
   | M(pol) + your stimulus | polarizer + P05 stimulus | your pathway in your state |
   The inhibitor wells of P05 are added to this list where your plan has them.
4. At 2 h after plating (the spun plate of P02), remove the medium and add the
   condition mix according to the plate map: 200 µL per 96-well, 2 mL per 6-well.
   Record the clock time.
5. Incubate overnight at 37 °C, 5% CO2. Harvest with P05 on Wednesday at 09:00.
6. Priming alternative, only with your supervisor's agreement: polarizer alone on
   Tuesday; on Wednesday at 09:00 aspirate, add warm DPBS gently along the well
   wall, aspirate, repeat once, add the P05 condition mixes, challenge 6 h, harvest
   at 15:00. TNF is at its peak then and IL-6 well up; the flow staining of that
   evening starts late.

## Controls

- M(-) is the reference for every comparison; the vehicle control stands in for it
  where the polarizer has a solvent.
- M(-) + LPS is the positive control every group shares; if it is negative, the
  reagent or the cells are the problem, not your polarizer.
- Endotoxin tolerance: a cell that has already seen LPS answers the next LPS weakly.
  Priming with LPS on purpose, and seeing the tolerance, is an extension (Section 6
  of the script).

## Checkpoints

- At harvest: LPS wells look activated, cells spread and often larger; IFNγ wells
  spread; dexamethasone and IL-10 wells look like M(-) or calmer. If every condition
  looks identical, check the stock dilutions before you blame the biology.

## Known failure modes

- No difference between conditions: cytokine inactive (freeze-thawed aliquot,
  carrier-free protein diluted without BSA, wrong dilution) or cells overgrown at
  stimulation. Check the plate photograph from P02.
- Suppression everywhere, including M(-): vehicle above 0.1%, or the cells were
  unhappy after the spin.
- LPS wells inconsistent: LPS not vortexed, aggregates pipetted unevenly.
- Cells detached after a wash (step 6): DPBS added onto the cells instead of along
  the wall.

## Output

Plate map with the stimulation time, lot numbers and dilution tubes of the stimuli,
and the photograph of each condition before harvest.
