# Day 5: Customer Segmentation with Advanced Feature Engineering

## Project Overview

This project implements comprehensive customer segmentation using unsupervised machine learning techniques, focusing on advanced feature engineering and statistical analysis. The project analyzes mall customer data to identify distinct customer personas and evaluate the relationship between gender and spending behavior through rigorous statistical testing.

## Objective

To perform customer segmentation using clustering algorithms with engineered features, and to statistically analyze the relationship between gender and spending patterns to provide actionable business insights for targeted marketing strategies.

## Dataset Information

- **Source**: Mall Customers dataset
- **Total Samples**: 200 customers
- **Features**: 5 original attributes (CustomerID, Gender, Age, Annual Income, Spending Score)
- **Target Analysis**: Unsupervised learning (no target variable)
- **Gender Distribution**: 112 Female (56%), 88 Male (44%)
- **Data Quality**: Complete dataset with no missing values

## Project Structure

```
Day_05/
├── README.md                                                   # Project documentation
├── 5_Smart_Segmentation_Unlocking_Customer_Personas_with_AI.ipynb  # Reference notebook
├── 5_Smart_Segmentation_Local_Working.ipynb                   # Local working version
├── Assignment/
│   └── Assignment_Complete.ipynb                              # Main assignment implementation
└── data/
    └── Mall_Customers.csv                                     # Customer dataset
```

## Submission Criteria

This assignment fulfills two specific requirements:

1. **Gender vs. Spending Score Analysis**: Analyze relationship between gender and spending patterns with statistical significance testing
2. **Feature Engineering for Clustering**: Create new features and perform clustering with optimal cluster determination

## Analysis Workflow

### Step 1: Setup and Data Loading
- Import essential libraries (pandas, numpy, sklearn, matplotlib, seaborn)
- Load mall customer dataset from data directory
- Initial data exploration and quality assessment

### Part 1: Gender vs. Spending Score Analysis

