from dotenv import load_dotenv
load_dotenv("../.env")

import requests
import selectorlib
from send_email import send_email
import time
import sqlite3


URL_TO_SCRAPE = "https://programmer100.pythonanywhere.com/tours/"
HEADERS_SCRAPING = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
EVENTS_FILEPATH = "events_data.txt"
DATABASE_FILEPATH = "events_data.db"
WAITING_PERIOD_SEC = 5


connection = sqlite3.connect(DATABASE_FILEPATH)


def scrape_url(url):
    """ Scrape the page source from the given URL """
    response = requests.get(url, headers=HEADERS_SCRAPING)
    source = response.text
    return source


def extract_event_information_from_scraped_data(source):
    """ Extract the desired data """
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def store_event_in_db(extracted):
    """ Store and event into the database """
    row_elements = extracted.split(",")
    row_elements = [item.strip() for item in row_elements]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row_elements)
    connection.commit()


def read_events_from_db(extracted):
    """ Select from the database the entries which have the band, city and date matching,
     in order to check if the event was already stored"""
    row_elements = extracted.split(",")
    row_elements = [item.strip() for item in row_elements]
    band, city, date = row_elements
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    return rows


if __name__ == "__main__":
    while True:
        scraped_data = scrape_url(URL_TO_SCRAPE)
        extracted_data = extract_event_information_from_scraped_data(scraped_data)

        if extracted_data != "No upcoming tours":
            stored_events = read_events_from_db(extracted_data)
            if not stored_events:
                store_event_in_db(extracted_data)
                message = f"""\
Subject: A new event was found! 

{extracted_data}
"""
                send_email(message)

        time.sleep(WAITING_PERIOD_SEC)