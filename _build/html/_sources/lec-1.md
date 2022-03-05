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

# Lecture 1: Python Basics

`Jupyter notebook` is a tools to make your programming in an interactive way, 
i.e., a cell-based environment where you can run your program in it one by one.
Compared to the original Python shell, it is more convinient to write, modify
and organize your code. In the remaining part of the lecture, I will 
refer `Python` as `Jupter notebook` if it does not make confuse. So let's go with it.

:::{note}
You do not need to install `Jupyter notebook` because we have installed 
`Anaconda` in the previous lecture and the latter one contains the former.
:::

Here is a simple illustration of `Jupyter notebook`'s user interface.
As you can see, it is consise and easy to understand.

```{figure} ./images/blank-notebook-ui.png
---
height: 200px
name: ui
---
**Notebook name**: You can change the notebook name here as you want. 
**Code cell**: A code cell is where you can write Python code. Once you have 
finished the code, press {guiLabel}`Shift`+{guiLabel}`Eneter` to run it.
```

## Using Python as a calculator
It is good to treat Python as a calculator when use it for the first time.
Try to type any equations in following box and run it!
```{code-cell}
1+2+3
```

Some common mathematical operators in Python are
- `+`: addition, `-`: subtraction
- `*`: represents multiplication $\times$
- `/`: represents division $\div$
- `//`: represents integral division
- `%`: represents modulo operation
- `**`: exponential
:::{note}
In mathematics, modulo operation returns the remainder. For example, 
the results of `7%2` in Python is `1` because the remainder of $7\div 2$ is $1$. 
:::

```{code-cell}
1+2, 1-2, 2*3, 5/3, 5//3, 5%3, 2**10
```

:::{hint}
What is the difference between `/` and `//`? Try by yourself!
:::
```{code-cell}
7/2, 7//2
```

**Error Message**
When you run some illegal equations, e.g., $1/0$ would lead to an error in Python.
```{code-cell}
1/0
```

Once you meet the message like this in your Python outputs, it means there can be
something wrong with your code, and you'd better to check it again. For debugging,
just copy the error message line and Google it!

```{figure} ./images/error.png
---
height: 400px
---
[StackOverflow](https://stackoverflow.com/questions/29836964/error-python-zerodivisionerror-division-by-zero) 
is a good place to find the solution to your issues.
```

## Variable
Variable is something whose value can be changed. In Python, we use the combination of
characters, digits, and underline(\_) as variable name, except digits cannot occur in the 
beginning of the name.

:::{note}
- `abc, ab2, _a, _2` are all okay as a variable name.
- `5G, @qq, ac.jp` are not variable names.
:::

In order to use a variable, you need to give it a value:
```{code-cell}
a = 2
```
If you try to use a variable without value, Python will complain with an error:
```{code-cell}
b
```

Some names are reserved by Python, so you cannot use them as variable name.
These names are called **keywords** and listed as below
```
False True None and as assert break class continue
def del elif else except finally for from global if 
import in is lambda nonlocal not or pass raise return
try while with yield
```

:::{note}
Some modern editors such as `Jupter notebook` provide colorful theme and highlight keywords,
variable, etc. in your code, but do not rely on it too much. Check by your eyes!
:::

### Type: `int` and `float`
Each value in Python has its type, e.g., `int` represets an integer
and `float` represets a float number, which is similar to real number
in mathematics.

Basically, one value is automatically assigned with a specific type and
you can use `type()` to look up its type.
```{code-cell}
type(1), type(-2), type(1.0)
```

There can be some abbrevations for `float` number. For example, if there
is only one zero before/after the point, we can omit it.
```{code-cell}
.01, 1.
```

**Scientific notation** is a common numbering system for large numbers,
and you can also use it in Python.

`[a]e[b]` is the standard form where `[a]` and `[b]` are integers and
this is equivalent to a `float` number $a\times 10^b$.
```{code-cell}
type(1e-2)
```

:::{note}
You can trust `int` because they are always accurate, while `float` are
not so much reliable because they are stored in computers in different
ways from `int`. In fact, `float` number will be formed into $a\times 2^b$
where $a,b$ are integers. Following is a simple example to show you
how computers deal with numbers in a way different from mathematics.
:::

```{code-cell}
a=1.1
b=2.2
a+b
```

