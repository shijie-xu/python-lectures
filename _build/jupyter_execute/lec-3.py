#!/usr/bin/env python
# coding: utf-8

# # Data Analysis with Python
# 
# In this lecture, we will learn to build a simple pipeline, by which Python will process your data automatically.
# 
# The pipeline includes
# - a module reading data from csv/excel file
# - a module plotting figure and saving it to disk.
# - combining them together to a Python script.
# 
# ```{figure} ./images/turtles.jpeg
# ---
# height: 300px
# ---
# The "Four Musketeers" for Python data analysis: `numPy`, `matplotlib`, 
# `pandas` and `seaborn`.
# ```
# 
# ## Preparation
# This is an advanced lecture so it is recommended to learn [lecture 1](lec-1.md) and [lecture 2](lec-2.md) if you have no background 
# in Python programming. Additionally, as `Seaborn` is based on `Matplotlib`, it is better if you have a touch 
# with `Matplotlib` which you can learn from lecture 2.
# 
# Pandas is a data analysis and manipulation tools based on Python. To learn Pandas, 
# the best material is the [official cookbook](https://pandas.pydata.org/pandas-docs/version/1.4.0/pandas.pdf) 
# which can be found at the [official website](https://pandas.pydata.org).
# However, it is too bored to read so long a technical book, and a better way for beginners is to learn with 
# simple examples.
# 
# Before start everything, we need to install Pandas as well as some other packages via {guiLabel}`pip`.
# - numpy: You may already have a basic understanding in lecture 2.
# - openpyxl: Pandas requires it to read excel file.

# In[1]:


get_ipython().system('pip install -q numpy pandas openpyxl ')


# :::{note} 
# - Here `-q` means quiet installation which can be ignored if you don not understand.
# - In Jupyter Notebook, command starting with mark `!` is NOT native Python code, 
# but a wrapped shell command, i.e. you can run `pip install numpy` to install `numpy`
# in your {guiLabel}`Anaconda Prompt Shell`.
# :::
# 
# 
# ## A simple example

# In[2]:


import pandas as pd, numpy as np

