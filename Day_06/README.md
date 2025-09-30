# Day 6: Time Series Analysis & Forecasting

## Project Overview

This project implements comprehensive time series analysis and forecasting using classical statistical methods. The project focuses on airline passenger data to demonstrate fundamental time series concepts including trend analysis, seasonality detection, stationarity testing, and advanced forecasting with ARIMA and SARIMA models.

## Objective

To build accurate time series forecasting models for airline passenger data, demonstrating understanding of stationarity concepts, data transformations, and the comparative performance between ARIMA and SARIMA models for seasonal time series data.

## Dataset Information

- **Source**: Airline Passenger Time Series dataset
- **Total Observations**: 144 monthly data points
- **Time Period**: January 1949 to December 1960 (12 years)
- **Features**: Month (datetime) and Passengers (count)
- **Data Quality**: Complete dataset with no missing values
- **Characteristics**: Strong upward trend with clear seasonal patterns

## Project Structure

```
Day_06/
├── README.md                                           # Project documentation
├── 6_Predicting_Future_Store_Sales_with_AI.ipynb      # Main tutorial notebook
├── 6_Time_Series_Local_Working.ipynb                  # Local working version
├── Assignment_Complete.ipynb                           # Assignment solution notebook
└── data/
    └── airline_passenger_timeseries.csv               # Time series dataset
```

## Submission Criteria

This assignment fulfills three specific requirements:

1. **Exploratory Data Analysis (EDA)**: Time series plot analysis including trend, seasonality, and variance
2. **Stationarity Testing**: ADF tests and transformations to achieve stationarity
3. **ARIMA Model Performance**: Model comparison and evaluation between ARIMA and SARIMA

## Analysis Workflow

### Step 1: Setup and Data Loading
- Import time series libraries (pandas, numpy, statsmodels, matplotlib)
- Load airline passenger dataset from data directory
- Convert to proper datetime index for time series analysis

### Submission Criteria 1: Exploratory Data Analysis (EDA)

#### Time Series Plot Analysis
- **Initial Visualization**: Complete time series plot from 1949-1960
- **Trend Identification**: Strong positive trend over 12-year period
- **Seasonality Detection**: Clear seasonal patterns with summer peaks
- **Variance Analysis**: Increasing variance over time (heteroscedasticity)
- **Data Characteristics**: Monthly frequency with consistent seasonal cycles

#### Seasonal Decomposition
- **Trend Component**: Extracted long-term upward movement
- **Seasonal Component**: Identified recurring annual patterns
- **Residual Component**: Analyzed remaining noise after decomposition
- **Decomposition Visualization**: Professional multi-panel time series plots

### Submission Criteria 2: Stationarity Testing

#### Understanding Stationarity
- **Concept Explanation**: Statistical properties constant over time
- **Importance**: Required for ARIMA modeling accuracy
- **Testing Method**: Augmented Dickey-Fuller (ADF) test implementation

#### Stationarity Test Results
- **Original Data ADF Test**:
  - Test statistic: 0.815
  - p-value: 0.991
  - Result: Non-stationary (p > 0.05)

- **Log Transformation**:
  - Applied to stabilize variance
  - ADF test statistic: -1.717
  - p-value: 0.422
  - Result: Still non-stationary

#### Data Transformations
- **Log Transformation**: Variance stabilization technique
- **First Differencing**: Remove trend component
- **Seasonal Differencing**: Handle seasonal patterns
- **Transformation Validation**: Statistical testing of each step

### Submission Criteria 3: ARIMA Model Performance

#### Model Implementation
- **Train-Test Split**: 80% training (115 observations), 20% testing (29 observations)
- **ARIMA Model**: Trained on log-transformed non-stationary data
- **SARIMA Model**: Seasonal ARIMA with proper differencing
- **Parameter Selection**: Systematic approach to model configuration

#### Model Comparison Results
- **ARIMA Performance**: Demonstrated poor performance on non-stationary data
- **SARIMA Performance**: Superior handling of seasonality and trends
- **Performance Metrics**: Mean Squared Error (MSE) comparison
- **Improvement Quantification**: Percentage improvement calculation

#### Forecasting Visualization
- **Training Data**: Historical observations visualization
- **Actual vs Predicted**: Side-by-side forecast comparison
- **Model Comparison**: ARIMA vs SARIMA forecast visualization
- **Professional Plotting**: Multi-series time series charts

## Key Results

### EDA Findings
- **Trend**: Strong positive growth from ~100 to ~400 passengers
- **Seasonality**: Consistent annual patterns with summer peaks
- **Variance**: Increasing variance requiring log transformation
- **Data Quality**: Complete dataset suitable for modeling

