import streamlit as st
import helper_functions

todos = helper_functions.getToDos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    helper_functions.writeToDos(todos)


st.title("My ToDoList App")
st.subheader("This is my ToDoList App")
st.write("This App increases your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,
                           key=todo)
    if checkbox:
        todos.pop(index)
        helper_functions.writeToDos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a ToDo:",
              placeholder="Add a new ToDo",
              on_change=add_todo,
              key="new_todo")