
# 1. Project Overview and Learning Objectives

## 1.1 Overview

This project requires students to convert user data from a CSV file into a TinyDB database. Students will write a Python script to read the CSV file, process the data, and store it in TinyDB. The project aims to teach students about structured data processing, file I/O operations, and database interactions using TinyDB, a lightweight NoSQL database.

- Read a CSV file with user data.
- Map CSV fields to a NoSQL database (TinyDB).
- Validate and ensure data integrity during migration.

Real-World Scenario: Organizations often need to migrate data from flat files (e.g., CSV) to databases for efficient querying. This project mimics that process using lightweight tools.

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Convert CSV to Database
```python
from csv_to_db import read_csv, insert_into_db

# Read CSV file
data = read_csv('user_data.csv')

# Insert into database
insert_into_db(data, 'users.json')
```

### 2. Query the Database
```python
from csv_to_db import query_db

# Get all records
all_users = query_db('users.json')

# Filter by specific field
male_users = query_db('users.json', 'gender', 'Male')
```

### Command Line Usage
```bash
python csv_to_db.py user_data.csv --db custom_db.json
```

## Example CSV Format (`user_data.csv`)
```csv
id,first_name,last_name,email,gender,job
1,John,Doe,john@example.com,Male,Engineer
2,Jane,Smith,jane@example.com,Female,Designer
```

## Testing
Run the test suite with:
```bash
pytest test/test_csv_to_db.py -v
```

Key test cases include:
- File not found handling
- Empty CSV files
- Data insertion verification
- Query filtering accuracy

## Requirements

- Dependencies listed in `requirements.txt`

## Common Operations

### Query from Command Line
```bash
python -c "from csv_to_db import query_db; print(query_db('users.json', 'job', 'Engineer'))"
```

### Create New Database
```python
from csv_to_db import insert_into_db
insert_into_db([{'id': '100', 'name': 'Test User'}], 'new_db.json')
```

## Notes
- Database files are stored in JSON format
- All fields are stored as strings
- Case-sensitive queries
- Requires consistent CSV header formatting

```

This README provides:
1. Clear installation instructions
2. API usage examples for all functions
3. Testing guidance
4. Common operation recipes
5. File format expectations
6. Environment requirements
7. Both programmatic and CLI usage examples