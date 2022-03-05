#!/usr/bin/env python
# coding: utf-8

# # Lecture 2: Python Basics
# 
# In this lecture, you will learn
# - advanced data types
# - basic data processing packages (coming soon)
# - basic file read/write operations (coming soon)
# 
# ## Advanced data types
# 
# The most attractive part of Python is its advanced data types including
# `list`, `tuple` and `dict`. These are in common use during modern
# programming languages but Python provides an extremely elegant way to 
# deal with them.
# 
# :::{tip}
# Since Python borrowed pretty much grammars from other languages, 
# people who are familiar with **MATLAB/Mathematica** would be also 
# familiar with these part.
# :::
# 
# ### `list`
# 
# A `list` in Python is a sequence of objects, which may be integers, string or others. 
# These objects are referenced with its names and seperated with comma in a pair of brackets:
# ```python
# [obj1, obj2, obj3, ... ]
# ```
# 
# Here are examples of `list` and you can try define new list by 
# combining the data types you have learned in previous lecture.

# In[1]:


list_of_numbers = [1,2,3,4]
list_of_strings = ['hello', 'world']


# :::{note}
# We usually use same type in a single `list`, but it is also possible
# to hybrid different types in a `list` like `[1, 'hello', 2, 'world']`.
# :::
# 
# `list` of `list` is also useful in some cases:

# In[2]:


list_of_list = [[1,2,3], [4,5,6], [7,8,9]]


# A more simple way to define a `list` is **list comprehension**, which
# has a standard form as below
# ```python
# [expr for index in collection]
# ```
# where `expr` is an expression, `index` is a index taken from `collection`. 
# Python will calculate the values of expression for each inedx in the
# collection and collect them together as a new `list`.

# In[3]:


list_square = [i**2 for i in range(10)]
print(list_square)


# List comprehension can be used with a condition, which would filter
# the elements in the `list`.

# In[4]:


l = [i for i in range(100) if i % 2 == 1]
print(l)


# #### Access elements in `list`
# `list` is an ordered sequence, which means indices are naturally binded
# with each element. Therefore, we can access single element in the `list`
# by the index following the `list` name:

# In[5]:


l = [1, 2, 3, 4]
print(l[1])


# :::{important}
# In Python, the indices start with zero and stop at $n-1$ where $n$ is
# the length of the `list`. So, `l[0]` is the first element in `l` and 
# `l[1]` is the second element in `l`.
# :::
# 
# :::{warning}
# Please make sure the indices are not out of bound. If you try to access
# such an element, Python would complain with an error.
# :::

# In[6]:


l = [1, 2, 3, 4]
l[4]


# Python also provides **negative index** which start from the last element
# with index $-1$ in an reversed ordered.

# In[ ]:


l = [1, 2, 3, 4]
print(l[-1], l[-2], l[-3], l[-4])


# :::{tip}
# You can use `list()` to cast a `range()` object into an list, e.g.,
# `list(range(5))` returns a `[0, 1, 2, 3, 4]`.
# :::
# 
# #### Slice operations
# 
# To access part of `list`, slice operation provides an elegant and concise
# way, i.e., it requires three parameters `start`, `end` and `step` to 
# get a sub-list from the `list`. For example,
# 
# ```python
# list_name[start:end:step]
# ```
# 
# represents a sub-list contains elements:
# 
# $$ start, start+step, start+2\times step, \ldots, start+k\times step < end $$
# 
# where
# 
# $$ k = \lfloor \frac{end-start}{step} \rfloor $$
# 
# such that $start+k\times step < end$.
# 
# In general, we do not give all three parameters but only two or one of them.
# By default, Python will treat
# - `start=0` and `end=-1` when `step>1` or
# - `start=-1` and `end=0` when `step<1`.
# 
# Suppose `l=[0,1,2,3,4]`, here are some examples:
# - `l[1:3] = l[1:3:1] = [0, 1, 2]`
# - `l[:3] = l[1:3:1] = [0, 1, 2]`
# - `l[::2] = l[0:-1:2] = [0, 2, 4]`
# - `l[::-1] = l[-1:0:-1] = [4, 3, 2, 1, 0]`
# 
# To modify an existing `list`, you need to select 
# one or more elements and assign them with a `list` or value.
# 
# To change single element:

