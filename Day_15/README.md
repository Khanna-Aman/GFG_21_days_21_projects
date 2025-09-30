# Day 15: Text-to-SQL via Prompt Engineering

## Project Overview

This project demonstrates the implementation of a Natural Language to SQL (NL2SQL) system using prompt engineering techniques with Google's Gemini AI model. The system enables non-technical users to query databases using plain English questions, which are automatically translated into executable SQL queries.

The project consists of two main components:
1. **Main Tutorial**: Building a Text-to-SQL generator for an e-commerce database
2. **Assignment**: Creating and analyzing a comprehensive employee dataset

## Table of Contents

- [Project Structure](#project-structure)
- [Main Tutorial: Text-to-SQL Generator](#main-tutorial-text-to-sql-generator)
- [Assignment: Employee Dataset Analysis](#assignment-employee-dataset-analysis)
- [Installation and Setup](#installation-and-setup)
- [Usage Instructions](#usage-instructions)
- [Technical Implementation](#technical-implementation)
- [Key Concepts](#key-concepts)
- [Dependencies](#dependencies)
- [Output Files](#output-files)

## Project Structure

```
Day_15/
├── README.md                                                                # Project documentation
├── 15_Talk_to_Your_Data_Building_a_Natural_Language_to_SQL_Generator.ipynb # Main tutorial notebook
├── Assignment_Employee_Dataset_Creation_Analysis.ipynb                      # Assignment solution notebook
├── employee_dataset_mockaroo.csv                                            # Original Mockaroo dataset (1,000 records)
├── employee_dataset_1000_records.csv                                        # Processed employee dataset
├── employee_dataset_summary_statistics.csv                                  # Statistical summary of dataset
├── department_analysis_summary.csv                                          # Department-wise analysis results
└── employee_dataset_data_dictionary.csv                                     # Data dictionary with field descriptions
```

## Main Tutorial: Text-to-SQL Generator

### Overview

The main tutorial demonstrates how to build a production-ready Text-to-SQL system that translates natural language questions into SQL queries for an e-commerce database.

### Key Features

- Natural language query processing using Google Gemini AI
- SQLite database integration with e-commerce schema
- Structured prompt engineering framework
- Automatic query generation and execution
- Error handling and validation
- Token usage tracking and optimization

### Database Schema

The system works with an e-commerce database containing three tables:

**Customers Table:**
- customer_id (INT, PRIMARY KEY)
- first_name (TEXT)
- last_name (TEXT)
- email (TEXT)
- city (TEXT)
- state (TEXT)
- country (TEXT)

**Products Table:**
- product_id (INT, PRIMARY KEY)
- product_name (TEXT)
- category (TEXT)
- price (REAL)
- stock_quantity (INT)

**Orders Table:**
- order_id (INT, PRIMARY KEY)
- customer_id (INT, FOREIGN KEY)
- product_id (INT, FOREIGN KEY)
- quantity (INT)
- order_date (TEXT)
- total_amount (REAL)

### Prompt Engineering Framework

The tutorial implements a comprehensive prompt structure with the following components:

1. **ROLE**: Defines the AI as an expert SQLite Database Engineer
2. **CONTEXT**: Establishes the business intelligence dashboard scenario
3. **TASK**: Specifies the NL2SQL translation requirements
4. **CONSTRAINTS**: Enforces read-only operations and schema adherence
5. **EXAMPLES**: Provides few-shot learning examples
6. **OUTPUT FORMAT**: Defines JSON response structure

### Core Functions

**get_sql_query(genai_client, prompt, user_query)**
- Sends natural language query to Gemini AI
- Returns JSON with SQL query and status
- Tracks token usage (input, thoughts, output)

**execute_query(query, db_name)**
- Executes SQL query on SQLite database
- Returns results as pandas DataFrame
- Handles connection management and error handling

**text2sql(genai_client, prompt, user_query)**
- Combines query generation and execution
- End-to-end natural language to results pipeline

### Example Queries

The tutorial demonstrates various query types:
- Simple lookups: "Show me all customers from California"
- Aggregations: "What is the total revenue by product category?"
- Joins: "List all orders with customer and product details"
- Complex analytics: "Find top 5 customers by total spending"

## Assignment: Employee Dataset Analysis

### Overview

The assignment focuses on creating a comprehensive employee dataset using Mockaroo and performing detailed analysis with professional visualizations and insights.

### Dataset Specifications

**Dataset Size:** 1,000 employee records

**Attributes (19 columns):**

1. **Personal Information:**
   - employee_id: Unique identifier
   - full_name: Complete name
   - first_name: First name
   - last_name: Last name
   - email: Email address
   - phone: Phone number

2. **Demographics:**
   - age: Employee age (22-64 years)
   - gender: Male/Female
   - city: Location

3. **Employment Details:**
   - department: 8 departments (IT, Sales, Marketing, HR, Finance, Operations, Engineering, Customer Service)
   - position: 40+ unique positions
   - employment_type: Full-time/Part-time/Contract
   - hire_date: Date of hire

4. **Professional Background:**
   - years_experience: Years of professional experience
   - education_level: High School/Bachelor's/Master's/PhD

5. **Compensation:**
   - salary: Annual salary ($35,000 - $285,000)
   - bonus: Annual bonus amount

6. **Performance:**
   - performance_rating: Rating scale 1-5
   - projects_completed: Number of completed projects

### Analysis Components

The assignment notebook includes:

1. **Data Quality Assessment:**
   - Missing value analysis
   - Duplicate detection
   - Data type validation
   - Unique value counts

2. **Descriptive Statistics:**
   - Summary statistics for numerical columns
   - Distribution analysis
   - Central tendency measures

3. **Department Analysis:**
   - Employee distribution by department
   - Average salary by department
   - Department-wise performance metrics

4. **Compensation Analysis:**
   - Salary distribution and ranges
   - Bonus analysis
   - Total compensation calculations
   - Salary correlation with experience and education

5. **Performance Analysis:**
   - Performance rating distribution
   - Correlation with salary
   - Projects completed analysis

6. **Demographics Analysis:**
   - Age distribution
   - Gender distribution
   - Education level distribution
   - Geographic distribution

### Visualizations

The notebook includes 12+ professional visualizations:

**Basic Charts:**
1. Department distribution (pie chart)
2. Salary distribution (histogram)
3. Age distribution (histogram)
4. Average salary by department (horizontal bar chart)
5. Performance rating distribution (bar chart)
6. Gender distribution (pie chart)
7. Education level distribution (bar chart)
8. Salary vs experience (scatter plot)
9. Employment type distribution (pie chart)

**Advanced Visualizations:**
10. Correlation heatmap (6 numerical variables)
11. Salary distribution by department (box plot)
12. Performance vs salary by department (scatter plot with color coding)

### Key Insights Generated

The analysis provides actionable insights including:
- Department with highest employee count
- Department with highest average salary
- Performance rating distribution patterns
- Gender distribution balance
- Education level impact on salary
- Experience correlation with compensation
- Employment type distribution

## Installation and Setup

### Prerequisites

- Python 3.7 or higher
- Google Colab account (recommended) or local Jupyter environment
- Google AI Studio API key (for Text-to-SQL functionality)

### Required Libraries

```python
# Data manipulation and analysis
pandas>=1.3.0
numpy>=1.20.0

# Visualization
matplotlib>=3.3.0
seaborn>=0.11.0

# Database
sqlite3 (built-in)

# AI/ML (for Text-to-SQL)
google-genai>=0.1.0

# Utilities
requests>=2.25.0
```

### Installation Steps

**For Google Colab:**

1. Open the notebook in Google Colab
2. Install required packages:
```python
!pip install google-genai
```

3. Set up API key in Colab Secrets:
   - Go to Google AI Studio: https://aistudio.google.com/
   - Generate API key
   - Add to Colab Secrets as 'GOOGLE_API_KEY'

**For Local Environment:**

1. Clone or download the project files
2. Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn google-genai requests
```

3. Set environment variable for API key:
```bash
export GOOGLE_API_KEY='your_api_key_here'
```

## Usage Instructions

### Running the Main Tutorial

1. Open `15_Talk_to_Your_Data_Building_a_Natural_Language_to_SQL_Generator.ipynb`
2. Execute cells sequentially
3. The notebook will:
   - Download sample e-commerce data from Mockaroo
   - Create SQLite database with three tables
   - Load data into database
   - Set up Gemini AI client
   - Demonstrate Text-to-SQL queries

4. Try custom queries by modifying the user_query variable:
```python
user_query = "Your natural language question here"
text2sql(genai_client, prompt, user_query)
```

### Running the Assignment

1. Open `Assignment_Employee_Dataset_Creation_Analysis.ipynb`
2. Execute cells sequentially
3. The notebook will:
   - Load pre-generated employee dataset
   - Perform data quality checks
   - Generate statistical summaries
   - Create visualizations
   - Export analysis results

4. All output files are automatically saved in the working directory

## Technical Implementation

### Text-to-SQL Architecture

The system follows a multi-step pipeline:

1. **User Input**: Natural language question
2. **Prompt Construction**: Combine system prompt with user query
3. **AI Processing**: Gemini AI generates SQL query
4. **Query Validation**: Check for syntax and schema compliance
5. **Execution**: Run query on SQLite database
6. **Result Formatting**: Return results as DataFrame

### Prompt Engineering Best Practices

The tutorial demonstrates key prompt engineering techniques:

**Role Definition:**
- Establishes AI as expert SQLite Database Engineer
- Specializes in NL2SQL translation

**Context Setting:**
- Business intelligence dashboard scenario
- Non-technical user audience
- Direct database execution context

**Task Specification:**
- Clear step-by-step instructions
- Schema understanding requirements
- Query generation guidelines

**Constraint Enforcement:**
- Read-only operations (SELECT only)
- Schema adherence
- No assumptions or inventions
- Proper SQL syntax

**Few-Shot Learning:**
- Multiple example queries
- Various complexity levels
- Expected output format demonstrations

**Output Formatting:**
- Structured JSON response
- Status and response fields
- Error handling guidance

### Data Generation with Mockaroo

Both notebooks utilize Mockaroo for realistic data generation:

**Mockaroo Features Used:**
- Realistic name generation
- Email address formatting
- Phone number patterns
- Date range specifications
- Categorical data (departments, positions)
- Numerical distributions (salary ranges)
- Custom field types

**Data Quality Characteristics:**
- No missing values
- Proper data types
- Realistic distributions
- Logical relationships (age vs experience)
- Diverse categorical values

## Key Concepts

### Natural Language to SQL (NL2SQL)

NL2SQL is a technology that translates natural language questions into SQL queries. Key aspects:

**Benefits:**
- Democratizes data access for non-technical users
- Reduces dependency on data analysts
- Enables self-service analytics
- Improves decision-making speed

**Challenges:**
- Ambiguous natural language interpretation
- Complex query requirements
- Schema understanding
- Error handling and validation

**Applications:**
- Business intelligence dashboards
- Customer support systems
- Data exploration tools
- Reporting automation

### Prompt Engineering

Prompt engineering is the practice of designing effective prompts for AI models:

**Core Components:**
1. **Role**: Define AI's expertise and function
2. **Context**: Provide background and scenario
3. **Task**: Specify exact requirements
4. **Constraints**: Set boundaries and limitations
5. **Examples**: Demonstrate expected behavior
6. **Output Format**: Define response structure

**Best Practices:**
- Use clear delimiters (Markdown headers)
- Provide specific instructions
- Include edge cases
- Define output format explicitly
- Use few-shot learning examples

### Database Design

The tutorial demonstrates proper database design:

**Normalization:**
- Separate tables for entities
- Primary and foreign keys
- Referential integrity

**Schema Definition:**
- Explicit data types
- Constraints and validations
- Indexing considerations

**Data Loading:**
- CSV to database import
- Data type enforcement
- Error handling

## Dependencies

### Core Libraries

**pandas (2.2.2)**
- Data manipulation and analysis
- DataFrame operations
- CSV file handling
- Statistical computations

**numpy (2.0.2)**
- Numerical operations
- Array manipulations
- Mathematical functions

**matplotlib (3.10.0)**
- Basic plotting and visualization
- Chart customization
- Figure management

**seaborn (0.13.2)**
- Statistical visualizations
- Enhanced plot aesthetics
- Color palettes

**sqlite3 (built-in)**
- Database creation and management
- Query execution
- Connection handling

**google-genai**
- Gemini AI model access
- Natural language processing
- Query generation

**requests**
- HTTP requests for data download
- API interactions

## Output Files

### Main Tutorial Outputs

**ecommerce.db**
- SQLite database file
- Contains customers, products, and orders tables
- Populated with Mockaroo-generated data

### Assignment Outputs

**employee_dataset_mockaroo.csv**
- Original dataset from Mockaroo
- 1,000 employee records
- 19 columns with complete data

**employee_dataset_1000_records.csv**
- Exported dataset after processing
- Same structure as original
- Validated and cleaned data

**employee_dataset_summary_statistics.csv**
- Statistical summary of numerical columns
- Count, mean, std, min, max, quartiles
- For all numerical attributes

**department_analysis_summary.csv**
- Department-wise aggregated metrics
- Employee count per department
- Average salary by department
- Performance metrics

**employee_dataset_data_dictionary.csv**
- Complete data dictionary
- Column names and descriptions
- Data types and ranges
- Example values

## Learning Outcomes

By completing this project, you will learn:

1. **Prompt Engineering:**
   - Structured prompt design
   - Role-context-task framework
   - Few-shot learning techniques
   - Output format specification

2. **Natural Language Processing:**
   - NL2SQL translation concepts
   - Query generation strategies
   - Error handling approaches

3. **Database Operations:**
   - SQLite database creation
   - Schema design and implementation
   - Data loading from CSV
   - Query execution and result handling

4. **Data Analysis:**
   - Exploratory data analysis
   - Statistical computations
   - Data quality assessment
   - Insight generation

5. **Data Visualization:**
   - Multiple chart types
   - Professional plot styling
   - Correlation analysis
   - Distribution visualization

6. **Python Programming:**
   - Function design and implementation
   - Error handling and validation
   - File I/O operations
   - API integration

## Advanced Topics Covered

### Retrieval-Augmented Generation (RAG)

The tutorial introduces RAG as a next step:
- Combining LLM knowledge with external data
- Dynamic schema retrieval
- Context-aware query generation

### Fine-Tuning Considerations

Discussion of model fine-tuning:
- When to fine-tune vs prompt engineering
- Data requirements
- Performance optimization

### System Architecture

Building production systems:
- Multi-agent architectures
- Query validation layers
- Result caching strategies
- User feedback loops

## Best Practices Demonstrated

1. **Code Organization:**
   - Modular function design
   - Clear documentation
   - Consistent naming conventions

2. **Error Handling:**
   - Try-except blocks
   - Connection management
   - Graceful degradation

3. **Data Quality:**
   - Validation checks
   - Type enforcement
   - Missing value handling

4. **Documentation:**
   - Comprehensive markdown cells
   - Code comments
   - Usage examples

5. **Reproducibility:**
   - Fixed random seeds (where applicable)
   - Clear data sources
   - Version tracking

## Troubleshooting

### Common Issues and Solutions

**Issue: API Key Not Found**
- Solution: Ensure GOOGLE_API_KEY is set in Colab Secrets or environment variables

**Issue: Database Connection Error**
- Solution: Check file paths and ensure database file exists

**Issue: Mockaroo Data Download Fails**
- Solution: Notebook includes fallback to pre-generated CSV files

**Issue: Visualization Not Displaying**
- Solution: Ensure matplotlib backend is properly configured

**Issue: Memory Error with Large Datasets**
- Solution: Process data in chunks or reduce dataset size

## Future Enhancements

Potential improvements and extensions:

1. **Interactive Dashboard:**
   - Streamlit or Dash integration
   - Real-time query interface
   - Result visualization

2. **Query Optimization:**
   - Query plan analysis
   - Index recommendations
   - Performance monitoring

3. **Advanced NL2SQL:**
   - Multi-table join handling
   - Subquery generation
   - Aggregate function support

4. **User Feedback Loop:**
   - Query correction mechanism
   - Learning from user edits
   - Confidence scoring

5. **Extended Analytics:**
   - Predictive modeling
   - Trend analysis
   - Anomaly detection

## References and Resources

**Mockaroo:**
- Website: https://mockaroo.com
- Documentation for realistic data generation
- API access for automated data creation

**Google AI Studio:**
- Website: https://aistudio.google.com/
- API key generation
- Model documentation

**SQLite:**
- Official documentation: https://www.sqlite.org/docs.html
- SQL syntax reference
- Best practices guide

**Prompt Engineering:**
- Best practices and frameworks
- Few-shot learning techniques
- Output formatting strategies

## Project Completion Checklist

- [x] Text-to-SQL system implementation
- [x] E-commerce database creation
- [x] Prompt engineering framework
- [x] Employee dataset generation (1,000 records)
- [x] Comprehensive data analysis
- [x] Professional visualizations (12+ charts)
- [x] Statistical summaries
- [x] Actionable insights
- [x] Data quality assessment
- [x] Multiple output files
- [x] Complete documentation
- [x] Google Colab compatibility

## Conclusion

This Day 15 project successfully demonstrates the power of prompt engineering for building practical NL2SQL systems and comprehensive data analysis workflows. The combination of AI-powered query generation and traditional data analysis techniques provides a complete toolkit for modern data science applications.

The assignment component showcases professional data analysis practices, from dataset creation through insight generation, with production-ready code and documentation suitable for real-world applications.

---


