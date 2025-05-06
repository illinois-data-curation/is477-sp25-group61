metadata_md = """
# Stroke Analysis Workflow - Metadata

## Project Overview

This project integrates individual health data (stroke occurrences) with state-level socioeconomic and RUCC data. The workflow explores links between health and socioeconomic/environmental factors via data cleaning, merging, simulation, and visualization.

---

## File Metadata

| File Name                           | Description                                                     | Created By               | Date       |
|-------------------------------------|-----------------------------------------------------------------|--------------------------|------------|
| `merged_census_rucc.csv`            | Cleaned census data merged with RUCC codes.                      | `merged_census_rucc.py`  | 2025-05-03 |
| `stroke_cleaned.csv`                | Cleaned stroke dataset.                                          | `stroke.py`              | 2025-05-03 |
| `df_final.csv`                      | Fully merged dataset (stroke + census).                          | `final_integration.py`   | 2025-05-03 |
| `df_final_simulated.csv`            | Dataset with simulated `individual_income` and `education_score`.| `simulation.py`          | 2025-05-03 |
| `pairplot_correlation.png`          | Pair plot showing relationships between health variables.        | `strokeAnalysis.py`      | 2025-05-03 |
| `heatmap_stroke_correlation.png`    | Correlation heatmap.                                             | `strokeAnalysis.py`      | 2025-05-03 |

---

## Workflow Steps

1. Clean Census Data.
2. Clean Stroke Data.
3. Integrate Data.
4. Simulate Data.
5. Analyze & Visualize.

---

## Data Dictionary

| Variable             | Description                                                           | Type        |
|----------------------|------------------------------------------------------------------------|-------------|
| `gender`             | Gender of the individual (0 = Female, 1 = Male).                       | Categorical |
| `ever_married`       | Marital status (Yes/No).                                               | Categorical |
| `RUCC_2023`          | Rural-Urban Continuum Code (1 = Metro, 9 = Most Rural).                | Integer     |
| `stroke`             | Stroke occurrence (0 = No, 1 = Yes).                                   | Categorical |
| `Median_Income`      | Median household income for the state.                                 | Numeric     |
| `Urban_Pct`          | Percentage of urban population in the state.                           | Numeric     |
| `individual_income`  | Simulated estimate of individual income.                               | Numeric     |
| `education_score`    | Simulated numerical representation of education level.                 | Numeric     |
| `bmi`                | Body Mass Index of the individual.                                     | Numeric     |
| `avg_glucose_level`  | Average glucose level.                                                 | Numeric     |
| `hypertension`       | Hypertension diagnosis (0 = No, 1 = Yes).                              | Categorical |
| `heart_disease`      | Heart disease diagnosis (0 = No, 1 = Yes).                             | Categorical |

---

## Notes on Data Quality

This dataset blends individual and state-level data. Please note:

- `education_score` and `individual_income` are **simulated** for analysis purposes.
- Socioeconomic variables are **state averages** (e.g., `Median_Income`), not personal data.
- Correlations may be weak due to mixing **individual health data with aggregate socioeconomic data**.
- Future work should aim to collect **true individual-level socioeconomic data** for stronger insights.

---

**Last Updated:** 2025-05-03
"""

with open("aboutProjectOutput/metadata.md", "w") as f:
    f.write(metadata_md)
