# Day 13: NIFTY 50 Stock Price Prediction with Machine Learning and Deep Learning

## Project Overview

This project implements comprehensive stock price prediction models for the NIFTY 50 index using both traditional machine learning and deep learning approaches. The project focuses on predicting the 'High' price of the NIFTY 50 index using multiple time-series forecasting models with varying time windows to compare their effectiveness and identify optimal prediction strategies.

## Objective

To develop and evaluate multiple predictive models for NIFTY 50 stock price forecasting:
- Compare traditional machine learning (KNN) with deep learning approaches (RNN, GRU, LSTM, Bidirectional LSTM)
- Analyze the impact of different time windows (30, 60, 90 days) on prediction accuracy
- Evaluate model performance using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE)
- Identify optimal model-window combinations for High price prediction

## Dataset Information

### NIFTY 50 Stock Data
- **Source**: Historical NIFTY 50 index data (data.csv)
- **Features**: Open, Close, High, Low prices
- **Target Variable**: High price prediction
- **Time Series Nature**: Sequential daily stock price data
- **Data Processing**: Sliding window approach for sequence generation

### Time Windows Analysis
- **30 days**: Short-term prediction patterns
- **60 days**: Medium-term trend analysis  
- **90 days**: Long-term pattern recognition
- **Sequence Generation**: Supervised learning datasets using sliding windows

## Project Structure

```
Day_13/
├── README.md                                       # Project documentation
├── Stock_Price_Prediction_NIfty_50.ipynb          # Main tutorial notebook
└── Assignment._NIFTY_50_Stock_Prediction.ipynb    # Assignment solution notebook
```

## Analysis Workflow

### Main Project Components

#### 1. Stock Price Prediction (Reference Implementation)
- **Comprehensive Pipeline**: ML and DL model comparison framework
- **Multiple Features**: Analysis of Open, Close, High, Low prices
- **Time Window Range**: 30-250 days for robust prediction
- **Model Variety**: Linear, tree-based, neural network approaches
- **Performance Tracking**: Training and testing error evaluation

#### 2. Assignment: High Price Prediction
- **Focused Implementation**: Specific to High price prediction
- **Required Models**: KNN, RNN, GRU, LSTM, Bidirectional LSTM
- **Standardized Training**: 50 epochs for all deep learning models
- **Systematic Evaluation**: MAE and RMSE metrics across all combinations
- **Professional Documentation**: Complete requirement tracking and results analysis

## Key Findings

### Model Performance Results

#### Assignment Implementation (High Price Prediction)
- **Total Experiments**: 15 model-window combinations
- **Best Overall Performance**: KNN with 30-day window
  - **MAE**: 188.6032
  - **RMSE**: 235.5385
- **Model Type Comparison**:
  - **Machine Learning (KNN)**: Average MAE 299.79, RMSE 372.53
  - **Deep Learning Models**: Average MAE 2924.94, RMSE 3111.29

#### Time Window Analysis
- **Best Time Window**: 90-day window (average performance)
- **Short-term Advantage**: 30-day window optimal for KNN
- **Pattern Recognition**: Longer windows better for deep learning models

### Technical Implementation

#### Machine Learning Models
- **KNN Regressor**: K-Nearest Neighbors with distance weighting
  - **Configuration**: n_neighbors=5, weights='distance'
  - **Data Processing**: StandardScaler normalization
  - **Feature Engineering**: Flattened sequence representation

#### Deep Learning Models
- **RNN Architecture**: Simple RNN with 50 units + Dense layers
- **GRU Architecture**: Gated Recurrent Unit with 50 units + Dense layers
- **LSTM Architecture**: Long Short-Term Memory with 50 units + Dense layers
- **Bidirectional LSTM**: Bidirectional wrapper with 50 units + Dense layers
- **Common Features**: Dropout (0.2), Adam optimizer, MSE loss

#### Training Configuration
- **Framework**: TensorFlow 2.19.0 with GPU support
- **Epochs**: 50 (assignment requirement)
- **Batch Size**: 32 (optimized for GPU)
- **Validation Split**: 20% for model validation
- **Callbacks**: EarlyStopping, ReduceLROnPlateau

## Deliverables

