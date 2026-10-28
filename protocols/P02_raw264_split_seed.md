# P02 RAW 264.7: scrape, count, split, seed

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P02 |
| Used in | Week 1 hands-on; Exp 1 and Exp 2 plating; passaging the stock |
| Hands-on time | 45 min |
| Wall-clock time | the plate is polarized at seeding (P04) and harvested or challenged the next morning |
| Resources | hood, incubator shelf, centrifuge, counter, microscope |
| Depends on | the group's stock flask (P01) at 60–80% confluence |
| Lab SOP | Zindel lab 0203 "RAW 264.7 – adherent cells" (v1.0, 2025-12-01), splitting section, and the lab's RAW 264.7 polarisation protocol (v1.0, 2025-12-08), seeding section. The SOP wins over this page. |

## Purpose

Detach, count and re-seed RAW 264.7 cells, either to keep the flask growing (split)
or to seed plates for an experiment at a defined density, with the polarizer already
in the suspension (P04). The same steps serve both, and the first time you do them is
on the staff culture, on the Friday of week 1.

## Materials

- Complete medium, warm (recipe in P01)
- DPBS (Gibco 14190144), warm
- Cell scraper, one per flask
- Plates: 6-well or 12-well for flow cytometry (week 2), 96-well flat-bottom for
  the supernatants (week 3), 24-well for the RNA extension; T25 or T75 for the
  stock
- Counter and trypan blue (as in P01)

## Before you start

- Plate map drawn in the notebook before any cell is touched: which well gets which
  state and stimulus, triplicates, controls.
- Plates labelled on the lid and the side: group, date, content.
- Calculate the volumes needed for the target density before scraping.

## Procedure

1. Inspect the flask. Record confluence and morphology. The lab splits at about
   80% confluence.
2. Aspirate the medium. Wash once gently with 5 mL warm DPBS and aspirate.
3. Add 3 mL (T25) or 10 mL (T75) fresh complete medium and scrape the whole
   surface with steady strokes, including the edges. RAW 264.7 are passaged by
   scraping, not trypsin.
4. With a serological pipette, wash the walls of the flask with the medium so that
   every cell is in suspension, then pipette up and down 3–5 times to break clumps.
   Transfer to a 15 mL tube.
5. Count with trypan blue. Record total, live, viability.
6. Split: seed 1:3 to 1:5 of the suspension into a fresh flask (3 mL final in a
   T25, 10 mL in a T75); RAW 264.7 double every 15–24 h (lab SOP). Record the
   split with the date and the course passage count, counted from the Friday thaw.
7. Seed for an experiment: centrifuge the needed cells (300 × g, 5 min), resuspend
   in fresh medium at the working density and plate

   | Format | Cells per well | Volume per well | Use |
   |---|---|---|---|
   | 96-well | 2 × 10^4 | 200 µL | supernatant for ELISA (lab-validated) |
   | 24-well | 1.2 × 10^5 | 500 µL | RNA arm, X01 |
   | 6-well | 6 × 10^5 | 2 mL | flow cytometry, P08 |

   The 96-well density is the lab's. The 24- and 6-well densities are scaled from it
   by growth area (about 6 × 10^4 cells/cm²).

   > **To verify:** the 24- and 6-well densities are derived, not tested. Check in
   > the first run that a 6-well seeded this way yields at least 1 × 10^6 cells per
   > well 48 h later for P08.

   Rock the plate gently in a cross pattern to spread the cells. Do not swirl;
   swirling piles cells in the centre.
8. Incubate overnight, about 19 h; the polarizer went in with the suspension (P04).
   Harvest (P08) or challenge (P05) the next morning.

## Controls

- One well of medium without cells per plate: background for the assays and a
  contamination check.
- Count twice if the two counts of the same suspension differ by more than 20%.

## Checkpoints

- After scraping: mostly single cells under the microscope, viability above 90%.
- Next morning: an even monolayer, about 40–60% confluent in the 96-well
  `[TODO: confirm expected confluence at stimulation in the first run]`. Uneven
  wells are noted in the plate map and excluded from triplicate statistics if they
  are outliers.

## Known failure modes

- Clumps: scraped too hard or pipetted too little. Pipette more gently, more times.
- Edge effect in plates: evaporation in outer wells. Fill the outer wells of a
  96-well plate with 200 µL DPBS if the plate map allows it, or seed only inner
  wells.
- Density wrong next day: counting error or cells not spread. Check the photograph
  from the day before.

## Output

Counts, passage number, volumes and the final plate map in the notebook; the plate
map is the file every later analysis is joined to.
