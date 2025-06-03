from dotenv import load_dotenv
load_dotenv("../.env")

import requests
import os
from datetime import datetime

NUM_ENTRIES_PER_DAY = 8


def get_weather_data(location, days, display_option):
    request_url = (f"http://api.openweathermap.org/data/2.5/forecast?"
           f"q={location}&"
           f"units=metric&"
           f"appid={os.getenv("OPENWEATHERMAP_API_KEY")}")
    response = requests.get(request_url)
    response_raw = response.json()

    response_filtered = response_raw["list"][:NUM_ENTRIES_PER_DAY*days]

    timestamps = [datetime.fromtimestamp(response_entry["dt"]) for response_entry in response_filtered]
    if display_option == "Temperature":
        weather_data = [response_entry["main"]["temp"] for response_entry in response_filtered]
    else:
        weather_data = [response_entry["weather"][0]["main"] for response_entry in response_filtered]

    return timestamps, weather_data


if __name__ == "__main__":
    print(get_weather_data("Barcelona", 2, "Sky"))