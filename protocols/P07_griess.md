# P07 Griess assay (nitrite)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P07 |
| Used in | Exp 2 |
| Hands-on time | 1 h |
| Wall-clock time | 1 h |
| Resources | plate reader (540 nm), multichannel pipette |
| Depends on | P05 supernatants (24 h arm) |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

## Purpose

Measure nitrite, the stable product of nitric oxide, as the proxy for Nos2 activity.
Nitrite is expected to be highest in M(IFNγ+LPS) and in LPS-challenged M(IFNγ). The
assay is informative in mouse cells only.

## Materials

- Griess reagent A: 1% sulfanilamide in 5% phosphoric acid
- Griess reagent B: 0.1% N-(1-naphthyl)ethylenediamine dihydrochloride in water
  `[TODO: supplier, or a commercial Griess kit]`
- Sodium nitrite standard, 0–100 µM, prepared in complete culture medium
- Clear flat-bottom 96-well plate
- Plate reader, 540 nm

## Before you start

- Plate map: standards in duplicate, samples in duplicate, medium blank.
- Supernatants thawed on ice and briefly spun.

## Procedure

1. Pipette 50 µL supernatant or standard per well.
2. Add 50 µL reagent A. Incubate 10 min at room temperature in the dark.
3. Add 50 µL reagent B. Incubate 10 min at room temperature in the dark.
4. Read absorbance at 540 nm within 30 min.
5. Export the raw table as CSV.

## Controls

- Blank: complete medium without cells.
- Standard curve in the same medium as the samples; phenol red and FBS affect the
  background.

## Checkpoints

- Standards form a pink gradient visible by eye; the blank is pale.
- M(IFNγ+LPS) wells are visibly pinker than M(-) before the plate is read.

## Known failure modes

- Everything pink: nitrite in the medium or the water used for the reagent.
- Nothing pink: wrong wavelength, old reagent B (turns brown), or the cells really
  made no nitric oxide, which M(-) and M(IL-4) should not.

## Output

Raw CSV and plate map. Concentrations in µM from the linear standard curve, in the
R template.
