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

# Lecture 3: Data Analysis 

:::{warning}
This page is still building. Please be patient for the coming lectures.
:::

In this lecture, we will learn data analysis as well as presentation in Python
including follwoing four packages:

```{figure} ./images/turtles.jpeg
---
height: 300px
---
The "Four Musketeers" for Python data analysis: `numPy`, `matplotlib`, 
`pandas` and `seaborn`.
```

**Why you need Python data analysis**

Basically, modern office suite like `Microsoft Excel` provides powerful features 
to process and present your data. However, they are lacking of flexibility and 
the features are hidden in their complex UI (user interface). On the other hand,
Python gives us more efficient and flexible  way to operate data. For example,
`Microsoft Excel` has a maximum row number $1048576=2^{20}$ in `Office 2007` 
or later while `pandas` can easily exceed this limitation.
```{figure} images/pandas-rows.png
---
height: 250px
---
A table has 100,000,000 rows x 1 columns.
```

It is also possible to custom a pipeline with help of these packages so
you can analyze data automatically. Once you build one, you can just run 
it every time when you have new data rather than operating data again and again.

## Preparation
:::{warning}
This is an advanced lecture so it is recommended to learn [lecture 1](lec-1.md) and
[lecture 2](lec-2.md) before it if you have no background in Python programming. 
:::

Pandas is a data analysis and manipulation tools based on Python. To learn Pandas, 
the best material is the [official cookbook](https://pandas.pydata.org/pandas-docs/version/1.4.0/pandas.pdf) 
which can be found at the [official website](https://pandas.pydata.org). The [documentation for pandas](https://pandas.pydata.org/docs/) is 
also helpful for your learning.

```{figure} images/pandas-docs.png
---
height: 300px
---
A sample entry of pandas docs. `DataFrame` is the basic data container in `pandas`.
```

Before start everything, we need to install Pandas as well as some other packages via {guiLabel}`pip`.
- `numPy`: `pandas` is based on `numPy`, an efficient numerical computation package written in C++.
- `openpyxl`: `pandas` requires it to read data from excel file.
- `matplotlib`: a graphical package to draw figures.

```{code-cell} ipython3
!pip install -q pandas numpy openpyxl matplotlib
```

:::{note} 
- Here `-q` means quiet installation which can be ignored if you don not understand.
- In Jupyter Notebook, command starting with mark `!` is NOT native Python code, 
but a wrapped shell command, i.e. you can run `pip install numpy` to install `numPy`
in your {guiLabel}`Anaconda Prompt Shell`.
:::

Let us import these two packages with short names:
```{code-cell}
import numpy as np
import pandas as pd
```

## Data container
`Pandas` provides two types of container `Series` and `DataFrame` which are used to store sequential
and tabular data respectively. 
```{figure} images/series.png
---
height: 100px
---
`Series` storing sequential data.
```
```{figure} images/dataframe.png
---
height: 200px
---
`DataFrame` storing tabular data.
```

Run following code to create two data containers.

```{code-cell} ipython3
s = pd.Series([1,2,3,4,5,6])
d = pd.DataFrame(np.arange(1, 19).reshape(3, -1))

print(s)
print(d)
```

:::{note}
Here `np.arange(1, 19)` will generate a arrary from $1$ to $18$, and `reshape(3, -1)`
will change the shape of arrary with first dimension as $3$. Parameter `-1` means it will be 
derivated internally and here will be replaced with $6$ because $6=18\div 3$.
:::

`shape` is a property of container and it is a tuple of dimensions.
```{code-cell}
print(s.shape)
print(d.shape)
```

For very large `DataFrame`, `Jupyter notebook` will only show a part of the content:

```{code-cell}
d = pd.DataFrame(np.random.randn(100, 30))
d
```

:::{note}
Here `np.random.randn(n, m)` will generate a random matrix with $n$ rows and $m$ columns.
Each element in the matrix follows the standard [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution) 
$ X\sim \frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$
:::

Try `head(n)` and it will give you the first $n$ rows of the `DataFrame` while `tail(n)`
will give the last $n$ rows.

```{code-cell}
d.head(5)
```

In order to make our examples meaningful, 
we employ a real-world dataset as an example to show how `pandas` works. [World Health Organization](https://covid19.who.int/info)
provides latest data about the COVID-19 such as vaccination and confirmed cases, which is keeped in CSV-format files. Here we 
refer to the vaccination data: [https://covid19.who.int/who-data/vaccination-data.csv](https://covid19.who.int/who-data/vaccination-data.csv).

```{code-cell}
:tags: [hide-output]

vac = pd.read_csv('https://covid19.who.int/who-data/vaccination-data.csv')
vac
```

:::{note}
`read_csv(path)` reads a CSV-format file from URL (Web link or local file) and returns a `DataFrame`.
For example, you can use `pd.read_csv('./data.csv')` to load csv file from your current directory.
:::


Properties `index` and `columns` will give the row/column labels:
```{code-cell}
vac.columns
```

In addition, you may want to sort by values, just like what we usually do in `Excel`.

```{code-cell}
:tags: [hide-output]
vac.sort_values(by='TOTAL_VACCINATIONS', ascending=False)
```

`T` property will return a transpose of `DataFrame`.
```{code-cell}
:tags: [hide-output]
vac.T
```

You can use `describe()` function to have a quick look on `DataFrame`:
```{code-cell}
vac.describe()
```
A better way to present data is using `plot()` function to draw all columns:
```{code-cell}
import matplotlib.pyplot as plt

vac = vac.sort_values(by='TOTAL_VACCINATIONS', ascending=False)
top20 = vac[['TOTAL_VACCINATIONS']][:20]
countries = vac['COUNTRY'][:20]
top20.index = countries

top20.plot.pie(y='TOTAL_VACCINATIONS', figsize=(15,15))
```
:::{tip}
`plot()` is a convinient way to visualize data in `pandas`, but it is
not perfect. We will learn more about the data visualization in following lectures.
:::

## Select

`Pandas` provides different ways to select elements in the `DataFrame`.
### `iloc`
`iloc[n]` will give the $n-1$ rows of the `DataFrame`, i.e., a `Series`.

```{code-cell}
vac.iloc[0]
```

:::{tip}
`iloc` index starts from $0$, instead of $1$. So the $n$-rows has a index $n-1$.
:::

In order to select multiple rows, just feed a list containing indices to the `iloc`:
```{code-cell}
vac.iloc[[0, 1, 2]]
```

Also, you can select both rows and columns at the same time:
```{code-cell}
vac.iloc[[0, 1, 2], [0, 4, 5]]
```

Or just access single element:
```{code-cell}
vac.iloc[0, 4]
```

:::{seealso}
You can also use [slice operations](lec-2.html#slice-operations) to access elements, try `vac.iloc[0:2, 0:3]`
:::
### `loc`

As you can see, `iloc` may be confused to read because it uses numbers as index. However,
`loc` provides another way to access by index and columns in `DataFrame`.
```{code-cell}
vac.loc[0:3, ["COUNTRY", "DATE_UPDATED", "TOTAL_VACCINATIONS"]]
```

:::{important}
Becareful with the **index** names in `iloc` and `loc`. They are different.
:::

### Boolean access
Both `loc` and `iloc` accept boolean parameters:
```{code-cell}
vac[vac['TOTAL_VACCINATIONS'] > 100000000]
```

### Modify

