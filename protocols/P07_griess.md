# P07 Griess assay (nitrite)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

> **To verify:** the lab has no Griess SOP yet. This page is a literature protocol
> and has not been run on course samples.

| | |
|---|---|
| ID | P07 |
| Used in | Exp 2 |
| Hands-on time | 1 h |
| Wall-clock time | 1 h |
| Resources | plate reader (540 nm), multichannel pipette |
| Depends on | P05 supernatants (16 h arm) |
| Lab SOP | none yet `[TODO: write and validate a lab SOP, or adopt a commercial kit]` |

## Purpose

Measure nitrite, the stable product of nitric oxide, as the proxy for Nos2 activity.
Nitrite is expected to be highest in M(IFNγ+LPS) and in LPS-challenged M(IFNγ). The
assay is informative in mouse cells only.

## Materials

- Griess reagent A: 1% sulfanilamide in 5% phosphoric acid
- Griess reagent B: 0.1% N-(1-naphthyl)ethylenediamine dihydrochloride in water
  `[TODO: supplier, or a commercial Griess kit]`
- Sodium nitrite standard, 0–100 µM, 2-fold series prepared in complete culture
  medium (the same DMEM with phenol red and FCS as the samples)
- Clear flat-bottom 96-well plate
- Plate reader, 540 nm

## Before you start

- Plate map: standards in duplicate, samples in duplicate, medium blank.
- Use the 50 µL aliquot set aside at the P05 harvest (cleared at 900 × g), or thaw
  the reserve aliquot on ice and spin briefly.

## Procedure

1. Pipette 50 µL supernatant or standard per well.
2. Add 50 µL reagent A. Incubate 10 min at room temperature in the dark.
3. Add 50 µL reagent B. Incubate 10 min at room temperature in the dark.
4. Read absorbance at 540 nm within 30 min.
5. Export the raw table and write a tidy CSV as in P06.

## Controls

- Blank: complete medium without cells.
- Standard curve in the same medium as the samples; phenol red and FCS affect the
  background.

## Checkpoints

- Standards form a pink gradient visible by eye; the blank is pale.
- M(IFNγ+LPS) wells are visibly pinker than M(-) before the plate is read.

   > **To verify:** with 2 × 10^4 cells in 200 µL for 16 h, nitrite may stay near the
   > detection limit (about 1–2 µM). If the first run reads flat, the Griess arm
   > needs the 24-well format or a longer challenge.

## Known failure modes

- Everything pink: nitrite in the medium or the water used for the reagent.
- Nothing pink: wrong wavelength, old reagent B (turns brown), too few cells, or the
  cells really made no nitric oxide, which M(-) and M(IL-4) should not.

## Output

Raw CSV and plate map. Concentrations in µM from the linear standard curve, in the
R template.
