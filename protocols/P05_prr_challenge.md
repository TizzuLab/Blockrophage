# P05 PRR challenge

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P05 |
| Used in | Exp 2 |
| Hands-on time | 45 min to stimulate, 45 min to harvest |
| Wall-clock time | 24 h |
| Resources | hood, incubator shelf, centrifuge, −20 °C freezer |
| Depends on | P04 completed and washed |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

## Purpose

Ask whether polarization changes the response to a danger signal. Every state is
challenged with LPS as the technical control shared by all groups, and with one
further ligand chosen by the group. The readout in the core is the 24 h supernatant
for ELISA (P06) and Griess (P07). The 6 h RNA arm is an extension (X01).

## Materials

| Stimulus | Receptor | Course role | Working concentration |
|---|---|---|---|
| LPS (E. coli O111:B4, ultrapure) | TLR4 | technical control for every group | 100 ng/mL |
| Pam3CSK4 | TLR1/2 | optional axis | 1 µg/mL |
| CpG ODN 1826 | TLR9 | optional axis | 1 µM |
| Zymosan (depleted) | Dectin-1 | optional axis | 10 µg/mL |
| R848 | TLR7 | optional axis | 1 µg/mL |

Working concentrations `[TODO: confirm in the first run; there is no separate
pilot]`. Suppliers and catalogue numbers `[TODO]`.

- Complete medium, warm
- 1.5 mL tubes for supernatant aliquots, labelled

## Before you start

- Draw the plate map in the notebook before you pipette anything. Layout rule:
  3 states (M(-), M(IFNγ), M(IL-4)) × 3 conditions (unstimulated, LPS, chosen axis),
  in triplicate, one time point (24 h). M(IFNγ+LPS) is not re-challenged (P04).
- One well per state stays unstimulated for P08.

## Procedure

1. Dilute the stimuli to working concentration in warm complete medium.
2. Add to the washed wells from P04 according to the plate map. Record the clock
   time.
3. Incubate 24 h.
4. Harvest: transfer the supernatant to a labelled tube, centrifuge 300 × g, 5 min
   to remove cells and debris, transfer the cleared supernatant to a fresh tube.
5. Aliquot: at least two aliquots per well (ELISA, Griess), freeze at −20 °C. Avoid
   repeated freeze-thaw; one aliquot per assay.
6. Photograph the wells before harvest; the morphology of challenged cells is part
   of the record.

## Controls

- Unstimulated well per state: baseline, and the comparison that shows what
  polarization alone does.
- LPS on M(-): the positive control that every group shares; if it is negative, the
  reagent or the cells are the problem, not the axis.
- Medium-only well from P02: detects a contaminated reagent, which shows as
  cytokine in a well that never saw cells.

## Checkpoints

- The plate map is in the notebook before the first pipette is touched.
- After 24 h: LPS wells are visibly activated. If not, do not harvest yet; ask.

## Known failure modes

- Flat response everywhere: LPS inactive (ultrapure LPS loses activity when stored
  diluted), or endotoxin contamination of the "unstimulated" medium making every
  well look stimulated. The medium-only control separates the two.
- Triplicates far apart: uneven seeding (P02) or pipetting order. Record the order.

## Output

Plate map with stimulation and harvest times, tube labels, freezer position, and
the photograph before harvest.
