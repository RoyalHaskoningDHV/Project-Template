# Cookiecutter template for projects

This project contains a cookiecutter template to use for all BL Digital projects.
It currently contains templates for Python and for R.

Author: Ruben Peters
Email: ruben.peters@rhdhv.com

# Usage

To use the cookiecutter template, first install cookiecutter:

```
pip install cookiecutter
```

Then run the cookiecutter command in the parent folder of the new project (usually `/home/user/Python/`):

```
cookiecutter https://corporateroot@dev.azure.com/corporateroot/Project%20Templates/_git/Project_Templates
```

or if you use SSH keys for DevOps:

```
cookiecutter git@ssh.dev.azure.com:v3/corporateroot/Project%20Templates/Project_Templates
```

If this fails with `cookiecutter.exceptions.UnknownRepoType`, you can clone the repo and run cookiecutter locally:

```
git clone git@ssh.dev.azure.com:v3/corporateroot/Project%20Templates/Project_Templates
cookiecutter Project_Templates/
```

Then cookiecutter will ask a series of questions to determine which files to use and values to include in the README, setup.py etc. When you've answered all questions, cookiecutter will generate the entire folder structure. The last step is to initialize git and send the template as initial commit:

```
git init
git add .
git commit -m "Initial commit"
git remote add origin <server>
git push origin main
```

# Setting up DevOps pipelines

The cookiecutter template will also generate some DevOps pipelines you can use for linting, unit tests and building your Python package. 

For more information on setting up linting and unit test pipelines, see: https://wikiddc.corporateroot.net/doku.php?id=python_linting_and_unit_tests_in_devops_pipelines

For more information on publising your Python code as Python package see: https://wikiddc.corporateroot.net/doku.php?id=publish_and_use_python_packages_in_azure_devops

# Project structure

After running the cookiecutter, your code should look like this:

    ├── {{cookiecutter.pkg_name}}  <- Source code for use in this project (for python or 'src' when using R or not using a package)
    │   ├── __init__.py            <- Makes cto a Python module
    │   │
    │   ├── data_sources           <- Scripts to download or generate data
    │   │   └── __init__.py
    │   │
    │   ├── models                 <- Scripts to train models and then use trained models to make predictions (not included here)
    │   │   └── __init__.py
    │   │
    │   ├── preprocessing          <- Scripts to preprocess data from `data_sources` to obtain features for ML
    │   │   └── __init__.py
    │   │
    │   └── visualization          <- Scripts to create exploratory and results oriented visualizations (not included here)
    │       └── __init__.py
    |
    ├── data               <- Hidden from source control
    │   └── raw_immutable  <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project to create web pages with docs; 
    |                         see sphinx-doc.org for details
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    |
    ├── output             <- Any generated output data or files by the ML model (hidden from source control).
    │   ├── models         <- Trained and serialized models, model predictions, or model summaries.
    │   ├── reports        <- Project report(s).
    │   └── visualizations <- Final visualizations (e.g. used in project report).
    │
    ├── pipelines          <- .yaml files for azure devops pipelines or github actions.
    │   ├── build-python-package.yaml
    │   ├── lint-python.yaml
    │   └── test-python.yaml
    |
    ├── references         <- All useful documents, manuals and meta-files related to the project.
    |
    ├── run                <- Contains script to run the model and create final output.
    │   └── configs        <- Various config files, e.g. one used for production, one for testing.
    |
    ├── tests              <- Include all unit and integration tests here.
    |
    ├── conftest.py        <- Necessary for smooth integration of coverage reports (only python)
    │
    ├── README.md          <- The top-level README for developers using this project.
    |
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt` (if in a hurry, not included here)
    |
    ├── setup.cfg          <- sets standard linting options of RHDHV Data Solutions (called by setup.py)
    |
    └── setup.py           <- makes project pip installable (pip install -e .) so package can be imported
                              Add the necessary dependencies here as well! Only for python language.
