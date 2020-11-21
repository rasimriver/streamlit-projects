# Introduction

This script allows to do some streamlit stuff. 

# Install

## Set-Up

Following the suggested set-up to work with this repo:
* Atom: [Link](https://atom.io/) - Used as simple IDE (any other alternative is sufficient too - However, git integration is suggested)
* Anaconda for your OS: [Link](https://www.anaconda.com/distribution/) - Used as command prompt and package manager

## Preparation and necessary packages

As usual start with cloning the repository:

> git clone https://YOUR-PERSONAL-ACCESS-TOKEN@github.com/rasimriver/streamlit-projects.git

Next, it is suggested to use a _virtual environment_ for your python environment. This can be done with Anaconda: [More Info](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)

> cd PATH/TO/YOUR/DIRECTORY

> conda create -n venv-str-tools python=3.7 anaconda

Now let's activate the enviroment

> conda activate venv-str-tools

And install the necessary additional packages

> pip install streamlit

# Run

1. Open Anaconda
> cd PATH/TO/YOUR/DIRECTORY

2. Activate the Virtual Envionment
> conda activate venv-str-tools

3. Start the engine:
> streamlit run str-tool.py
