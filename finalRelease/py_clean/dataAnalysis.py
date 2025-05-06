import pandas as pd 
import numpy as np
from itertools import combinations

df_simulated = pd.read_csv("integration/df_final_simulated.csv")
df_simulated.head()

# Stroke Prevalence by Residence Type
stroke_by_residence = df_simulated.groupby("Residence_type")["stroke"].mean()
stroke_by_residence

# Identify numeric columns (excluding the target variable)
numeric_columns = df_simulated.select_dtypes(include="number").drop(columns=["stroke"]).columns

# Store interaction columns in a dictionary
interaction_data = {}
interaction_results = []

for col1, col2 in combinations(numeric_columns, 2):
    interaction_name = f"{col1}_x_{col2}"
    interaction_values = df_simulated[col1] * df_simulated[col2]
    interaction_data[interaction_name] = interaction_values
    corr = np.corrcoef(interaction_values, df_simulated["stroke"])[0, 1]
    interaction_results.append((interaction_name, corr))
    
# Concatenate new interaction features in one go (efficient!)
interaction_df = pd.DataFrame(interaction_data)
df_simulated = pd.concat([df_simulated, interaction_df], axis=1)

# Top 5 interaction terms by absolute correlation
interaction_results_df = pd.DataFrame(interaction_results, columns=["Interaction_Term", "Correlation_with_Stroke"])
top5 = interaction_results_df.reindex(
    interaction_results_df["Correlation_with_Stroke"].abs().sort_values(ascending=False).index).head(5)
top5

health_indicators = ["hypertension", "heart_disease", "bmi", "avg_glucose_level"]
socioeconomic_vars = ["Median_Income", "individual_income", "education_score"]

# Compute correlations
edu_health_corr = df_simulated[["education_score"] + health_indicators].corr().loc["education_score", health_indicators]
income_stroke_corr = df_simulated[["individual_income", "stroke"]].corr().iloc[0, 1]
socio_corr_stroke = df_simulated[socioeconomic_vars + ["stroke"]].corr()["stroke"].drop("stroke")

# Create new interaction terms
df_simulated["income_x_age"] = df_simulated["individual_income"] * df_simulated["age"]
df_simulated["education_x_bmi"] = df_simulated["education_score"] * df_simulated["bmi"]
df_simulated["income_x_glucose"] = df_simulated["individual_income"] * df_simulated["avg_glucose_level"]

# Correlation of interaction terms with stroke
interaction_corr_stroke = df_simulated[[
    "income_x_age", "education_x_bmi", "income_x_glucose", "stroke"
]].corr()["stroke"].drop("stroke")

# Assemble results into labeled DataFrames
edu_health_df = edu_health_corr.reset_index()
edu_health_df.columns = ["Variable", "Education vs Health"]
income_stroke_df = pd.DataFrame({
    "Variable": ["individual_income"],
    "Individual Income vs Stroke": [income_stroke_corr]
})

socio_corr_df = socio_corr_stroke.reset_index()
socio_corr_df.columns = ["Variable", "Socioeconomic vs Stroke"]

interaction_corr_df = interaction_corr_stroke.reset_index()
interaction_corr_df.columns = ["Variable", "Socioeconomic vs Stroke"]

# Combine all socioeconomic correlations
socio_combined_df = pd.concat([socio_corr_df, interaction_corr_df], ignore_index=True)
socio_combined_df

# Merge everything into final summary
final_summary = pd.merge(edu_health_df, income_stroke_df, on="Variable", how="outer")
final_summary = pd.merge(final_summary, socio_combined_df, on="Variable", how="outer")
# Save the final summary to CSV
final_summary.to_csv("integration/final_summary.csv", index=False)




