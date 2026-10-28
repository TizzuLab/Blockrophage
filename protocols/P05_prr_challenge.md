# P05 PRR challenge

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P05 |
| Used in | Exp 2 |
| Hands-on time | 45 min to stimulate, 45 min to harvest |
| Wall-clock time | overnight, about 20 h in the course rhythm (the lab validated 16 h) |
| Resources | hood, incubator shelf, plate centrifuge, −20 °C freezer |
| Depends on | P04 completed and washed |
| Lab SOP | Zindel lab "RAW 264.7 polarisation" (v1.0, 2025-12-08), stimulation and harvesting sections. The SOP wins over this page. |

## Purpose

Ask whether polarization changes the response to a danger signal. Every state is
challenged with LPS as the technical control shared by all groups, and with one
further ligand chosen by the group. The readout in the core is the overnight
supernatant for ELISA (P06) and Griess (P07). The 6 h RNA arm is an extension (X01).

## Materials

| Stimulus | Receptor | Course role | Working concentration |
|---|---|---|---|
| LPS (E. coli O111:B4, ultrapure), lab stock; tube L1 from P04 | TLR4 | technical control for every group | 100 ng/mL |
| Pam3CSK4 | TLR1/2 | optional axis | 1 µg/mL |
| CpG ODN 1826 | TLR9 | optional axis | 1 µM |
| Zymosan (depleted) | Dectin-1 | optional axis | 10 µg/mL |
| R848 | TLR7 | optional axis | 1 µg/mL |

> **To verify:** only the LPS ladder has been run in the lab (100 ng/mL for 16 h
> gives about 300 pg/mL IL-6 from 2 × 10^4 cells in 200 µL, see P06). The other
> working concentrations are literature values; suppliers and catalogue numbers
> `[TODO]`.

- Complete medium, warm
- 96-well V-bottom plate (Faust 6091901) for clearing the supernatants, or 1.5 mL
  tubes for the larger formats
- Labelled tubes or a sealed plate for the frozen aliquots

## Before you start

- Draw the plate map in the notebook before you pipette anything. Layout rule:
  3 states (M(-), M(IFNγ), M(IL-4)) × 3 conditions (unstimulated, LPS, chosen axis),
  in triplicate, one time point. M(IFNγ+LPS) is not re-challenged (P04).
- One set of wells per state stays unstimulated for P08.
- Prepare 100× stocks of the stimuli in complete medium as in P04, and one master
  mix per condition (7 µL of 100× per 700 µL medium). Vortex LPS between steps.

## Procedure

1. Remove the medium from the washed wells of P04 and add the condition mix
   according to the plate map: 200 µL per 96-well. Record the clock time.
2. Incubate overnight at 37 °C, 5% CO2. In the course the challenge is set up on
   Tuesday about 2 h after plating (about 15:00) and harvested on Wednesday at
   09:00, about 18 h; the lab validated 16 h (17:00 to
   09:00). Record the real time.
3. Photograph the wells before harvest; the morphology of challenged cells is part
   of the record.
4. Harvest: transfer 180 µL supernatant per well into a V-bottom 96-well plate in
   the same layout. Centrifuge the plate 900 × g, 5 min, to remove cells and debris.
5. Transfer the cleared supernatant to a fresh plate or tubes without touching the
   pellet: 100 µL goes onto the ELISA plate if P06 runs the same day (the lab starts
   coating and blocking the ELISA plate before harvesting), 50 µL to the Griess
   plate (P07), the rest is frozen at −20 °C as a reserve. Avoid repeated
   freeze-thaw; one aliquot per assay.

## Controls

- Unstimulated well per state: baseline, and the comparison that shows what
  polarization alone does.
- LPS on M(-): the positive control that every group shares; if it is negative, the
  reagent or the cells are the problem, not the axis.
- Medium-only well from P02: detects a contaminated reagent, which shows as
  cytokine in a well that never saw cells.

## Checkpoints

- The plate map is in the notebook before the first pipette is touched.
- At harvest: LPS wells are visibly activated. If not, do not harvest yet; ask.

## Known failure modes

- Flat response everywhere: LPS inactive (ultrapure LPS loses activity when stored
  diluted; make the 100× stocks fresh), or endotoxin contamination of the
  "unstimulated" medium making every well look stimulated. The medium-only control
  separates the two.
- Triplicates far apart: uneven seeding (P02), LPS aggregates, or pipetting order.
  Record the order.
- Debris in the ELISA: supernatant taken before or without the 900 × g spin.

## Output

Plate map with stimulation and harvest times, tube or plate labels, freezer
position, and the photograph before harvest.
