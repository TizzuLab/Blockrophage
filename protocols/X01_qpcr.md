# X01 RNA isolation and qPCR (extension)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

> Extension. Requires the 6 h lysate arm to be planned into Exp 2 at the challenge
> step, and RNA, cDNA and qPCR kits `[TODO]`. Ask your supervisor before week 3.

| | |
|---|---|
| ID | X01 |
| Used in | Extension |
| Hands-on time | 1 h at challenge (lysates), then about 1.5 days for RNA, cDNA and qPCR |
| Wall-clock time | 6 h for the lysate arm, then 2 days |
| Resources | hood, −80 °C freezer, RNA bench, qPCR instrument `[TODO: platform]` |
| Depends on | P04 and P05; extra wells in the P05 plate map |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

## Purpose

Measure transcripts of outputs, receptors and transcription factors in the
polarized and challenged states, to ask whether polarization changes the receptor,
the output, or both.

## Materials

- Lysis buffer (RLT or TRIzol) `[TODO]`, RNA isolation kit `[TODO]`, cDNA kit
  `[TODO]`, SYBR or probe chemistry `[TODO: platform]`
- Primers: housekeepers Actb, Hprt. Outputs: Il6, Tnf, Il1b, Nos2, Arg1, Retnla,
  Chil3, Mrc1. Receptors: Tlr4, Tlr2, Tlr9, Clec7a, Tlr7. Transcription factors:
  Irf5, Irf4, Socs1, Socs2 `[TODO: sequences or assay IDs]`.

## Before you start

- Add a 6 h arm to the P05 plate map: the same states and conditions, in triplicate,
  harvested at 6 h instead of 24 h.
- RNase-free bench and tips.

## Procedure

1. At 6 h after challenge: aspirate the medium, lyse the cells directly in the well
   with lysis buffer, transfer to a tube, freeze at −80 °C.
2. Isolate RNA per kit; measure concentration and purity.
3. cDNA per kit with equal RNA input per sample.
4. qPCR: each group runs the housekeepers, the output genes relevant to its axis,
   Nos2, Arg1, Tlr4 and the receptor of its axis. Technical duplicates.
5. Export Ct values as CSV.

## Controls

- No-RT control per sample.
- No-template control per primer pair.
- M(-) unstimulated as the ΔΔCt reference.

## Checkpoints

- RNA A260/280 about 2.0; housekeeper Ct values within 1 cycle across samples.

## Known failure modes

- Housekeepers drift with stimulation: use the mean of both and report it.
- Late Ct for receptors in M(IL-4): may be real suppression; the no-RT control says
  whether the signal is genomic.

## Output

Ct CSV, plate layout, ΔΔCt against M(-) unstimulated in the R template, plots by
state and stimulus.
