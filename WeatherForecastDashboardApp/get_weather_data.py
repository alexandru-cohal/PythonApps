from dotenv import load_dotenv
load_dotenv("../.env")

import requests
import os


def get_weather_data(location, days, display_option):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={os.getenv("OPENWEATHERMAP_API_KEY")}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_weather_data("Barcelona", 2, "Temperature"))