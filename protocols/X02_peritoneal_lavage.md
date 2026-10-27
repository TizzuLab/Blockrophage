# X02 Peritoneal lavage (extension)

> **Under construction.** This course runs for the first time in spring 2027 and is being built in the open. Interested students are welcome to apply and to give input ([contact](https://zindellab.ch/contact.html), [issues](https://github.com/TizzuLab/blockrophage-course/issues)). **Please do not use these protocols in the lab yet.** Values are unverified until this notice is gone.

> Extension. Requires mouse availability and licence coverage for post-mortem lavage
> `[TODO: confirm licence coverage; record genotype per mouse]`. Mice are
> breeding-surplus animals euthanised for colony management, of any genotype. No
> animal is killed for this course and no live animal experiment is performed.

| | |
|---|---|
| ID | X02 |
| Used in | Extension |
| Hands-on time | 20 min per mouse, then staining as P08 |
| Wall-clock time | half a day, coordinated with a cytometer slot |
| Resources | animal facility access with a supervisor, dissection bench, ice, cooled centrifuge, cytometer slot |
| Depends on | P08 panel and a reserved cytometer slot; polarized RAW cells ready on the same day |
| Lab SOP | Zindel lab 0603 "PerCFL lavage from mice" (v1.0, 2025-08-22) and 0605 "Peritoneal and mesothelial cell isolation combined" (preliminary). The SOP wins over this page. The lab SOP's anaesthesia step does not apply: course mice are euthanised by the facility. |

## Purpose

Obtain resident tissue macrophages without digestion and run them on the shared
panel in the same session as the polarized RAW cells. The first result, before any
activation marker, is that no in vitro cell falls into the large-peritoneal-
macrophage gate.

## Materials

- FACS buffer, ice-cold: PBS, 3% FCS, 2 mM EDTA, 10 mM HEPES (recipe in P08);
  15 mL per mouse. The lab's combined SOP alternatively uses DPBS with 2 mM EDTA
  and collects into a tube with 1 mL FCS.
- 10 mL syringe and 22G Insyte catheter (BD 381323)
- 50 mL tubes, labelled, on ice
- 70% ethanol, scissors, forceps, a board or surgical mat to fix the mouse
- ACK erythrocyte lysis buffer if the lavage is bloody (recipe in the protocol
  index)
- Counter, FACS reagents as in P08

## Before you start

- Supervisor present for the whole procedure.
- Mouse euthanised by the facility's approved method; genotype, sex and age
  recorded.
- P08 staining plan extended with the lavage samples, CD19 and Ly6C.

## Procedure

1. Fix the mouse on its back, wet the fur with 70% ethanol.
2. Cut the skin across the abdomen at the height of the hind legs and strip it up
   to the thorax, exposing the intact peritoneal wall. Do not open the peritoneum.
3. Insert the catheter through the peritoneal wall at the level of the hind leg,
   slightly left of the midline, away from the bladder and the vena cava. Withdraw
   the needle, leave the plastic catheter in place.
4. Inject 5 mL ice-cold buffer, massage the abdomen gently for 30 s, and withdraw
   the fluid slowly through the same catheter into the 50 mL tube on ice. Repeat
   three times in total (15 mL).
5. Centrifuge 300 × g, 5 min, 4 °C. If the pellet is red, resuspend in 1 mL ACK
   buffer for 2 min at room temperature, top up with buffer and centrifuge again.
6. Resuspend in buffer and count. Expect a few million cells per mouse, of which
   large peritoneal macrophages are roughly a third.
7. Stain with the course panel (P08) and acquire in the same session as the
   polarized RAW cells.
8. Hand the carcass to X03 if an organ is to be harvested.

## Controls

- CD19 gate removes B cells; F4/80 against MHCII separates large and small
  peritoneal macrophages; ICAM2 and Gata6 confirm resident identity.

## Checkpoints

- Recovery of most of the injected volume; a bloody lavage is noted and may be
  excluded.

## Known failure modes

- Low cell number: fluid lost on withdrawal, catheter tip against the gut or in
  the fat; reposition rather than push.
- Bloody lavage: a vessel was hit on insertion; lyse the erythrocytes and note it.
- Few LPM: older mouse or prior inflammation; record age and findings.

## Output

Cell counts, mouse metadata, FCS files, and the gated statistics side by side with
the RAW samples.