# In[ ]:


l = [1, 2, 3, 4]
l[1] = -1
print(l)


# To changes multiple elements:

# In[ ]:


l = [1, 2, 3, 4]
l[:2] = [-1, 0]
print(l)


# :::{note}
# Other operations for `list`:
# - `l.append(x)` will append a new element `x` at the tail of the `l`.
# - `l.insert(pos, value)` will insert a new element `value` at index of `pos`.
# - `l1 + l2` will concatenate two lists `l1` and `l2`.
# - `l * n` will repeat `l` for $n$ times.
# :::
# 
# We can also use `for`-loop to travel a `list`:

# In[ ]:


p = [1, 2, 3, 4, 5]
for i in p:
    print(i)


# :::{seealso}
# Please refer to [lecture 1](./lec-1.html#for-loop) to recall `for`-loop statement.
# :::
# 
# ### `tuple`
# 
# `tuple` is baisically same as `list` except it is contained
# in `()` and its elements are unchangeable. It shares
# the majority of features that `list` also have. For example,
# - hybrid data types: `(1, 'hello')` is a tuple.
# - slice operation: `t[::-1], t[0:2], t[:1:]` are okay.
# - repeating: `t * 3` return `tuple` containing `t` for three times.
# 
# **Packing** and **Unpacking** are common operations in Python when you deal with
# `list` or `tuple`, i.e., we can explicitly assign elements to multiple variables,
# vice versa.

# In[ ]:


a = 1
b = 2
c = 3
t = a, b, c # note here, we do not need brackets ()
print(t)
c, d, e = t
print(c, d)


# :::{tip}
# Sometimes, we do not want to assign all elements, please use underscore `_`, i.e.,
# `_, b = s` is equivalent to assign `b` with `s[1]` and drop `s[0]` for two-element 
# `tuple` or `list` `s`.
# :::
# 
# The packing and unpacking are often used to define multi-value functions:

# In[ ]:


def mutli_value_func(x):
    return x-1, x+1
a, b = mutli_value_func(20)
print(a, b)


# ### `dict`
# 
# Both `list` and `tuple` can be accessed with its indices. However, in some cases, 
# number-based indices are not convinient to remember and understand. More general
# data types as indices are employed in `dict` data type. In fact, integers, string 
# or even tuple can be the indices (named `key`) of `dict`.
# 
# The standard form of a `dict` is 
# ```python
# {key1:value1, key2:value2, ...}
# ```
# For example, here is a `dict`:

# In[ ]:


d = {1:'apple', 2:'banana', 3:'orange'}


# :::{note}
# Be careful with the type of `key` because some types cannot be 
# a `key` of `dict`, e.g., `list`. Following code would give an error.
# :::

# In[ ]:


wrong_dict = {[1,2]:2, [1,2,3]:3}


# To access element in the `dict`, try

# In[ ]:


d[1]


# where `1` is one of the key of `d`.
# 
# `dict` provide function `keys()` get all keys:

# In[ ]:


d.keys()


# :::{note}
# Please try `values()` and `items()` to learn by yourself.
# :::

# In[ ]:


print(d.values())
print(d.items())


# To check if an value is in the `dict`, you can use `in` keyword:

# In[ ]:


d = {'apple':1, 'banana':2, 'orange':3}
'something' in d


# Also, you can travel `dict` by `for`-loop and this will pick all keys 
# in the `dict`:

# In[ ]:


for key in d:
    print(key, d[key])


# We can also define a **dict comprehension** like **list comprehension**, 
# and the way

# In[ ]:


dd = {fruit:d[fruit]+1 for fruit in d]}


# will define a new `dict`.
