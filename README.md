# 🌦️ Sydney Weather Prediction Suite
<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

A full-stack machine learning application that provides localized weather forecasts for Sydney, Australia. The project utilizes a **FastAPI** backend for model inference and a **Streamlit** frontend for user interaction.

---

## 🚀 Deployed Link

1. [Streamlit Community Cloud](https://syd-weather-forecast.streamlit.app/)
2. [FastAPI hosting the ML Model](https://advmla-at2-25548684-latest.onrender.com/)

---

## Overview
This project consists of two distinct machine learning experiments designed to solve different meteorological challenges using historical data from the Open-Meteo Archive API.

### 1. Rain-or-Not (Classification)
- **Objective**: Predict if it will rain exactly **7 days after** a given input date.
- **Model**: Scikit-learn Pipeline (Experiment 1).
- **Features**: Apparent temperature, humidity, cloud cover, sunshine duration, and wind metrics.

### 2. Cumulative Precipitation (Regression)
- **Objective**: Forecast the total **cumulative precipitation (mm)** over a 3-day (72-hour) window.
- **Model**: Scikit-learn Pipeline (Experiment 2).
- **Features**: Hourly data points including soil moisture, dew point, and cloud cover at various altitudes.

---

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

### 4. Run the Streamlit App using Poetry

```bash
poetry run streamlit run app/main.py
```
