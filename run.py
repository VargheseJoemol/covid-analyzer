from covid.downloader import download_csv
from covid.loader import load_into_db
from covid.analyzer import query_top_countries
from covid.logger import get_logger
import os

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

csv_file = os.path.join(DATA_DIR, "owid.csv")

logger = get_logger()

def main():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    db_file = "covid.db"

    download_csv(url, csv_file)
    load_into_db(csv_file, db_file)
    result = query_top_countries(db_file, days=1500)
    logger.info(result)

if __name__ == "__main__":
    main()

