# X01 RNA isolation and qPCR (extension)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

> Extension. Requires the 6 h lysate arm to be planned into Exp 3 at the challenge
> step, 24-well plates in C1, and the RNA, cDNA and qPCR reagents below. Ask your
> supervisor before week 3.

| | |
|---|---|
| ID | X01 |
| Used in | Extension |
| Hands-on time | 1 h at challenge (lysates), then about 1.5 days for RNA, cDNA and qPCR |
| Wall-clock time | 6 h for the lysate arm, then 2 days |
| Resources | hood, −80 °C freezer, RNA bench with PCR hood, NanoDrop, thermal cycler, Roche LightCycler 480 II |
| Depends on | C2 and C4; extra 24-well plate in the C4 plate map |
| Lab SOP | Zindel lab 032 "Nanodrop" (v1.0, 2025-08-11), 033 "Reverse transcription" (iScript version, v1.0, 2025-08-11), 034 "SYBR Green real-time PCR" and 034 "TaqMan real-time PCR" (v1.2, 2025-10-09). The SOP wins over this page. |

## Purpose

Measure transcripts of outputs, receptors and transcription factors in the
polarized and challenged states, to ask whether polarization changes the receptor,
the output, or both.

## Materials

- Lysis buffer and RNA isolation kit `[TODO: the lab's RNA extraction SOP is not
  in the protocol collection; name the kit]`
- NanoDrop, 1.2 µL per measurement, ultrapure water for the blank
- cDNA: iScript cDNA Synthesis Kit (Bio-Rad 1708890); RNase-free tubes, thermal
  cycler. (The lab also has an Omniscript protocol with random primers; iScript is
  the simpler one for the course.)
- qPCR, SYBR chemistry: SYBR Green master mix `[TODO: the lab's SYBR product]`,
  primers ordered from Microsynth (0.04 µmol, desalted, dried), 384-well plate
  (Axygen for LightCycler 480, Merck AXYPCR384LC480WNF) or 96-well, sealing foil
  (Sarstedt 95.1999), ultrapure water (Thermo 10977035)
- qPCR, probe chemistry (alternative): FastStart Universal Probe Master with ROX
  (Merck 4913949001) and TaqMan assays; housekeeper eukaryotic 18S (Thermo 4352930E)
- Housekeepers the lab uses with SYBR: Gapdh and Rps29. Targets: outputs Il6, Tnf,
  Il1b, Nos2, Arg1, Retnla, Chil3, Mrc1; receptors Tlr4, Tlr2, Tlr9, Clec7a, Tlr7;
  transcription factors Irf5, Irf4, Socs1, Socs2 `[TODO: primer sequences from the
  literature, validated by melting curve]`
- RNase Zap (Invitrogen AM9780)

## Before you start

- Add a 6 h arm to the C4 plate map on a 24-well plate (1.2 × 10^5 cells per well,
  C1): the same states and conditions, in triplicate, harvested at 6 h instead of
  16 h.

> [!NOTE]
> A 96-well gives too little RNA for 500 ng per cDNA reaction.

- Clean the bench and the PCR hood with RNase Zap and ethanol; RNase-free tips.

## Procedure

1. At 6 h after challenge: aspirate the medium, lyse the cells directly in the well
   with lysis buffer, transfer to a tube, freeze at −80 °C.
2. Isolate RNA per kit. Measure on the NanoDrop: blank with 1.2 µL ultrapure
   water, clean the pedestals between samples, 1.2 µL sample. Accept A260/280 of
   1.8–2.0 (below 1.7 the sample is not used) and A260/230 of 2 or above.
3. cDNA with iScript, 10 µL per reaction on ice in the PCR hood: 2 µL 5× reaction
   mix, 0.5 µL reverse transcriptase, 500 ng RNA in at most 7.5 µL, RNase-free water
   to 10 µL. Cycler: **`5 min 25 °C, 20 min 46 °C, 1 min 95 °C, hold 4 °C`**. Store at
   −80 °C or use directly.
4. Dilute the cDNA 1:8 in ultrapure water.
5. Primer mix per gene: 10 µL forward (100 µM) + 10 µL reverse (100 µM) + 80 µL
   water.
6. qPCR plate on ice, SYBR, 384-well: 5 µL master mix + 0.5 µL primer mix + 0.5 µL
   water per well, then 4 µL diluted cDNA (96-well: 10 + 1 + 1 µL, then 8 µL cDNA).
   Technical duplicates or triplicates. Seal firmly, press the edges, centrifuge
   **`500 × g, 2 min`**.
7. LightCycler 480 II: new experiment from the lab's SYBR template, assign
   replicates and targets in the sample editor, run. Analysis: absolute
   quantification, second-derivative maximum, check that replicate curves overlap
   and drop a replicate whose Cp is clearly off; melting curve analysis, one peak
   per primer pair. Export the Cp table.
8. Each group runs the housekeepers, the output genes relevant to its axis, Nos2,
   Arg1, Tlr4 and the receptor of its axis.

## Controls

- No-RT control per sample.
- No-template control per primer pair.
- M(-) unstimulated as the ΔΔCt reference.

## Checkpoints

- RNA A260/280 about 2.0; housekeeper Cp values within 1 cycle across samples.
- One melting peak per primer pair; a second peak means primer dimers or an
  unspecific product, and the pair is not used.

## Known failure modes

- Housekeepers drift with stimulation: use the mean of both and report it.
- Late Cp for receptors in M(IL-4): may be real suppression; the no-RT control says
  whether the signal is genomic.
- Plate seal lifting at the edges: evaporation, outlier wells at the border.

## Output

Cp CSV, plate layout, ΔΔCt against M(-) unstimulated in the R template, plots by
state and stimulus, housekeepers named.
