# Telco Customer Churn Dataset

## Dataset Overview

This folder contains the Telco Customer Churn dataset used for predicting customer churn in Day 7 of the GeeksforGeeks 21-Days-21-Projects challenge.

## Files Description

### 📊 WA_Fn-UseC_-Telco-Customer-Churn.csv
**Complete customer dataset for churn prediction**
- **Size**: 7,043 customers
- **Features**: 21 features + 1 target variable (Churn)
- **Purpose**: Training and evaluation of churn prediction models
- **Churn Rate**: 26.5% (1,869 churned customers)

## Dataset Characteristics

### Feature Types
- **Customer Demographics**: Gender, age group, partner, dependents
- **Account Information**: Tenure, contract type, payment method, billing preferences
- **Service Usage**: Phone service, internet service, streaming services, security features
- **Financial**: Monthly charges, total charges
- **Target Variable**: Churn (Yes/No) - binary classification

### Key Feature Categories

#### 1. Customer Demographics (4 features)
- **gender**: Male/Female customer gender
- **SeniorCitizen**: Whether customer is senior citizen (0/1)
- **Partner**: Whether customer has a partner (Yes/No)
- **Dependents**: Whether customer has dependents (Yes/No)

#### 2. Account Information (4 features)
- **tenure**: Number of months customer has stayed with company
- **Contract**: Contract term (Month-to-month, One year, Two year)
- **PaperlessBilling**: Whether customer uses paperless billing (Yes/No)
- **PaymentMethod**: Payment method (Electronic check, Mailed check, Bank transfer, Credit card)

#### 3. Service Features (6 features)
- **PhoneService**: Whether customer has phone service (Yes/No)
- **MultipleLines**: Whether customer has multiple lines (Yes/No/No phone service)
- **InternetService**: Internet service provider (DSL, Fiber optic, No)
- **OnlineSecurity**: Whether customer has online security (Yes/No/No internet service)
- **OnlineBackup**: Whether customer has online backup (Yes/No/No internet service)
- **DeviceProtection**: Whether customer has device protection (Yes/No/No internet service)

#### 4. Premium Services (3 features)
- **TechSupport**: Whether customer has tech support (Yes/No/No internet service)
- **StreamingTV**: Whether customer has streaming TV (Yes/No/No internet service)
- **StreamingMovies**: Whether customer has streaming movies (Yes/No/No internet service)

#### 5. Financial Information (3 features)
- **MonthlyCharges**: Amount charged to customer monthly
- **TotalCharges**: Total amount charged to customer
- **Churn**: Whether customer churned (Yes/No) - TARGET VARIABLE

### Data Quality

#### Missing Values
- **TotalCharges**: 11 missing values (customers with 0 tenure)
- **Handling**: Missing values filled with 0 or median imputation
- **Impact**: Minimal impact on overall analysis

#### Data Types
- **Categorical**: 16 features (binary and multi-class)
- **Numerical**: 3 features (tenure, MonthlyCharges, TotalCharges)
- **Target**: Binary (Yes/No converted to 1/0)

#### Class Distribution
- **No Churn**: 5,174 customers (73.5%)
- **Churn**: 1,869 customers (26.5%)
- **Imbalance**: Moderate class imbalance requiring balanced sampling

### Feature Engineering Opportunities

#### Created Features (19 additional)
1. **Customer Value Features**
   - Average monthly charges over tenure
   - Charges per service subscribed
   - Monthly charge ratio to total charges

2. **Service Engagement Features**
   - Total number of services
   - Service penetration rate
   - Security consciousness indicator

3. **Risk Assessment Features**
   - High-risk payment patterns
   - New customer with high charges
   - Charge outlier detection

4. **Behavioral Patterns**
   - Tenure stability relative to contract
   - Family account indicator
   - High bandwidth usage patterns

## Usage in Analysis

### Preprocessing Steps
1. **Missing Value Treatment**: Handle TotalCharges missing values
2. **Data Type Conversion**: Convert categorical to numerical encoding
3. **Feature Scaling**: Standardization for linear models
4. **Class Balancing**: Handle 73%/27% imbalanced distribution

### Model Development
- **Training Split**: 80% training, 20% testing with stratification
- **Models**: Logistic Regression, Random Forest, Gradient Boosting, XGBoost
- **Evaluation**: Accuracy, F1-score, Precision, Recall, ROC-AUC
- **Optimization**: Hyperparameter tuning with Grid Search CV

### Business Applications
- **Customer Retention**: Identify high-risk customers for retention campaigns
- **Resource Allocation**: Focus retention efforts on most likely churners
- **Revenue Protection**: Prevent revenue loss through proactive intervention
- **Customer Segmentation**: Understand different customer behavior patterns

## Data Source

- **Original Source**: IBM Watson Analytics Sample Datasets
- **Domain**: Telecommunications customer behavior
- **License**: Public dataset for educational and research purposes
- **Academic Use**: Permitted for learning and analysis

## Technical Notes

- **File Format**: CSV with comma separators
- **Encoding**: UTF-8
- **Index**: customerID serves as unique identifier
- **Size**: ~1MB total file size
- **Compatibility**: Standard pandas DataFrame loading

### Loading Example
```python
import pandas as pd
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
```

## Key Insights from Dataset

### Churn Patterns
- **Contract Type**: Month-to-month contracts have highest churn rate
- **Payment Method**: Electronic check users churn more frequently
- **Service Usage**: Customers with fewer services tend to churn more
- **Tenure**: New customers (0-12 months) have highest churn risk

### Business Implications
- **Retention Strategy**: Focus on month-to-month contract customers
- **Service Bundling**: Encourage multiple service adoption
- **Payment Optimization**: Promote automatic payment methods
- **New Customer Care**: Enhanced onboarding for first-year customers

This dataset provides an excellent foundation for learning classification techniques, feature engineering, and real-world machine learning workflows in the telecommunications domain.
