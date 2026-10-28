# P01 RAW 264.7: thaw, expand, growth curve

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P01 |
| Used in | Exp 1 |
| Hands-on time | 45 min on the thaw day, 20 min per count after that |
| Wall-clock time | Tuesday 13:00 to Thursday 15:00 of week 2, about 50 h |
| Resources | hood, incubator shelf (37 °C, 5% CO2), centrifuge, Neubauer chamber or Countess III, microscope |
| Depends on | nothing; first bench step of the course |
| Lab SOP | Zindel lab 0203 "RAW 264.7 – adherent cells" (v1.0, 2025-12-01). The SOP wins over this page. |

## Purpose

Bring one cryovial of RAW 264.7 cells into culture, expand them in a flask, and
record five counts between Tuesday afternoon and Thursday afternoon (about 0, 19,
25, 43 and 49 h after the thaw). The counts give the growth curve and the doubling time of the line in your hands; both go on the poster and are
compared with the published value. The same flask supplies the cells for P02 and P03.

## Materials

- RAW 264.7 cryovial, one per group, from the staff stock `[TODO: passage number and
  mycoplasma test date]`
- Complete medium, 50 mL: 44.5 mL DMEM high glucose with GlutaMAX (Gibco 31966021),
  5 mL heat-inactivated FCS (Gibco A5256801), 0.5 mL penicillin-streptomycin
  (Gibco 15140122). Final 10% FCS, 1% P/S. Warm to 37 °C before use.
- DPBS without calcium and magnesium (Gibco 14190144)
- T25 flask for the thaw, T75 for expansion
- 12-well plate for the counting wells: one well per count, five wells plus one
  spare `[TODO: lab standard plate and density]`
- 15 mL tubes, serological pipettes (5, 10, 25 mL), 1 mL pipette, cell scraper
- Trypan blue (Sigma T8154) and a Neubauer chamber, or the Countess III with
  counting slides (Thermo C10228)
- Water bath at 37 °C, 70% ethanol

## Before you start

- Read P02 and P03 as well; the three protocols are one experiment.
- Everything from here on is sterile work in the laminar flow hood.
- Medium and DPBS warmed, hood wiped, waste container ready. Flask labelled with
  cell line, passage, date and group; copy every piece of information from the vial
  label onto the flask.
- Notebook page prepared with a table: date, time, count, viability, volume, passage.

## Procedure

Thaw day (Tuesday 23 March, 13:00; every step was practised on the staff culture on
Friday)

1. Prepare a 15 mL tube with 10 mL warm complete medium.
2. Take the vial from the staff tank in a closed transport container. Spray it with
   70% ethanol before it goes into the hood.
3. Thaw by dilution, not in the water bath: add 1 mL warm complete medium to the
   frozen vial with a 1 mL pipette, take the medium that has thawed off the ice back
   into the 15 mL tube, and repeat until the vial is empty. Work fast; viability
   drops with every minute the cells sit in DMSO.
4. Centrifuge 300 × g, 5 min, room temperature, to remove the DMSO. Aspirate the
   supernatant.
5. Resuspend the pellet in 5 mL warm complete medium. If the cells are sticky, break
   clumps with a 1 mL pipette until you have a single-cell suspension. Take 10 µL for
   the count (step 6) and transfer the rest to a T25 flask.
6. Count with trypan blue. Record total cells, live cells and viability. This is the
   first point of the growth curve (t = 0).
   If viability is above 80%, about 7 × 10^5 live cells of this suspension seed the
   P09 plate (standard curve and MTT growth curve); below that, the P09 plate is
   seeded from the staff stock flask.
7. Seed the counting wells from the same suspension: 5 × 10^4 live cells in 1 mL per
   well, six wells of a 12-well plate `[TODO: lab standard density]`. Every later
   count scrapes one whole well, so the flask is only touched for the medium change
   and the freeze.
8. Incubate at 37 °C, 5% CO2. Distribute the cells by gently rocking the flask once
   before closing the incubator; do not swirl.

Counts (Wednesday and Thursday, 09:00 and 15:00)

9. Inspect under the microscope before anything else: morphology (round to
   spindle-shaped, adherent), density, debris, signs of contamination (turbidity,
   colour change, particles moving between cells). Photograph one field at 10× for
   the notebook.
10. Take a count: scrape one counting well according to P02, steps 1 to 5, and count
    the suspension with trypan blue. Record the count, the viability and the real
    clock time; the five points (thaw, Wed 09:00, Wed 15:00, Thu 09:00, Thu 15:00)
    are the growth curve `[TODO: confirm with the lab that counting wells are the
    course standard, or define a counting shortcut]`.
11. Change the medium of the flask on Wednesday, or whenever the medium turns yellow: aspirate,
    add fresh warm complete medium gently along the side of the flask. RAW cells
    adhere loosely; do not pipette onto the cell layer.
12. Split only if the flask reaches about 80% confluence before Thursday: follow
    P02. Move from the T25 to a T75 at the first split.
13. Thursday: after the 09:00 count, freeze from the flask according to P03 at
    11:00. After the 15:00 count, discard the counting wells. No
    cultures are kept over the Easter break.

## Controls

- Medium-only flask or well, incubated alongside: detects contaminated medium.
- Published doubling time of RAW 264.7: the lab SOP works with 15–24 h; ATCC gives
  a similar range. Your curve should be in that range or you have a reason to find.
- The P09 MTT growth curve from the same suspension: a second doubling time by an
  independent readout.

## Checkpoints

- After the thaw: viability above 80%. Below that, note it, keep going, and plan a
  second vial from the staff stock if the flask is empty on Wednesday morning.
- Wednesday morning: cells attached and spreading. If most cells are floating and
  round, they are either dead (trypan blue) or recently divided (fine).
- Thursday morning: the flask 60–80% confluent. Beyond 90%, split immediately; RAW cells change
  behaviour when overgrown.

## Known failure modes

- Low viability after thaw: DMSO exposure too long or vial thawed too slowly. Thaw
  by dilution as in step 3, work faster.
- Cells not attaching: cold medium or an FCS lot problem. Check the medium
  temperature first.
- Yellow medium within 24 h: too many cells or contamination. Look under the
  microscope before deciding.
- Doubling time far outside the published range: counting error is the first
  suspect. Recount before concluding anything about the cells.

## Output

Growth table in the notebook (date, time, live count, viability, volume, passage,
who counted), one photograph per day, the plot of log cell number against time and
the doubling time with the formula used. Note every deviation from this page.
