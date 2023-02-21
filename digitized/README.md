README in `bildersammlung-buddhismus-public/digitized`.

## Overview

This document defines the workflow for digitizing folders with the ScanTent. 

## Creator

This dataset was created by the University of Basel's Research and Infrastructure Support RISE (rise@unibas.ch) in 2022.

## License

The intellectual property rights pertaining to the digital objects in this dataset (viz. the digital images produced by following the workflow in this document) resp. the rights of the persons displayed on these images are under investigation; **you are therefore not allowed to use or distribute said digital objects or derivates thereof for any purpose other than granted by RISE**.

## Workflow

### Prequisites

- ScanTent
- Latex gloves or similar
- Laptop (or USB A outlet) to power ScanTent
- Smartphone with DocScan app installed and access to the internet
- Transkribus user account
- Working surface (table or similar)

### Preparation

- Clean your working surface and your hands
- Set up the ScanTent on your working surface
- Clean the lense of your smartphone
- Open the DocScan app and log in with your Transkribus user account
- Put on your gloves
- Take the filings out of the binder and place them in a stack (called input stack) on the working surface with the first filing on top
- A filing denotes anything that was filed in the binder, e.g., a blank page, a page with glued on images or text, a single photocopied page, a transparent folder with various pages or contents, and pages that are stapled together

### Scanning

Scanning is undertaken in three different steps: context, container, images

#### Scanning the context

Context scan are scans of the filings as given. These scans are used for two purposes:
1. Establishing the system for archiving the materials, and
2. Providing context for single images

Workflow:
- In the DocScan app, create a document entitled "Context FOLDER_NAME" where `FOLDER_NAME` is the name of the folder
- Use manual mode with standard settings; adjust "Text orientation" to be flush with image orientation
- Put the empty folder front up in the ScanTent and take a picture, and similar for its back
- Put the top filing from the input stack front up in the ScanTent and take a picture, and similar for its back (including empty front and/or back pages); ensure that the page is in focus (green squares on page) and correctly recognized by the automatic crop feature (orange frame around page); if not satisfactory retake picture; put the filing face down on a new stack (called output stack)
- Repeat previous step until input stack is empty
- Turn over output stack (called input stack again)

#### Scanning opaque containers

Some filings are opaque containers. This means that the contents of these filings are not identifiable via its context scan, e.g., a transparent folder with various pages or contents, or pages that are stapled together. By contrast, a page with glued on images is a transparent container in that all its contents are identifiable via the context scan.

Workflow:
- In the DocScan app, create a document entitled "Containers FOLDER_NAME" where `FOLDER_NAME` is the name of the folder
- Use manual mode with standard settings; adjust "Text orientation" to be flush with image orientation
- Take the top filing from the input stack and check whether it is an opaque container; if no, put the filing on a new stack (called output stack) and go to the next step; if yes, take out the contents of the opaque container and put them on a new stack (called content input stack) so that the sequence of the contents is preserved with the first content on top of the stack; take a blank picture (or picture of the empty filing); for each content on the content input stack, undertake a context scan (see above) until the content input stack is empty
- Repeat previous step until input stack is empty
- Turn over output stack (called input stack again)

#### Scanning images

Some filings contain images.  

Workflow:
- In the DocScan app, create a document entitled "Images FOLDER_NAME" where `FOLDER_NAME` is the name of the folder
- Use manual mode with standard settings; adjust "Text orientation" to be flush with image orientation
- Take the top filing from the input stack and check whether it contains (at least) one image; if no, put the filing on a new stack (called output stack); if yes, the sequence of the image is from top left to bottom right; take the image out of the filing; take a picture of the image and its back; ensure that the image is in focus (green squares on page) and and correctly recognized by the automatic crop feature (orange frame around image) - if the image is small, the scan surface needs to be elevated in order to reduce distance between image an camera; put the image back in the filing 
- Repeat previous step until input stack is empty

### Clean up

- In the DocScan app, crop the scans in each document and make sure all documents are uploaded to Transkribus.
- In SWITCHdrive under https://drive.switch.ch/index.php/s/BftYDNCk7KgGaWq, create a new folder using the scanned folder's inscribed name; create the subfolder "Context", "Containers", "Images". For each document, export its images from Transkribus and upload them to the corresponding subfolder. Exported images should be named "DOCNAME_DOCID_PAGENR.jpg" where `DOCNAME` is the name of the document, `DOCID` is the Transkribus document ID, and `PAGENR` is the page number. For example, the first image of the document called "Context WE 1 Moderner Buddhismus Europa und Asien Teil 1" with ID 1251916 becomes "Context_WE_1_Moderner_Buddhismus_Europa_und_Asien_Teil_1_1251916_0001.jpg". Note that any whitespace in `DOCNAME` must be replaced with an underscore. When exporting images using Transkribus Lite, software such as Adobe Bridge must be used to rename images. When exporting images from Transkribus Expert Client, the filename pattern `DOCNAME_${docId}_${pageNr}` can be used to generate the required filenames. For example, exporting images from the document "Context WE 1 Moderner Buddhismus Europa und Asien Teil 1" uses the pattern `Context_WE_1_Moderner_Buddhismus_Europa_und_Asien_Teil_1_${docId}_${pageNr}`.

### Notes on scanning the folders

Metadata and notes on workflow adaptions go into this spreadsheet: [https://docs.google.com/spreadsheets/d/1udfmKWExSlhcMMAeMTKuLM4DyKRJtt48XU-wDlgBuzI/edit#gid=0](https://docs.google.com/spreadsheets/d/1udfmKWExSlhcMMAeMTKuLM4DyKRJtt48XU-wDlgBuzI/edit#gid=0)


## To dos
