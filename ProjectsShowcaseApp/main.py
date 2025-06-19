import streamlit as st
import pandas
from math import ceil

SELF_DESCRIPTION = """Hi! I am Alex! 

I am passionate about anything that blinks, beeps, spins or has at least a line of code in it."""

CONTENT_DESCRIPTION = """Now the time to play around in peace with Python finally arrived! 

Below you can find the apps I have built while taking the Udemy course \"Python Mega Course: Learn Python in 60 Days, 
Build 20 Apps\". 

Some more details can be found also in the [README.md](https://github.com/alexandru-cohal/PythonApps/blob/master/README.md) file of the 
repository where I keep all these treasures :) 

Feel free to contact me if you see something interesting or if you have any improvement ideas!"""

PROJECTS_DESCRIPTION_FILEPATH = "projects_data.csv"

# Get the projects' information from the separate CSV file
projects_df = pandas.read_csv(PROJECTS_DESCRIPTION_FILEPATH, sep=",")
index_middle_projects_df = ceil(len(projects_df) / 2)

st.set_page_config(layout="wide")

# Top part of the page - Self introduction
column_introd_left, column_introd_right = st.columns(2)

with column_introd_left:
    st.image("images/myself.jpeg")

with column_introd_right:
    st.title("Alexandru Cohal")
    st.info(SELF_DESCRIPTION)

st.write(CONTENT_DESCRIPTION)

# Bottom part of the page - List of Apps
column_proj_left, column_proj_empty, column_proj_right = st.columns([1.5, 0.5, 1.5])

with column_proj_left:
    for index, row in projects_df[:index_middle_projects_df].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("../screenshots/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with column_proj_right:
    for index, row in projects_df[index_middle_projects_df:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("../screenshots/" + row["image"])
        st.write(f"[Source Code]({row['url']})")