#### Statistical Analysis
- **Descriptive Statistics**: Comprehensive analysis by gender groups
- **Distribution Analysis**: Gender distribution and spending score characteristics
- **Hypothesis Testing**: 
  - Independent t-test for mean differences
  - Mann-Whitney U test for non-parametric comparison
  - Effect size calculation (Cohen's d)

#### Comprehensive Visualizations
- Box plots showing spending distribution by gender
- Violin plots displaying density distributions
- Normalized histograms for direct comparison
- Mean comparison bar charts with error bars
- Scatter plots: Age vs Spending Score by gender
- Scatter plots: Income vs Spending Score by gender

#### Statistical Results
- **Male Spending**: Mean 48.51, Std 27.90
- **Female Spending**: Mean 51.53, Std 24.11
- **T-test p-value**: 0.4137 (not significant)
- **Effect Size**: -0.1167 (negligible)
- **Conclusion**: Gender does NOT significantly influence spending behavior

### Part 2: Feature Engineering for Clustering

#### Feature Engineering Process
- **Income-to-Spending Ratio**: Annual Income / Spending Score
  - Higher values = conservative spenders
  - Lower values = enthusiastic spenders
- **Age Group (Numeric)**: Categorical age groupings (1=Young, 2=Adult, 3=Middle-aged, 4=Senior)
- **Customer Value Score**: Weighted combination (0.6 × Normalized Income + 0.4 × Normalized Spending)
- **Spending Efficiency**: Spending Score / Age (spending intensity per year)

#### Clustering Implementation
- **Feature Selection**: 6 features (3 original + 3 engineered)
- **Data Preprocessing**: StandardScaler normalization
- **Quality Assurance**: NaN and infinite value handling

#### Optimal Cluster Determination
- **Elbow Method**: WCSS analysis for k=1 to 10
- **Silhouette Analysis**: Cluster separation quality assessment
- **Optimal k**: 7 clusters (highest silhouette score: 0.441)
- **Final WCSS**: 216.18

#### Cluster Analysis and Visualization
- **6-Panel Comprehensive Visualization**:
  - 2D scatter plots with multiple feature combinations
  - 3D scatter plot for multi-dimensional perspective
  - Cluster size distribution analysis
  - Feature importance heatmap by cluster
- **Cluster Distribution**: 7 segments ranging from 1.0% to 23.0% of customers

## Key Results

### Gender Analysis Findings
- **Statistical Conclusion**: No significant gender effect on spending (p > 0.05)
- **Business Implication**: Gender-neutral marketing strategies recommended
- **Alternative Focus**: Age and income identified as primary segmentation variables

### Customer Segmentation Results
- **7 Distinct Clusters**: Successfully identified customer personas
- **Cluster Quality**: Silhouette score of 0.441 indicates good separation
- **Feature Engineering Impact**: Engineered features enhanced clustering effectiveness

### Cluster Characteristics
- **High-Value Customers**: High income, high spending segments
- **Conservative Affluent**: High income, low spending segments  
- **Enthusiastic Spenders**: Low income, high spending segments
- **Budget-Conscious**: Low income, low spending segments
- **Moderate Customers**: Balanced income and spending patterns

### Business Insights
- **Marketing Strategy**: Tailored approaches for each customer segment
- **Channel Recommendations**: Age-based marketing channel selection
- **Product Positioning**: Income and spending-based product targeting

## Technical Implementation

### Tools and Libraries
- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Scikit-learn**: Machine learning algorithms and preprocessing
- **Matplotlib/Seaborn**: Data visualization
- **SciPy**: Statistical analysis and hypothesis testing

### Machine Learning Techniques
- **Unsupervised Learning**: Customer segmentation without target variable
- **K-Means Clustering**: Primary clustering algorithm
- **Feature Engineering**: Creative feature creation for enhanced clustering
- **Cluster Optimization**: Elbow Method and Silhouette Analysis
- **Statistical Testing**: Hypothesis testing for gender analysis

### Statistical Methods
- **Descriptive Statistics**: Mean, standard deviation, distribution analysis
- **Hypothesis Testing**: Independent t-test, Mann-Whitney U test
- **Effect Size Analysis**: Cohen's d for practical significance
- **Cluster Validation**: Silhouette score and WCSS evaluation

## Deliverables

1. **Gender Analysis Report**: Statistical analysis with clear conclusions
2. **Feature Engineering Documentation**: Process and rationale for new features
3. **Customer Segmentation Model**: 7-cluster solution with business interpretation
4. **Comprehensive Visualizations**: Multi-panel analysis and cluster visualization
5. **Business Recommendations**: Marketing strategies for each customer segment
6. **Statistical Validation**: Rigorous testing and cluster quality assessment

## Assignment Completion Status

**STATUS: FULLY COMPLETED**

Both submission criteria successfully met:
- ✓ Gender vs. Spending Score analysis with statistical testing and visualizations
- ✓ Feature engineering for clustering with optimal k determination and interpretation
- ✓ Comprehensive documentation of feature engineering process
- ✓ Elbow Method implementation for cluster optimization
- ✓ Detailed cluster visualization and business interpretation

## Usage Instructions

1. **Environment Setup**: Install required Python libraries
2. **Data Preparation**: Ensure Mall_Customers.csv is in data directory
3. **Notebook Execution**: Run Assignment_Complete.ipynb sequentially
4. **Statistical Analysis**: Review gender vs spending analysis results
5. **Feature Engineering**: Examine engineered feature creation process
6. **Clustering Analysis**: Evaluate optimal cluster determination and results
7. **Business Application**: Apply customer segment insights to marketing strategy

## Results and Impact

This project demonstrates advanced customer analytics capabilities, providing actionable insights for retail marketing strategy. The statistical analysis definitively shows that gender-based marketing segmentation is not effective, while the clustering analysis identifies 7 distinct customer personas that can drive targeted marketing campaigns.

The feature engineering approach successfully enhanced clustering effectiveness, creating meaningful customer segments based on spending behavior, income levels, and demographic characteristics. Each segment receives tailored marketing recommendations based on their unique characteristics and preferences.

## Key Learning Outcomes

- **Statistical Analysis**: Hypothesis testing and effect size interpretation
- **Feature Engineering**: Creative feature creation for unsupervised learning
- **Clustering Optimization**: Systematic approach to determining optimal clusters
- **Business Translation**: Converting analytical results into actionable strategies
- **Data Visualization**: Comprehensive multi-dimensional data presentation
- **Customer Analytics**: Professional customer segmentation methodology

## Future Enhancements

- **Advanced Clustering**: Explore hierarchical clustering and DBSCAN algorithms
- **Feature Selection**: Implement automated feature selection techniques
- **Predictive Modeling**: Build models to predict customer segment membership
- **Temporal Analysis**: Analyze customer behavior changes over time
- **A/B Testing**: Validate marketing strategies through controlled experiments
- **Real-time Segmentation**: Develop dynamic customer segmentation system
