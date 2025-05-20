import streamlit as st
import helper_functions

todos = helper_functions.getToDos()

st.title("My ToDoList App")
st.subheader("This is my ToDoList App")
st.write("This App increases your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a ToDo:",
              placeholder="Add a new ToDo")