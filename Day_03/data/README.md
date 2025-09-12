# Housing Market Dataset

## Dataset Overview

This folder contains the Ames Housing dataset used for predicting house prices in Day 3 of the GeeksforGeeks 21-Days-21-Projects challenge.

## Files Description

### 📊 train.csv
**Training dataset for model development**
- **Size**: 1,460 houses
- **Features**: 79 features + 1 target variable (SalePrice)
- **Purpose**: Training and validation of machine learning models
- **Price Range**: $34,900 - $755,000

### 🔍 test.csv  
**Test dataset for final predictions**
- **Size**: 1,459 houses
- **Features**: 79 features (no SalePrice)
- **Purpose**: Generate predictions for Kaggle submission
- **Format**: Same structure as training data minus target variable

### 📋 data_description.txt
**Comprehensive feature documentation**
- **Content**: Detailed description of all 79 features
- **Categories**: Numerical and categorical variable explanations
- **Values**: Possible values and their meanings for each feature
- **Essential**: Reference for understanding feature engineering

### 📤 sample_submission.csv
**Kaggle submission format template**
- **Structure**: Id, SalePrice columns
- **Purpose**: Template for competition submission
- **Format**: CSV with proper column headers

## Dataset Characteristics

### Feature Types
- **Numerical Features**: 36 variables (areas, years, counts, etc.)
- **Categorical Features**: 43 variables (quality ratings, types, conditions)
- **Target Variable**: SalePrice (continuous, log-transformed for modeling)

### Key Feature Categories
1. **House Characteristics**: Size, age, style, condition
2. **Location**: Neighborhood, lot configuration, proximity features  
3. **Quality Ratings**: Overall quality, exterior/interior conditions
4. **Utilities & Amenities**: Garage, basement, fireplace, pool
5. **Sales Information**: Year sold, sale type, sale condition

### Data Quality
- **Missing Values**: Present in multiple features (handled systematically)
- **Skewness**: Target variable requires log transformation
- **Outliers**: Some extreme values in house prices and sizes
- **Encoding**: Mixed data types requiring preprocessing

## Usage in Analysis

### Preprocessing Steps
1. **Missing Value Imputation**: Domain-specific strategies for different feature types
2. **Feature Engineering**: Created 5 new meaningful features
3. **Categorical Encoding**: Ordinal and one-hot encoding as appropriate
4. **Feature Scaling**: Standardization for linear models

### Model Development
- **Training Split**: 80% training, 20% validation
- **Models**: Linear Regression (baseline) + XGBoost (advanced)
- **Evaluation**: RMSE, MAE, R² metrics
- **Submission**: Generated predictions for test set

## Data Source

- **Original Source**: Kaggle House Prices: Advanced Regression Techniques Competition
- **Competition URL**: https://www.kaggle.com/c/house-prices-advanced-regression-techniques
- **License**: Competition data usage terms
- **Academic Use**: Permitted for educational purposes

## Technical Notes

- **File Format**: CSV with comma separators
- **Encoding**: UTF-8
- **Index**: Id column serves as unique identifier
- **Size**: ~500KB total for all files
- **Compatibility**: Standard pandas DataFrame loading

This dataset provides an excellent foundation for learning regression techniques, feature engineering, and real-world machine learning workflows in the housing market domain.
