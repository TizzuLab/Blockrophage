# P02 RAW 264.7: scrape, count, split, seed

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

| | |
|---|---|
| ID | P02 |
| Used in | Exp 1, Exp 2 |
| Hands-on time | 45 min |
| Wall-clock time | 24 h before stimulation |
| Resources | hood, incubator shelf, centrifuge, counter, microscope |
| Depends on | P01 flask at 60–80% confluence, or staff stock culture |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

## Purpose

Detach, count and re-seed RAW 264.7 cells, either to keep the flask growing (split)
or to seed plates for an experiment at a defined density 24 h before stimulation.
The same steps serve both.

## Materials

- Complete medium, warm (as in P01)
- Sterile PBS
- Cell scraper, one per flask
- Plates: 12-well for supernatant assays, 6-well for flow cytometry `[TODO: or the
  lab's standard formats]`; T75 for continued expansion
- Counter and trypan blue

## Before you start

- Plate map drawn in the notebook before any cell is touched: which well gets which
  state and stimulus, triplicates, controls.
- Plates labelled on the lid and the side: group, date, content.
- Calculate the volumes needed for the target density before scraping.

## Procedure

1. Inspect the flask. Record confluence and morphology.
2. Aspirate the medium. Rinse once gently with 5 mL PBS and aspirate.
3. Add 5 mL fresh complete medium and scrape the whole surface with steady strokes.
   RAW 264.7 are passaged by scraping, not trypsin.
4. Pipette the suspension up and down 3–5 times to break clumps. Transfer to a
   15 mL tube.
5. Count with trypan blue. Record total, live, viability.
6. Split: seed `[TODO: 1:5 to 1:10, lab standard]` of the suspension into a fresh
   T75 with `[TODO: 12–15 mL]` complete medium. Keep the passage number below
   `[TODO]`; record the new passage in the notebook.
7. Seed for an experiment: dilute to the working density and plate

   | Format | Cells per well | Volume per well | Use |
   |---|---|---|---|
   | 12-well | `[TODO: cells/well]` | 1 mL | supernatant for ELISA and Griess |
   | 6-well | `[TODO: cells/well]` | 2 mL | flow cytometry |
   | 96-well | `[TODO: cells/well]` | 200 µL | optional, phagocytosis or viability extensions |

   Rock the plate gently in a cross pattern to spread the cells. Do not swirl;
   swirling piles cells in the centre.
8. Incubate 24 h before stimulation (P04).

## Controls

- One well of medium without cells per plate: background for the assays and a
  contamination check.
- Count twice if the two counts of the same suspension differ by more than 20%.

## Checkpoints

- After scraping: mostly single cells under the microscope, viability above 90%.
- Next morning: an even monolayer at `[TODO: expected confluence at stimulation]`.
  Uneven wells are noted in the plate map and excluded from triplicate statistics
  if they are outliers.

## Known failure modes

- Clumps: scraped too hard or pipetted too little. Pipette more gently, more times.
- Edge effect in plates: evaporation in outer wells. Fill the outer wells with PBS if
  the plate map allows it, or seed only inner wells.
- Density wrong next day: counting error or cells not spread. Check the photograph
  from the day before.

## Output

Counts, passage number, volumes and the final plate map in the notebook; the plate
map is the file every later analysis is joined to.
