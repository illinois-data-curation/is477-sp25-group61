# Stroke Risk & Socioeconomic Factors: A Data Integration & Simulation Approach

**Link to Archival Record:** 

**Dropbox Folder:** https://uofi.box.com/s/gzi9ls3qg0trx7l4nv182iud1s0uijmy 

**Github Repository:** https://github.com/illinois-data-curation/is477-sp25-group61

**Github Final Release:** https://github.com/illinois-data-curation/is477-sp25-group61/releases/tag/final-project

## Contributors  
Michelle Liu, Sophomore at the University of Illinois Urbana-Champaign  
Sophomore Class of 2027  
Finance and Data Science, Minor in Chemistry  
Github Repository Link: https://github.com/illinois-data-curation/is477-sp25-group61

---

## Summary  

Examining cardiovascular health in relation to educational attainment, urban or rural living conditions, and broader socioeconomic factors is essential for understanding and addressing health disparities in the United States. Cardiovascular diseases remain one of the leading causes of death nationally, but its prevalence and outcomes are not evenly distributed across the population. Research consistently shows that individuals with lower levels of education tend to have higher rates of heart disease, potentially due to limited health literacy, reduced access to care, and increased exposure to health risks such as poor diet, smoking, and physical inactivity. Socioeconomic factors, including income and employment status, also play a critical role in shaping health behaviors and determining access to preventive and ongoing care. Understanding how these variables intersect can help target interventions, guide policy, and ultimately reduce preventable cardiovascular morbidity and mortality across diverse communities.

Cardiovascular diseases remain a leading cause of death nationally, but their distribution is not uniform. Prior research has shown strong associations between lower education, lower income, and higher cardiovascular risk. My motivation for choosing this research project/study is because I previously worked in medical assisting and noticed that cardiovascular diseases were the most common in regular patients. Since our office focused on lower income families and individuals on Medicare, I was curious about if there was a correlation between an individual’s socioeconomic background and if they were more likely to develop such diseases. 

Overall, our goal was to investigate whether integrating health and socioeconomic datasets could highlight meaningful correlations, especially focusing on simulated interaction effects like income × age and education × BMI.

---

## Research Questions  
- How does educational attainment relate to health indicators at the individual level?  
- Is there a relationship between individual income and stroke occurrence and how do broader socioeconomic variables correlate with stroke risk?  

---

## The Analysis Workflow  
- Integrated the Kaggle stroke dataset with ACS Census + USDA RUCC data.  
- Analyzed individual dataset patterns using pairplots, heatmaps, and correlation matrices  
- Simulated individual-level socioeconomic variables (e.g., income, education_score) using state medians + noise  
- Engineered interaction terms to capture nuanced health disparities  
- Investigated correlation between simulated data, integrated data, and individual features  

---

# Data Profile

### Stroke Dataset (Kaggle Non-API)  
**[Link to Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)**

Federico Soriano Palacios is an Associate at Oliver Wyman with a strong background in data science and analytics. He holds a double Master’s degree in Data Science from Universidad Pontificia Comillas and the University of Sydney, graduating top of his class and earning multiple academic awards. He’s also a Kaggle Grandmaster and CFA Level I passer. He originally obtained this dataset from a confidential source and said to contact him for more information; however after doing so, he had not responded. Therefore, I tried to document as much information as I can about this dataset. 

The dataset contains both 8 categorical and 3 quantitative variables. The primary variables we will be analyzing are gender, age, hypertension, heart disease, avg_glucose_level, bmi, stroke, work type, and residence_type.  
To define some of the more technical variables:  

- **Hypertension**, or high blood pressure, is a condition where the force of the blood against the artery walls is consistently too high. It increases the risk of stroke, heart disease, and other health problems.  
- **Body Mass Index (BMI)** is a numerical measure that assesses whether an individual has a healthy body weight relative to their height. To note:  
  - Underweight: < 18.5  
  - Normal: 18.5 – 24.9  
  - Overweight: 25 – 29.9  
  - Obese: ≥ 30  
- **Avg_Glucose_Level**: High glucose levels can be an indicator of diabetes, which is a major risk factor for stroke. To note:  
  - Normal: Less than 100 mg/dL  
  - Pre-diabetes: 100–125 mg/dL  
  - Diabetes: 126 mg/dL or higher  

The remaining variables will be evaluated for further analysis after conducting exploratory data analysis on each dataset and integrating them. Additionally, they may be considered as potential confounding variables in the later stages of analysis, especially if unexpected correlations arise between our primary target variables.

**License**: Proprietary (requires permission from dataset creator)  
**Note**: Since I wasn’t too sure if this data was reproducible, I chose to do a checksum on this dataset in order to check the integrity.

---

### American Community Survey US Census Dataset (API)  

**Link to US Census Website**  https://www.census.gov/acs/www/data/data-tables-and-tools/data-profiles/2022/

