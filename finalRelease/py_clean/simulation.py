import pandas as pd
import numpy as np

df = pd.read_csv("integration/df_final.csv")
df.head()

np.random.seed(42)

df_simulated = df.copy()

# Simulate individual-level income: add noise to state-level Median_Income
df_simulated["individual_income"] = df_simulated["Median_Income"] + np.random.normal(0, 10000, size=len(df_simulated))
df_simulated.head()

# Simulate individual-level education score based on state-level education counts
edu_weights = {"HS_Grad": 1, "Bachelors": 2, "Masters": 3, "Doctorate": 4}
df_simulated["education_score"] = (
    df_simulated["HS_Grad"] * edu_weights["HS_Grad"] +
    df_simulated["Bachelors"] * edu_weights["Bachelors"] +
    df_simulated["Masters"] * edu_weights["Masters"] +
    df_simulated["Doctorate"] * edu_weights["Doctorate"]
)

# Normalize the education score to a 0–100 scale for interpretability
edu_min = df_simulated["education_score"].min()
edu_max = df_simulated["education_score"].max()
df_simulated["education_score"] = 100 * (df_simulated["education_score"] - edu_min) / (edu_max - edu_min)

df_simulated[["stroke", "age", "hypertension", "heart_disease", "bmi", "avg_glucose_level", "Median_Income", "individual_income", "education_score", "Urban_Pct", "State_Type"
]].head()

df_simulated.to_csv("integration/df_final_simulated.csv", index=False)

