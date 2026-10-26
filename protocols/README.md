# Protocols

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

One file per protocol, all on the same template (00_TEMPLATE.md): header table,
purpose, materials, before you start, procedure, controls, checkpoints, known failure
modes, output. Values the lab has not yet confirmed are marked `[TODO]`. Where the
lab has a validated SOP, the SOP wins and the protocol links to it.

P-files are the core programme, X-files are extensions from the nerd ladder.

| ID | Title | Used in | Hands-on time | Wall-clock time | Resources |
|---|---|---|---|---|---|
| P01 | RAW 264.7: thaw, expand, growth curve | Exp 1 | 45 min day 1, 20 min/day after | 4 days | hood, incubator, centrifuge, counter, microscope |
| P02 | RAW 264.7: scrape, count, split, seed | Exp 1, Exp 2 | 45 min | 24 h before stimulation | hood, incubator, centrifuge, counter |
| P03 | RAW 264.7: freeze and re-thaw own stock | Exp 1 | 45 min + 45 min | overnight at −80 °C, nitrogen over the break | hood, centrifuge, freezing container, −80 °C, liquid nitrogen |
| P04 | Polarization | Exp 2 | 30 min + 30 min wash | 24 h | hood, incubator |
| P05 | PRR challenge | Exp 2 | 45 min + 45 min harvest | 24 h | hood, incubator, centrifuge, −20 °C |
| P06 | ELISA IL-6 and TNF | Exp 2 | 3–4 h | 1 day | plate reader, multichannel pipette |
| P07 | Griess assay | Exp 2 | 1 h | 1 h | plate reader |
| P08 | Flow cytometry of polarized RAW cells | Exp 2 (core), X02 | 2 h stain + 1 h acquisition | half day | hood, centrifuge, cytometer slot, FlowJo seat |
| X01 | RNA isolation and qPCR | Extension | 1 h + 1.5 days | 6 h arm, then 2 days | hood, −80 °C, RNA bench, qPCR instrument |
| X02 | Peritoneal lavage | Extension | 1 h per mouse + staining | half day, with cytometer slot | animal facility, dissection bench, centrifuge, cytometer slot |
| X03 | Organ harvest and F4/80 IHC | Extension | 1 h + 2 h + 2 × 3 h | about 5 days | dissection bench, cryostat, histology bench, slide scanner |

## Dependencies in time

- P02 plates are seeded 24 h before P04.
- P04 runs 24 h, then wash, then P05 runs 24 h; P08 uses the unchallenged wells of
  P04 on the day of the P05 challenge.
- P06 and P07 run on the P05 supernatants, the same day or later from frozen aliquots.
- P03 vials are re-thawed on the Monday after the break; Exp 2 plates come from the
  staff stock.
- X02 and X03 share a mouse and must land on a cytometer slot.
