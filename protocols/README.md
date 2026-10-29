# Protocols

← Back to the [course script](../README.md#readme)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

One file per protocol, all on the same template (00_TEMPLATE.md): header table,
purpose, materials, before you start, procedure, controls, checkpoints, known failure
modes, output. Values the lab has not yet confirmed are marked `[TODO]`; things
the lab has a protocol for but has not run in the course format carry a
`> [!IMPORTANT] **To verify:**` callout. Where the lab has a validated SOP, the SOP wins and the
protocol names it (lab SOP number, version and date; the SOPs themselves are
internal documents). Figures live in `figures/`. Every incubation and centrifugation
you set or time is bold and boxed, like **`37 °C, 5% CO2, 16 h`**; the formatting
rules are at the top of the template.

Five core protocols (C) carry the course, in the order you meet them: cells,
polarization, phenotype, challenge, readout. X-files are optional extensions
(Section 5 of the script, Extensions). The S-file is for the staff.

**Core**

| ID | Title | Used in | Hands-on time | Wall-clock time | Resources |
|---|---|---|---|---|---|
| [C1](C1_raw264_culture.md) | RAW 264.7 culture: thaw, split, seed | week 1 Friday (thaw the stock flask); Exp 1 and 3 plating; passaging | 45 min for the thaw, 45 min per split or seeding | the flask lives the whole course; a seeded plate is used the next morning | hood, incubator, centrifuge, counter, microscope |
| [C2](C2_polarization.md) | Polarization: the menu | Exp 1, Exp 3 | 30 min, at seeding | about 19 h, Tue to Wed | hood, incubator, vortex |
| [C3](C3_flow_cytometry.md) | Flow cytometry of polarized RAW cells | Exp 1 (week 2), X02 | 2 h stain + 1 h acquisition | half day | hood, cooled plate centrifuge, heating block, cytometer slot, FlowJo seat |
| [C4](C4_prr_challenge.md) | Danger-signal challenge: PAMPs, DAMPs, inhibitors | Exp 3 (week 3 Wed) | 45 min + 45 min harvest | 16 h overnight (default) or 6 h | hood, incubator, plate centrifuge, −20 °C, −80 °C |
| [C5](C5_elisa.md) | ELISA IL-6 (default) or TNF | Exp 3 (week 3 Thu) | 3–4 h + coating the day before | 2 days | plate reader (450 nm), multichannel pipette |

**Extensions**

| ID | Title | Used in | Hands-on time | Wall-clock time | Resources |
|---|---|---|---|---|---|
| [X01](X01_qpcr.md) | RNA isolation and qPCR | Extension | 1 h + 1.5 days | 6 h arm, then 2 days | hood, −80 °C, RNA bench, NanoDrop, thermal cycler, LightCycler 480 II |
| [X02](X02_peritoneal_cells_flow.md) | Peritoneal cells on the shared flow panel | Extension | 30 min + staining | half day, with cytometer slot | surplus peritoneal cell suspension provided by staff, ice, cooled centrifuge, cytometer slot |
| [X03](X03_tissue_sections_ihc.md) | F4/80 IHC on tissue sections | Extension | 1 h + 2 × 3 h | about 5 days | surplus fixed tissue or blocks provided by staff, histology facility (paraffin), pressure cooker, histology bench, slide scanner |
| [X04](X04_griess.md) | Griess assay | Extension, on the Exp 3 supernatants | 1 h | 1 h | plate reader |
| [X05](X05_mtt.md) | MTT assay: metabolic activity as a proxy for cell number | Extension | 40 min + 20 min per read day | 3.5 h per read, same day | hood, incubator, plate reader (560 or 570 nm plus reference), multichannel pipette |

**Staff**

| ID | Title | Used in | Hands-on time | Wall-clock time | Resources |
|---|---|---|---|---|---|
| [S01](S01_raw264_freeze.md) | RAW 264.7: backup vials and the stock over the break | Thu of week 2, Easter break | 45 min + 20 min per split | overnight at −80 °C, then −140 °C | hood, centrifuge, freezing container, −80 °C, −140 °C |

## Dependencies in time

- C1: the group's stock flask is thawed on Friday of week 1 and lives until the
  end of the course; the staff carry it over the weekend and the break (S01).
- Exp 1 (week 2): C1 plates on Tuesday 13:00 with the polarizer in the suspension
  (C2); C3 harvests, stains and fixes on Wednesday, acquires on Thursday morning.
- Exp 3 (week 3): C1 plates on Tuesday 13:00 with the polarizer (C2); C4
  challenges on Wednesday 09:00, overnight (default) or 6 h; C5 plates are coated
  on Wednesday 16:30 and run on Thursday. X04 (extension) runs on the same
  supernatants.
- X02 needs a cytometer slot on the day the peritoneal cells are available; X03
  tissue must reach the facility in week 1. Both depend on surplus primary material
  from ongoing work in the lab; ask on the first afternoon.

## Plate formats

One seeding density, scaled by growth area (C1): 96-well plates (2 × 10^4 cells,
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
