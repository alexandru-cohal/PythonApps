import streamlit as st
import sqlite3
import plotly.express as px


DATABASE_FILEPATH = "temp_data.db"

# Get the date from the database
connection_db = sqlite3.connect(DATABASE_FILEPATH)
cursor_db = connection_db.cursor()
cursor_db.execute("SELECT date,temperature FROM temps")
entries_db = cursor_db.fetchall()
date_data = [entry[0] for entry in entries_db]
temp_data = [entry[1] for entry in entries_db]

# Display the data
st.title("Average World Temperature")

figure = px.line(x=date_data,
                 y=temp_data,
                 labels={"x": "Date", "y":"Temperature"})
st.plotly_chart(figure)