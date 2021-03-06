# Materials for the workshop _Introduction to Python and the Python Ecosystem_, April 20<sup>th</sup>, 2018


[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/CreateCodeLearn/data-science-track/master?filepath=Workshop_Coding)

This repository contains materials for a workshop on __Introduction to Python and the Python Ecosystem__. In order to re-run the workshop materials we encourage you to use the [_conda_](https://conda.io/docs/) package manager. Once installed, we created a new environment called `ccl_python` by typing

`conda create -n ccl_python python=3`

in the command line. It is recommended to add the [conda-forge channel](https://conda-forge.org/) to your conda channels:

`conda config --add channels conda-forge` 

You activate your new environment by typing 

`source activate ccl_python` (on LINUX and Mac) or

`activate ccl_python` (on WINDOWS). 

During the workshop we installed additional Python modules by typing

`conda install numpy pandas matplotlib seaborn holoviews notebook`. 

Then you are ready to go (if you are stuck check out the [conda documentation site](https://conda.io/docs/user-guide/tasks/manage-environments.html#)). 

> Alternatively, you may launch [binder](https://mybinder.org/) to get a reproducible executable environment immediately in your browser. Simply click the _launch binder_ icon in the upper left corner, or go [here](https://mybinder.org/v2/gh/CreateCodeLearn/data-science-track/master?filepath=Workshop_Coding).


***

If for any reason you did not attend the workshop, but want to follow along you may create an environment and install all required dependencies on your machine by calling

`conda env create -f environment.yml`.

This command creates an environment based on the information provided in the `environment.yml` file. Activate your environment as shown above, then you are ready to go.



