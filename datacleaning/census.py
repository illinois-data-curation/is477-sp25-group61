import requests 
import pandas as pd
import matplotlib
import hashlib

api_key = "df976c50384d9ee14627e6f9e477a6f47b59822c"

base_url = "https://api.census.gov/data/2022/acs/acs1"

variables = [
    "NAME",            # State name
    "B19013_001E",     # Median household income
    "B15003_017E",     # High school graduate
    "B15003_022E",     # Bachelor's degree
    "B15003_023E",     # Master's degree
    "B15003_025E"      # Doctorate degree
]

url = f"{base_url}?get={','.join(variables)}&for=state:*&key={api_key}"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data[1:], columns=data[0])
df = df.rename(columns={
    "NAME": "State",
    "B19013_001E": "Median_Income",
    "B15003_017E": "High_School_Grad",
    "B15003_022E": "Bachelors_Degree",
    "B15003_023E": "Masters_Degree",
    "B15003_025E": "Doctorate_Degree"
})

df

