# COVID-19 Global Data Tracker

### Project Overview

This repository contains a Jupyter Notebook for analyzing and reporting global COVID-19 trends, using the owid-covid-data.csv dataset from Our World in Data. The notebook covers data loading, cleaning, exploratory data analysis (EDA), visualizations of cases, deaths, and vaccinations, and communicates key insights in narrative form.

### Contents

- **README.md** – Project description, setup instructions, and usage guide.

- **notebooks/** – Directory containing the main analysis notebook:

- **covid19_global_data_tracker.ipynb** – Step-by-step data analysis and reporting.

- **data/** – Directory storing the raw dataset:

- **owid-covid-data.csv** – COVID-19 global data file.

### Prerequisites

- Ensure you have the following installed:

- Python 3.8 or higher

- Jupyter Notebook (or VS Code with Jupyter extension)

- pandas

- matplotlib

- seaborn

**Optional:**

- plotly

- geopandas

## You can install the required Python packages with:
```bash 
pip install pandas matplotlib seaborn plotly geopandas
```
### Setup Instructions

Clone this repository or download the files.

Place the dataset owid-covid-data.csv into the data/ folder.

Navigate to the root directory and launch Jupyter Notebook:
```
jupyter notebook
```
Open notebooks/covid19_global_data_tracker.ipynb and follow the analysis steps.

Project Structure
``` 
├── README.md
├── data
│   └── owid-covid-data.csv
├── notebooks
│   └── covid19_global_data_tracker.ipynb
└── requirements.txt
```
### Next Steps

1. We will now create and populate the Jupyter Notebook with:

2. Data Loading & Exploration

3. Data Cleaning

4. Exploratory Data Analysis (EDA)

5. Vaccination Visualizations

6. Choropleth Map (optional)

7. Key Insights & Conclusions