# Weather Forecasting Models

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for
│                         36120_25SP_AT2 and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── 36120_25SP_AT2   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes 36120_25SP_AT2 a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py          <- Code to run model inference with trained models
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

---

---

# Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Sidsuresh/Production_Weather_Forecasting_Models.git
cd 36120_25SP_AT2/
```

### 2. Install the dependencies using Poetry

Make sure you have poetry installed on your system.

```bash
poetry install
```

### 3. Run the Jupyter Lab using Poetry

```bash
poetry run jupyter lab
```

### 4. Navigate to the following folders

1. notebooks\ folder to view the 4 jupyter notebooks
2. models\ folder to view the 4 models
3. dataset\raw folder to view the train and test datasets
4. dataset\processed folder to view the processed training and validation datasets for all 4 experiments.
5. dataset\processed\25548684_submissions folder to view the submission.csv for all 4 experiments.
