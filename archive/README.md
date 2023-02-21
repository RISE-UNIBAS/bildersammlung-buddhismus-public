README in `bildersammlung-buddhismus/archive`.

## Overview

Tropy project to establish an archival order of the collection. Relevant Tropy database is `bildersammlung-buddhismus/Archivordnung/archivordnung.tpy`.

## Creator

This dataset was created by the University of Basel's Research and Infrastructure Support RISE (rise@unibas.ch) in 2022 and 2023.

## License

This dataset is licensed under a Creative Commons Attribution 4.0 International License.

## Workflow draft for ingesting scanned folders into Tropy

1. Scan folder as per the instructions in `bildersammlung-buddhismus/Digitalisate/README.md`.
2. Create a list entitled "FOLDER_ID" where `FOLDER_ID` is the ID of the folder as per https://docs.google.com/spreadsheets/d/1udfmKWExSlhcMMAeMTKuLM4DyKRJtt48XU-wDlgBuzI/edit#gid=0.
3. Add all images from `bildersammlung-buddhismus/Digitalisate/FOLDER_NAME/Context` to this list.
4. Create an item per filing (each filing has exactly two images).
5. For each item, assign a type chosen from the "Filings" schema below.
6. Move all items typed "Ordner" or "Zwischenblatt" to the list "Makulatur" (and remove them from the list "Schachtel FOLDER_NAME").
7. For each item typed "Fotoblatt", add the corresponding images from `bildersammlung-buddhismus/Digitalisate/FOLDER_NAME/Images`. Ensure that these images are added in sequence, the recto images after the recto image of the Fotoblatt, and the verso images after the verso image of the Fotoblatt. Remember that each photo has two images (recto and verso; recto comes before verso in the sequence of images). For each recto image of a photo, use the `bildersammlung-buddhismus/Archivordnung/Images format.ttp" photo template and fill in the `Image format` field (allowed values see schema below).
8. For each item typed as opaque container (e.g., "Klarsichtmappe", "Geheftete Blätter"), add the corresponding images from `bildersammlung-buddhismus/Digitalisate/FOLDER_NAME/Containers`. Ensure that these images are added in sequence and after the recto/verso images of the opaque container.

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

## 