# Covid Analyzer

A Python-based data pipeline and analysis tool that downloads, stores, and analyzes COVID-19 data from trusted sources.

---

## Features

-  Download real-time COVID data (CSV format)
-  Load data into SQLite for structured querying
-  Run SQL-based analytics (top affected countries, case trends)
-  Unit tests for data loading and querying
-  Built-in logging and test automation via GitHub Actions

---

## Project Structure

```
covid-analyzer/
├── covid/                # Source modules (downloader, loader, analyzer)
├── tests/                # Pytest unit tests
├── data/                 # Downloaded CSV files
├── covid.db              # SQLite database (created automatically)
├── covid.log             # Log file with debug/info entries
├── run.py                # Entry script to execute the full pipeline
├── requirements.txt      # Python dependencies
├── pytest.ini            # Pytest config
└── README.md             # Project documentation
```

---

## How to Run

### 1. Clone the repo and create a virtual environment:

```bash
git clone https://github.com/your-username/covid-analyzer.git
cd covid-analyzer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the full pipeline:

```bash
python run.py
```

### 3. Run tests:

```bash
pytest
```

---

## Sample SQL Queries

```sql
-- Top 5 countries with most cases in last 7 days
SELECT location, SUM(new_cases) AS total
FROM covid_data
WHERE date >= DATE('now', '-7 day')
GROUP BY location
ORDER BY total DESC
LIMIT 5;
```

---

## Tech Stack

- Python 3.10+
- `requests`, `pandas`, `sqlite3`
- Pytest for testing
- GitHub Actions for CI

---


