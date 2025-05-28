from dotenv import load_dotenv
load_dotenv("../.env")

import requests
import os
import streamlit as st
from datetime import datetime

DAILY_IMAGE_PATH = "daily_image.jpg"

# Create the request for getting the daily image information
request_url = ("https://api.nasa.gov/planetary/apod?"
               f"api_key={os.getenv("NASA_API_KEY")}")

# Send the request and get the response
response = requests.get(request_url)
response_content = response.json()

# Parse the response and get the image's explanation and url
image_title = response_content["title"]
image_explanation = response_content["explanation"]
image_url = response_content["url"]

# Get and save the image
response = requests.get(image_url)

with open(DAILY_IMAGE_PATH, "wb") as file_image:
    file_image.write(response.content)

# Display the title, image and explanation
st.title(f"Daily Astronomy Photo - {datetime.today().strftime("%d.%m.%Y")}")
st.header(image_title)
st.image("daily_image.jpg")
st.write(image_explanation)