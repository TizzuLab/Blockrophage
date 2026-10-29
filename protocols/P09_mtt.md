# P09 MTT assay: metabolic activity as a proxy for cell number

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P09 |
| Used in | Optional, extension: a growth curve of the stock, or a viability check on wells whose supernatant has been harvested. Not part of the core since the 2026-10-28 revision |
| Hands-on time | 20 min to seed, 40 min for the standard curve and the first read, 20 min per read after that |
| Wall-clock time | 3.5 h per read (3 h MTT, 15 min solubilisation, read), same day |
| Resources | hood, incubator shelf, plate reader with a 560 or 570 nm filter and a reference filter, multichannel pipette, orbital shaker (optional), microscope |
| Depends on | a counted live-cell suspension from P01 step 5 (thaw day) or P02 step 5 |
| Lab SOP | none yet `[TODO]`. This page is built from three published sources, listed at the end; the lab has not run an MTT assay in this format. |

## Purpose

A second, independent growth curve of RAW 264.7 next to the daily flask counts of
P01, and a standard curve that shows what the assay can and cannot resolve. MTT
(3-(4,5-dimethylthiazol-2-yl)-2,5-diphenyltetrazolium bromide) is a yellow,
water-soluble salt that living cells reduce to a purple, insoluble formazan; the
reduction is done by NAD(P)H-dependent oxidoreductases, largely outside the
mitochondria. Dissolve the formazan and the absorbance is proportional to the
number of metabolically active cells, as long as every cell reduces MTT at the
same rate. That condition is the whole lesson of this protocol: the assay counts
metabolic activity, not cells, and the two diverge whenever the metabolic state
changes, for example in freshly thawed cells, in overgrown wells or in polarized
macrophages. The doubling time from P09 is compared with the one from P01 counts;
where they differ, the notebook says which one is trusted and why.

## Materials

- MTT powder `[TODO: order; not in the lab's protocol collection as of 2026-10]`:
  Thermo M6494 (1 g) or Sigma M5655 (500 mg). Light sensitive. MTT is a suspected
  mutagen: gloves, weigh in a hood or with a mask, solid waste as chemical waste.
- MTT stock, 5 mg/mL in DPBS (12 mM): 50 mg MTT in 10 mL sterile DPBS, vortex until
  dissolved, filter through 0.22 µm, 1 mL aliquots in amber or foil-wrapped tubes,
  4 °C in the dark for up to 4 weeks (or −20 °C for longer). A stock that has
  turned blue or green is discarded. One aliquot serves 100 wells.
- Solubiliser, acid isopropanol: 0.04 M HCl in isopropanol. For 10 mL, 400 µL of
  1 M HCl into 9.6 mL isopropanol (or 33 µL of 37% HCl). Room temperature, closed
  bottle, flammable. 100 µL per well; 10 mL serves one plate.
  Alternative when the plate can wait until the next morning: SDS-HCl, 1 g SDS in
  10 mL 0.01 M HCl, 100 µL per well, 4 to 18 h at 37 °C (see Sources).
- Complete medium, warm (recipe in P01). Phenol-red-free DMEM for the MTT step is
  cleaner but not required with the acid solubiliser `[TODO: Gibco 21063029 if the
  lab stocks it]`.
