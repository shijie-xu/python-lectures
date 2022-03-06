---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3

---

# Welcome to Python World!

This is a series of lectures to give beginners a feel for how python programming is proceed.


## How to use this interactive lectures

**For beginners, installing Python in the machine is pretty hard. Here we provide both the 
tutorial for [setting up environments](install-anaconda) and an online interactive python
environment.**

### Download this page
If you want to print this page, you can download the pdf files.
```{figure} images/download-pdf.png
---
height: 350px
---
Download PDF file.
```

### Launch the interactive environments
In order to run the code and learn by your own, you'd better to launch the interactive cells,
where the Python code are stored. You can find a cell [Here](lec-1.html#using-python-as-a-calculator).

Firstly, Open the lecture page, e.g., [Lecture 1](lec-1) and you would find
some buttons in the top of the page, click the {fa}`rocket` icon and choose {guiLabel}`Live Code`.

```{figure} images/guide-1.png
---
height: 250px
---
Launch **Live Code** to make cells executable.
```
Then, the applications will start, you can see following information in the top of the page.
```{figure} images/guide-2.png
---
height: 200px
---
The cells are building.
```
After a waiting for one minute (or more), the building is finished.
```{figure} images/guide-3.png
---
height: 75px
---
cells are ready.
```
### Run cells
You can run and edit any code in the cells on the page, e.g., [Using Python as a calculator](lec-1.html#using-python-as-a-calculator).
```{figure} images/guide-4.png
---
height: 250px
---
A cell in the page
```


## Table of contents

```{tableofcontents}
```

## The organization of lecture files

[Jupyter Book](https://jupyterbook.org/intro.html) 
is an open source project for building beautiful, 
publication-quality books and documents from computational material.
These lectures are based on Jupter Book and
all of the materials (PDF, Jupter Notebook, this site, etc.) are compiled from
[MyST Markdown](https://myst-nb.readthedocs.io/en/latest/index.html) files. The pipeline
is shown as below

```{figure} images/organization.png
---
height: 200px
---
**Jupyter Book(Website)**: If you do not install any Python environments yet, visit the website.
**Jupyter Notebook(*.ipynb)**: Run code in local machine.
```

