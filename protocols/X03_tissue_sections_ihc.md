# X03 F4/80 immunohistochemistry on tissue sections (extension)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/Blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

> Extension. Depends on primary material: we may be able to provide fixed tissue or
> paraffin blocks that are surplus from ongoing experimental work in the lab. Plan
> with your supervisor on the first afternoon; processing, embedding and sectioning
> by the facility span several days, so the tissue has to be committed in week 1.

| | |
|---|---|
| ID | X03 |
| Used in | Extension |
| Hands-on time | 1 h sectioning, 2 × 3 h staining |
| Wall-clock time | about 5 days (processing and embedding by the facility, sectioning, two staining days) |
| Resources | fume hood, histology facility for processing, embedding and sectioning `[TODO: ETH facility and turnaround]`, pressure cooker, histology bench, slide scanner `[TODO: instrument]` |
| Depends on | surplus fixed tissue or paraffin blocks provided by staff |
| Lab SOP | Zindel lab 011 "IHC staining (Biotin ABC)" (v1.0, 2026-07-16) and 01 "HE staining" (v1.0, 2026-03-18); both paraffin protocols. The SOP wins over this page. |

## Purpose

Test the hypothesis that every tissue contains F4/80-positive macrophages, in the
tissue available to your group, by single-colour immunohistochemistry on paraffin
sections, with an H&E serial section for orientation.

## Materials

- Fixed tissue in 70% ethanol or paraffin blocks, as provided; cassettes
- Paraffin processing, embedding and 3.5 µm sections by the histology facility;
  coated slides
- Deparaffinisation and dehydration: xylene, 100%, 95% and 70% ethanol, distilled
  water
- Antigen retrieval: citrate buffer pH 6 (10× stock diluted to 1× in distilled
  water, 200 mL), pressure cooker
- TBS and TBS with Tween 20 (TBST)
- Protein block and antibody diluent: 3% goat serum, 0.5% casein, 0.025% Tween 20,
  0.1% sodium azide in TBS
- Primary antibody: rat anti-mouse F4/80 `[TODO: FFPE-compatible clone and
  dilution; the lab SOP does not fix the clone]`
- 3% hydrogen peroxide in TBS (17 mL 35% H2O2 to 200 mL)
- Biotinylated secondary anti-rat, 1:200 in diluent
- VECTASTAIN Elite ABC-HRP reagent, ready to use (AdipoGen VC-PK-7100)
- DAB enhanced liquid substrate (Sigma D3939), 1 drop (30 µL) per 1 mL buffer
- Mayer's haematoxylin, HCl-ethanol for differentiation, eosin for the H&E slide
- Eukitt mounting medium, coverslips

## Before you start

- Tissue chosen from what staff can provide; ask for a piece of spleen as the
  positive control whenever one is available.
- Record what the staff tell you about the sample: tissue, fixation date, and the
  experiment it came from.
- Formaldehyde and xylene handled in the fume hood.
- Slides labelled with pencil (solvent-proof).

## Procedure

1. The tissue arrives fixed. Transfer to 70% ethanol if it is not already, and hand
   the cassettes to the histology facility for processing, paraffin embedding and
   3.5 µm sections. Ask for serial sections: one for F4/80, one for the no-primary
   control, one for H&E. Blocks that arrive already embedded skip to sectioning.
2. Deparaffinise: 2 × xylene 3 min, 2 × 100% ethanol 5 min, 95% ethanol 3 min,
   70% ethanol 3 min, distilled water 5 min.
3. Antigen retrieval in 1× citrate buffer pH 6 in the pressure cooker, 110 °C for
   15 min; let cool 25–30 min. Rinse in TBS 4 min.
4. Block with protein blocking solution, 30 min, room temperature.
5. Primary F4/80 in antibody diluent, overnight at 4 °C. The no-primary section
   gets diluent only.
6. Day 2: rinse in cold TBST 4 min. Quench endogenous peroxidase with 3% H2O2 in
   TBS, 10 min. Rinse TBST 4 min.
7. Biotinylated secondary 1:200 in diluent, 1 h, room temperature. Rinse TBST 4 min.
8. ABC-HRP reagent, 30 min, room temperature. Rinse TBST 4 min.
9. Develop with DAB, watching under the microscope until the positive control is
   brown and the no-primary section is still clean; rinse in distilled water.
10. Counterstain: Mayer's haematoxylin 7 min, rinse in running tap water until
    clear, differentiate with 1–2 dips of HCl-ethanol, blue under running tap water
    10 min.
11. Dehydrate: 70% ethanol 1 min, 2 × 95% 1 min, 3 × 100% 1 min, ethanol/xylene 1:1
    1 min, 3 × xylene 1 min. Mount with Eukitt.
12. H&E on the serial section per the lab SOP: haematoxylin as above, eosin 1 min
    15 s, 1–3 dips 70% ethanol, dehydrate, mount.
13. Image on the slide scanner. Submit the scan and a short legend to the atlas.

## Controls

- No-primary section: secondary, ABC and DAB background.
- Spleen, when available: positive control; red-pulp macrophages are bright.

## Checkpoints

- Positive control brown, no-primary section clean: the stain works and the tissue
  result can be read.

## Known failure modes

- Everything brown: endogenous peroxidase not quenched, or DAB developed too long.
- Nothing brown, positive control included: primary not FFPE-compatible or
  inactive, retrieval skipped, or wrong secondary species.
- Sections lifting off: retrieval too harsh or uncoated slides.

## Reading the result

F4/80 is bright on Kupffer cells, red-pulp macrophages and large peritoneal
macrophages, and dim on alveolar macrophages and lymph node sinus macrophages. A
weak result in lung or lymph node is a finding, not a failure, if the controls are
clean.

## Output

Scanned slides, the legend, and the atlas submission as a merge request; the
hypothesis and its outcome on the poster.
