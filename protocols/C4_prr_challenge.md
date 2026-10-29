# C4 Danger-signal challenge: PAMPs, DAMPs and inhibitors

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

## Purpose

Test the pathway your group drew on the first afternoon: which ligand, which
receptor, and how you prove that it is this receptor and not something else in the
tube. Every group shares LPS on M(-) as the positive control; your group adds one
stimulus from the menu, optionally one inhibitor, and reads IL-6 (default) or TNF
(alternative) in the supernatant (C5). The cells go to the freezer as RNA or
protein lysate for the extensions; flow on challenged cells only if the group finds
a slot in the facility's regular booking calendar.

## The menu

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

## Before you start

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

## Procedure

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

## Controls

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
  morphology before harvest.
- Triplicates far apart: uneven seeding (C1), aggregates, or pipetting order.
  Record the order.
- Debris in the ELISA: supernatant taken before or without the 900 × g spin.

## Output

Plate map with challenge and harvest times, tube or plate labels, freezer
positions of supernatants and lysates, and the photograph before harvest.
