# Netflix Analysis Methodology - Submission Questions Explained

## How I Developed the Analysis to Answer Submission Questions

This document explains exactly how I approached each submission question and the reasoning behind my analytical methods.

## Question 1: How has the distribution of content ratings changed over time?

### My Approach
```python
# Step 1: Group by year and rating
ratings_by_year = netflix_df.groupby(['year_added', 'rating']).size().unstack(fill_value=0)

# Step 2: Analyze top ratings for each year
for year in sorted(netflix_df['year_added'].unique())[-5:]:
    year_data = netflix_df[netflix_df['year_added'] == year]['rating'].value_counts().head(3)
```

### Why This Method?
- **Groupby Analysis**: Used pandas groupby to create a cross-tabulation of years vs ratings
- **Time Series Focus**: Focused on recent 5 years to show current trends
- **Top 3 Ratings**: Showed top 3 ratings per year to identify dominant patterns
- **Percentage Calculation**: Calculated percentages to show relative importance

### Key Finding
TV-MA consistently dominates (36.8% overall), showing Netflix's strategic focus on mature content.

---

## Question 2: Is there a relationship between content age and its type?

### My Approach
```python
# Step 1: Create derived feature
netflix_df['content_age'] = netflix_df['year_added'] - netflix_df['release_year']

# Step 2: Statistical analysis by type
age_by_type = netflix_df.groupby('type')['content_age'].agg(['mean', 'median', 'std'])
```

### Why This Method?
- **Feature Engineering**: Created `content_age` as a derived metric (year_added - release_year)
- **Statistical Aggregation**: Used mean, median, and standard deviation to understand distributions
- **Comparative Analysis**: Directly compared Movies vs TV Shows
- **Range Analysis**: Examined min/max values to understand data spread

### Key Finding
Movies average 5.6 years old when added, TV Shows only 2.3 years - Netflix acquires TV content much fresher.

---

## Question 3: Content production trends (release year vs year added)?

### My Approach
```python
# Step 1: Identify same-year releases
same_year = netflix_df[netflix_df['release_year'] == netflix_df['year_added']]

# Step 2: Calculate percentages by year
same_year_by_year = same_year.groupby('year_added').size()
for year, count in same_year_by_year.items():
    total_year = len(netflix_df[netflix_df['year_added'] == year])
    percentage = (count/total_year)*100
```

### Why This Method?
- **Same-Year Indicator**: Used equality comparison to identify "fresh" content
- **Percentage Calculation**: Calculated what portion of each year's additions were same-year releases
- **Trend Analysis**: Tracked this percentage over time to identify patterns
- **Business Insight**: Same-year releases indicate Netflix's investment in current content

### Key Finding
2020 had 42.4% same-year releases (highest), showing Netflix's increasing focus on fresh content.

---

## Question 4: Most common words in content descriptions?

### My Approach
```python
# Step 1: Text aggregation
all_descriptions = ' '.join(netflix_df['description'].fillna('').astype(str))

# Step 2: Word extraction with regex
words = re.findall(r'\b[a-zA-Z]{3,}\b', all_descriptions.lower())

# Step 3: Stop word removal
stop_words = {'the', 'and', 'for', ...}  # 200+ common words
filtered_words = [word for word in words if word not in stop_words and len(word) > 3]

# Step 4: Frequency counting
word_counts = Counter(filtered_words)
```

### Why This Method?
- **Text Preprocessing**: Combined all descriptions into single corpus for analysis
- **Regex Pattern**: Used `\b[a-zA-Z]{3,}\b` to extract meaningful words (3+ characters)
- **Stop Word Filtering**: Removed 200+ common English words to focus on content-specific terms
- **Frequency Analysis**: Used Counter to rank words by occurrence

### Key Finding
"woman" (429), "friends" (383), "series" (357) are top themes, revealing Netflix's focus on female narratives and relationships.

---

## Question 5: Who are the top directors on Netflix?

### My Approach
```python
# Step 1: Handle multi-value fields
all_directors = []
for directors in netflix_df['director'].dropna():
    if directors != 'Unknown':
        director_list = [director.strip() for director in directors.split(',')]
        all_directors.extend(director_list)

# Step 2: Frequency counting
director_counts = pd.Series(all_directors).value_counts()
```

### Why This Method?
- **Multi-Value Handling**: Split comma-separated director fields to count individual directors
- **Data Cleaning**: Stripped whitespace and excluded 'Unknown' entries
- **Flattening**: Extended list to handle multiple directors per title
- **Ranking**: Used value_counts() for automatic frequency ranking

### Key Finding
Jan Suter (21 titles) leads, followed by Raúl Campos (19). Mix of prolific TV directors and renowned filmmakers like Scorsese and Spielberg.

---

## Overall Methodology Principles

### 1. **Data-Driven Approach**
- Every insight backed by quantitative analysis
- Used pandas groupby, aggregation, and statistical functions
- Calculated percentages and trends for context

### 2. **Feature Engineering**
- Created derived features like `content_age` for deeper insights
- Transformed categorical data for meaningful comparisons
- Handled multi-value fields (directors, countries, genres)

### 3. **Text Processing**
- Applied NLP techniques for description analysis
- Used regex for pattern extraction
- Implemented stop word filtering for meaningful results

### 4. **Business Context**
- Interpreted technical findings in business terms
- Connected data patterns to Netflix's content strategy
- Provided actionable insights for content decisions

### 5. **Comprehensive Coverage**
- Addressed temporal trends (time-based analysis)
- Examined content characteristics (age, type, ratings)
- Analyzed production patterns (fresh vs acquired content)
- Investigated textual themes (description analysis)
- Identified key personnel (director analysis)

## Technical Skills Demonstrated

1. **Pandas Operations**: groupby, aggregation, pivot tables, value_counts
2. **Feature Engineering**: derived metrics, data transformation
3. **Text Processing**: regex, string manipulation, frequency analysis
4. **Statistical Analysis**: mean, median, standard deviation, percentages
5. **Data Cleaning**: handling missing values, multi-value fields
6. **Time Series Analysis**: temporal trend identification
7. **Business Intelligence**: translating data into actionable insights

This methodology ensures comprehensive, data-driven answers to all submission questions while demonstrating advanced data analysis capabilities.
