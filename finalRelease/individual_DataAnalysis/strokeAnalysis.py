import pandas as pd
import numpy as np

df = pd.read_csv("data/stroke.csv")
df.head()

df.shape

df.dropna(inplace=True)

df.shape

df.columns

df.head()

# Change Gender to Binary Variables (1/0)
df['gender'] = df['gender'].map({'Male': 1, 'Female': 0, 'Other': 2})

# Change Ever Married to Binary Variables (1/0)
df['ever_married'] = df['ever_married'].fillna('No')
df['ever_married'] = df['ever_married'].map({'Yes': 1, 'No': 0})

df['Residence_type'] = df['Residence_type'].map({'Urban': 1, 'Rural': 0})

corr_matrix = df[["gender", "age", "hypertension", "heart_disease", "ever_married", "avg_glucose_level", "bmi", "stroke", "Residence_type"]].corr()
corr_matrix

import seaborn as sns
import matplotlib.pyplot as plt

# Pairplot With Selected Variables
selected_columns = ["gender", "age", "hypertension", "heart_disease", "ever_married",
                    "avg_glucose_level", "bmi", "stroke", "Residence_type"]
sns.pairplot(df[selected_columns], hue="stroke", palette="Set2", diag_kind="kde")
plt.suptitle("Pair Plot of Selected Health Variables", y=1.02)
plt.savefig("individual_file_displays/pairplot_correlation.png", dpi=300, bbox_inches="tight")
plt.show()

# Heatmap With Selected Variables 
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix of Stroke-Related Variables")
plt.savefig("individual_file_displays/heatmap_stroke_correlation.png", dpi=300, bbox_inches="tight")
plt.show()
