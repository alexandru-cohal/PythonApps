import streamlit as st

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