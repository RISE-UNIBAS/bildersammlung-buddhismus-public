README in `bildersammlung-buddhismus-public/indexing`.

## Overview

Tropy project to index the collection. 

## Creator

This dataset was created by the University of Basel's Research and Infrastructure Support RISE (rise@unibas.ch) in 2023.

## License

This dataset is licensed under a Creative Commons Attribution 4.0 International License.

## File structure and overview

### Tropy project

- `/indexing/indexing.tpy`

### Required Tropy templates

- `/indexing/AneingungBuddhismus.ttp`. Metadata template for objects.
- `/indexing/ImagesFormat.ttp`. Metadata template for images.

### Data basis

- `/indexing/archivordnung_transformed.json`. Original data basis for Tropy project. Created by running `/scripts/Client.run_transformation` on `/archive/archivordnung.json`. Note that items classified as `Dubletten` in `/archive/archivordnung.tpy` do not have an ID and are not included in `/indexing/indexing.tpy`.

### Work in progress

- `/indexing/workflow`. Semi-automated workflow on `students` branch to collaborate on Tropy project to index the collection.

### Data modelling

- `/indexing/model`.

### Data analysis

- `/indexing/analysis.` Data analysis created by running `Client.run_analysis` on `/indexing/workflow/master_export.json`.

## How to use this Tropy project

Note that specific guidelines (e.g., Round 1) trump general guidelines!

### Round 2 (2023-05-03)

1. Checkout the `students` branch and make sure it is up-to-date.
2. Make a copy of `/indexing/indexing.tpy` entitled `/indexing/indexing_name.tpy` where "name" is your name.
3. Open `/indexing/indexing_name.tpy` with Tropy; if needed import the required templates `/indexing/AneingungBuddhismus.ttp` and `/indexing/ImagesFormat.ttp`
4. Follow the instructions on [ADAM](https://adam.unibas.ch/goto_adam_wiki_wpage_2942_1546444.html) for indexing and correcting the images assigned to you.
5. Export **_all objects_** from Tropy as JSON-LD (if not all objects are exported, there might be errors regarding the metadata namespaces). See Tropy documentation for instructions: https://docs.tropy.org/other-features/export. Save it as a file called `name_round_2.json` to `/indexing/workflow/user_export` where "name" is your name.
6. In GitHub Desktop, deselect all files/changes excluding `/indexing/workflow/user_export/name_round_2.json` before committing to the `students`-branch.
7. Push your changes.

### Round 1 (2023-04-05)

1. Checkout the `students` branch and make sure it is up-to-date.
2. Make a copy of `/indexing/indexing.tpy` entitled `/indexing/indexing_name.tpy` where "name" is your name.
3. Open `/indexing/indexing_name.tpy` with Tropy and import the required templates `/indexing/AneingungBuddhismus.ttp` and `/indexing/ImagesFormat.ttp`. The metadata section should look like this (here for object `F0001`):
![](https://raw.githubusercontent.com/RISE-UNIBAS/bildersammlung-buddhismus-public/main/docs/images/round_1_meta.png)
4. In Tropy, select the objects assigned to you via your name tag.
5. For each object assigned to you:
   1. If possible fill in the fields `Inscribed creator`, `Inscribed date`, `Inscribed person shown`, and `Inscribed location shown`.
      1. Each field has a corresponding field without the "inscribed"-part. Use this field only if you know the value of the field but the value is not inscribed anywhere.
      2. If a field has multiple values (e.g., a `Foto`-object with multiple persons shown), use semicolon `;` to separate values (e.g., "name one; name two; name three").
      3. Be sure to take into account an object's `Is Part Of`-field. For example, some metadata about a Foto object might only be found on the corresponding Fotoblatt object.
   2. Add the tag `rescan` if one of the object's images is too blurry to read.
   3. Add the tag `rights_inscribed` if there is inscribed information about the copy rights of the object.
   4. Add the tag `problem` you have problems with filling in the fields and want to discuss the case in class.
   5. Add the tag `done_round_1`.
6. Export **_all objects_** from Tropy as JSON-LD (if not all objects are exported, there might be errors regarding the metadata namespaces). See Tropy documentation for instructions: https://docs.tropy.org/other-features/export. Save it as a file called `name_round_1.json` to `/indexing/workflow/user_export` where "name" is your name.
7. In GitHub Desktop, deselect all files/changes excluding `/indexing/workflow/user_export/name_round_1.json` before committing to the `students`-branch.
8. Push your changes.

### General indexing guidelines for students

#### Setup

1. Create a GitHub account, get write access to this repo from the course admins, download and install GitHub Desktop (or similar).
2. Clone this repo. Since this repo does not contain the image folders/files in `/digitized`, download `bildersammlung-buddhismus-0.2.0.zip` from the private URL provided on ADAM and replace `/digitized` in this repo with `/digitized` from the unzipped download.
3. Open `/indexing/indexing.tpy` with Tropy.
4. Import the required Tropy templates `/indexing/AneingungBuddhismus.ttp` and `/indexing/ImagesFormat.ttp`. [See Tropy documentation for instructions](https://docs.tropy.org/in-the-template-editor/export-import-templates).
5. Consolidate the photo library. [See Tropy documentation for instructions](https://docs.tropy.org/using-tropy/add_files#consolidate-your-photo-library.). If it does not work out of the box, in Tropy go to `Edit\Preferences\Link phtos` and set the value to `Relative to the project file`.

#### Indexing

For illustration, assume you are assigned to index objects with IDs F0001-F0099 on January 1, 2023:

1. In GitHub Desktop (or similar), checkout branch `students`.
2. Make sure the branch is up-to-date.
3. Open "indexing/indexing.tpy" in Tropy.
4. Index the objects with IDs F0001-F0099 in Tropy.
5. Export all objects from Tropy as JSON-LD. See Tropy documentation for instructions: https://docs.tropy.org/other-features/export. Save it as a file called `name_2023-01-01.json` to `/indexing/workflow/user_export` where "name" is your name.
6. Commit and push your changes.

### Indexing guidelines for course admins

#### Automation and branch protection
- Students should not be able to simply push to `main`, so `main` is protected by rule requiring approved pull request from `CODEOWNERS` (i.e., course admins) before merging.
- However, students should be able to push indexing updates to a designated folder without review (automatic ingest will run on this folder).
- Solution: have `students` branch that is not protected, run automation on `students` and make pull request once a round of indexing is completed.
- ~~Better solution: have `students` branch that is not protected, but run automation on `main` by somehow letting the action bypass the branch protection rules (see https://github.com/community/community/discussions/13836), perhaps by running the action as member of `CODEOWNERS`?~~

## To dos

- [x] Setup automatic ingest
- [x] Fix template names
- [x] Namespace error when exporting only partial items: `dcterms:date` becomes `date` if `dc:date` is empty, dito for `dcterms:creator`.
- [ ] Add description of `/indexing/model`.
