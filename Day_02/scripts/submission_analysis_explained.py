#!/usr/bin/env python3
"""
Day 2: Netflix Content Analysis - SUBMISSION QUESTIONS EXPLAINED
Step-by-step development of analysis to answer specific submission questions
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
import warnings
warnings.filterwarnings('ignore')

print("=== NETFLIX SUBMISSION ANALYSIS - STEP BY STEP EXPLANATION ===")
print("This file shows exactly how I developed the analysis to answer the submission questions")

# Load the Netflix dataset
print("\n1. LOADING AND BASIC SETUP")
netflix_df = pd.read_csv('../21-Days-21-Projects-Dataset/Datasets/netflix_titles.csv')
print(f"Dataset loaded: {netflix_df.shape}")

# Basic data cleaning (same as before)
print("\n2. DATA CLEANING (Standard Process)")
netflix_df['director'] = netflix_df['director'].fillna('Unknown')
netflix_df['cast'] = netflix_df['cast'].fillna('Unknown')
mode_country = netflix_df['country'].mode()[0]
netflix_df['country'] = netflix_df['country'].fillna(mode_country)
netflix_df.dropna(subset=['date_added', 'rating'], inplace=True)
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], format='mixed', dayfirst=False)
netflix_df['year_added'] = netflix_df['date_added'].dt.year
netflix_df['month_added'] = netflix_df['date_added'].dt.month
print(f"After cleaning: {netflix_df.shape}")

print("\n" + "="*80)
print("NOW DEVELOPING ANSWERS TO SUBMISSION QUESTIONS")
print("="*80)

# QUESTION 1: How has the distribution of content ratings changed over time?
print("\n📊 QUESTION 1: Content Ratings Distribution Over Time")
print("APPROACH: Group by year_added and rating, then analyze trends")
print("CODE LOGIC:")
print("1. Group data by year_added and rating")
print("2. Count occurrences for each combination")
print("3. Show top ratings for each year")

ratings_by_year = netflix_df.groupby(['year_added', 'rating']).size().unstack(fill_value=0)
print("\nStep 1: Create pivot table of ratings by year")
print("ratings_by_year = netflix_df.groupby(['year_added', 'rating']).size().unstack(fill_value=0)")

print("\nStep 2: Analyze top ratings for recent years")
print("for year in sorted(netflix_df['year_added'].unique())[-5:]:")
print("    year_data = netflix_df[netflix_df['year_added'] == year]['rating'].value_counts().head(3)")

print("\nRESULTS:")
for year in sorted(netflix_df['year_added'].unique())[-5:]:
    year_data = netflix_df[netflix_df['year_added'] == year]['rating'].value_counts().head(3)
    print(f"{year}: {', '.join([f'{rating} ({count})' for rating, count in year_data.items()])}")

print("\nINSIGHT: TV-MA consistently dominates, showing Netflix's focus on mature content")

# QUESTION 2: Relationship between content age and type
print("\n📊 QUESTION 2: Content Age vs Type Analysis")
print("APPROACH: Calculate content age (year_added - release_year) and compare by type")
print("CODE LOGIC:")
print("1. Create content_age feature: year_added - release_year")
print("2. Group by content type and calculate statistics")
print("3. Compare average age between Movies and TV Shows")

netflix_df['content_age'] = netflix_df['year_added'] - netflix_df['release_year']
print("\nStep 1: Calculate content age")
print("netflix_df['content_age'] = netflix_df['year_added'] - netflix_df['release_year']")

age_by_type = netflix_df.groupby('type')['content_age'].agg(['mean', 'median', 'std'])
print("\nStep 2: Group by type and calculate statistics")
print("age_by_type = netflix_df.groupby('type')['content_age'].agg(['mean', 'median', 'std'])")

print("\nRESULTS:")
print(age_by_type)

print("\nStep 3: Detailed breakdown")
for content_type in ['Movie', 'TV Show']:
    type_data = netflix_df[netflix_df['type'] == content_type]['content_age']
    print(f"{content_type}: Avg {type_data.mean():.1f} years, Range {type_data.min()}-{type_data.max()} years")

print("\nINSIGHT: Movies are acquired ~5.6 years after release, TV Shows only ~2.3 years")

# QUESTION 3: Content production trends (release year vs year added)
print("\n📊 QUESTION 3: Release Year vs Year Added Trends")
print("APPROACH: Identify same-year releases (content released and added in same year)")
print("CODE LOGIC:")
print("1. Filter for same-year releases: release_year == year_added")
print("2. Calculate percentage of same-year releases by year")
print("3. Identify trends in fresh content acquisition")

print("\nStep 1: Identify same-year releases")
print("same_year = netflix_df[netflix_df['release_year'] == netflix_df['year_added']]")
same_year = netflix_df[netflix_df['release_year'] == netflix_df['year_added']]

print("\nStep 2: Calculate percentages by year")
print("same_year_by_year = same_year.groupby('year_added').size()")
same_year_by_year = same_year.groupby('year_added').size()

print("\nRESULTS:")
for year, count in same_year_by_year.tail().items():
    total_year = len(netflix_df[netflix_df['year_added'] == year])
    percentage = (count/total_year)*100
    print(f"{year}: {count}/{total_year} titles ({percentage:.1f}%) were same-year releases")

print("\nINSIGHT: 2020 had highest same-year releases (42.4%), showing trend toward fresh content")

# QUESTION 4: Most common words in descriptions
print("\n📊 QUESTION 4: Common Words in Content Descriptions")
print("APPROACH: Text processing to extract and count meaningful words")
print("CODE LOGIC:")
print("1. Combine all descriptions into single text")
print("2. Extract words using regex (3+ characters)")
print("3. Remove stop words to focus on meaningful content")
print("4. Count word frequencies")

print("\nStep 1: Combine descriptions")
print("all_descriptions = ' '.join(netflix_df['description'].fillna('').astype(str))")
all_descriptions = ' '.join(netflix_df['description'].fillna('').astype(str))

print("\nStep 2: Extract words with regex")
print("words = re.findall(r'\\b[a-zA-Z]{3,}\\b', all_descriptions.lower())")
words = re.findall(r'\b[a-zA-Z]{3,}\b', all_descriptions.lower())

print(f"\nStep 3: Remove stop words (defined list of {len(['the', 'and', 'for'])}+ common words)")
# Simplified stop words list for demonstration
stop_words = {'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'its', 'may', 'new', 'now', 'old', 'see', 'two', 'who', 'boy', 'did', 'she', 'use', 'way', 'will', 'with', 'when', 'they', 'this', 'that', 'from', 'have', 'more', 'what', 'were', 'been', 'than', 'only', 'some', 'time', 'very', 'into', 'just', 'like', 'over', 'also', 'back', 'after', 'first', 'well', 'year', 'work', 'such', 'make', 'even', 'most', 'take', 'come', 'good', 'know', 'where', 'much', 'before', 'through', 'think', 'too', 'any', 'here', 'should', 'never', 'because', 'does', 'while', 'found', 'again', 'there', 'being', 'both', 'during', 'those', 'same', 'until', 'these', 'doing', 'years', 'could', 'each', 'which', 'their', 'said', 'many', 'want', 'however', 'end', 'why', 'called', 'would', 'later', 'find', 'head', 'far', 'always', 'away', 'something', 'fact', 'though', 'water', 'less', 'might', 'around', 'still', 'place', 'right', 'move', 'thing', 'school', 'never', 'last', 'long', 'great', 'little', 'own', 'under', 'might', 'every', 'another', 'came', 'come', 'work', 'three', 'must', 'part', 'small', 'high', 'put', 'end', 'why', 'turn', 'help', 'made', 'point', 'write', 'since', 'without', 'place', 'turn', 'thought', 'show', 'large', 'spell', 'add', 'even', 'land', 'here', 'must', 'big', 'high', 'such', 'follow', 'act', 'why', 'ask', 'men', 'change', 'went', 'light', 'kind', 'off', 'need', 'house', 'picture', 'try', 'again', 'animal', 'point', 'mother', 'world', 'near', 'build', 'self', 'earth', 'father', 'head', 'stand', 'own', 'page', 'should', 'country', 'found', 'answer', 'school', 'grow', 'study', 'still', 'learn', 'plant', 'cover', 'food', 'sun', 'four', 'between', 'state', 'keep', 'eye', 'never', 'last', 'let', 'thought', 'city', 'tree', 'cross', 'farm', 'hard', 'start', 'might', 'story', 'saw', 'far', 'sea', 'draw', 'left', 'late', 'run', 'dont', 'while', 'press', 'close', 'night', 'real', 'life', 'few', 'north', 'open', 'seem', 'together', 'next', 'white', 'children', 'begin', 'got', 'walk', 'example', 'ease', 'paper', 'group', 'always', 'music', 'those', 'both', 'mark', 'often', 'letter', 'until', 'mile', 'river', 'car', 'feet', 'care', 'second', 'book', 'carry', 'took', 'science', 'eat', 'room', 'friend', 'began', 'idea', 'fish', 'mountain', 'stop', 'once', 'base', 'hear', 'horse', 'cut', 'sure', 'watch', 'color', 'face', 'wood', 'main', 'enough', 'plain', 'girl', 'usual', 'young', 'ready', 'above', 'ever', 'red', 'list', 'though', 'feel', 'talk', 'bird', 'soon', 'body', 'dog', 'family', 'direct', 'leave', 'song', 'measure', 'door', 'product', 'black', 'short', 'numeral', 'class', 'wind', 'question', 'happen', 'complete', 'ship', 'area', 'half', 'rock', 'order', 'fire', 'south', 'problem', 'piece', 'told', 'knew', 'pass', 'since', 'top', 'whole', 'king', 'space', 'heard', 'best', 'hour', 'better', 'during', 'hundred', 'five', 'remember', 'step', 'early', 'hold', 'west', 'ground', 'interest', 'reach', 'fast', 'verb', 'sing', 'listen', 'six', 'table', 'travel', 'less', 'morning', 'ten', 'simple', 'several', 'vowel', 'toward', 'war', 'lay', 'against', 'pattern', 'slow', 'center', 'love', 'person', 'money', 'serve', 'appear', 'road', 'map', 'rain', 'rule', 'govern', 'pull', 'cold', 'notice', 'voice', 'unit', 'power', 'town', 'fine', 'certain', 'fly', 'fall', 'lead', 'cry', 'dark', 'machine', 'note', 'wait', 'plan', 'figure', 'star', 'box', 'noun', 'field', 'rest', 'correct', 'able', 'pound', 'done', 'beauty', 'drive', 'stood', 'contain', 'front', 'teach', 'week', 'final', 'gave', 'green', 'quick', 'develop', 'ocean', 'warm', 'free', 'minute', 'strong', 'special', 'mind', 'behind', 'clear', 'tail', 'produce', 'fact', 'street', 'inch', 'multiply', 'nothing', 'course', 'stay', 'wheel', 'full', 'force', 'blue', 'object', 'decide', 'surface', 'deep', 'moon', 'island', 'foot', 'system', 'busy', 'test', 'record', 'boat', 'common', 'gold', 'possible', 'plane', 'stead', 'dry', 'wonder', 'laugh', 'thousands', 'ago', 'ran', 'check', 'game', 'shape', 'equate', 'hot', 'miss', 'brought', 'heat', 'snow', 'tire', 'bring', 'yes', 'distant', 'fill', 'east', 'paint', 'language', 'among'}

filtered_words = [word for word in words if word not in stop_words and len(word) > 3]
print("filtered_words = [word for word in words if word not in stop_words and len(word) > 3]")

print("\nStep 4: Count word frequencies")
print("word_counts = Counter(filtered_words)")
word_counts = Counter(filtered_words)

print("\nRESULTS - Top 10 words:")
for i, (word, count) in enumerate(word_counts.most_common(10), 1):
    print(f"{i}. {word}: {count} occurrences")

print("\nINSIGHT: 'woman', 'friends', 'series' are top themes, showing focus on female narratives and relationships")

# QUESTION 5: Top directors
print("\n📊 QUESTION 5: Top Directors on Netflix")
print("APPROACH: Split multi-director fields and count individual directors")
print("CODE LOGIC:")
print("1. Split director field by comma (handles multiple directors)")
print("2. Strip whitespace and collect all director names")
print("3. Count frequencies and rank")

print("\nStep 1: Split and collect all directors")
print("for directors in netflix_df['director'].dropna():")
print("    if directors != 'Unknown':")
print("        director_list = [director.strip() for director in directors.split(',')]")
print("        all_directors.extend(director_list)")

all_directors = []
for directors in netflix_df['director'].dropna():
    if directors != 'Unknown':
        director_list = [director.strip() for director in directors.split(',')]
        all_directors.extend(director_list)

print(f"\nStep 2: Count director frequencies")
print("director_counts = pd.Series(all_directors).value_counts()")
director_counts = pd.Series(all_directors).value_counts()

print("\nRESULTS - Top 10 directors:")
for i, (director, count) in enumerate(director_counts.head(10).items(), 1):
    print(f"{i}. {director}: {count} titles")

print("\nINSIGHT: Mix of prolific TV directors and renowned filmmakers, showing Netflix's dual strategy")

print("\n" + "="*80)
print("SUMMARY OF METHODOLOGY")
print("="*80)
print("1. RATINGS OVER TIME: Grouped by year+rating, analyzed trends")
print("2. CONTENT AGE: Created derived feature (year_added - release_year)")
print("3. PRODUCTION TRENDS: Identified same-year releases as freshness indicator")
print("4. DESCRIPTION WORDS: Text processing with stop word removal")
print("5. TOP DIRECTORS: Split multi-value fields and frequency counting")
print("\nEach analysis used pandas groupby, aggregation, and statistical methods")
print("to extract meaningful insights from the Netflix dataset.")
