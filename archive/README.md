README in `bildersammlung-buddhismus-public/archive`.

## Overview

Tropy project to establish an archival order of the collection. Relevant Tropy database is `bildersammlung-buddhismus-public/archive/archivordnung.tpy`.

## Creator

This dataset was created by the University of Basel's Research and Infrastructure Support RISE (rise@unibas.ch) in 2022 and 2023.

## License

This dataset is licensed under a Creative Commons Attribution 4.0 International License.

## File structure and overview

### Tropy project

- `/archive/archivordnung.tpy`
- `/archive/archivordnung.json`. Export of `/archive/archivordnung.tpy` (sorted by `Title`).

### Required Tropy templates

- `/archive/Aneingung des Buddhismus.ttp`. Metadata template for objects.
- `/archive/Images format.ttp`. Metadata template for images.

## Ingesting scanned folders into Tropy

### Workflow

1. Scan folder as per the instructions in `bildersammlung-buddhismus-public/digitized/README.md`.
2. Create a list entitled "FOLDER_ID" where `FOLDER_ID` is the ID of the folder as per https://docs.google.com/spreadsheets/d/1udfmKWExSlhcMMAeMTKuLM4DyKRJtt48XU-wDlgBuzI/edit#gid=0.
3. Add all images from `bildersammlung-buddhismus-public/digitized/FOLDER_NAME/Context` to this list.
4. Create an item per filing (each filing has exactly two images).
5. For each item, assign a type chosen from the "Filings" schema below.
6. Move all items typed "Ordner" or "Zwischenblatt" to the list "Makulatur" (and remove them from the list "Schachtel FOLDER_NAME").
7. For each item typed "Fotoblatt", add the corresponding images from `bildersammlung-buddhismus-public/digitized/FOLDER_NAME/Images`. Ensure that these images are added in sequence, the recto images after the recto image of the Fotoblatt, and the verso images after the verso image of the Fotoblatt. Remember that each photo has two images (recto and verso; recto comes before verso in the sequence of images). For each recto image of a photo, use the `bildersammlung-buddhismus-public/archive/Images format.ttp" photo template and fill in the `Image format` field (allowed values see schema below).
8. For each item typed as opaque container (e.g., "Klarsichtmappe", "Geheftete Blätter"), add the corresponding images from `bildersammlung-buddhismus-public/digitized/FOLDER_NAME/Containers`. Ensure that these images are added in sequence and after the recto/verso images of the opaque container.

### Metadata schema

#### Filings

Filings have one of the following types:
- Ordner: folder
- Klarsichtmappe: transparent folder with contents
- Fotoblatt: a page with attached photo
- Geheftete Blätter: pages that are stapled together
- Blatt: page without photo but other content
- Aufgeklebt: page with glued on content
- Zwischenblatt: an empty page

#### Images format template

- Allowed values for the mandatory field `Image format`: A4, A5, A6, A7
- Take the smallest fitting value if no exact fit is given.

## Physically archiving folders

Instructions are given for a single folder.

### Prerequisites

- Latex gloves or similar
- Archiving materials (Archivbox, Jurismappen, Archivmappen, Fotomappen)
- Soft pencil (B3 or higher) and eraser
- PC with two screens
- Work station where you can put the folder, archiving materials, and you can see your PC screens

### Preparation

- Clean your working surface and your hands
- Open `/archive/archivordnung.tpy` on one screen and navigate to the folder in question
- Open `/indexing/indexing.tpy`, sort by `Source` and navigate to the folder in question
- Make ready required archiving materials

### Workflow

1. Add the folder's ID to the Box.
2. Add IDs to Jurismappen and Archivmappen based on `/archive/archivordnung.tpy`.
3. Open the folder take the first filing.
   1. Match the filing to the item in `/indexing/indexing.tpy` (use `/archive/archivordnung.tpy` for an overview if required).
   2. Add the item's ID.
   3. If the item is a container:
      1. Add the IDs of the contained items to the item and to the container.
   4. File the item(s) in the Archivmappe.
   5. If the Archivmappe is complete, file it in the Jurismappe.
   6. If the Jurismappe is complete, file it in the Box.
4. Repeat for the next filing in the folder

### Where to add IDs?

Locations in descending order of priority. Always make sure the ID is legible and does not obscure or impinge on the item.

#### Box

- Front top right corner, optional top right on sides

#### Jurismappen, Archivmappen

- Front top right corner, optional complete signature

#### Fotoblätter

- Front top right corner

#### Fotos

- On the Foto: back top right corner
- On the Fotoblatt: exactly where the Foto was taken from

#### Blätter, Aufgeklebt

- Back top right corner if back is empty
- Front top right corner

### Record of manual changes to IDs

Note that items classified as `Dubletten` in `/archive/archivordnung.tpy` do not have an ID and are not included in `/indexing/indexing.tpy`.

- `F01-JM003-AM002-B0013` misclassified (`Blatt` instead of `Foto`), new `F01-JM003-AM002-F0247`
- `F02-JM001-AM005-B0316` deleted (`Makulatur`)
- `F02-JM001-AM006-B0325` deleted (back side of `F02-JM001-AM006-B0324`)
- `F02-JM001-AM006-B0327` deleted (back side of `F02-JM001-AM006-B0326`)
- `F02-JM001-AM006-B0329` deleted (back side of `F02-JM001-AM006-B0328`)
- `F02-JM001-AM006-B0331` deleted (back side of `F02-JM001-AM006-B0330`)
- `F02-JM001-AM007-F0163` misclassified (`Foto` instead of `Blatt`), new `F02-JM001-AM007-B0340`
- `F02-JM001-AM008-B0334` misclassified (`Blatt` instead of `Foto`), new `F01-JM003-AM002-F0248`
- `F03-JM004-AM046-B0157` becomes `F03-JM004-AM047-B0157`, and `F03-JM004-AM046-B0341` was added (missing scan)

## To dos

- [ ] Add workflow for packing the materials