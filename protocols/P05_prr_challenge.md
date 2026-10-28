# P05 Danger-signal challenge: PAMPs, DAMPs and inhibitors

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P05 |
| Used in | Exp 2 and Exp 4, on one plate with P04 |
| Hands-on time | 45 min to stimulate, 45 min to harvest |
| Wall-clock time | overnight, about 18 h in the course rhythm (the lab validated 16 h) |
| Resources | hood, incubator shelf, plate centrifuge, −20 °C freezer |
| Depends on | P02 plates spun down and adhered for 2 h; the P04 master mixes |
| Lab SOP | Zindel lab "RAW 264.7 polarisation" (v1.0, 2025-12-08), stimulation and harvesting sections. The SOP wins over this page. |

## Purpose

Test the pathway your group drew on the first afternoon: which ligand, which
receptor, and how you prove that it is this receptor and not something else in the
tube. Every group shares LPS on M(-) as the positive control; your group adds one
stimulus from the menu, optionally one inhibitor, and reads IL-6 or TNF in the
supernatant (P06) and the surface phenotype of the cells (P08). Together with P04
this is one plate and one overnight step. The 6 h RNA arm is an extension (X01).

## The menu

PAMPs. All of these are known to work in RAW 264.7, which expresses TLR2, TLR3,
TLR4, TLR7, TLR9 and Dectin-1.

| Stimulus | Receptor | Working concentration | Note |
|---|---|---|---|
| LPS (E. coli O111:B4, ultrapure), lab stock; tube L1 from P04 | TLR4 | 100 ng/mL | validated in the lab; the control every group shares |
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

> **To verify:** only the LPS ladder has been run in the lab (100 ng/mL for 16 h
> gives about 300 pg/mL IL-6 from 2 × 10^4 cells in 200 µL, see P06). All other
> working concentrations are literature values; order PAMPs and inhibitors
> endotoxin-tested (InvivoGen or equivalent); suppliers and catalogue numbers
> `[TODO]`.

- Complete medium, warm
- 96-well V-bottom plate (Faust 6091901) for clearing the supernatants, or 1.5 mL
  tubes for the larger formats
- Labelled tubes or a sealed plate for the frozen aliquots

## Before you start

- Draw the plate map in the notebook before you pipette anything. Layout rule: the
  six conditions of P04 in triplicate, plus your inhibitor wells, M(-) + your
  stimulus + inhibitor and M(-) + LPS + inhibitor, plus the vehicle well the
  inhibitor needs. One time point. One set of M(-) and M(pol) wells on the flow
  plate stays for P08.
- Prepare the 100× stocks of the stimuli and inhibitors in complete medium as in
  P04 and one master mix per condition (7 µL of each 100× per 700 µL medium). Vortex
  LPS between steps.
- Necrotic lysate: scrape 10^6 of your own cells into 1 mL medium, freeze at −80 °C
  and thaw at 37 °C three times, centrifuge 900 × g for 5 min, keep the supernatant
  on ice and use it the same day at 1:10.

## Procedure

1. TAK-242 wells: at 2 h after plating, add the 100× inhibitor or its vehicle to the
   wells that get it and incubate 1 h. Polymyxin B is mixed into the stimulus master
   mix 30 min before step 2.
2. Remove the medium from the adhered wells of P02 and add the condition mixes of P04
   and of this page according to the plate map: 200 µL per 96-well. Record the clock
   time.
3. Incubate overnight at 37 °C, 5% CO2. In the course the challenge is set up on
   Tuesday about 2 h after plating (about 15:00) and harvested on Wednesday at
   09:00, about 18 h; the lab validated 16 h (17:00 to 09:00). Record the real time.
4. Photograph the wells before harvest; the morphology of challenged cells is part
   of the record.
5. Harvest: transfer 180 µL supernatant per well into a V-bottom 96-well plate in
   the same layout. Centrifuge the plate 900 × g, 5 min, to remove cells and debris.
6. Transfer the cleared supernatant to a fresh plate or tubes without touching the
   pellet, in aliquots: one for the ELISA (P06, Thursday), the rest frozen at −20 °C
   as a reserve. Avoid repeated freeze-thaw; one aliquot per assay.
7. The cells of the flow plate are harvested and stained the same afternoon (P08).

## Controls

- Unstimulated M(-): baseline, and M(pol) alone: what polarization does by itself.
- LPS on M(-): the positive control every group shares; if it is negative, the
  reagent or the cells are the problem, not your stimulus.
- Medium-only well from P02: detects a contaminated reagent, which shows as cytokine
  in a well that never saw cells.
- Inhibitor vehicle: DMSO at 0.1% on LPS wells.
- Pam3CSK4 with TAK-242: TLR2 must survive the TLR4 inhibitor, or the inhibitor is
  toxic rather than specific.
- LPS with polymyxin B: proves that polymyxin B works before you trust it on your
  DAMP.

## Checkpoints

- The plate map and the pathway drawing are in the notebook before the first pipette
  is touched.
- At harvest: LPS wells are visibly activated. If not, do not harvest yet; ask.

## Known failure modes

- Flat response everywhere: LPS inactive (ultrapure LPS loses activity when stored
  diluted; make the 100× stocks fresh), or endotoxin contamination of the
  "unstimulated" medium making every well look stimulated. The medium-only control
  separates the two.
- Your stimulus works but polymyxin B kills it: it was endotoxin. That is a result,
  and the most common one in the DAMP literature.
- TAK-242 kills everything including Pam3CSK4: toxicity or vehicle; check the
  viability on the flow plate.
- Triplicates far apart: uneven seeding (P02), aggregates, or pipetting order.
  Record the order.
- Debris in the ELISA: supernatant taken before or without the 900 × g spin.

## Output

Plate map with stimulation and harvest times, tube or plate labels, freezer
position, and the photograph before harvest.