### Type: `string`
A `string` is some words quoted with quotation marks `'` or `"`.
```{code-cell}
s = "hello world."
s
```
When the `string` contain quotation mark itself, try swith different
ones, e.g., 
```{code-cell}
s = '"python is good", he said'
s
```
or use escaped character `\"` to replace `"`:
```{code-cell}
s = "\"python is good\", he said"
s
```
For multiple-line `string`, use triple quoations like

```{code-cell}
"""
this is a multiple-line string
this is a multiple-line string
this is a multiple-line string
"""
```

:::{tip}
A line of code begins with sharp symbol `#` is a comment in Python.
Python will not process any comment and it is only used to explain your code.
:::

More interestingly, Python can naturally deal with Unicode symbol such as 
Chinese characters or Japanese Kana.
```{code-cell}
北海道大学 = "hokudai.ac.jp"
北海道大学
```

**Cast between different types**

Python provides `int()` to cast something to an integer:
```{code-cell}
int(1.5), int('1234')
```
and `float()` to cast something to a `float` number
```{code-cell}
float(1)
```

### Boolean type
Boolean type has only two values: `True` and `False`.
You can directly assign boolean value to a variable, or it can 
also be produced in boolean expression like
```{code-cell}
type(1==1)
```

:::{tip}
More boolean expressions:
- `==`: compare two numbers
- `<=`: less or equal $\le$
- `>=`: greater or equal $\ge$
- `<`: less
- `>`: greater
- `!=`: not equal
:::

Python also provdes keyword `not`, which is calculated by 
`not True = False` and `not False = True`.

Try these boolean expressions by yourself!
```{code-cell}
1<2, 1<=1, 3!=4
```

### `print()` function
Here we introduce `print()` which is a useful for basic outputs.
It can outputs numbers,
```{code-cell}
print(1,2,3,4)
```
or `string`
```{code-cell}
print("hello", ", ", "world.")
```

## Statement
Statement is something to control the computation in your program.
In the previous section, all of our computation is single. However, 
in practice, we often want to do many computations by Python:
```
computation 1
computation 2
computation 3
...
```
Without statements, computation would be tedious and bored, and 
programming would be impossible. In this section,
We will learn three important statements in Python.

### Assignment statement
Assignment statements in Python is simple, with standard form
```
var = expression
```
where `var` is a variable name and `expression` could be numbers, 
strings, boolean values and more complex calculation.

```{code-cell}
x = 1+2
boolean_var = True
text = "Python is good"
```

:::{note}
More assignment operatoins:
- `var += expression` is equivalent to `var = var + expression`
- `var -= expression` is equivalent to `var = var - expression`
- `var *= expression` is equivalent to `var = var * expression`
- `var /= expression` is equivalent to `var = var / expression`
:::

### Conditional statement

```{figure} ./images/cond.png
---
height: 400px
---
A conditional statement usually has two branches. In each running, 
Python will choose only one of them depending on if the condition
is `True` or `False`. 
```

In Python, a standard form code corresponding to the above figure is like
```python
if condition:
    some statements
else:
    some statements
```

However, sometimes we have only one branch to run, so 
```python
if condition:
    some statements
```
is also okay.

Please notice the indentatoin (4 spaces here), otherwise, you code will be wrong.
```{figure} ./images/inden.png
---
height: 100px
---
The red block represents a 4-space indentation. Please be careful with it.
```
Python use indentatoin to emphase code in different levels, which would help
Python to recognize the code as a conditional statements. If there is no 
indentation in Python, the following code
```python
if condition:
statement 1
statement 2
```
is confused for Python because it do not know the bound of branch. 

Fore more branches, we can use keyword `elif` to extend `if-else` form:
```python
if condition 1:
    statement 1
elif condition 2:
    statement 2:
...
(more branches)
...
else:
    some statements
```

:::{note}
Please try to write a GPA calculator with Python. The standard is shown as 
- $4.0$ for score $\ge 85$;
- $3.0$ for $75\le$ score $<85$;
- $2.0$ for $60\le$ score $<75$;
- $1.0$ for score $<60$.
:::
```{code-cell}
score = float(input("Input your score, and press 'Enter' key: "))
# write you code here
print("Your GPA is", gpa)
```

### Loop statement
Loop is a simple way to deal with tedious work by Python. In a loop,
the program would repeatedly do the samething until the loop ends.

In Python, there are two types of loop statements: `while`- and `for`-loop.

#### While loop
The standard form is 
```python
while condition expression:
    some statements
```
:::{important}
Please also notice the indentation here.
:::

Here is a simple example to compute $1+2+3+\ldots+100$, and by the formula

$$ \sum_{i=1}^n i = \frac{n(n+1)}{2} $$

