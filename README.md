# Python Data Science Primer

This primer will take you through some of the tools Python has for data science:
mathematical operations, statistics, visualization, machine learning, etc.

I will assume knowledge of python and some basic knowledge of the topics.
I won't be delving into the mathematical details of how the tools work.
Instead, I will focus on what they do, why you might use them and how to use them.

## Table of Contents

- [Usage] (#usage)
- [Installation] (#installation)
- [NumPy] (#numpy)

## Usage

All the content will be in the form of [Jupyter notebooks](http://jupyter.org/).
You can view it all directly on github without installing anything.
But I'd recommend playing along to get the most out of it.
If you're completely new to all the of tools being introduced, I'd recommend going
in the order outlined in this README because I will be building on the content
as I go along.

## Installation

You need to have [python3](https://www.python.org/download/releases/3.0/) installed.
If you're on Windows, I highly recommend using [Anaconda](https://www.continuum.io/downloads).

After that open a command line and run:

    pip install -r requirements.txt
    
Now from the root of this repository run:

    jupyter notebook
    
to launch Jupyter which will open a browser window where you can navigate through the files of the repo.

## NumPy

First up is [NumPy](http://www.numpy.org/).  NumPy, short for _Numerical Python_,
is the foundation of pretty much every mathematical python library.  It's primary
function is doing matrix operations.  It does a lot more, but I will be focusing
on the essentials.  

The [NumPy notebook](numpy/numpy.ipynb) goes over arrays, matrices, indexing, mathematical operations and statistical operations.
