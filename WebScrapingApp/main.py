import time

from dotenv import load_dotenv
load_dotenv("../.env")

import requests
import selectorlib
from send_email import send_email


URL_TO_SCRAPE = "https://programmer100.pythonanywhere.com/tours/"
HEADERS_SCRAPING = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
EVENTS_FILEPATH = "events_data.txt"
WAITING_PERIOD_SEC = 60


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


def store_event_in_file(extracted):
    """ Store a new event in the events file """
    with open(EVENTS_FILEPATH, "a") as file:
        file.write(extracted + "\n")


def read_events_from_file():
    """ Read the events from the events file """
    with open(EVENTS_FILEPATH, "r") as file:
        return file.read()


if __name__ == "__main__":
    while True:
        scraped_data = scrape_url(URL_TO_SCRAPE)
        extracted_data = extract_event_information_from_scraped_data(scraped_data)

        stored_events = read_events_from_file()
        if extracted_data != "No upcoming tours":
            if extracted_data not in stored_events:
                store_event_in_file(extracted_data)
                message = f"""\
Subject: A new event was found! 

{extracted_data}
"""
                send_email(message)

        time.sleep(WAITING_PERIOD_SEC)