README in `bildersammlung-buddhismus/indexing`.

## Overview

Tropy project to index the collection. 

## Creator

This dataset was created by the University of Basel's Research and Infrastructure Support RISE (rise@unibas.ch) in 2023.

## License

This dataset is licensed under a Creative Commons Attribution 4.0 International License.

## File structure and overview

### Tropy project

- `/Erschliessung/erschliessung.tpy`

### Required Tropy templates

- `/Erschliessung/Aneingung des Buddhismus.ttp`. Metadata template for objects.
- `/Erschliessung/Images format.ttp`. Metadata template for images.

### Data basis

- `/Erschliessung/archivordnung_transformed.json`. Original data basis for Tropy project. Created by running `/Scripts/Client.run_transformation` on `/Archivordnung/archivordnung.json`.

## How to use this Tropy project

### Guidelines for people indexing

#### Setup

1. Clone this repository in order to ensure that the image files in `/Digitalisate` are available (you have to manually put them there after copying them from the University file server).
2. Open `/Erschliessung/erschliessung.tpy` with Tropy.
3. Import the required Tropy templates `/Erschliessung/Aneingung des Buddhismus.ttp` and `/Erschliessung/Images format.ttp`. [See Tropy documentation for instructions](https://docs.tropy.org/in-the-template-editor/export-import-templates).
4. Consolidate the photo library. [See Tropy documentation for instructions](https://docs.tropy.org/using-tropy/add_files#consolidate-your-photo-library.). If it does not work out of the box, in Tropy go to `Edit\Preferences\Link phtos` and set the value to `Relative to the project file`.

#### Indexing

For illustration, assume you are assigned to index objects with IDs F0001-F0099 on January 1, 2023:

1. Clone the `bildersammlung-buddhismus` repository if you have not already done so. Make sure all files are up-to-date.
2. Create a new Git branch entitled "Name 2023-01-01" where `Name` is your name.
3. Index the objects with IDs F0001-F0099 in Tropy.
4. Export all objects from Tropy as JSON-LD. [See Tropy documentation for instructions.](https://docs.tropy.org/other-features/export) Save it as a file called `name_2023-01-01.json` to the folder `/Erschliessung/new_imports` where `name` is your name.
5. Commit and push your changes to your branch (you should commit and push whenever you finished an indexing session even before creating `name_2023-01-01.json`).
6. Create a pull request. One of the course leaders will review your request and approve or reject it. If it is approved, you are done; if not, update or change your files as requested.

## To dos

- [ ] Add instructions for how to add digitized images
- [ ] Revise steps 5 and following in indexing guide
- [ ] Guidelines for project managers
