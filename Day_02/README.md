# Day 2: Netflix Content Strategy Analysis

## Project Overview

Professional analysis of Netflix's content library to understand their content acquisition and curation strategy. This project analyzes 7,770 Netflix titles to reveal insights about content ratings, acquisition patterns, production trends, and directorial choices.

## Analysis Files

### 📊 Netflix_Content_Analysis.ipynb
**Main analysis notebook with comprehensive solutions**
- All 5 submission questions answered with detailed visualizations
- Professional presentation with 20+ charts and plots
- Data-driven insights and strategic recommendations
- Complete statistical analysis and trend identification

### 📋 2_Cracking_the_Code_An_Inside_Look_at_Netflix's_Content_Strategy.ipynb
**Original assignment questions with solutions summary**
- Assignment questions as provided
- Quick solutions summary for each question
- References to detailed analysis in main notebook

## Dataset Information

- **Source**: Netflix Titles Dataset from GeeksforGeeks 21-Days-21-Projects
- **Size**: 7,770 titles after data cleaning
- **Time Period**: 2008-2021
- **Content Types**: Movies (69.1%) and TV Shows (30.9%)

## Key Analysis Questions

1. **Content Ratings Evolution**: How has the distribution of content ratings changed over time?
2. **Content Age vs Type**: Is there a relationship between content age and its type?
3. **Production Trends**: Can we identify trends in content production based on release year vs year added?
4. **Content Themes**: What are the most common words in content descriptions?
5. **Director Analysis**: Who are the top directors on Netflix?

## Key Findings

### Strategic Insights

- **Mature Audience Focus**: TV-MA consistently dominates (37-40%) showing Netflix's strategic focus on adult viewers
- **Fresh TV Content**: TV shows are acquired 3.3 years fresher than movies (2.3 vs 5.6 years)
- **Same-Year Releases**: 2020 showed peak with 42.4% same-year releases, indicating increasing focus on fresh content
- **Female-Centric Narratives**: "woman" is the most common word in descriptions, showing emphasis on female protagonists
- **Global Strategy**: Content from 681+ countries with US dominance but strong international presence

### Netflix's Winning Formula

1. **Mature, diverse, global content** targeting adult audiences
2. **Fresh TV shows + established movie catalog** acquisition strategy
3. **Female-driven narratives and relationship stories** as core themes
4. **Mix of prolific directors and renowned filmmakers** for content creation
5. **Increasing investment in same-year releases** for competitive advantage

## Repository Structure

```
Day_02/
├── README.md                                                                      # Project overview and findings
├── Netflix_Content_Analysis.ipynb                                                # Main analysis with comprehensive solutions
├── 2_Cracking_the_Code_An_Inside_Look_at_Netflix's_Content_Strategy.ipynb       # Assignment questions with solutions summary
└── data/
    └── README.md                                                                 # Dataset documentation
```

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Khanna-Aman/GFG_21_days_21_projects.git
   cd GFG_21_days_21_projects/Day_02
   ```

2. **Install required packages**:
   ```bash
   pip install pandas numpy matplotlib seaborn wordcloud
   ```

3. **Run the analysis**:
   - Open `Netflix_Content_Analysis.ipynb` for complete analysis
   - Open `2_Cracking_the_Code_An_Inside_Look_at_Netflix's_Content_Strategy.ipynb` for assignment questions
   - Execute all cells to reproduce the analysis
   - The notebook will automatically clone the dataset repository

## Technical Implementation

- **Data Processing**: Comprehensive cleaning, feature engineering, text analysis
- **Visualization**: 20+ professional plots across all analyses
- **Statistical Analysis**: Descriptive statistics, trend analysis, distribution analysis
- **Tools**: Python (pandas, numpy, matplotlib, seaborn, wordcloud)

## Results Summary

The analysis reveals Netflix's sophisticated content strategy focused on mature audiences, fresh TV content, global reach, female-driven narratives, and balanced talent acquisition. This data-driven analysis provides actionable insights into Netflix's evolution from a movie-focused platform to a comprehensive entertainment ecosystem.

**Status**: Complete  
**Analysis Type**: Comprehensive EDA  
**Insights Generated**: Content strategy, geographic distribution, genre analysis  
**Technical Implementation**: Professional data cleaning and analysis workflow
