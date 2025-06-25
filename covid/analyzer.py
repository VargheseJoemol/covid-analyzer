import pandas as pd
from covid.logger import get_logger
import sqlite3

logger = get_logger()

def query_top_countries(db_file, days=7):
	try:
		logger.info("Retrieving top countries with highest new covid cases for last {} day".format(days))
		conn = sqlite3.connect(str(db_file))
		query = f"""
			SELECT location, SUM(new_cases) as total_new_cases
			FROM covid_data
			WHERE date >= DATE('now', '-{days} day')
			GROUP BY location
			ORDER BY total_new_cases DESC
			LIMIT 10;
			"""
		df = pd.read_sql_query(query, conn)
		conn.close()
		logger.info("Result: {}".format(df))
		return df
	except Exception as e:
		logger.error("Exception occurred: {}".format(e))
		return None
			
