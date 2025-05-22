import streamlit as st
import pandas

st.set_page_config(layout="wide")

column1, column2 = st.columns(2)

with column1:
    st.image("images/myself.png")

with column2:
    st.title("Alexandru Cohal")
    self_description = """Hi! I am Alex!"""
    st.info(self_description)

content = """Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content)

projects_df = pandas.read_csv("projects_data.csv", sep=";")

column3, column_empty, column4 = st.columns([1.5, 0.5, 1.5])

with column3:
    for index, row in projects_df[:2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("../screenshots/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with column4:
    for index, row in projects_df[2:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("../screenshots/" + row["image"])
        st.write(f"[Source Code]({row['url']})")