### Notebooks
1. **Reference Implementation**: Comprehensive stock prediction pipeline
2. **Assignment Solution**: Focused High price prediction with required models

### Key Outputs
- **Performance Comparison**: Detailed results across all model-window combinations
- **Statistical Analysis**: Best/worst performers identification
- **Visualization**: Professional charts showing model performance
- **Results Export**: CSV file with complete experimental results

## Installation and Usage

### Prerequisites
```bash
# Core dependencies
pip install tensorflow pandas numpy matplotlib seaborn scikit-learn

# For enhanced functionality
pip install tqdm jupyter ipykernel

# GPU support (optional)
pip install tensorflow-gpu
```

### System Requirements
- **Python**: 3.8+ (tested with 3.13.5)
- **TensorFlow**: 2.19.0+
- **Memory**: 8GB+ RAM recommended
- **GPU**: NVIDIA GPU with CUDA support (optional but recommended)
- **Storage**: 2GB+ for data and models

### Running the Project
1. **Reference Implementation**: Execute Stock_Price_Prediction_NIfty_50.ipynb
2. **Assignment**: Run Assignment._NIFTY_50_Stock_Prediction.ipynb for complete analysis
3. **Data Requirements**: Ensure data.csv is available in the working directory

### Expected Runtime
- **Assignment Training**: 45-60 minutes (with GPU)
- **Reference Implementation**: 60-90 minutes (depending on model selection)
- **Data Processing**: 5-10 minutes for all time windows

## Results and Impact

### Technical Achievements
| Component | Specification | Performance |
|-----------|--------------|-------------|
| Models Evaluated | 5 models | KNN, RNN, GRU, LSTM, Bidirectional LSTM |
| Time Windows | 3 windows | 30, 60, 90 days |
| Best MAE | 188.6032 | KNN with 30-day window |
| Best RMSE | 235.5385 | KNN with 30-day window |
| Training Framework | TensorFlow 2.19.0 | GPU-optimized execution |
| Total Experiments | 15 combinations | Complete systematic evaluation |

### Practical Applications
1. **Financial Trading**: Short-term price prediction for trading strategies
2. **Risk Management**: Volatility assessment and portfolio optimization
3. **Investment Planning**: Medium to long-term trend analysis
4. **Algorithm Development**: Model comparison framework for financial ML
5. **Research**: Time series forecasting methodology validation

## Assignment Completion Status

All assignment requirements successfully fulfilled:
- **Target Variable**: High price prediction implemented
- **Required Models**: All 5 models (KNN, RNN, GRU, LSTM, Bidirectional LSTM) implemented
- **Time Windows**: All 3 windows (30, 60, 90 days) tested
- **Training Epochs**: 50 epochs for deep learning models as required
- **Evaluation Metrics**: MAE and RMSE calculated for all combinations
- **Results Documentation**: Comprehensive analysis and comparison provided

## Future Enhancements

1. **Advanced Architectures**: Transformer models, attention mechanisms
2. **Feature Engineering**: Technical indicators, sentiment analysis
3. **Ensemble Methods**: Model combination strategies
4. **Real-time Prediction**: Live data integration and streaming predictions
5. **Risk Metrics**: Value at Risk (VaR) and other financial risk measures
6. **Multi-asset Prediction**: Extension to other stock indices and assets

## Technical Notes

- **Data Preprocessing**: Proper sequence generation with sliding windows
- **Model Optimization**: GPU acceleration with memory growth enabled
- **Error Handling**: Robust training pipeline with exception management
- **Reproducibility**: Fixed random seeds for consistent results
- **Scalability**: Efficient batch processing for large datasets
- **Documentation**: Comprehensive logging and result tracking

## External Resources

- **NIFTY 50 Information**: https://www.niftyindices.com/
- **TensorFlow Documentation**: https://www.tensorflow.org/
- **Scikit-learn Documentation**: https://scikit-learn.org/
- **Time Series Forecasting**: https://www.tensorflow.org/tutorials/structured_data/time_series
- **Financial ML Resources**: Various academic papers on stock prediction methodologies

This project successfully demonstrates advanced time series forecasting techniques applied to financial data, providing a comprehensive framework for stock price prediction using both traditional and modern machine learning approaches with systematic evaluation and professional documentation.
