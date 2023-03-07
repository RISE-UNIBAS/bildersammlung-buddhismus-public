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

- `/indexing/Aneingung des Buddhismus.ttp`. Metadata template for objects.
- `/indexing/Images format.ttp`. Metadata template for images.

### Data basis

- `/indexing/archivordnung_transformed.json`. Original data basis for Tropy project. Created by running `/scripts/Client.run_transformation` on `/archive/archivordnung.json`.

## How to use this Tropy project

### Indexing guidelines for students

#### Setup

1. Create a GitHub account, get write access to this repo from the course admins, download and install GitHub Desktop (or similar).
2. Clone this repo. Since this repo does not contain the image folders/files in `/digitized`, download `bildersammlung-buddhismus-0.2.0.zip` from the private URL provided on ADAM and replace `/digitized` in this repo with `/digitized` from the unzipped download.
3. Open `/indexing/indexing.tpy` with Tropy.
4. Import the required Tropy templates `/indexing/Aneingung des Buddhismus.ttp` and `/indexing/Images format.ttp`. [See Tropy documentation for instructions](https://docs.tropy.org/in-the-template-editor/export-import-templates).
5. Consolidate the photo library. [See Tropy documentation for instructions](https://docs.tropy.org/using-tropy/add_files#consolidate-your-photo-library.). If it does not work out of the box, in Tropy go to `Edit\Preferences\Link phtos` and set the value to `Relative to the project file`.

#### Indexing

For illustration, assume you are assigned to index objects with IDs F0001-F0099 on January 1, 2023:

1. In GitHub Desktop (or similar), checkout branch `students`.
2. Make sure the branch is up-to-date.
3. Open "indexing/erschliessung.tpy" in Tropy.
4. Index the objects with IDs F0001-F0099 in Tropy.
5. Export all objects from Tropy as JSON-LD. See Tropy documentation for instructions: https://docs.tropy.org/other-features/export. Save it as a file called "name_2023-01-01.json" to `/indexing/workflow/user_export` where "name" is your name.
6. Commit and push your changes.

### Indexing guidelines for course admins

#### Automation and branch protection
- Students should not be able to simply push to `main`, so `main` is protected by rule requiring approved pull request from `CODEOWNERS` (i.e., course admins) before merging.
- However, students should be able to push indexing updates to a designated folder without review (automatic ingest will run on this folder).
- Solution: have `students` branch that is not protected, run automation on `students` and make pull request once a round of indexing is completed.
- ~~Better solution: have `students` branch that is not protected, but run automation on `main` by somehow letting the action bypass the branch protection rules (see https://github.com/community/community/discussions/13836), perhaps by running the action as member of `CODEOWNERS`?~~

## To dos

- [x] Setup automatic ingest
