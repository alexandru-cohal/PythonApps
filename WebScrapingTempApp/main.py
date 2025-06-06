import requests
import selectorlib
from datetime import datetime
import sqlite3
import time


URL_TO_SCRAPE = "https://programmer100.pythonanywhere.com/"
EXTRACTOR_FILEPATH = "extractor.yaml"
DATABASE_FILEPATH = "temp_data.db"
EXECUTION_PERIOD_SEC = 2


def scrape_url(url):
    """ Scrape the webpage using the given url """
    response = requests.get(url)
    return response.text


def extract_temp_data_from_scraped_data(scraped_data):
    """ Extract the temperature data from the scraped data """
    extractor = selectorlib.Extractor.from_yaml_file(EXTRACTOR_FILEPATH)
    value = extractor.extract(scraped_data)["temperature"]
    return value


if __name__ == "__main__":
    connection_db = sqlite3.connect(DATABASE_FILEPATH)

    while True:
        # Get the data (i.e. current time and current temperature)
        time_current = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
        scraped_data = scrape_url(URL_TO_SCRAPE)
        temp_current = extract_temp_data_from_scraped_data(scraped_data)

        # Add the data to the database
        cursor_db = connection_db.cursor()
        cursor_db.execute("INSERT INTO temps VALUES (?,?)", (time_current, temp_current))
        connection_db.commit()

        time.sleep(EXECUTION_PERIOD_SEC)