### Stationarity Analysis
- **Original Data**: Non-stationary (ADF p-value: 0.991)
- **Log-Transformed**: Still non-stationary (ADF p-value: 0.422)
- **Transformation Need**: Differencing required for stationarity
- **Statistical Validation**: Proper ADF testing methodology

### Model Performance
- **SARIMA Superiority**: Significantly outperformed ARIMA
- **Seasonal Handling**: SARIMA effectively captured seasonal patterns
- **Forecasting Accuracy**: Improved prediction quality with seasonal modeling
- **Statistical Significance**: Clear performance difference demonstrated

### Final Conclusions
1. **Stationarity Impact**: Non-stationary data significantly affects ARIMA performance
2. **Model Selection**: SARIMA handles seasonality and non-stationarity better
3. **Practical Recommendations**: Always test stationarity, use appropriate transformations, consider seasonal patterns

## Technical Implementation

### Tools and Libraries
- **Python**: Core programming language
- **Pandas**: Time series data manipulation
- **NumPy**: Numerical computations
- **Statsmodels**: Time series analysis and modeling (ARIMA, SARIMA, ADF test)
- **Matplotlib/Seaborn**: Time series visualization
- **Scikit-learn**: Performance metrics (MSE, MAE)

### Time Series Techniques
- **Seasonal Decomposition**: Trend, seasonal, and residual component analysis
- **Stationarity Testing**: Augmented Dickey-Fuller test
- **Data Transformations**: Log transformation and differencing
- **ARIMA Modeling**: AutoRegressive Integrated Moving Average
- **SARIMA Modeling**: Seasonal ARIMA with seasonal differencing
- **Forecasting Evaluation**: MSE-based model comparison

### Statistical Methods
- **ADF Test**: Stationarity hypothesis testing
- **Log Transformation**: Variance stabilization
- **Differencing**: Trend and seasonal removal
- **Model Diagnostics**: Residual analysis and validation
- **Performance Metrics**: Quantitative model evaluation

## Deliverables

1. **Complete EDA**: Time series analysis with trend and seasonality identification
2. **Stationarity Analysis**: ADF testing and transformation documentation
3. **Model Comparison**: ARIMA vs SARIMA performance evaluation
4. **Forecasting Results**: Professional visualization of model predictions
5. **Statistical Validation**: Rigorous testing and transformation methodology
6. **Business Insights**: Practical recommendations for time series modeling

## Assignment Completion Status

**STATUS: FULLY COMPLETED**

All submission criteria successfully met:
- ✓ Exploratory Data Analysis with time series plot analysis
- ✓ Stationarity testing with ADF tests and transformations
- ✓ ARIMA model performance comparison and evaluation
- ✓ Comprehensive documentation of methodology and results
- ✓ Professional visualization and statistical validation

## Usage Instructions

1. **Environment Setup**: Install required time series libraries (statsmodels)
2. **Data Preparation**: Ensure airline_passenger_timeseries.csv is in data directory
3. **Notebook Execution**: Run Assignment_Complete.ipynb sequentially
4. **EDA Analysis**: Review time series plots and decomposition results
5. **Stationarity Testing**: Examine ADF test results and transformations
6. **Model Evaluation**: Compare ARIMA vs SARIMA performance metrics
7. **Forecasting**: Analyze prediction accuracy and visualization

## Results and Impact

This project demonstrates professional time series analysis capabilities, providing insights into airline passenger growth patterns and seasonal behavior. The analysis clearly shows the importance of stationarity testing and appropriate model selection for accurate forecasting.

The comparative analysis between ARIMA and SARIMA models provides valuable insights for practitioners, demonstrating that seasonal models significantly outperform basic ARIMA when dealing with seasonal time series data. The methodology established can be applied to various business forecasting scenarios including sales prediction, demand planning, and resource allocation.

## Key Learning Outcomes

- **Time Series Fundamentals**: Understanding trend, seasonality, and residual components
- **Stationarity Concepts**: Critical importance for model accuracy
- **Data Transformations**: Log transformation and differencing techniques
- **Model Selection**: ARIMA vs SARIMA for seasonal data
- **Forecasting Evaluation**: Quantitative performance assessment
- **Statistical Validation**: Rigorous testing methodology

## Future Enhancements

- **Advanced Models**: Explore Prophet, LSTM, or other modern forecasting methods
- **Hyperparameter Tuning**: Systematic optimization of ARIMA/SARIMA parameters
- **Cross-Validation**: Time series cross-validation for robust evaluation
- **Confidence Intervals**: Uncertainty quantification in forecasts
- **External Variables**: Incorporate exogenous variables (SARIMAX)
- **Real-time Forecasting**: Implement streaming prediction system
