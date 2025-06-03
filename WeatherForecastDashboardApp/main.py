import streamlit as st

st.title("Weather Forecast")
location = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days for the forecast")
display_option = st.selectbox("Data to view", options=("Temperature", "Sky"))
st.subheader(f"{display_option} for the next {days} day(s) in {location}")