import streamlit as st
import plotly.express as px
from get_weather_data import get_weather_data

SKY_IMAGES_PATHS = {"Clear":    "images_sky/clear.png",
                    "Clouds":   "images_sky/cloud.png",
                    "Rain":     "images_sky/rain.png",
                    "Snow":     "images_sky/snow.png"}

# Set the GUI and get the needed information
st.title("Weather Forecast")
location = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days for the forecast")
display_option = st.selectbox("Data to view", options=("Temperature", "Sky"))
st.subheader(f"{display_option} for the next {days} day(s) in {location}")

# Get the desired temperature / sky data
if location:
    timestamps, weather_data = get_weather_data(location, days, display_option)

    if display_option == "Temperature":
        # Add the temperature plot
        figure = px.line(x=timestamps, y=weather_data, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)
    else:
        # Add the sky images
        sky_images_paths = [SKY_IMAGES_PATHS[sky_type] for sky_type in weather_data]
        st.image(sky_images_paths, width=150)