import pandas as pd
import os 
import numpy as np

merged_census_rucc = pd.read_csv("integration/merged_census_rucc.csv")

merged_census_rucc.head()

len(merged_census_rucc)

df_stroke = pd.read_csv("integration/stroke_cleaned.csv")
df_stroke.head()

len(df_stroke)

import numpy as np
# Set seed for reproducibility
np.random.seed(42)

rural_states = merged_census_rucc[merged_census_rucc["State_Type"] == "Rural"]["state"].tolist()
urban_states = merged_census_rucc[merged_census_rucc["State_Type"] == "Urban"]["state"].tolist()
mixed_states = merged_census_rucc[merged_census_rucc["State_Type"] == "Mixed"]["state"].tolist()

def simulate_state(row):
    if row["Residence_type"] == "Rural":
        return np.random.choice(rural_states + mixed_states)
    elif row["Residence_type"] == "Urban":
        return np.random.choice(urban_states + mixed_states)
    else:
        return np.random.choice(mixed_states)
    
df_stroke["state"] = df_stroke.apply(simulate_state, axis=1)

df_stroke["state"] = df_stroke["state"].astype(str).str.zfill(2)
merged_census_rucc["state"] = merged_census_rucc["state"].astype(str).str.zfill(2)

final_df = pd.merge(df_stroke, merged_census_rucc, on="state", how="left")
final_df.head()

final_df.to_csv("integration/df_final.csv", index=False)
