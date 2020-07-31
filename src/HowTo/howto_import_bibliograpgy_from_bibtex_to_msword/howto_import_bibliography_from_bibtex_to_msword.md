# How To Import Bibliography From A BibTeX File To MS Word Document

Managing bibliographies could become a headache if not dealt with strategically. Those of you who have used **`LaTeX`**, know that managing bibliography with `BibTeX` is one of the benefits of using LaTeX as opposed to using MS Word. However, there could be scenarios when you may want to work using MS Word, while still having the simplicity of managing the bibliography using BibTeX.

Here, I present to you a **Ten Steps** receipe to do this. In fact logically speaking it is only three steps: 

- Create bibliography as a BibTeX (`.bib`) file.
- Upload the `.bib` file to Mendley and download the bibliography as an XML (`.xml`) file using the export functionality in Mendley.
- Import the `.xml` file with bibliography into MS Word using **Manage Sources** functionality for **References** and create **Bibliography**.

A sample BibTeX file looks like this:

```latex
%  A sample bibliography file: citations.bib
%  

@article{goodfellow2016nips,
  title={NIPS 2016 tutorial: Generative adversarial networks},
  author={Goodfellow, Ian},
  journal={arXiv preprint arXiv:1701.00160},
  year={2016}
}

@inproceedings{goodfellow2014generative,
  title={Generative adversarial nets},
  author={Goodfellow, Ian and Pouget-Abadie, Jean and Mirza, Mehdi and Xu, Bing and Warde-Farley, David and Ozair, Sherjil and Courville, Aaron and Bengio, Yoshua},
  booktitle={Advances in neural information processing systems},
  pages={2672--2680},
  year={2014}
}

@misc{wandb,
title = {Experiment Tracking with Weights and Biases},
year = {2020},
note = {Software available from wandb.com},
url={https://www.wandb.com/},
author = {Biewald, Lukas},
}
```

## A. Create bibliography as a BibTeX (`.bib`) file

1. Create a bibliography file with citations saved in BibTeX format. 
   Save it. Let us name the file `citations.bib`.

## B. Upload bibliography to Mendley and export as XML for MS Word

Upload the `.bib` file to Mendley and download the bibliography as an XML (`.xml`) file using the export functionality in Mendley.

1. Log into your [Mendley Account][#mendley].
   - Open a free Mendley account (if you don't have one already) at: https://www.mendeley.com/. 
   - Mendley helps you manage your references online. 
   - You don't have to download any software for this process.

   [#mendley]: https://www.mendeley.com/

1. Create a Folder in Mendley. Let us call it **`Test Refs`**.
   - Click on <kbd>+ Add</kbd>.
   - Click on <kbd>New Folder</kbd>.
   - Name it `Test Refs`.

1. Upload the bibliography file (`citations.bib`) to Mendley.
   - Click on <kbd>+ Add</kbd>.
   - Click on <kbd>Import BibTeX (.bib)</kbd>.
   - Select the file, `citations.bib` from your computer.
   - Click on <kbd>OK</kbd> to complete the import (if asked).

1. Add the imported references to the target folder `Test Refs`. 
   - The imported files are added to `All Documents` by default.
   - Click on <kbd>All Documents</kbd>.
   - Select all the references you just imported (usually they are at the top).
   - Click on <kbd>Add to</kbd>.
   - Select the target folder: `Test Refs`.
   - Click on <kbd>Add to</kbd>.
   - This adds all the selected documents to the target folder.

1. Export the bibliographies from the target folder as an XML file with extension `.xml`.
   - Click on the target folder: <kbd>Test Refs</kbd>.
   - Select all the documents in folder `Test Refs`.
   - Click on <kbd>Export to MS Word</kbd>.
   - This will download your bibliographies as an XML file, typically named: `xml-export.xml`.

## C. Import Bibliography from XML file to MS Word

Import the `.xml` file with bibliography into MS Word using **Manage Sources** functionality for **References** and create **Bibliography**.

1. Open MS Word and import the bibliographies from the XML file.
   - Open MS Word: either an *existing* document or a *new* document.
   - Click on **References** ribbon.
   - Click on <kbd>**Manage Sources**</kbd> >> <kbd>**Browse**</kbd>.
   - Select the downloaded XML file from your computer.
   - Select all the references on the left box: <kbd>SHIFT</kbd> + <kbd>⇓</kbd>
   - Click on <kbd>**Copy ->**</kbd>, to copy these references to the box on the right side (Current List).
   - Click on <kbd>**Close**</kbd>.

1. Time to test if the porting worked or not. 
   - Click on **Bibliography**.
   - Select the type of refences you want. For now let us select **References**.
   - This should insert a list of references into the MS Word file.

1. Congratulations! You have ported the bibliography from the `.bib --> .xml --> .docx`. 

---

> **CONGRATULATIONS!!** You have successfully imported your references from a BibTeX format to MS Word file. 

## How to get BibTeX for a research article

1. Go to Google Scholar.
2. Search for the research paper/book.
3. Click on the quotation sign and select BibTeX.
   [![BibTeX from Google Scholar][#front-page-google-scholar-bibtex]][#yt-google-scholar-bibtex]

   [#yt-google-scholar-bibtex]: https://youtu.be/aB_W2RORVdw
   [#front-page-google-scholar-bibtex]: resources/Google_Scholar_BibTeX_Demo_FrontPage.png
   [#cite-google-scholar]: resources/google_scholar_search_example.png 