**Link to API** https://api.census.gov/data/2022/acs/acs1

The 2022 American Community Survey (ACS) 1-Year Estimates provide a detailed snapshot of socioeconomic conditions across the United States at the state level. This analysis focuses on key variables related to income, education, and employment. Median household income (B19013_001E) serves as a core indicator of economic well-being, while educational attainment is captured through bachelor's (B15003_022E), master's (B15003_023E), and doctorate (B15003_025E) degree completion. Additional measures such as the poverty count (B17001_002E) and unemployment (B23025_005E) provide insight into economic hardship and labor market conditions.

**License**: Public domain (US Census data)

---

### USDA Rural Urban Continuum Codes  
**Link to Dataset** https://www.ers.usda.gov/data-products/rural-urban-continuum-codes

The USDA’s 2023 Rural-Urban Continuum Codes (RUCC) provide a county-level classification system that distinguishes areas based on population size and proximity to metropolitan areas. These codes range from 1 to 9, with lower numbers representing highly urbanized, metro counties and higher numbers indicating more remote, rural counties. The RUCC system allows researchers and policymakers to analyze geographic patterns beyond the traditional urban-rural divide by incorporating nuanced distinctions such as small metro, adjacent nonmetro, and isolated rural areas. By aggregating these codes to the state level, it's possible to classify states as predominantly Urban, Rural, or Mixed based on the distribution of their counties.

**License**: Public domain

---

## Key findings

### Summary of Stroke Dataset Cleaning and Analysis:

#### Cleaning Step for Stroke Dataset CSV

**Initial Inspection & Cleaning**  
- Loaded the dataset (stroke.csv) and checked its structure (shape, head).  
- Dropped all rows with missing values using dropna(), ensuring a complete dataset for analysis.

**Variable Standardization & Encoding**  
- Converted gender into a binary variable:  
  - Male = 1, Female = 0, Other = 2.  
- Filled missing values in ever_married with 'No' and encoded as binary:  
  - Yes = 1, No = 0.  
- Recoded Residence_type into binary:  
  - Urban = 1, Rural = 0.

**Exploratory Correlation Analysis**  
- Selected key health-related variables (age, hypertension, heart disease, glucose, BMI, etc.).  
- Created a correlation matrix to examine linear relationships between predictors and stroke outcomes.

**Visualization**  
- Produced a pairplot (scatterplot matrix) to visually explore interactions between variables, with stroke status highlighted by color.  
- Generated a heatmap of the correlation matrix for an at-a-glance view of variable relationships.

**Individual DataSet Findings:**  
- The heatmap of stroke-related variables showed that while most features had weak linear correlations with stroke occurrence, the strongest (though still modest) positive correlation was between age and stroke (~0.08). Age also showed moderate positive correlations with hypertension and heart disease, which is expected given cardiovascular risk factors rise with age.  
- The pairplot helped visualize distributions and bivariate relationships. You could see clear trends where older individuals and those with hypertension or heart disease were more likely to have a stroke. Additionally, there was clustering in BMI and glucose levels by stroke status, though no strong pattern stood out visually across all variables.

---

### Summary of Data Integration & Simulation Steps:

**Census API Data Retrieval:**  
- Accessed the American Community Survey (ACS) 2022 data programmatically using the Census API.  
- Variables included median income and detailed educational attainment (high school, bachelor's, master's, doctorate).  
- The data was pulled into a pandas DataFrame, cleaned, and columns were renamed for clarity.

**RUCC Dataset Cleaning & Classification:**  
- Loaded the USDA’s Rural-Urban Continuum Codes (RUCC) dataset and filtered it to only include relevant 2023 codes.  
- Converted RUCC codes into binary labels ("Urban" vs. "Rural") based on the USDA classification system.  
- Aggregated RUCC codes at the state level and calculated urban/rural percentages and classified each state as:  
  - Urban (≥80% urban)  
  - Rural (≥50% rural)  
  - Mixed (everything else)

**State-Level Merging:**  
- Merged the ACS data and the RUCC summaries on the state FIPS code, creating a combined state-level dataset with both socioeconomic and urban/rural indicators.

**Simulated State Assignment:**  
- Using the cleaned stroke dataset, assigned a simulated U.S. state to each individual based on their Residence_type:  
  - Rural individuals were randomly assigned to rural/mixed states.  
  - Urban individuals were randomly assigned to urban/mixed states.  
- This step ensured a plausible geographic link between individuals and state-level socioeconomic data.

**Integrated/Simulated Data Findings:**  
| Feature                 | Correlation with Stroke |
|-------------------------|-------------------------|
| Median_Income           | +0.012                  |
| Individual_Income       | +0.006                  |
| Education_Score         | −0.017                  |
| income_x_age            | +0.206                  |
| income_x_glucose        | +0.119                  |
| education_x_bmi         | −0.006                  |

