# Day 1: Data Storytelling - Analyzing Survival on the Titanic

## Project Overview

This project performs comprehensive exploratory data analysis (EDA) on the Titanic dataset to understand the key factors that influenced passenger survival. The analysis follows a complete data science workflow from data loading and cleaning to visualization and profiling.

## Objective

To perform a step-by-step exploratory data analysis that uncovers insights about survival patterns on the Titanic, serving as a complete guide covering data loading, cleaning, analysis, feature engineering, and visualization with theoretical explanations at each stage.

## Dataset

- **Source**: Titanic passenger dataset
- **Size**: 891 passengers with 12 features
- **Key Variables**: Passenger class, sex, age, fare, embarkation port, survival status

## Project Structure

```
Day_01/
├── README.md                                                      # Project documentation
├── 1_Data_Storytelling_Analysing_Survival_on_the_Titanic.ipynb  # Main tutorial notebook
├── Assignment_titanic_analysis.ipynb                             # Assignment solution notebook
└── sample.html                                                    # Generated profiling report
```

## Analysis Workflow

### 1. Data Loading and Initial Exploration
- Loaded Titanic dataset from CSV file
- Examined dataset structure, dimensions, and data types
- Identified missing values and data quality issues

### 2. Data Cleaning and Preprocessing
- **Missing Value Treatment**:
  - Age: Filled missing values with median age
  - Embarked: Filled missing values with mode (most common port)
  - Cabin: Created binary feature 'Has_Cabin' due to high missing percentage (77%)
- **Feature Engineering**:
  - Created meaningful categorical variables
  - Extracted titles from passenger names
  - Binned continuous variables for better analysis

### 3. Exploratory Data Analysis
- **Survival Analysis**: Overall survival rate of 38.4%
- **Demographic Analysis**: 
  - Gender impact on survival rates
  - Age distribution and survival patterns
  - Passenger class effects on survival
- **Correlation Analysis**: Identified relationships between variables
- **Visualization**: Created comprehensive plots and charts

### 4. Data Profiling
- Generated comprehensive HTML profiling report using ydata-profiling
- Automated statistical analysis of all variables
- Interactive visualizations and correlation matrices
- Missing value patterns and data quality assessment

## Key Findings

- **Gender Effect**: Significant difference in survival rates between male and female passengers
- **Class Impact**: Higher passenger classes showed better survival rates
- **Age Patterns**: Certain age groups had different survival probabilities
- **Embarkation Port**: Passengers from different ports showed varying survival rates

## Technical Implementation

### Tools and Libraries Used
- **Python 3.x**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib/Seaborn**: Data visualization
- **ydata-profiling**: Automated data profiling

### Environment Setup
- Resolved matplotlib compatibility issues with ydata-profiling
- Implemented error handling for robust execution
- Created fallback mechanisms for different environments

## Deliverables

1. **Main Notebook**: Complete EDA with detailed explanations
2. **HTML Profiling Report**: Comprehensive automated data analysis
3. **Documentation**: Professional project documentation

## Assignment Completion

**Status**: COMPLETED

All assignment requirements have been successfully fulfilled:
- Comprehensive exploratory data analysis performed
- Data cleaning and preprocessing completed
- ydata-profiling HTML report generated
- Professional documentation provided

## Usage Instructions

1. **Run the Analysis**:
   ```bash
   jupyter notebook 1_Data_Storytelling_Analysing_Survival_on_the_Titanic.ipynb
   ```

2. **View Profiling Report**:
   - Open `Assignment/sample.html` in any web browser
   - Interactive report with detailed statistics and visualizations

3. **Requirements**:
   ```bash
   pip install pandas numpy matplotlib seaborn ydata-profiling
   ```

## Results and Impact

This analysis provides valuable insights into the factors that influenced survival on the Titanic, demonstrating the power of data storytelling in uncovering historical patterns. The methodology can be applied to similar datasets for comprehensive exploratory analysis.

## Future Enhancements

- Predictive modeling for survival prediction
- Advanced feature engineering techniques
- Machine learning model implementation
- Interactive dashboard development

---

**Note**: This project is part of a 21-day data science challenge focusing on practical applications of data analysis and visualization techniques.
