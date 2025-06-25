from covid.loader import load_into_db
import sqlite3
import pandas as pd

def test_load_into_db(tmp_path):
    db = tmp_path / "test.db"
    csv = tmp_path / "sample.csv"
    # Create small sample CSV
    df = pd.DataFrame({
        "location": ["A", "B"],
        "date": ["2023-01-01", "2023-01-02"],
        "new_cases": [10, 20]
    })
    df.to_csv(csv, index=False)
    
    load_into_db(csv, db)
    conn = sqlite3.connect(str(db))
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM covid_data")
    count = cur.fetchone()[0]
    conn.close()
    
    assert count == 2

