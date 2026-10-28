# P08 Flow cytometry of polarized RAW 264.7

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P08 |
| Used in | Exp 2 (core: polarized RAW cells); X02 (extension: peritoneal cells on the same panel) |
| Hands-on time | 2 h staining, 1 h acquisition (plus 2.5 h if the intranuclear option is run) |
| Wall-clock time | half a day; fixed samples can be acquired the next day |
| Resources | hood, cooled centrifuge with plate rotor, heating block, cytometer slot reserved by the facility `[TODO: instrument, slot dates]`, FlowJo seat |
| Depends on | P04 unchallenged 6-well per state, 24 h after polarization |
| Lab SOP | Zindel lab "Flow cytometry" (v2.0, 2026-02-16) and "Flow cytometry antibody titration" (v1.0, 2025-08-22); panels in the lab's panel workbook. The SOP wins over this page. |

## Purpose

Phenotype the states of your group's design on the course antibody panel: M(-) and
your polarizer, with and without the challenge. The panel is shared
with the peritoneal cells extension (X02) so that in vitro and tissue cells can be compared
directly in the same session. In the core it is run on RAW cells only.

## Materials

Course panel. The rows with a clone are antibodies the lab runs and has titrated
on peritoneal cells (dilution factors from the lab's panel workbook, titrated with
1 × 10^6 cells in 50 µL). The others are not in the lab's stock yet.

| Marker | Purpose | Lab reagent (fluorochrome, clone, catalogue number) | Dilution |
|---|---|---|---|
| Viability dye | exclude dead cells | Fixable Viability Dye eFluor 506 (Thermo 65-0866-18) | 1:500–1:700 |
| CD45 | haematopoietic | BUV496, clone I3/2 (BD 752411) | 1:300 |
| CD11b | myeloid | APC-Cy7, clone M1/70 (BioLegend 101226) | 1:400 |
| F4/80 | macrophage; hi on LPM, lo on SPM | BUV395, clone T45-2342 (BD 565614) | 1:150 |
| MHCII (I-A/I-E) | M(IFNγ) in vitro; SPM in vivo | AF700, clone M5/114 (56-5321-82) | 1:150 |
| ICAM2 (CD102) | resident LPM | FITC, clone 3C4 (116129) | 1:200 |
| Gata6 (intranuclear) | resident LPM transcription factor | PE, clone D61E4 (Cell Signaling 26452S), with isotype control | 1:100 |
| Ly6C | monocytes | PerCP-Cy5.5, clone HK1.4 (Thermo 45-5932-82) | 1:400 |
| CD19 | B cells in peritoneal samples | Spark Blue 550 (BioLegend 115566) | 1:800 |
| CD86 | M(IFNγ) | `[TODO: not in the lab panel; order and titrate]` | |
| CD206 | M(IL-4) | `[TODO: not in the lab panel for mouse; order and titrate]` | |
| Tim4 | resident LPM, optional beside Gata6 | `[TODO: not in the lab panel]` | |
| Arg1 (intracellular) | M(IL-4); optional, high risk | PE or APC, clone A1exF5, with isotype `[TODO: order and titrate]` | |
| Intracellular Nos2 | optional | `[TODO: not in the lab panel]` | |

> **To verify:** the fluorochrome choices come from a panel built for the lab's
> 5-laser instrument at Bern (BD LSRII SORP, with a spectral option). Rebuild the
> panel with the ETH flow facility for the instrument the course gets, and keep the
> clones. Titrate CD86 and CD206 before the course; the activation readout rests on
> them.

- FACS buffer (the lab calls it "MACS buffer"), 500 mL: 478 mL PBS, 15 mL FCS
  (3%), 2 mL 0.5 M EDTA (2 mM), 5 mL 1 M HEPES (10 mM). Buffer recipes are in the
  protocol index.
- Fc block: anti-mouse CD16/32 (BioLegend 101302), 1:100
- UltraComp eBeads compensation beads (Thermo 01-2222-42)
- eBioscience Foxp3 / Transcription Factor Staining Buffer Set (Thermo 00-5523-00)
  for the Gata6 and other intranuclear options
- 96-well V-bottom plate (Faust 6091901), flow tubes with cell-strainer cap
- Trypan blue (Sigma T8154), Neubauer chamber or Countess III with slides (Thermo
  C10228)

## Before you start

- Cytometer slot confirmed; the facility reserves slots for the course, two groups
  per slot.
- Staining plan in the notebook: samples, unstained, live/dead control, single
  stains on beads, FMOs for MHCII, CD86 and CD206.
