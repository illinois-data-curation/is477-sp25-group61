# **IS 477 ProjectPlan**

**Michelle Liu**
---

## **Overview**

This final project is for my IS 477 Course, focusing on *Data Curation, Management, and Reproducibility* at the University of Illinois Urbana-Champaign.

Examining cardiovascular health in relation to educational attainment, urban or rural living conditions, and broader socioeconomic factors is essential for understanding and addressing health disparities in the United States. Cardiovascular diseases remain one of the leading causes of death nationally, but its prevalence and outcomes are not evenly distributed across the population. Research consistently shows that individuals with lower levels of education tend to have higher rates of heart disease, potentially due to limited health literacy, reduced access to care, and increased exposure to health risks such as poor diet, smoking, and physical inactivity. Socioeconomic factors, including income and employment status, also play a critical role in shaping health behaviors and determining access to preventive and ongoing care. Understanding how these variables intersect can help target interventions, guide policy, and ultimately reduce preventable cardiovascular morbidity and mortality across diverse communities.

This will be a python-focused project with multiple different packages used which will be documented across each stage to ensure that the analysis can be replicated. SQL will be utilized as needed. We will integrate data between 2 primary datasets, a Kaggle Stroke CSV Dataset and the American Community Survey Census Dataset. Additionally, other datasets (like the USDA Economic Research) will be used to help with integrating the two main datasets. The purpose of this project is to utilize this integrated dataset to conduct analysis on our research questions as well as to note down any significant noticings along the way. 

---

## **Team**

**Michelle Liu** (Sophomore Studying Finance and Data Science)

- **Data Cleaning, Integration, Research Analysis, and Troubleshooting**
---

## **Research Questions**

1. **Holding age groups constant**, how do different education levels (high school, undergraduate, and masters/doctorate degrees) impact an individual’s chance of developing different cardiovascular diseases?

2. **Are certain cardiovascular diseases more likely to happen to individuals of different income levels?** If so, what is the strength of correlation?
---

## **Datasets**

### **Stroke Dataset (Kaggle Non-API)**
[Link to Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)

Federico Soriano Palacios is an Associate at Oliver Wyman with a strong background in data science and analytics. He holds a double Master’s degree in Data Science from Universidad Pontificia Comillas and the University of Sydney, graduating top of his class and earning multiple academic awards. He’s also a Kaggle Grandmaster and CFA Level I passer. He originally obtained this dataset from a confidential source and said to contact him for more information (which I will do later into the weeks). This Dataset contains both 8 categorical and 3 quantitative variables. The primary variables we will be analyzing are gender, age, hypertension, heart disease, avg_glucose_level, bmi, stroke, work type, and residence_type.  

## To define some of the more technical variables:

- Hypertension, or high blood pressure, is a condition where the force of the blood against the artery walls is consistently too high. It increases the risk of stroke, heart disease, and other health problems.
Body Mass Index (BMI) is a numerical measure that assesses whether an individual has a healthy body weight relative to their height. To note: Underweight: < 18.5, Normal: 18.5 – 24.9, Overweight: 25 – 29.9, Obese: ≥ 30

- Avg_Glucose_Level: High glucose levels can be an indicator of diabetes, which is a major risk factor for stroke. To note: Normal: Less than 100 mg/dL, Pre-diabetes: 100–125 mg/dL, Diabetes: 126 mg/dL or higher

- The remaining variables will be evaluated for further analysis after conducting exploratory data analysis on each dataset and integrating them. Additionally, they may be considered as potential confounding variables in the later stages of analysis, especially if unexpected correlations arise between our primary target variables.  

### **American Community Survey US Census Dataset (API)**
[Link to API](https://api.census.gov/data/2022/acs/acs1)

The 2022 American Community Survey (ACS) 1-Year Estimates provide a detailed snapshot of socioeconomic conditions across the United States at the state level. This analysis focuses on key variables related to income, education, and employment. Median household income (B19013_001E) serves as a core indicator of economic well-being, while educational attainment is captured through bachelor's (B15003_022E), master's (B15003_023E), and doctorate (B15003_025E) degree completion. Additional measures such as the poverty count (B17001_002E) and unemployment (B23025_005E) provide insight into economic hardship and labor market conditions. 

### **USDA Rural Urban Continuum Codes**
[Link to Dataset](https://www.ers.usda.gov/data-products/rural-urban-continuum-codes)

The USDA’s 2023 Rural-Urban Continuum Codes (RUCC) provide a county-level classification system that distinguishes areas based on population size and proximity to metropolitan areas. These codes range from 1 to 9, with lower numbers representing highly urbanized, metro counties and higher numbers indicating more remote, rural counties. The RUCC system allows researchers and policymakers to analyze geographic patterns beyond the traditional urban-rural divide by incorporating nuanced distinctions such as small metro, adjacent nonmetro, and isolated rural areas. By aggregating these codes to the state level, it's possible to classify states as predominantly Urban, Rural, or Mixed based on the distribution of their counties. 
---

## **Timeline**

### **Week 1: Project Set Up and Initial Cleaning/Exploration**
- Explore different data sets (API/nonAPI) and ensure credibility and appropriate licensing  
- Begin exploring potential data cleaning methods and import any necessary packages  
- Execute checksums to check for any data alterations or errors  

### **Week 2/3: Data Cleaning and Initial Exploratory Analysis**
- Clean each dataset and analyze any missing values and see if it’s systematically missing or if we can drop any observations
- Handle any inconsistent data and adjust utilizing code 
- Create individual data visualizations to analyze distributions of target variable columns and note down any multicollinearity across variables 

### **Week 4: Data Integration and Troubleshooting**
- Research data integration options 
- Adjust any necessary variables (binary encoding/generalizing certain variables)
- Implement data analysis of combined dataset using other python packages like seaborn to produce correlation matrices, pairplots, etc 

### **Week 5: Research Analysis and Documentation**
- Finalize data analyses and document all data profiling, quality assessment, and cleaning 
- Add any necessary markdowns and create structure for code 

### **Week 6: Ensure Reproducibility and Citations**
- Create a reproducible package and document citation of data and software used and all licensing 
- Create metadata for package and showcase automated end-to-end workflow execution 
- Archive project to a repository 

## Other Resources:
Attend office hours once a week to ask for any feedback or help to make sure I’m on the right track. Reach out to any peers to read over code/work to ensure analyses make sense. 






