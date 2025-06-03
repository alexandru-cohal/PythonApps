import streamlit as st
import plotly.express as px

st.title("Weather Forecast")
location = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days for the forecast")
display_option = st.selectbox("Data to view", options=("Temperature", "Sky"))
st.subheader(f"{display_option} for the next {days} day(s) in {location}")


def get_weather_data(days):
    dates = ["2022-10-25", "2022-10-26", "2022-10-27"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


dates, temperatures = get_weather_data(days)

figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)