from covid.logger import get_logger
import pandas as pd
import sqlite3

logger = get_logger()
def load_into_db(csv_file, db_file):
	try:
		logger.info("Loading CSV data from {} to SQLite dbfile {}".format(csv_file, db_file))
		data = pd.read_csv(csv_file, parse_dates=["date"])
		conn = sqlite3.connect(str(db_file))
		data.to_sql("covid_data", conn, if_exists="replace", index=False)
		conn.close()
		logger.info("Data loaded to database")
		return True
	except Exception as e:
		logger.error("Exception occured: {}".format(e))
		return False
		