- DPBS (Gibco 14190144) for the outer wells
- 96-well flat-bottom clear plate, reagent reservoir, multichannel pipette, foil
- Plate reader: the lab's Promega GloMax Discover. `[TODO: confirm the absorbance
  filters on the instrument; the textbook wavelength is 570 nm with a 630 nm
  reference. If the GloMax carries 560 and 750 nm, read 560 with 750 as reference
  and say so in the methods.]`

## Before you start

- Plate map drawn in the notebook (template below). Outer wells get 200 µL DPBS
  as an evaporation guard (P02, known failure modes).
- Live count of the suspension done (trypan blue), dilutions calculated so that
  every well receives 100 µL. The whole plate needs about 7 × 10^5 live cells, a
  quarter of a vial; the rest goes into the P01 flask.
- MTT stock and solubiliser at room temperature. Cold solubiliser does not dissolve
  the crystals.
- Plate reader booked at 12:30, 14:30 and 16:00 on the read days, with the filter
  pair tested on an empty plate once before Tuesday.

Plate map, 100 µL per well:

| Columns | Rows | Content | Read on |
|---|---|---|---|
| 1 and 12 | A to H | DPBS, 200 µL | never |
| 2, 3, 4 | A to H | standard curve, one column per replicate: A 8 × 10^4, B 4 × 10^4, C 2 × 10^4, D 1 × 10^4, E 5 × 10^3, F 2.5 × 10^3, G 1.25 × 10^3, H medium only | Wednesday, seeded 09:00, read 14:30 |
| 5, 6, 7 | B to D | 2.5 × 10^3 cells (low density) | Wed 09:00, Thu 09:00, Thu 12:30; one column per read |
| 5, 6, 7 | E to G | 1 × 10^4 cells (high density) | Wed 09:00, Thu 09:00, Thu 12:30; one column per read |
| 8, 9, 10 | B to D | medium only, blank for that read | with its cell column |
| 8, 9, 10 | E to G | 1 × 10^4 cells, spare set (repeat or microscope check) | as needed |
| 5 to 11 | A and H; column 11 B to G | DPBS, 200 µL | never |

The t = 0 point of the growth curve is the seeded cell number, taken from the P01
count on Tuesday. The standard curve, seeded on Wednesday morning from the counted
staff suspension, converts OD into cell number.

## Procedure

Tuesday 13:00 (growth-curve columns, from the P01 thaw suspension or the staff stock
flask)

1. Prepare the two growth-curve suspensions in complete medium: 2.5 × 10^4 cells/mL
   (1.2 mL) and 1 × 10^5 cells/mL (2.2 mL).
2. Fill the outer wells with 200 µL DPBS. Plate 100 µL per well into columns 5 to 7
   and medium only into columns 8 to 10 according to the map. Rock the plate in a
   cross pattern; do not swirl. Back into the incubator; nothing is read today.

Wednesday 09:00 (standard curve and read 1)

3. Prepare 2.6 mL of 8 × 10^5 live cells/mL from the counted staff suspension, then
   a 1:2 series in complete medium down to 1.25 × 10^4 cells/mL (seven tubes, 1.3 mL
   each is enough). Plate 100 µL per well into columns 2 to 4. Incubate 2 h at
   37 °C, 5% CO2, so that the cells attach
   `[TODO: confirm 2 h is enough for RAW 264.7 to attach; the source figure used 4 h]`.
4. Add 10 µL MTT stock straight into the medium: at 09:00 to every well of columns
   5 and 8 (read 1), at 11:00 to every well of columns 2 to 4, including the
   medium-only row. Tap the plate gently. Incubate 3 h at 37 °C in the dark (plate
   in the incubator is dark enough).
5. Look at a high-density well under the microscope: purple needle-shaped crystals
   in and around the cells, none in the medium-only wells.
6. Without removing the medium, add 100 µL acid isopropanol to each well that
   received MTT. Cover with foil and shake 15 min on the orbital shaker, or
   pipette up and down ten times per well with the multichannel pipette. Check one
   well under the microscope: no crystals left, uniform purple.
7. Read within 1 h at 570 nm (or 560 nm) with the reference filter: 12:30 for read
   1, 14:30 for the standard curve. Export the raw file with the group, date and
   plate map name in the file name.

Thursday (reads 2 and 3)

8. Steps 4 to 7 on columns 6 and 9 at 09:00 (read 12:30) and on columns 7 and 10 at
   12:30 (read 16:00). Record the real clock times; the fit uses the hours since
   seeding, about 19, 43 and 47 h.
9. Before adding MTT, photograph one high-density and one low-density well at
   10×, and record the colour of the medium. Yellow medium in the high-density
   wells on Thursday is noted, not corrected.

Optional, Experiments 2 and 4 (viability after supernatant harvest)

10. After the supernatant has been taken off for ELISA and Griess (P05), add
    100 µL warm complete medium and 10 µL MTT stock to the emptied wells and
    continue from step 4. Blanks are medium-only wells of the same plate. Read
    the result as metabolic activity per well, not as a cell count: IFNγ and LPS
    change macrophage metabolism, and nitric oxide inhibits mitochondrial
    respiration, so a lower OD in M(IFNγ+LPS) wells is expected even with no cell
    death. A trypan blue count of a scraped parallel well is the viability
    control.

## Controls

- Medium-only wells, with MTT and solubiliser, on every read day: the blank. A
  blank above 0.1 OD `[TODO: verify on the GloMax]` points to contaminated medium
  or a reducing compound.
- The day-0 standard curve: eight points in triplicate. It gives the OD per
  10^4 cells, the lowest density the assay distinguishes from blank, and the
  density at which the curve bends. Every later OD is converted to a cell number
  with this curve, and the conversion is only trusted inside its linear range.
- The P01 flask count of the same day: the independent readout. Two curves, two
  doubling times; both go on the poster.
- Known interferences, from the sources: reducing compounds (ascorbic acid,
  glutathione, dithiothreitol, coenzyme A, polyphenols) reduce MTT without cells;
  serum and phenol red raise the background, which the blank removes and the acid
  solubiliser reduces by turning phenol red yellow.

## Checkpoints

- After 3 h MTT: purple crystals in cell wells, none in blanks. Crystals nowhere:
  stock dead (discard if discoloured) or cells dead; check with trypan blue.
- After solubilisation: no crystals under the microscope, uniform colour. Top
  standard between OD 1 and 2. Above 2.5 the reader saturates: halve all densities
  in the next run and record it.
- Standard curve: linear fit with R² above 0.98 over the range used. If the top
  points fall below the line, cap the usable range there and say so in the legend.
- Thursday high-density wells: expected 3 to 9 × 10^4 cells per well at 43 to 47 h
  from a 15 to 24 h doubling time; if the OD is at the top of the standard curve,
  the low-density wells carry the doubling time.

## Known failure modes

- Crystals do not dissolve: solubiliser was cold, or too little mixing. Warm to
  room temperature, mix again, 15 min on the shaker.
- OD drifts between two reads of the same plate: isopropanol evaporates and the
  formazan precipitates. Read within 1 h, keep the foil on until the reader.
- High blank: medium contaminated with cells or bacteria, or a reducing compound.
  Fresh medium, sterile tips, a new MTT aliquot.
- Doubling time from MTT shorter than from the counts: per-cell MTT reduction
  rises as the thawed cells recover, which inflates the slope. Say so, and use the
  P01 counts for the number on the poster.
- Doubling time from MTT longer than from the counts: high-density wells left the
  linear range, or the medium turned acidic. Use the low-density wells only.
- Edge effect: unequal ODs across a replicate column with the outermost well off.
  The DPBS guard was skipped or the lid sat crooked. Note the well as excluded.

## Output

Raw reader exports (one file per read day, named group_date_P09), the plate map,
blank-subtracted ODs, the standard-curve fit (slope, intercept, R², linear range),
cell numbers per well, the plot of log cell number against time for both densities,
the doubling time with the formula, and the same plot next to the P01 counts
`[TODO: growth-curve template in code/]`. Every deviation from this page in the
notebook.

## Sources, and which value comes from where

This protocol was assembled from three documents on 2026-10-27, not from a lab SOP.

- **Mosmann 1983**, J Immunol Methods 65:55–63, the original assay: MTT 5 mg/mL in
  PBS, 10 µL per 100 µL well, 4 h at 37 °C, 100 µL acid isopropanol (0.04 M HCl
  in isopropanol) added to the well without removing the medium, mixed until the
  crystals dissolve, read within 1 h at 570 nm with a 630 nm reference; the acid
  turns phenol red yellow so that it does not interfere. Read via the citations in
  the Thermo manual below; the paper itself is `[TODO: add PDF to the lab's
  literature folder]`.
- **Thermo Fisher, CyQUANT MTT Cell Proliferation Assay Kit, MAN0019028 Rev. B.0,
  2021-09-02** (the former Vybrant kit; MTT powder M6494): 12 mM stock from 5 mg
  MTT in 1 mL PBS, stored at 4 °C for up to 4 weeks protected from light; 10 µL
  per 100 µL well; 4 h or overnight at 37 °C, 2 h above 10^5 cells per well;
  SDS-HCl (1 g SDS in 10 mL 0.01 M HCl), 100 µL per well, 4 to 18 h at 37 °C,
  longer incubations lower the sensitivity (Niks 1990); read at 570 nm; a rapid
  variant with 50 µL DMSO read at 540 nm; linearity up to about 10^6 Jurkat cells
  per well after 4 h attachment; seed 5,000 to 10,000 cells per well to reach
  optimal density in 48 to 72 h; strong recommendation against phenol red. Cites
  Mosmann 1983, Berridge and Tan 1993 and Liu et al. 1997 for the mechanism.
- **Abcam, MTT Cell Proliferation Assay Kit ab211091, protocol book v2d,
  2026-03-12** (the kit behind the Abcam protocol page): aspirate the medium, 50 µL
  serum-free medium plus 50 µL MTT reagent per well, 3 h at 37 °C, 150 µL MTT
  solvent, 15 min on an orbital shaker under foil, read at 590 nm; background
  wells with serum-free medium; warm solvent, never cold; serum and phenol red
  listed as interferences; a list of reducing compounds that give false signal;
  a discoloured reagent is discarded; 5,000 to 10,000 cells per well as seeding
  guidance. The kit's reagent and solvent compositions are not disclosed.

What was taken from where:

| Item in this page | Value | Source |
|---|---|---|
| MTT stock | 5 mg/mL in DPBS, 12 mM, filtered, 4 °C dark, 4 weeks | Mosmann; Thermo |
| MTT per well | 10 µL into 100 µL | Mosmann; Thermo |
| MTT incubation | 3 h | Abcam (Mosmann and Thermo use 4 h; 3 h fits the course day) |
| Solubiliser | 0.04 M HCl in isopropanol, 100 µL, medium not removed | Mosmann |
| Mixing | 15 min orbital shaker under foil, or pipetting | Abcam |
| Read | within 1 h, 570 nm, reference 630 nm | Mosmann (Abcam kit reads 590 nm) |
| Reader | GloMax Discover, filters to confirm | lab, P06 |
| Seeding guidance | 5,000 to 10,000 cells per well for 48 to 72 h | Abcam; Thermo |
| Course densities | 2.5 × 10^3 and 1 × 10^4 per well | this page: chosen so that the wells stay well below 3 × 10^5 at 48 h with a 15 to 24 h doubling time (lab SOP 0203) |
| Standard curve range | 1.25 × 10^3 to 8 × 10^4 per well | this page, inside the Thermo linearity statement |
| Attachment before day-0 MTT | 2 h | this page, to verify; Thermo figure used 4 h |
| Phenol red, serum | blanks; acid solvent; phenol-red-free optional | Mosmann; Thermo; Abcam |
| Interfering compounds | ascorbate, glutathione, DTT, coenzyme A, polyphenols | Abcam FAQ |
| Warm solvent | never cold | Abcam |
| Polarized cells caveat | metabolic state changes MTT reduction | Berridge and Tan 1993, Liu 1997, via Thermo; the NO and respiration point is textbook macrophage biology, see background section 5.4 |
| Complete medium, DPBS, plate, outer-well guard | lab recipes | P01, P02 |
