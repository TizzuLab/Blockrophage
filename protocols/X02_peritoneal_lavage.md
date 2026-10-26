# X02 Peritoneal lavage (extension)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

> Extension. Requires mouse availability and licence coverage for post-mortem lavage
> `[TODO: confirm licence coverage; record genotype per mouse]`. Mice are
> breeding-surplus animals euthanised for colony management, of any genotype. No
> animal is killed for this course and no live animal experiment is performed.

| | |
|---|---|
| ID | X02 |
| Used in | Extension |
| Hands-on time | 1 h per mouse, then staining as P08 |
| Wall-clock time | half a day, coordinated with a cytometer slot |
| Resources | animal facility access with a supervisor, dissection bench, ice, centrifuge, cytometer slot |
| Depends on | P08 panel and a reserved cytometer slot; polarized RAW cells ready on the same day |
| Lab SOP | [TODO: link to the validated lab SOP; the SOP wins over this page] |

## Purpose

Obtain resident tissue macrophages without digestion and run them on the shared
panel in the same session as the polarized RAW cells. The first result, before any
activation marker, is that no in vitro cell falls into the large-peritoneal-
macrophage gate.

## Materials

- Ice-cold PBS with 2 mM EDTA, 5 mL per mouse
- Syringe and needle for injection and withdrawal `[TODO: gauge]`
- Tubes on ice, counter, FACS reagents as in P08

## Before you start

- Supervisor present for the whole procedure.
- Genotype and sex of the mouse recorded.
- P08 staining plan extended with the lavage samples and CD19.

## Procedure

1. Inject 5 mL ice-cold PBS/EDTA into the peritoneal cavity of the euthanised
   mouse.
2. Massage gently for 30 s.
3. Withdraw the fluid, keep on ice.
4. Count. Expect a few million cells, of which large peritoneal macrophages are
   roughly a third.
5. Stain with the course panel (P08) and acquire in the same session as the
   polarized RAW cells.
6. Hand the carcass to X03 if an organ is to be harvested.

## Controls

- CD19 gate removes B cells; F4/80 against MHCII separates large and small
  peritoneal macrophages; Tim4 with ICAM2 confirms resident identity.

## Checkpoints

- Recovery of most of the injected volume; a bloody lavage is noted and may be
  excluded.

## Known failure modes

- Low cell number: fluid lost on withdrawal, or the needle entered the gut.
- Few LPM: older mouse or prior inflammation; record age and findings.

## Output

Cell counts, mouse metadata, FCS files, and the gated statistics side by side with
the RAW samples.