**Key Takeaways:**  
- **Main Effect Findings:** All direct relationships (education, income) show very weak correlations to stroke, likely due to the granularity gap between individual-level health data and state-level socioeconomic statistics.  
- **Interaction Effects Shine:** The income × age (0.206) and income × glucose (0.119) results reveal stronger signals: socioeconomic disadvantage might magnify health risks as people age or in the presence of poor glucose control.

---

## Future Work

Through the process of this project, a key lesson was the critical importance of data granularity when merging datasets from different sources. I aimed to analyze how socioeconomic factors, like income and education, impact stroke risk, but quickly realized that combining individual-level health data with state-level socioeconomic data introduces limitations. While simulated variables (individual income and education score) helped approximate person-level effects, they highlighted the risk of overinterpreting synthetic data and underscored the need for true individual-level socioeconomic indicators to yield stronger, more reliable insights.

I also learned the value of engineering interaction terms, which surfaced stronger relationships (income × age and income × glucose) compared to standalone variables. This suggests that compounded socioeconomic and health factors may play a larger role in stroke risk than isolated metrics.

For future work, I propose:  
- Acquiring finer-grained data, ideally at the county or individual level, to improve precision.  
- Expanding the scope of health indicators to include diet, physical activity, access to healthcare, and mental health metrics potentially through integrating/expanding to other datasets.  
- Applying a balancing technique to correct for class imbalance in stroke occurrence, which could enhance the power of predictive modeling.  
- Testing machine learning models (such as logistic regression or Random Forest with cross-validation) using real, non-simulated SES data to validate initial insights onto unseen data.
---

## Reproducing This Project

To reproduce this project from scratch, follow the steps below:

1. **Clone the Repository:**

   ```bash
   git clone [INSERT YOUR REPO LINK]
   cd final_project

2. **Set up your Python Enviornment:**

   ```bash
   pip install -r requirements.txt

3. **Download the Data:**
   Box: https://uofi.box.com/s/gzi9ls3qg0trx7l4nv182iud1s0uijmy
   
   Go to the inputData folder and download and save stroke.csv and ruralurbancodes2023.csv to the data/folder.
   
   Make sure folder paths match what's listed in the Snakefile and code.

5. **Set Up Your API Key:**
   Request a US Census API Key:
   
   **Link to Dataset:** https://www.ers.usda.gov/data-products/rural-urban-continuum-codes
   
   Save the key in a plain text file named apikey.txt in your root project folder (same folder as Snakefile)

6. **Run the full workflow using Snakemake:**
   
   - This will:
     - Retrieve and integrate Census + RUCC data
     - Clean and transform the stroke dataset
     - Simulate new variables
     - Generate visualizations (heatmaps/paiplot)
     - Create metadata and checksum documentation
       
   ```bash
   snakemake -j 1

8. **(Optional) Visualize the Workflow DAG:**
   ```bash
   snakemake --dag | dot -Tpng > dag_workflow.png
   
---

## References

- Stroke Prediction Dataset. Federico Soriano Palacios. Available via Kaggle: https://www.kaggle.com/fedesoriano/stroke-prediction-dataset  
- American Community Survey (ACS) 1-Year Estimates (2022). U.S. Census Bureau. API Documentation: https://www.census.gov/data/developers/data-sets/acs-1year.html  
- USDA Rural-Urban Continuum Codes (RUCC) 2023. U.S. Department of Agriculture, Economic Research Service. Dataset available at: https://www.ers.usda.gov/data-products/rural-urban-continuum-codes/  
- pandas: Python Data Analysis Library. The pandas development team. Available at: https://pandas.pydata.org/  
- numpy: Fundamental package for scientific computing. Harris et al., Nature 585, 357–362 (2020). Available at: https://numpy.org/  
- requests: HTTP for Humans. Kenneth Reitz and contributors. Available at: https://requests.readthedocs.io/  
- seaborn: Statistical Data Visualization. Michael Waskom and the seaborn development team. Available at: https://seaborn.pydata.org/  
- matplotlib: Visualization with Python. John D. Hunter et al. Available at: https://matplotlib.org/  
- scikit-learn: Machine Learning in Python. Pedregosa et al., Journal of Machine Learning Research, 12, pp. 2825-2830, 2011. Available at: https://scikit-learn.org/  
- Snakemake: A scalable bioinformatics workflow engine. Johannes Köster and Sven Rahmann. Bioinformatics, 28(19), 2520-2522, 2012. DOI: https://doi.org/10.1093/bioinformatics/bts480  
- Python. Python Software Foundation. Available at: https://www.python.org/
- edotor. edotor. Available at: https://edotor.net/  
- ChatGPT. OpenAI. (2025). Used to assist in formatting citations and references. Also used for formatting structure of README. Available at: https://chat.openai.com/
- GitHub Repository. https://github.com/illinois-data-curation/is477-sp25-group61

