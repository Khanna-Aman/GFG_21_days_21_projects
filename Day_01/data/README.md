# Data Directory

## Dataset Source

The Titanic dataset is automatically downloaded from the GeeksforGeeks 21 Days 21 Projects Dataset Repository:

**Repository**: https://github.com/GeeksforgeeksDS/21-Days-21-Projects-Dataset  
**File Path**: `Datasets/Titanic-Dataset.csv`

## Dataset Information

**Name**: Titanic Passenger Data  
**Records**: 891 passengers  
**Features**: 12 columns  
**Format**: CSV

## Automatic Data Loading

The dataset is automatically cloned and loaded when running the analysis script:

```python
# Automatic repository cloning
git clone https://github.com/GeeksforgeeksDS/21-Days-21-Projects-Dataset.git

# Data loading
titanic_df = pd.read_csv('21-Days-21-Projects-Dataset/Datasets/Titanic-Dataset.csv')
```

## Data Schema

| Column | Type | Description |
|--------|------|-------------|
| PassengerId | int | Unique passenger identifier |
| Survived | int | Survival status (0=No, 1=Yes) |
| Pclass | int | Passenger class (1, 2, 3) |
| Name | string | Passenger name |
| Sex | string | Gender (male, female) |
| Age | float | Age in years |
| SibSp | int | Number of siblings/spouses aboard |
| Parch | int | Number of parents/children aboard |
| Ticket | string | Ticket number |
| Fare | float | Passenger fare |
| Cabin | string | Cabin number |
| Embarked | string | Port of embarkation (C, Q, S) |

## Data Quality Notes

- **Missing Values**: Age (177), Cabin (687), Embarked (2)
- **Data Types**: Mixed numeric and categorical
- **Target Variable**: Survived (binary classification)

## Usage

No manual data download required. The analysis script handles all data acquisition automatically.
