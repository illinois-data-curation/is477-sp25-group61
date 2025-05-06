import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_stroke = pd.read_csv("data/stroke.csv")
df_stroke.head()

df_stroke.shape

df_stroke.dropna(inplace=True)

df_stroke.shape

df_stroke.columns

# Change Gender to Binary Variables (1/0)
df_stroke['gender'] = df_stroke['gender'].map({'Male': 1, 'Female': 0, 'Other': 2})

# Change Ever Married to Binary Variables (1/0)
df_stroke['ever_married'] = df_stroke['ever_married'].fillna('No')
df_stroke['ever_married'] = df_stroke['ever_married'].map({'Yes': 1, 'No': 0})

# Export Cleaned and Updated Stroke CSV to A Updated_Files Folder 
import os
os.makedirs("integration", exist_ok=True)
df_stroke.to_csv("integration/stroke_cleaned.csv", index=False)

