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
- [Matplotlib] (#matplotlib)
- [StasModels] (#statsmodels)
- [Contributing] (#contributing)

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

The contents of the [NumPy notebook](numpy/numpy.ipynb) are:
* Arrays
* Matrices
* Array Creation Functions
* Generating Random Arrays
* Reshape
* Mathematical Operations
* Statistics

## Matplotlib

[Matplotlib](http://matplotlib.org/) is the most commonly used python library for creating 2D-plots.  It's API interface is inspired by MATLAB.  

The contents of the [Matplotlib notebook](matplotlib/matplotlib.ipynb) are:
* Line Graphs
* Scatter Plots
* Combining Plots and Creating Legends
* Histograms
* Styling

## StatsModels

[StatsModels](http://statsmodels.sourceforge.net/stable/index.html) is a library for running statistical models.

The [Regression notebook](statsmodels/regression.ipynb) inlcudes:
* OLS Linear Regression
* Using OLS Linear Regression to do Polynomial regression
* Categorical Variables in OLS Linear Regression

## Contributing

Contributions are more than welcome - from additional functionality I skipped
over to whole new packages I didn't include.  [Here's](https://github.com/docmarionum1/python-data-science-primer/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) a list of things I've already identified that I'd like to add.
