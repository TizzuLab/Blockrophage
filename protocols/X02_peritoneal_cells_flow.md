# X02 Peritoneal cells on the shared flow panel (extension)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

> Extension. Depends on primary material: we may be able to provide peritoneal
> lavage cells that are surplus from ongoing experimental work in the lab. Whether
> and when such a suspension is available is decided with your supervisor on the
> first afternoon; the cells arrive ready, on ice, as a suspension.

| | |
|---|---|
| ID | X02 |
| Used in | Extension |
| Hands-on time | 30 min receiving, counting and lysis, then staining as C3 |
| Wall-clock time | half a day, coordinated with a cytometer slot |
| Resources | ice, cooled centrifuge, counter, cytometer slot |
| Depends on | C3 full panel and a reserved cytometer slot; polarized J774A.1 cells ready on the same day; a surplus peritoneal cell suspension provided by staff |
| Lab SOP | Zindel lab "Flow cytometry" (v1.2) and "Flow cytometry antibody titration" for the staining; the SOP wins over this page. |

## Purpose

Run resident tissue macrophages, obtained without digestion, on the shared panel in
the same session as the polarized J774A.1 cells. The first result, before any
activation marker, is that no in vitro cell falls into the large-peritoneal-
macrophage gate.

## Materials

- FACS buffer, ice-cold: PBS, 3% FCS, 2 mM EDTA, 10 mM HEPES (recipe in the
  protocol index)
- 15 mL or 50 mL tubes, labelled, on ice
- ACK erythrocyte lysis buffer if the suspension is bloody (recipe in the protocol
  index)
- Counter, FACS reagents as in C3

## Before you start

- Confirm with your supervisor that a surplus suspension is available on a day
  with a cytometer slot, and that your polarized J774A.1 cells are ready the same day.
- C3 staining plan extended with the peritoneal samples on the full panel, and one
  well of each polarized J774A.1 state stained with the full panel too, so the
  overlay has F4/80 and the lineage markers.
- Record what the staff tell you about the sample: source of the material, date,
  volume, any treatment it carries over from the experiment it came from.

## Procedure

1. Receive the suspension on ice.

> [!WARNING]
> Keep it cold from here on; peritoneal macrophages adhere to plastic within
> minutes at room temperature.

2. Centrifuge **`300 × g, 5 min, 4 °C`**. If the pellet is red, resuspend in 1 mL ACK
   buffer, **`room temperature, 2 min`**, top up with buffer and centrifuge again.
3. Resuspend in FACS buffer and count. Expect large peritoneal macrophages to be
   roughly a third of the cells in a healthy sample.
4. Stain with the full panel (C3), surface first, then fixation, permeabilization
   and the intracellular CD206 and Arg1 stain, and acquire in the same session as
   the polarized J774A.1 cells.
5. Gate: live single CD45+ cells; remove T cells (CD3), B cells (CD19),
   neutrophils (Ly-6G), eosinophils (Siglec-F) and mast cells (CD117); then
   CD11b+ cells, F4/80 against MHCII for large (F4/80 high, MHCII low) and small
   (F4/80 low, MHCII high) peritoneal macrophages; Ly-6C marks monocytes and CD11c
   dendritic cells. Read CD86, CD206 and Arg1 on the macrophage gates, and overlay
   the polarized J774A.1 cells on the same gates.

> [!WARNING]
> Neutrophils express Arg1 too. Gate Ly-6G+ cells out before you read Arg1 on
> macrophages.

## Controls

- The lineage gates (CD3, CD19, Ly-6G, Siglec-F, CD117) remove non-macrophages;
  F4/80 against MHCII separates large and small peritoneal macrophages.
- Same single-stain and fluorescence-minus-one controls as C3; the peritoneal
  sample and the J774A.1 cells share the compensation.

## Checkpoints

- A clear F4/80 high, MHCII low population exists in the peritoneal sample before
  anything else is interpreted; if it is missing, note the sample history and ask.

## Known failure modes

- Low cell number: the suspension was small or lost cells on the way; stain what
  you have and reduce the panel rather than the cell number per tube.
- Bloody suspension: lyse the erythrocytes and note it.
- Ly-6G and CD19 smear into each other: AF488 and Spark Blue 550 overlap on the
  blue laser. They mark different cells, so both work as exclusion gates; check
  the single stains and the compensation before blaming the sample.
- AF700 (MHCII) and APC-Cy7 (CD11b) are both bright on macrophages and neighbours
  on the red laser: compensate with care, and set the F4/80 against MHCII gate on
  FMOs.
- Few large peritoneal macrophages: prior inflammation in the experiment the sample
  came from; record the sample history and treat the result as a finding.

## Output

Cell counts, sample metadata as provided by staff, FCS files, and the gated
statistics side by side with the J774A.1 samples.
