from covid.downloader import download_csv
import os

def test_downloader(tmp_path):
	url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
	csv_file = tmp_path / "test.csv"
	assert download_csv(url, csv_file)
	assert os.path.exists(csv_file)
	assert os.path.getsize(csv_file) > 1000
	
