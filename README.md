# Data Cleaner

##  Usage

From the project root:

```bash
python -m datacleaner sample.csv
```

This command will:

- Preview `sample.csv` in the terminal  
- Generate `report.txt` with a full column-wise analysis  
- Generate `cleaned_sample.csv` containing the cleaned dataset  

You can adjust the cleaning threshold or the output filename by modifying the `clean_csv` call inside `main.py`.

---

##  Requirements

- **Python 3.10+**
- No external dependencies  
  (Uses only Python’s standard library: `csv`, `sys`, `pathlib`)

---

##  Motivation

This project was created as an introductory portfolio project to develop foundational skills in:

- File I/O operations  
- Working with CSV data  
- Implementing basic data analysis logic  
- Building command-line tools  
- Preparing for data-oriented workflows in **Data Science** and **Machine Learning**

---

- ## Project Structure

```text
data-cleaner/
├── datacleaner/
│   ├── __init__.py
│   ├── __main__.py
│   └── main.py
├── sample.csv
└── README.md