- Cells harvested by scraping into cold FACS buffer and counted: at least
  0.5 × 10^6 cells per stain (the antibodies were titrated with 1 × 10^6).
- Work on ice or at 4 °C until fixation; heating block at 95 °C for the live/dead
  control.

## Procedure

1. Harvest the unchallenged 6-well of each state by scraping into cold FACS buffer.
   Count. Centrifuge 300 × g, 5 min, 4 °C.
2. Resuspend each sample in 200 µL PBS and transfer to the V-bottom plate.
3. Live/dead control: take 100 µL of one sample into a tube, 95 °C for 5 min, then
   on ice 5 min, and add it back to the remaining 100 µL of live cells of that
   well. This well is stained with the viability dye only.
4. Wash all wells with 200 µL PBS; centrifuge 300 × g, 5 min, 4 °C; flick the plate
   to discard the supernatant (the same wash from here on).
5. Viability dye plus Fc block, 50 µL per well in PBS (not in buffer: serum
   quenches the dye), 20 min, 4 °C, dark. Unstained well gets 50 µL PBS. Wash with
   PBS.
6. Surface stain: antibody mix in FACS buffer, 50 µL per well, 20 min, 4 °C, dark.
   Unstained and live/dead wells get buffer only. FMO wells get the mix minus one
   antibody.
7. Single stains for compensation on beads, in parallel: vortex the beads 30 s, one
   drop (about 30 µL) made up to 400 µL with buffer serves four wells of 100 µL;
   add 1 µL of one antibody per well, plus one well of beads without antibody.
   20 min, 4 °C, dark.
8. Wash all wells twice with FACS buffer.
9. Optional intranuclear stain (Gata6, Nos2, Arg1): fixation/permeabilisation
   working solution (1 part concentrate in 4 parts diluent), 50 µL per well, 60 min,
   4 °C, dark; wash with 1× permeabilisation buffer; intranuclear mix in
   permeabilisation buffer, 50 µL, 90 min, 4 °C, dark; wash with permeabilisation
   buffer. Include the isotype control for Gata6.
10. Resuspend in 200 µL FACS buffer and filter through the strainer cap into flow
    tubes. Keep on ice in the dark; fixed samples can be acquired the next day.
11. Acquire on the facility cytometer with the compensation controls recorded in
    the same session. Record at least 10,000 live single cells per sample
    `[TODO: confirm with the facility]`.
12. Export FCS files named with group, date, sample.

### Optional: intracellular Arg1, the high-risk arm

Arg1 is cytoplasmic, so it is stained after the surface stain and after fixation and
permeabilization with the Foxp3 buffer set, following the kit insert: fix 30 min,
wash twice in permeabilization buffer, Fc block, stain Arg1 and its isotype 30 min in
permeabilization buffer, wash twice, resuspend in FACS buffer. Permeabilization costs
some surface signal, so the surface markers go on first and the FMOs are run on
permeabilized cells too. Expect a small shift in M(IL-4) at best: the induction is
reliable at the mRNA level in RAW 264.7 and modest as protein. The group that takes
this arm learns fixation and permeabilization, and says on the poster that the arm
was high risk by design `[TODO: titrate the clone before the course]`.

## Controls

- Unstained and single-stain beads for compensation; the heat-killed live/dead well
  for the viability gate.
- FMO for MHCII, CD86 and CD206: the markers that carry the result.
- Isotype control and FMO for Gata6 or Arg1 if an intracellular option is run.
- M(-) as the reference state.

## Checkpoints

- Viability above 80% in M(-); M(IFNγ+LPS) may be lower.
- MHCII and CD86 higher in M(IFNγ) than M(-), CD206 higher in M(IL-4): if neither
  moves, check the stimulation before the staining.
- Arg1 by intracellular stain shows at most a small shift in M(IL-4); the FMO and
  the isotype decide whether it is real. No shift is a result, not a failure.

## Known failure modes

- RAW cells clump after scraping: the EDTA in the buffer helps; filter through the
  strainer cap and pipette gently.
- Autofluorescence in activated cells: use the FMOs, not the unstained control, to
  set gates.
- Dim viability stain: dye diluted in buffer instead of PBS.
- ICAM2 and Gata6 negative on every RAW sample: expected. No in vitro cell falls
  into the large-peritoneal-macrophage gate; that is a result.

## Output

FCS files, compensation matrix, staining plan. Gating in FlowJo (licences from the
facility `[TODO: confirm seats and whether they run on student laptops]`); export
gated population statistics as CSV into the notebook. Do not try to gate in R.
