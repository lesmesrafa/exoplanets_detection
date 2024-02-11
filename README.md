# Exoplanet Detection Using the Transit Method

<p align="center">
  <a href="https://docs.python.org/3.9/">
  <img alt="Python version" src="https://img.shields.io/badge/python-3.9-blue?&logo=python">
  </a>
  <a href="https://github.com/pre-commit/pre-commit"><img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit" alt="pre-commit" style="max-width:100%;"></a>
  <a href="https://github.com/astral-sh/ruff">
  <img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json?style=for-the-badge">
  </a>
  <a href="https://mypy-lang.org/">
  <img alt="Checked with mypy" src="https://www.mypy-lang.org/static/mypy_badge.svg">
  </a>
  <a href="https://github.com/psf/black">
  <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
  </a>
  <a href="https://jupyterbook.org">
  <img alt="Documentation with jupyterbook" src="https://raw.githubusercontent.com/executablebooks/jupyter-book/master/docs/images/badge.svg">
  </a>
</p>

## Overview

This project focuses on **detecting🔍🔭 exoplanets🪐🌍** using the transit method, a technique that **identifies planets** outside our solar system through the **temporary dimming of a star as an exoplanet passes in front of it**. By **using** the change in flux (light intensity) data of several thousand stars, **Spiking Neural Networks (SNNs)** are applied to efficiently process and analyze the observational data.

## Data Description

The dataset comprises observations of several thousand stars, each annotated with a binary label:
- `2` indicates a star confirmed to have at least one exoplanet in orbit, potentially hosting multi-planet systems.
- `1` denotes stars without confirmed exoplanets.

These labels are derived from continuous monitoring of stars' light flux over extended periods, looking for regular dimming patterns indicative of orbiting bodies. Such stars are initially considered 'candidate' systems, with further investigations required to 'confirm' the presence of exoplanets.

If you want to download the data please click [here](https://www.kaggle.com/datasets/keplersmachines/kepler-labelled-time-series-data)

## Objectives

- **Efficient Data Analysis**: Implement Spiking Neural Networks (SNNs) to analyze star flux data with minimal energy consumption, making the process suitable for space-based observations.
- **Exoplanet Detection**: Identify potential exoplanet-hosting stars from flux measurements, focusing on those with dimming patterns consistent with planetary transits.
- **Validation of Candidates**: Classify stars into candidates and confirm systems based on their light intensity patterns, aiding in the prioritization of stars for further study.

## Results

The implementation of Spiking Neural Networks (SNNs) for the analysis of stellar flux data has yielded promising results:

- **Test Loss**: 0.10, indicating a low error rate in the predictions made by the model.
- **Test Accuracy**: 97.85%, showcasing the model's high reliability in classifying stars correctly as hosting or not hosting exoplanets.
- **Sensitivity**: 40.00%, reflecting the model's capability to identify true positives, though it suggests a need for improvement in detecting stars with exoplanets more effectively.
- **Specificity**: 98.42%, demonstrating the model's strength in correctly identifying stars that do not host exoplanets, thereby minimizing false positives.
- **AUC-ROC**: 81.1834%, indicating a good ability of the model to distinguish between classes, though there is potential for further refinement to improve sensitivity without significantly reducing specificity.

These results underscore the efficacy of SNNs in processing astronomical data for exoplanet detection, particularly under the constraints of space-based observations. The high accuracy and specificity are encouraging, though the sensitivity indicates a challenge in detecting all true exoplanet-hosting stars, highlighting an area for future research and model optimization. The AUC-ROC score supports the model's overall discriminative capability, suggesting a balanced performance across various decision thresholds.


## Further Information

For more insights into the transit method and its role in exoplanet exploration, visit [NASA's Exoplanet Exploration Page](https://exoplanets.nasa.gov).





## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

To configure the coverage threshold, go to the `.coveragerc` file.

## Project dependencies

To generate or update the dependency requirements for your project:


```
python -m piptools compile --upgrade --resolver backtracking -o src/requirements.lock src/requirements.txt -v
```
```
pip install -r src/requirements.lock
```

This will `pip-compile` the contents of `src/requirements.txt` into a new file `src/requirements.lock`. You can see the output of the resolution by opening `src/requirements.lock`.

After this, if you'd like to update your project requirements, please update `src/requirements.txt` and re-run `kedro build-reqs`.


## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `catalog`, `context`, `pipelines` and `session`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r src/requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to convert notebook cells to nodes in a Kedro project
You can move notebook code over into a Kedro project structure using a mixture of [cell tagging](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#cell-tags) and Kedro CLI commands.

By adding the `node` tag to a cell and running the command below, the cell's source code will be copied over to a Python file within `src/<package_name>/nodes/`:

```
kedro jupyter convert <filepath_to_my_notebook>
```
> *Note:* The name of the Python file matches the name of the original notebook.

Alternatively, you may want to transform all your notebooks in one go. Run the following command to convert all notebook files found in the project root directory and under any of its sub-folders:

```
kedro jupyter convert --all
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can run `kedro activate-nbstripout`. This will add a hook in `.git/config` which will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.


