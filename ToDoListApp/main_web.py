import streamlit as st
import helper_functions

todos = helper_functions.getToDos()

def add_todo():
    """ Callback function which adds the written To-Do to the list """
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    helper_functions.writeToDos(todos)

st.title("ToDoList App")
st.write("**Current ToDos:**")
st.write("")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        helper_functions.writeToDos(todos)
        del st.session_state[todo]
        st.rerun()
st.write("")
st.write("**New ToDo:**")
st.text_input(label="New ToDo",
              label_visibility="hidden",
              placeholder="Text of the new ToDo",
              on_change=add_todo,
              key="new_todo")