we know the answer is $\frac{100\times(100+1)}{2}=5050$. So let Python check this!
```{code-cell}
i = 1
s = 0
while i<101:
    s += i
    i += 1
print(s)
```

:::{important}
If your code does not give any responses as you expect, check 
if there are any errors in the `while`-loop, e.g., can Python
ends the loop while reasonable iterations.
:::
#### For loop
Although $while$-loop can help us to do anything we want. 
For loop is more convinient in some cases. It has a standard form shown as below
```python
for element in collection:
    some statements
```
Here collection is a special object in Python 
from which we can pick up its elements one by one. In `for`-loop,
Python will pick each element in the order, and run the statements
and then pick another element until the loop ends.

:::{note}
`range(start, end, step)` is such a special object providing a
collection of all numbers from `start` to `end` with a interval 
`step`. More specifically, it contains $k$ numbers:

`start, start + step, start + 2*step, ..., start + k*step`

where 

$$ k = \lfloor \frac{end-start}{step} \rfloor $$

such that $start+k\times step < end$.
:::

Try to fill following code to make it do the same thing to the previous one.
```{code-cell}
s = 0
for i in range(1, 101):
    # write code here
print(s)
```

## Function and Package
### Function
Function is a code block can be invoked so that you can reuse your
code in an elegant way. A standard form is shown as below
```python
def func_name(param1, param2, ..., param n):
    some code
    return something
```
A simple addition function is here:
```{code-cell}
def add(x, y):
    return x+y
```
A very imporat applications of function is using it recursively. 
For example, to define factorial function:

$$ n! = n\times (n-1)\times(n-2)\ldots\times 2\times 1, 0!=1 $$

we notice that it has a recursive definition, i.e., 

$$ n! = n\times (n-1)!, 0!=1$$

So we can write the code in a few lines:
```{code-cell}
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
factorial(69)
```
:::{note}
Be careful with recursive definition, it often sucks.
:::

**Lambda expression** (also refered as lambda function, anonymous function)
is a function that defined without function name. In order to make code
simple and clean, Python provides lambda expression in a easy way:
```python
lambda param1, param2, ..., param n : func_body
```
where `func_body` must be a expression whose value will be return.

For example, you can define average function in just one line of code:
```{code-cell}
avg = lambda a, b : (a+b)/2
print(avg(3, 4))
```

:::{tip}
The key point to understand lambda expression is to treat function as
a sort of variable. In this way, we can define "the function of function", 
e.g. the integral calculation. 
:::

The definte integrals can be computed approximately as following formula:

$$ \int_a^b f(x) dx \sim \frac{b-a}{N}\sum_{i=1}^N f(a+\frac{i(b-a)}{N}) $$

So, we try to define this in Python:
```{code-cell}
def integrate(f, a, b):
    N = 10000
    s = 0
    for i in range(N):
         s += f(a+i*(b-a)/N)
    return s*(b-a)/N
integrate(lambda x:x**2, 0, 1)
```
The above code gives the estimated value of $\int_0^1 x^2=\frac{1}{3}$.

In practice, the majority of work in programming is to invoke the functions
in some places. These functions could be very complex and have a long list
of parameters so that you have no time to understand them all. Python has 
a feature named **default parameters** to figure out this problem, i.e., leave
some parameters with default values when it was defined by the author. 
Therefore, you can only focus on the remaining parameters.

```{code-cell}
def add(x, y=1):
    return x+y
print(add(1))
print(add(1, 2))
```
The above `add()` function requires two parameters, however, parameter `y` is set
with default value $1$ so you can ignore it. Both `add(1)` or `add(1,2)` are
correct.

### Package
In modern programming, reusing the other people's code is very important
and that is also why Python is so successful because it has one of the 
most powerful package management and plentiful package resources.

Before using a package, you need to install it. Some popular packages may
be already installed by Anaconda. If you want to install a new package,
e.g., `numPy`, try following
command in your `Jupyter notebook`:
```{code-cell}
!pip install numpy
```
:::{note}
The letter case of package name does not matter here.
:::

As you can see, Python will output several lines of message during installing.

Once the package is installed, you can `import` it before using. Also, you can 
give a short name for it, or just import specific functions from package.
```{code-cell}
import random
import numpy as np
from math import pi, sin, cos
```
Once you have imported the package, you can use it like following:
```{code-cell}
print(random.randint(0, 5)) # randint(0, 5) will return a integer in [0, 5)
print(cos(pi))
```



