# Day 2: Netflix Content Analysis

## Project Overview

In-depth exploratory data analysis (EDA) of Netflix's content strategy, analyzing trends in content production, popular genres, content ratings, and distribution patterns.

## Objectives

- Perform comprehensive EDA on Netflix dataset
- Analyze content trends over time
- Understand geographical distribution of content
- Examine genre preferences and rating patterns
- Extract insights about Netflix's content strategy

## Dataset Information

**Source**: Netflix Titles Dataset  
**Records**: 7,787 titles (7,770 after cleaning)  
**Features**: 12 columns  
**Content Types**: Movies (69.1%) and TV Shows (30.9%)  
**Time Range**: 2008-2021

## Key Findings

### Content Distribution
- **Movies**: 5,372 titles (69.1%)
- **TV Shows**: 2,398 titles (30.9%)
- **Peak Addition Year**: 2019 with 2,153 titles
- **Peak Addition Month**: December with 832 titles

### Geographic Analysis
- **Top Producer**: United States (3,793 titles)
- **International Presence**: Strong content from India (990), UK (722), Canada (412)
- **Global Strategy**: Content from 681 different countries/regions

### Content Characteristics
- **Average Movie Duration**: 99.3 minutes
- **Average TV Show Seasons**: 1.8 seasons
- **Most Common Rating**: TV-MA (36.8% of content)
- **Popular Genres**: International Movies, Dramas, Comedies

### Content Strategy Insights
- **International Focus**: Heavy emphasis on international content
- **Mature Audience**: 36.8% rated TV-MA, targeting adult viewers
- **Diverse Portfolio**: Content spanning multiple genres and countries
- **Recent Content**: Strong focus on content from 2015 onwards

## Technical Implementation

### Data Cleaning Process
1. **Missing Value Treatment**:
   - Director/Cast: Filled with "Unknown"
   - Country: Filled with mode (United States)
   - Date/Rating: Dropped rows with missing values

2. **Feature Engineering**:
   - Extracted year and month from date_added
   - Parsed duration for movies and TV shows
   - Split multi-value fields (countries, genres)

3. **Data Validation**:
   - Converted date_added to datetime format
   - Ensured data type consistency
   - Verified no missing values after cleaning

## Files Structure

```
Day_02/
├── README.md                                           # Project documentation
├── 2_Cracking_the_Code_An_Inside_Look_at_Netflix's_Content_Strategy.ipynb  # Local notebook
├── netflix_analysis_github.ipynb                      # GitHub version (with git clone)
└── netflix_analysis_local.py                          # Local Python script
```

## Usage

### Local Execution
```bash
# Run Python script
python netflix_analysis_local.py

# Or use Jupyter notebook
jupyter notebook 2_Cracking_the_Code_An_Inside_Look_at_Netflix's_Content_Strategy.ipynb
```

### GitHub/Colab Execution
```bash
# Use the GitHub version which includes git clone
jupyter notebook netflix_analysis_github.ipynb
```

## Key Insights Summary

1. **Content Volume**: Netflix has significantly more movies than TV shows
2. **Global Strategy**: Strong international content focus, especially from US and India
3. **Target Audience**: Primarily mature content (TV-MA rating most common)
4. **Genre Diversity**: Wide range of genres with emphasis on international and drama content
5. **Growth Pattern**: Steady content addition with peak in 2019
6. **Seasonal Trends**: Higher content additions in Q4 (October-December)

## Technical Skills Demonstrated

- **Data Cleaning**: Handling missing values, data type conversion
- **Time Series Analysis**: Analyzing trends over time
- **Text Processing**: Parsing multi-value fields (genres, countries)
- **Statistical Analysis**: Descriptive statistics and distributions
- **Data Visualization**: Creating meaningful charts and graphs
- **Feature Engineering**: Creating derived features for analysis

## Assignment Status

**Status**: Complete  
**Analysis Type**: Comprehensive EDA  
**Insights Generated**: Content strategy, geographic distribution, genre analysis  
**Technical Implementation**: Professional data cleaning and analysis workflow
