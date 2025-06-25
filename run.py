from covid.downloader import download_csv
from covid.loader import load_into_db
from covid.analyzer import query_top_countries
from covid.logger import get_logger

logger = get_logger()

def main():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    csv_file = "data/owid.csv"
    db_file = "covid.db"

    download_csv(url, csv_file)
    load_into_db(csv_file, db_file)
    result = query_top_countries(db_file, days=1500)
    logger.info(result)

if __name__ == "__main__":
    main()

