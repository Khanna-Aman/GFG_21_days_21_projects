# Day 1: Titanic Dataset Analysis and Profiling

## Project Overview

Comprehensive exploratory data analysis (EDA) and profiling of the Titanic dataset to understand survival patterns and generate automated data profiling reports.

## Objectives

- Perform end-to-end data analysis on the Titanic dataset
- Handle missing values and perform data cleaning
- Engineer meaningful features for analysis
- Generate comprehensive data profiling reports
- Extract key insights about survival patterns

## Dataset Information

**Source**: GeeksforGeeks 21 Days 21 Projects Dataset Repository  
**Records**: 891 passengers  
**Features**: 12 original features, 15 after feature engineering  
**Target Variable**: Survived (0 = No, 1 = Yes)

## Project Structure

```
Day_01/
├── README.md                           # Project documentation
├── notebooks/
│   └── titanic_analysis.ipynb         # Original analysis notebook
├── scripts/
│   └── run_profiling.py               # Automated profiling script
├── reports/
│   └── sample.html                    # Generated profiling report
└── data/
    └── (Dataset loaded from external repository)
```

## Key Features

### Original Features
- PassengerId: Unique identifier
- Survived: Survival status (target variable)
- Pclass: Passenger class (1st, 2nd, 3rd)
- Name: Passenger name
- Sex: Gender
- Age: Age in years
- SibSp: Number of siblings/spouses aboard
- Parch: Number of parents/children aboard
- Ticket: Ticket number
- Fare: Passenger fare
- Cabin: Cabin number
- Embarked: Port of embarkation

### Engineered Features
- Has_Cabin: Binary indicator for cabin information availability
- FamilySize: Total family members aboard (SibSp + Parch + 1)
- IsAlone: Binary indicator for solo travelers
- Title: Extracted social title from name
- Age groups and other derived features

## Data Cleaning Process

1. **Missing Value Treatment**:
   - Age: Filled with median (29.7 years)
   - Embarked: Filled with mode ('S')
   - Cabin: Converted to binary feature Has_Cabin

2. **Feature Engineering**:
   - Created family-related features
   - Extracted titles from names
   - Generated categorical age groups

3. **Data Validation**:
   - Verified no missing values after cleaning
   - Confirmed data type consistency

## Key Insights

- **Overall Survival Rate**: 38.4%
- **Gender Impact**: Females had 74.2% survival rate vs 18.9% for males
- **Class Effect**: 1st class 63.0%, 2nd class 47.3%, 3rd class 24.2%
- **Age Factor**: Children had higher survival rates
- **Family Size**: Moderate family sizes showed optimal survival rates

## Technical Implementation

### Requirements
- Python 3.12+
- pandas, numpy for data manipulation
- matplotlib, seaborn for visualization
- ydata-profiling for automated reporting

### Execution
1. Run the automated script:
   ```bash
   python scripts/run_profiling.py
   ```

2. View the generated report:
   ```bash
   open reports/sample.html
   ```

### Compatibility Notes
- Script handles Python version compatibility issues
- Includes fallback mechanisms for profiling package failures
- Automated dataset loading with error handling

## Results

The analysis successfully generated a comprehensive profiling report demonstrating:
- Complete data quality assessment
- Statistical summaries for all features
- Correlation analysis
- Missing value patterns
- Distribution analysis

## Assignment Completion

**Status**: Complete  
**Deliverable**: HTML profiling report (sample.html)  
**Methodology**: Following original notebook workflow with automated execution  
**Quality**: Professional implementation with proper error handling

## Files Description

- `notebooks/titanic_analysis.ipynb`: Original GeeksforGeeks analysis notebook
- `scripts/run_profiling.py`: Automated script for data processing and report generation
- `reports/sample.html`: Final HTML profiling report for submission
- `README.md`: This documentation file
