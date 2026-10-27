# Protocols

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

One file per protocol, all on the same template (00_TEMPLATE.md): header table,
purpose, materials, before you start, procedure, controls, checkpoints, known failure
modes, output. Values the lab has not yet confirmed are marked `[TODO]`; things
the lab has a protocol for but has not run in the course format carry a
`> **To verify:**` callout. Where the lab has a validated SOP, the SOP wins and the
protocol names it (lab SOP number, version and date; the SOPs themselves are
internal documents). Figures live in `figures/`.

P-files are the core programme, X-files are optional extensions (Section 6 of the script).

| ID | Title | Used in | Hands-on time | Wall-clock time | Resources |
|---|---|---|---|---|---|
| P01 | RAW 264.7: thaw, expand, growth curve | Exp 1 | 45 min day 1, 20 min/day after | 4 days | hood, incubator, centrifuge, counter, microscope |
| P02 | RAW 264.7: scrape, count, split, seed | Exp 1, Exp 2 | 45 min | 24 h before stimulation | hood, incubator, centrifuge, counter |
| P03 | RAW 264.7: freeze and re-thaw own stock | Exp 1 | 45 min + 45 min | overnight at −80 °C, nitrogen over the break | hood, centrifuge, freezing container, −80 °C, liquid nitrogen |
| P04 | Polarization | Exp 2 | 45 min + 30 min wash | 24 h | hood, incubator, vortex |
| P05 | PRR challenge | Exp 2 | 45 min + 45 min harvest | 16 h (overnight) | hood, incubator, plate centrifuge, −20 °C |
| P06 | ELISA IL-6 and TNF | Exp 2 | 3–4 h + coating the day before | 2 days | plate reader (450 nm), multichannel pipette |
| P07 | Griess assay | Exp 2 | 1 h | 1 h | plate reader |
| P08 | Flow cytometry of polarized RAW cells | Exp 2 (core), X02 | 2 h stain + 1 h acquisition | half day | hood, cooled plate centrifuge, heating block, cytometer slot, FlowJo seat |
| X01 | RNA isolation and qPCR | Extension | 1 h + 1.5 days | 6 h arm, then 2 days | hood, −80 °C, RNA bench, NanoDrop, thermal cycler, LightCycler 480 II |
| X02 | Peritoneal cells on the shared flow panel | Extension | 30 min + staining | half day, with cytometer slot | surplus peritoneal cell suspension provided by staff, ice, cooled centrifuge, cytometer slot |
| X03 | F4/80 IHC on tissue sections | Extension | 1 h + 2 × 3 h | about 5 days | surplus fixed tissue or blocks provided by staff, histology facility (paraffin), pressure cooker, histology bench, slide scanner |

## Dependencies in time

- P02 plates are seeded 24 h before P04.
- P04 runs 24 h, then wash, then P05 runs 16 h overnight; P08 uses the
  unchallenged wells of P04 on the day of the P05 challenge.
- P06 and P07 run on the P05 supernatants, the same day or later from frozen aliquots.
- P03 vials are re-thawed on the Monday after the break; Exp 2 plates come from the
  staff stock.
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
