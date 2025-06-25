from covid.loader import load_into_db
from covid.analyzer import query_top_countries
import pandas as pd
import sqlite3

def test_query_top_countries(tmp_path):
    db = tmp_path / "test.db"
    df = pd.DataFrame({
        "location": ["USA", "USA", "India", "India"],
        "date": ["2024-01-01", "2024-01-02", "2024-01-01", "2024-01-02"],
        "new_cases": [100, 150, 200, 50]
    })
    df.to_csv(tmp_path / "sample.csv", index=False)
    load_into_db(tmp_path / "sample.csv", db)
    
    result = query_top_countries(db, days=15000)
    print(result)
    assert not result.empty
    assert "USA" in result["location"].values
    assert result["total_new_cases"].sum() == 500

