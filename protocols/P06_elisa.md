# P06 ELISA for IL-6 and TNF

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P06 |
| Used in | Exp 2 |
| Hands-on time | 3–4 h, with incubation waits |
| Wall-clock time | 1 day (overnight coating if the kit requires it) |
| Resources | plate reader, multichannel pipette, plate washer or wash bottle, bench space |
| Depends on | P05 supernatants (24 h arm) |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

## Purpose

Quantify IL-6 and TNF in the challenge supernatants. These are the NF-κB outputs of
the TLR pathway and the main readout of whether polarization primes or suppresses
the response.

## Materials

- Mouse IL-6 and TNF ELISA kits `[TODO: kit, supplier, catalogue number]`
- Supernatant aliquots from P05, thawed on ice
- Complete medium for standard dilution and blanks
- Plate reader at 450 nm (with 570 nm reference) `[TODO: instrument, software]`

## Before you start

- Kit instructions read once completely; coat the night before if required.
- Plate map for the ELISA plate drawn in the notebook: standard curve in duplicate,
  blanks, samples, which dilutions.
- Dilution: supernatants of LPS-stimulated RAW cells are far above the standard
  range. There is no pilot run; in Exp 2 the first ELISA plate includes each sample
  at two dilutions `[TODO: e.g. 1:10 and 1:100 for LPS wells, neat and 1:10 for
  unstimulated]`, and the dilution that lands in the linear range is used for the
  rest of the plates.

## Procedure

1. Follow the kit per manufacturer `[TODO: paste the step list of the chosen kit
   here once ordered]`.
2. Standard curve: serial dilution in complete medium, duplicate, 7 points plus
   blank.
3. Samples at the dilutions from the plate map, in the same medium.
4. Read at 450 nm, reference 570 nm, within the time the kit specifies after the
   stop solution.
5. Export the raw absorbance table as CSV, named with group, date, plate, analyte.

## Controls

- Blank (medium only): background.
- LPS on M(-): the positive control shared by all groups.
- Medium-only well from P02 run as a sample: detects reagent contamination.

## Checkpoints

- The standard curve is monotonic and the top standard is below saturation.
- At least one dilution of every sample falls inside the standard range; otherwise
  rerun that sample at another dilution.

## Known failure modes

- Samples above the top standard: dilute more.
- High blank: insufficient washing or contaminated medium.
- Edge wells drifting: evaporation during incubation; cover the plate.

## Output

Raw CSV, the ELISA plate map, dilution factors per sample. Concentrations are
calculated in the R template with a four-parameter logistic fit and reported in
pg/mL; where cell numbers differ between wells, normalise per cell.
