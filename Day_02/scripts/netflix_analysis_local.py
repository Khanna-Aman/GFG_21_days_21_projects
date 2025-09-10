#!/usr/bin/env python3
"""
Day 2: Netflix Content Analysis - LOCAL VERSION
In-Depth Exploratory Data Analysis (EDA)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style for plots
sns.set_style('darkgrid')
plt.style.use('default')

print("=== Day 2: Netflix Content Analysis ===")
print("Loading Netflix dataset from local path...")

# Load the Netflix dataset from local path
netflix_df = pd.read_csv('../21-Days-21-Projects-Dataset/Datasets/netflix_titles.csv')

print(f"Dataset loaded successfully!")
print(f"Shape: {netflix_df.shape}")
print("\nFirst few rows:")
print(netflix_df.head())

print("\n=== Data Information ===")
print(netflix_df.info())

print("\n=== Data Cleaning and Transformation ===")

# 1. Handle missing values in 'director' and 'cast'
netflix_df['director'] = netflix_df['director'].fillna('Unknown')
netflix_df['cast'] = netflix_df['cast'].fillna('Unknown')

# 2. Handle missing 'country' with mode
mode_country = netflix_df['country'].mode()[0]
netflix_df['country'] = netflix_df['country'].fillna(mode_country)

# 3. Drop rows with missing 'date_added' and 'rating'
netflix_df.dropna(subset=['date_added', 'rating'], inplace=True)

# 4. Convert 'date_added' to datetime
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], format='mixed', dayfirst=False)

# 5. Create new features for year and month added
netflix_df['year_added'] = netflix_df['date_added'].dt.year
netflix_df['month_added'] = netflix_df['date_added'].dt.month

print("Missing values after cleaning:")
print(netflix_df.isnull().sum())

print("\n=== Exploratory Data Analysis ===")

# 1. Content Type Distribution
print("\n1. Content Type Distribution")
type_counts = netflix_df['type'].value_counts()
print(f"Movies: {type_counts['Movie']} ({type_counts['Movie']/len(netflix_df)*100:.1f}%)")
print(f"TV Shows: {type_counts['TV Show']} ({type_counts['TV Show']/len(netflix_df)*100:.1f}%)")

# 2. Content Added Over Time Analysis
print("\n2. Content Added Over Time")
yearly_content = netflix_df.groupby(['year_added', 'type']).size().unstack(fill_value=0)
print("Content added by year (last 5 years):")
print(yearly_content.tail())

# 3. Top Countries by Content Production
print("\n3. Top Countries by Content Production")
all_countries = []
for countries in netflix_df['country'].dropna():
    if countries != 'Unknown':
        country_list = [country.strip() for country in countries.split(',')]
        all_countries.extend(country_list)

country_counts = pd.Series(all_countries).value_counts().head(10)
print("Top 10 countries:")
for i, (country, count) in enumerate(country_counts.head(10).items(), 1):
    print(f"{i}. {country}: {count} titles")

# 4. Content Ratings Distribution
print("\n4. Content Ratings Distribution")
rating_counts = netflix_df['rating'].value_counts()
print("Content ratings distribution:")
for rating, count in rating_counts.head(10).items():
    print(f"{rating}: {count} titles ({count/len(netflix_df)*100:.1f}%)")

# 5. Release Year Analysis
print("\n5. Release Year Analysis")
release_year_counts = netflix_df['release_year'].value_counts().sort_index()
recent_years = release_year_counts[release_year_counts.index >= 2015]
print("Content by release year (2015 onwards):")
print(recent_years.tail(10))

# 6. Genre Analysis
print("\n6. Genre Analysis")
all_genres = []
for genres in netflix_df['listed_in'].dropna():
    genre_list = [genre.strip() for genre in genres.split(',')]
    all_genres.extend(genre_list)

genre_counts = pd.Series(all_genres).value_counts().head(15)
print("Top 15 genres:")
for i, (genre, count) in enumerate(genre_counts.head(15).items(), 1):
    print(f"{i}. {genre}: {count} titles")

# 7. Duration Analysis for Movies
print("\n7. Movie Duration Analysis")
movies_df = netflix_df[netflix_df['type'] == 'Movie'].copy()
movies_df['duration_minutes'] = movies_df['duration'].str.extract(r'(\d+)').astype(int)

print(f"Average movie duration: {movies_df['duration_minutes'].mean():.1f} minutes")
print(f"Median movie duration: {movies_df['duration_minutes'].median():.1f} minutes")
print(f"Shortest movie: {movies_df['duration_minutes'].min()} minutes")
print(f"Longest movie: {movies_df['duration_minutes'].max()} minutes")

# 8. TV Show Seasons Analysis
print("\n8. TV Show Seasons Analysis")
tv_shows_df = netflix_df[netflix_df['type'] == 'TV Show'].copy()
tv_shows_df['seasons'] = tv_shows_df['duration'].str.extract(r'(\d+)').astype(int)

print(f"Average TV show seasons: {tv_shows_df['seasons'].mean():.1f}")
print(f"Median TV show seasons: {tv_shows_df['seasons'].median():.1f}")
print(f"Most seasons: {tv_shows_df['seasons'].max()}")

# 9. Monthly Addition Patterns
print("\n9. Monthly Addition Patterns")
monthly_additions = netflix_df['month_added'].value_counts().sort_index()
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
print("Content additions by month:")
for month, count in monthly_additions.items():
    print(f"{month_names[int(month)-1]}: {count} titles")

print("\n=== Key Insights ===")
print(f"• Netflix has {len(netflix_df)} total titles after cleaning")
print(f"• {type_counts['Movie']/len(netflix_df)*100:.1f}% are movies, {type_counts['TV Show']/len(netflix_df)*100:.1f}% are TV shows")
print(f"• Content spans from {netflix_df['year_added'].min()} to {netflix_df['year_added'].max()}")
print(f"• Top producing country: {country_counts.index[0]} with {country_counts.iloc[0]} titles")
print(f"• Most common rating: {netflix_df['rating'].mode()[0]}")
print(f"• Most popular genre: {genre_counts.index[0]} with {genre_counts.iloc[0]} titles")
print(f"• Average movie length: {movies_df['duration_minutes'].mean():.0f} minutes")
print(f"• Peak addition month: {month_names[monthly_additions.idxmax()-1]} with {monthly_additions.max()} titles")

print("\n=== Additional Analysis for Submission Questions ===")

# Q1: How has the distribution of content ratings changed over time?
print("\n1. Content Ratings Distribution Over Time")
ratings_by_year = netflix_df.groupby(['year_added', 'rating']).size().unstack(fill_value=0)
print("Top ratings by year (last 5 years):")
for year in sorted(netflix_df['year_added'].unique())[-5:]:
    year_data = netflix_df[netflix_df['year_added'] == year]['rating'].value_counts().head(3)
    print(f"{year}: {', '.join([f'{rating} ({count})' for rating, count in year_data.items()])}")

# Q2: Relationship between content age and type (Movie vs TV Show)
print("\n2. Content Age vs Type Analysis")
netflix_df['content_age'] = netflix_df['year_added'] - netflix_df['release_year']
age_by_type = netflix_df.groupby('type')['content_age'].agg(['mean', 'median', 'std'])
print("Content age statistics by type:")
print(age_by_type)

print("\nContent age distribution:")
for content_type in ['Movie', 'TV Show']:
    type_data = netflix_df[netflix_df['type'] == content_type]['content_age']
    print(f"{content_type}: Avg {type_data.mean():.1f} years, Range {type_data.min()}-{type_data.max()} years")

# Q3: Trends in content production (release year vs year added)
print("\n3. Content Production Trends: Release Year vs Year Added")
recent_content = netflix_df[netflix_df['release_year'] >= 2010]
production_trends = recent_content.groupby(['release_year', 'year_added']).size().reset_index(name='count')
print("Same-year releases (content released and added in same year):")
same_year = netflix_df[netflix_df['release_year'] == netflix_df['year_added']]
same_year_by_year = same_year.groupby('year_added').size()
for year, count in same_year_by_year.tail().items():
    total_year = len(netflix_df[netflix_df['year_added'] == year])
    percentage = (count/total_year)*100
    print(f"{year}: {count}/{total_year} titles ({percentage:.1f}%) were same-year releases")

# Q4: Most common word pairs in descriptions
print("\n4. Most Common Words in Content Descriptions")
from collections import Counter
import re

all_descriptions = ' '.join(netflix_df['description'].fillna('').astype(str))
# Clean and extract words
words = re.findall(r'\b[a-zA-Z]{3,}\b', all_descriptions.lower())
# Remove common stop words
stop_words = {'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'its', 'may', 'new', 'now', 'old', 'see', 'two', 'who', 'boy', 'did', 'she', 'use', 'way', 'will', 'with', 'when', 'they', 'this', 'that', 'from', 'have', 'more', 'what', 'were', 'been', 'than', 'only', 'some', 'time', 'very', 'into', 'just', 'like', 'over', 'also', 'back', 'after', 'first', 'well', 'year', 'work', 'such', 'make', 'even', 'most', 'take', 'come', 'good', 'know', 'where', 'much', 'before', 'through', 'think', 'too', 'any', 'here', 'should', 'never', 'because', 'does', 'while', 'found', 'again', 'there', 'being', 'both', 'during', 'those', 'same', 'until', 'these', 'doing', 'years', 'could', 'each', 'which', 'their', 'said', 'many', 'want', 'however', 'end', 'why', 'called', 'would', 'later', 'find', 'head', 'far', 'always', 'away', 'something', 'fact', 'though', 'water', 'less', 'might', 'around', 'still', 'place', 'right', 'move', 'thing', 'school', 'never', 'last', 'long', 'great', 'little', 'own', 'under', 'might', 'every', 'another', 'came', 'come', 'work', 'three', 'must', 'part', 'small', 'high', 'put', 'end', 'why', 'turn', 'help', 'made', 'point', 'write', 'since', 'without', 'place', 'turn', 'thought', 'show', 'large', 'spell', 'add', 'even', 'land', 'here', 'must', 'big', 'high', 'such', 'follow', 'act', 'why', 'ask', 'men', 'change', 'went', 'light', 'kind', 'off', 'need', 'house', 'picture', 'try', 'again', 'animal', 'point', 'mother', 'world', 'near', 'build', 'self', 'earth', 'father', 'head', 'stand', 'own', 'page', 'should', 'country', 'found', 'answer', 'school', 'grow', 'study', 'still', 'learn', 'plant', 'cover', 'food', 'sun', 'four', 'between', 'state', 'keep', 'eye', 'never', 'last', 'let', 'thought', 'city', 'tree', 'cross', 'farm', 'hard', 'start', 'might', 'story', 'saw', 'far', 'sea', 'draw', 'left', 'late', 'run', 'dont', 'while', 'press', 'close', 'night', 'real', 'life', 'few', 'north', 'open', 'seem', 'together', 'next', 'white', 'children', 'begin', 'got', 'walk', 'example', 'ease', 'paper', 'group', 'always', 'music', 'those', 'both', 'mark', 'often', 'letter', 'until', 'mile', 'river', 'car', 'feet', 'care', 'second', 'book', 'carry', 'took', 'science', 'eat', 'room', 'friend', 'began', 'idea', 'fish', 'mountain', 'stop', 'once', 'base', 'hear', 'horse', 'cut', 'sure', 'watch', 'color', 'face', 'wood', 'main', 'enough', 'plain', 'girl', 'usual', 'young', 'ready', 'above', 'ever', 'red', 'list', 'though', 'feel', 'talk', 'bird', 'soon', 'body', 'dog', 'family', 'direct', 'leave', 'song', 'measure', 'door', 'product', 'black', 'short', 'numeral', 'class', 'wind', 'question', 'happen', 'complete', 'ship', 'area', 'half', 'rock', 'order', 'fire', 'south', 'problem', 'piece', 'told', 'knew', 'pass', 'since', 'top', 'whole', 'king', 'space', 'heard', 'best', 'hour', 'better', 'during', 'hundred', 'five', 'remember', 'step', 'early', 'hold', 'west', 'ground', 'interest', 'reach', 'fast', 'verb', 'sing', 'listen', 'six', 'table', 'travel', 'less', 'morning', 'ten', 'simple', 'several', 'vowel', 'toward', 'war', 'lay', 'against', 'pattern', 'slow', 'center', 'love', 'person', 'money', 'serve', 'appear', 'road', 'map', 'rain', 'rule', 'govern', 'pull', 'cold', 'notice', 'voice', 'unit', 'power', 'town', 'fine', 'certain', 'fly', 'fall', 'lead', 'cry', 'dark', 'machine', 'note', 'wait', 'plan', 'figure', 'star', 'box', 'noun', 'field', 'rest', 'correct', 'able', 'pound', 'done', 'beauty', 'drive', 'stood', 'contain', 'front', 'teach', 'week', 'final', 'gave', 'green', 'quick', 'develop', 'ocean', 'warm', 'free', 'minute', 'strong', 'special', 'mind', 'behind', 'clear', 'tail', 'produce', 'fact', 'street', 'inch', 'multiply', 'nothing', 'course', 'stay', 'wheel', 'full', 'force', 'blue', 'object', 'decide', 'surface', 'deep', 'moon', 'island', 'foot', 'system', 'busy', 'test', 'record', 'boat', 'common', 'gold', 'possible', 'plane', 'stead', 'dry', 'wonder', 'laugh', 'thousands', 'ago', 'ran', 'check', 'game', 'shape', 'equate', 'hot', 'miss', 'brought', 'heat', 'snow', 'tire', 'bring', 'yes', 'distant', 'fill', 'east', 'paint', 'language', 'among'}
filtered_words = [word for word in words if word not in stop_words and len(word) > 3]
word_counts = Counter(filtered_words)
print("Top 15 words in descriptions:")
for i, (word, count) in enumerate(word_counts.most_common(15), 1):
    print(f"{i}. {word}: {count} occurrences")

# Q5: Top directors on Netflix
print("\n5. Top Directors on Netflix")
# Split directors and count
all_directors = []
for directors in netflix_df['director'].dropna():
    if directors != 'Unknown':
        director_list = [director.strip() for director in directors.split(',')]
        all_directors.extend(director_list)

director_counts = pd.Series(all_directors).value_counts().head(15)
print("Top 15 directors by number of titles:")
for i, (director, count) in enumerate(director_counts.items(), 1):
    print(f"{i}. {director}: {count} titles")

print("\n=== Analysis Complete ===")
print("Comprehensive Netflix analysis with submission questions completed successfully!")
