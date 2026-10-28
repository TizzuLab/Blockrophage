# Protocols

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

One file per protocol, all on the same template (00_TEMPLATE.md): header table,
purpose, materials, before you start, procedure, controls, checkpoints, known failure
modes, output. Values the lab has not yet confirmed are marked `[TODO]`; things
the lab has a protocol for but has not run in the course format carry a
`> **To verify:**` callout. Where the lab has a validated SOP, the SOP wins and the
protocol names it (lab SOP number, version and date; the SOPs themselves are
internal documents). Figures live in `figures/`.

P-files are the core programme, X-files are optional extensions (Section 5 of the script, Extensions).

| ID | Title | Used in | Hands-on time | Wall-clock time | Resources |
|---|---|---|---|---|---|
| P01 | RAW 264.7: thaw and seed the group's stock flask | week 1 Friday; stock for Exp 1 and 3 | 45 min, then 20 min per split | the whole course | hood, incubator, centrifuge, counter, microscope |
| P02 | RAW 264.7: scrape, count, split, seed | week 1 hands-on, Exp 1, Exp 3, passaging | 45 min | polarized at seeding, harvested or challenged next morning | hood, incubator, centrifuge, counter |
| P03 | RAW 264.7: backup vials and the stock over the break (staff) | Thu of week 2, Easter break | 45 min + 20 min per split | overnight at −80 °C, then −140 °C | hood, centrifuge, freezing container, −80 °C, −140 °C |
| P04 | Polarization: the menu | Exp 1, Exp 3 | 30 min, at seeding | about 19 h, Tue to Wed | hood, incubator, vortex |
| P05 | Danger-signal challenge: PAMPs, DAMPs, inhibitors | Exp 3 (week 3 Wed) | 45 min + 45 min harvest | 16 h overnight (default) or 6 h | hood, incubator, plate centrifuge, −20 °C, −80 °C |
| P06 | ELISA IL-6 (default) or TNF | Exp 3 (week 3 Thu) | 3–4 h + coating the day before | 2 days | plate reader (450 nm), multichannel pipette |
| P07 | Griess assay | Extension | 1 h | 1 h | plate reader |
| P08 | Flow cytometry of polarized RAW cells | Exp 1 (week 2), X02 | 2 h stain + 1 h acquisition | half day | hood, cooled plate centrifuge, heating block, cytometer slot, FlowJo seat |
| P09 | MTT assay: metabolic activity as a proxy for cell number | optional, extension | 40 min + 20 min per read day | 3.5 h per read, same day | hood, incubator, plate reader (560 or 570 nm plus reference), multichannel pipette |
| X01 | RNA isolation and qPCR | Extension | 1 h + 1.5 days | 6 h arm, then 2 days | hood, −80 °C, RNA bench, NanoDrop, thermal cycler, LightCycler 480 II |
| X02 | Peritoneal cells on the shared flow panel | Extension | 30 min + staining | half day, with cytometer slot | surplus peritoneal cell suspension provided by staff, ice, cooled centrifuge, cytometer slot |
| X03 | F4/80 IHC on tissue sections | Extension | 1 h + 2 × 3 h | about 5 days | surplus fixed tissue or blocks provided by staff, histology facility (paraffin), pressure cooker, histology bench, slide scanner |

## Dependencies in time

- P01: the group's stock flask is thawed on Friday of week 1 and lives until the
  end of the course; the staff carry it over the weekend and the break (P03).
- Exp 1 (week 2): P02 plates on Tuesday 13:00 with the polarizer in the suspension
  (P04); P08 harvests, stains and fixes on Wednesday, acquires on Thursday morning.
- Exp 3 (week 3): P02 plates on Tuesday 13:00 with the polarizer (P04); P05
  challenges on Wednesday 09:00, overnight (default) or 6 h; P06 plates are coated
  on Wednesday 16:30 and run on Thursday. P07 (extension) runs on the same
  supernatants.
- X02 needs a cytometer slot on the day the peritoneal cells are available; X03
  tissue must reach the facility in week 1. Both depend on surplus primary material
  from ongoing work in the lab; ask on the first afternoon.

## Plate formats

One seeding density, scaled by growth area (P02): 96-well plates (2 × 10^4 cells,
200 µL) for everything that ends in a supernatant assay, 6-well plates for flow
cytometry, 24-well plates for the RNA extension.

## Buffers (lab recipes)

| Buffer | Recipe | Notes |
|---|---|---|
| Complete medium (50 mL) | 44.5 mL DMEM high glucose GlutaMAX (Gibco 31966021), 5 mL heat-inactivated FCS (Gibco A5256801), 0.5 mL penicillin-streptomycin (Gibco 15140122) | warm to 37 °C |
| FACS buffer (500 mL) | 478 mL 1× PBS, 15 mL FCS, 2 mL 0.5 M EDTA, 5 mL 1 M HEPES | 3% FCS, 2 mM EDTA, 10 mM HEPES; the lab calls it MACS buffer |
| PBS 10× (1 L) | 80 g NaCl, 2 g KCl, 11.5 g Na2HPO4, 2 g KH2PO4, water to 800 mL, pH 7.2–7.4 with HCl, to 1 L | autoclave, 4 °C |
| EDTA 0.5 M (1 L) | 146.13 g EDTA in 800 mL water, pH 8 with NaOH, to 1 L | autoclave, 4 °C, 1 year |
| HEPES 1 M (1 L) | 238.3 g HEPES in 800 mL water, pH 8 with NaOH, to 1 L | autoclave, 4 °C, dark |
| ACK lysis buffer (1 L) | 8.29 g NH4Cl (155 mM), 1 g KHCO3 (10 mM), 200 µL 0.5 M EDTA (0.1 mM), water to 800 mL, pH 7.4, to 1 L | autoclave, room temperature |
