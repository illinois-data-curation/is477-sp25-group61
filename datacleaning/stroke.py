import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"stroke.csv")
df.head()

df.shape

df.dropna(inplace=True)

df.shape

df.columns

# Change Gender to Binary Variables (1/0)
df['gender'] = df['gender'].map({'Male': 1, 'Female': 0, 'Other': 2})

# Change Ever Married to Binary Variables (1/0)
df['ever_married'] = df['ever_married'].fillna('No')
df['ever_married'] = df['ever_married'].map({'Yes': 1, 'No': 0})

# Change Residence Type to Binary Variables (1/0)
df['Residence_type'] = df['Residence_type'].map({'Urban': 1, 'Rural': 0})

# Correlation Matrix With Selected Variables 
df[["gender", "age", "hypertension", "heart_disease", "ever_married", "avg_glucose_level", "bmi", "stroke", "Residence_type"]].corr()

selected_columns = ["gender", "age", "hypertension", "heart_disease", "ever_married",
                    "avg_glucose_level", "bmi", "stroke", "Residence_type"]
sns.pairplot(df[selected_columns], hue="stroke", palette="Set2", diag_kind="kde")
plt.suptitle("Pair Plot of Selected Health Variables", y=1.02)
plt.show()


