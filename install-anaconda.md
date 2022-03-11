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

# Setup Programming Environments

In this lecture, we will learn  
- to install Python on the machine.

## Introduction

> Life is short, use Python.

Python is a popular high-level programming language created 
by *Guido van Rossum*, and released in 1991. It is used in various cases including
- scientific computing
- software development
- web development (Yes, the page you are reading is powered by Python!)
- system scripting

Also, you may choose to learn Python for
- its simple yet precise syntax, elegant way to organize code, and
- efficiency to save more 90% programming time compared with C/C++, Java, etc.

I strongly recommend to choose `Anaconda`,
a Python distribution aiming to simplify using for researchers
who have no experience in programming. `Jupyter`, a web-based editor
to write, modify and run Python code, is also contained in Anaconda. 

:::{tip}
(Optional) For those who prefer to write code in a desktop editor, 
[Visual Studio Code](https://code.visualstudio.com) would be a good choice.
Another better choice is [PyCharm](https://www.jetbrains.com/pycharm/download/),
which provides a complete toolchain for engineering purpose.
:::

## Install Anaconda 

Step 1. Download Anaconda installer.
```{figure} ./images/download-anaconda.png
---
height: 400px
name: download pycharm
---
Go to [Anaconda download page](https://www.anaconda.com/products/individual)
and click the {guiLabel}`Download` button to start downloading. 
```

Step 2. Double click the installer to lanuch.

Step 3. Read the licensing terms and click {guiLabel}`I Agree`.

Step 4. Select an install for {guiLabel}`Just Me`.

Step 5. Select a destination folder to install Anaconda and click the {guiLabel}`Next` button.
```{figure} ./images/select-dest-folder.png
---
height: 400px
name: select destination folder
---
Select the location on your machine to install.
```
:::{warning}
Make sure the location does NOT contain any non-ASCII characters or spaces.
:::

Step 6: Click {guiLabel}`Install`.

Step 7: Click {guiLabel}`Next`.

Step 8: We do not install `PyCharm` now, so click {guiLabel}`Next`.

Step 9: Uncheck the two boxes and click {guiLabel}`Finish` to close the installer.
```{figure} ./images/finish.png
---
height: 400px
name: finish
---
Congrats! You have successfully installed Anaconda.
```

:::{important}
Some issues may occur during the installation.
- No Administrator privilege granted (reported by Enyu). If this happen,
  please try again by right click installer and choose {guiLabel}`Run as Administrator`
  in the menu.
- Installtion path contains Chinese characters (reported by Haozhu).
  If this happen, choose another location.
If you meet other issues, please contact me.
:::
## Launch Jupyter notebook
After the installation, you can find `Jupyter` in you start menu by 
searching for keyword `jupyter`, shown as below
```{figure} ./images/jupyter.jpeg
---
height: 600px
name: jupter
---
Click the item to launch a Jupyter notebook.
```

Then, a new shell window will pop up and `Jupyter` will launch your defautl browser and open your home directory.
Click the {guiLabel}`New` button and choose {guiLabel}`Python 3 (ipykernel)`,
```{figure} ./images/home.png
---
height: 400px
name: home
---
```

Then, a new `Jupter notebook` will be created.
```{figure} ./images/nb.png
---
height: 150px
name: nb
---
Congrats! You have created a `Jupyter notebook`.
```

## Useful links
1. https://www.w3schools.com/python/default.asp Baisc Python tutorial
2. https://www.runoob.com/python/python-tutorial.html Python tutorial (only in Chinese)
3. https://www.rdkit.org/ Python package for Cheminformatics
4. https://biopython.org/ Python Package for Computational Molecular Biology
