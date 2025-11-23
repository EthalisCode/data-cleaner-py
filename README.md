# data-cleaner

A simple command-line data cleaning tool written in pure Python (no external dependencies).  
It previews a CSV file, analyzes columns (missing values, unique values), and generates:

- A human-readable report (`report.txt`)
- A cleaned CSV file (`cleaned_sample.csv` by default)

This project is focused on learning Python for data work and preparing for machine learning workflows.

---

## Features

- Preview CSV:
  - Number of columns
  - Number of rows (excluding header)
  - Header row
  - First N data rows

- Column-wise analysis:
  - Count of empty values per column
  - Percentage of empty values
  - Number of unique (non-empty) values
  - Results saved into `report.txt`

- Data cleaning:
  - Automatically removes columns that have more than a configurable percentage of empty values (default: 50%)
  - Writes a cleaned CSV file (default: `cleaned_sample.csv`)
  - Appends a “Cleaning Summary” to `report.txt`

---

## Project Structure

```text
py-data-cleaner/
├── datacleaner/
│   ├── __init__.py
│   ├── __main__.py
│   └── main.py
├── sample.csv
└── README.md
