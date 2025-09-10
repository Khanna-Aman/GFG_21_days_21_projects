# Day 2 Data Directory

## Dataset Information

**Dataset**: Netflix Titles Dataset  
**Source**: [GeeksforGeeks 21-Days-21-Projects-Dataset](https://github.com/GeeksforgeeksDS/21-Days-21-Projects-Dataset)  
**File**: `netflix_titles.csv`

## Dataset Description

The Netflix dataset contains information about movies and TV shows available on Netflix as of 2021.

### Features (12 columns):
- **show_id**: Unique identifier for each title
- **type**: Content type (Movie or TV Show)
- **title**: Name of the content
- **director**: Director(s) of the content
- **cast**: Main cast members
- **country**: Country/countries of production
- **date_added**: Date when content was added to Netflix
- **release_year**: Year the content was originally released
- **rating**: Content rating (TV-MA, TV-14, R, etc.)
- **duration**: Duration (minutes for movies, seasons for TV shows)
- **listed_in**: Genres/categories
- **description**: Brief description of the content

### Dataset Statistics:
- **Total Records**: 7,787 titles
- **After Cleaning**: 7,770 titles
- **Content Split**: 69.1% Movies, 30.9% TV Shows
- **Time Range**: Content added from 2008-2021
- **Geographic Coverage**: 681 countries/regions

## Data Access

The dataset is automatically downloaded when running the analysis notebooks using:
```bash
!git clone "https://github.com/GeeksforgeeksDS/21-Days-21-Projects-Dataset"
```

For local development, the dataset is available at:
```
../21-Days-21-Projects-Dataset/Datasets/netflix_titles.csv
```

## Data Quality Notes

- **Missing Values**: Handled during preprocessing
- **Multi-value Fields**: Director, cast, country, and genres contain comma-separated values
- **Date Format**: date_added requires parsing to datetime format
- **Duration Format**: Mixed format (minutes for movies, seasons for TV shows)
