import requests
import pandas as pd

with open("apikey.txt") as f:
    api_key = f.read().strip()

acs_base = "https://api.census.gov/data/2022/acs/acs1"

acs_vars = [
    "NAME", "B19013_001E",  # Median income
    "B15003_001E",          # Total education population (25+)
    "B15003_017E",          # High school grad
    "B15003_022E",          # Bachelor's
    "B15003_023E",          # Master's
    "B15003_025E"           # Doctorate
]

acs_url = f"{acs_base}?get={','.join(acs_vars)}&for=state:*&key={api_key}"
acs_response = requests.get(acs_url)
acs_data = acs_response.json()

acs_df = pd.DataFrame(acs_data[1:], columns=acs_data[0])
acs_df = acs_df.rename(columns={
    "NAME": "State",
    "B19013_001E": "Median_Income",
    "B15003_001E": "Edu_Total",
    "B15003_017E": "HS_Grad",
    "B15003_022E": "Bachelors",
    "B15003_023E": "Masters",
    "B15003_025E": "Doctorate"
})

acs_df[["Median_Income", "Edu_Total", "HS_Grad", "Bachelors", "Masters", "Doctorate"]] = \
acs_df[["Median_Income", "Edu_Total", "HS_Grad", "Bachelors", "Masters", "Doctorate"]].astype(int)
    
acs_df.head()

rucc_df = pd.read_csv("data/ruralurbancodes2023.csv", dtype={'FIPS': str}, encoding='latin1') # Use latin1 because  RUCC CSV file isn’t in UTF-8 encoding which is typical for government files
rucc_df.head()

# Filter for RUCC_2023 only Clean Dataset 
rucc_clean = rucc_df[rucc_df["Attribute"] == "RUCC_2023"].copy()
rucc_clean["RUCC_2023"] = pd.to_numeric(rucc_clean["Value"], errors="coerce")
rucc_clean = rucc_clean.dropna(subset=["RUCC_2023"])
rucc_clean["RUCC_2023"] = rucc_clean["RUCC_2023"].astype(int)

def label_urban_rural(code):
    if code in [1, 2, 3]:
        return "Urban"
    else:
        return "Rural"

rucc_clean["RUCC_Label"] = rucc_clean["RUCC_2023"].apply(label_urban_rural)

# Extract state FIPS
rucc_clean["state"] = rucc_clean["FIPS"].str[:2]

# Group and Count
state_counts = rucc_clean.groupby(["state", "RUCC_Label"]).size().unstack(fill_value=0)
state_counts["Total"] = state_counts.sum(axis=1)

# Calculate Percentages of Urban/Rural Areas In Each State and Classify State as Primarily Urban or Rural 
for col in ["Urban", "Rural"]:
    if col in state_counts.columns:
        state_counts[f"{col}_Pct"] = (state_counts[col] / state_counts["Total"]) * 100
    else:
        state_counts[f"{col}_Pct"] = 0

def classify_state(row):
    if row["Urban_Pct"] >= 80:
        return "Urban"
    elif row["Rural_Pct"] >= 50:
        return "Rural"
    else:
        return "Mixed"

state_counts["State_Type"] = state_counts.apply(classify_state, axis=1)


# Formatting
state_counts = state_counts.reset_index()
state_counts["state"] = state_counts["state"].astype(str).str.zfill(2)

acs_df["state"] = acs_df["state"].astype(str).str.zfill(2)
merged_df = pd.merge(acs_df, state_counts, on="state", how="left")

merged_df.head()

import os
os.makedirs("final_project/integration", exist_ok=True)

# Export the merged DataFrame
merged_df.to_csv("integration/merged_census_rucc.csv", index=False)
