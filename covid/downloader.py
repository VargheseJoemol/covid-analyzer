import requests
from covid.logger import get_logger

logger = get_logger()
def download_csv(url, filename):
	logger.info("Downloading csv file from url: {}".format(url))
	try:
		response = requests.get(url, stream=True)
		response.raise_for_status()
		with open(filename, "wb") as f:
			for chunk in response.iter_content(chunk_size=8192):
				f.write(chunk)
		logger.info("Downloading completed")
		return True
	except Exception as e:
		logger.error("Exception occured: {}".format(e))
		return False


