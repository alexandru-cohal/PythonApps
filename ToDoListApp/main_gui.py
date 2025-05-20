import helper_functions
import FreeSimpleGUI as sg
import time
import os

GUI_READ_PERIOD_MS = 500

# Create empty "todos.txt" file if not already existent
if not os.path.exists(helper_functions.FILEPATH_DEFAULT):
    with open(helper_functions.FILEPATH_DEFAULT, "w") as file:
        pass

# Frontend
sg.theme("DarkGrey10")

label_time = sg.Text("Current Date and Time:",
                     font=("Helvetica", 12, "bold"))
label_current_time = sg.Text("", key="time")
label_new_todo = sg.Text("New ToDo:",
                         font=("Helvetica", 12, "bold"))
input_box = sg.InputText(tooltip="Enter ToDo",
                         key="todo",
                         size=(47,1))
add_button = sg.Button("Add",
                       size=(10,1))
label_current_todo = sg.Text("Current ToDos:",
                             font=("Helvetica", 12, "bold"))
list_box = sg.Listbox(values=helper_functions.getToDos(),
                      key="todos_list",
                      enable_events=True,
                      size=(45,10))
edit_button = sg.Button("Edit",
                        size=(10,1))
complete_button = sg.Button("Complete",
                            size=(10,1))
column_button = sg.Column([[edit_button], [complete_button]])
exit_button = sg.Button("Exit",
                        size=(10,1))
window = sg.Window("ToDoList App",
                   layout=[[label_time],
                           [label_current_time],
                           [label_new_todo],
                           [input_box, add_button],
                           [label_current_todo],
                           [list_box, column_button],
                           [exit_button]],
                   font=('Helvetica', 12))

# Backend
while True:
    event, value = window.read(timeout=GUI_READ_PERIOD_MS)

    window["time"].update(value=time.strftime("%d %b %Y, %H:%M:%S"))

    match event:
        case "Add":
            todos = helper_functions.getToDos()
            todos.append(value['todo'] + '\n')
            helper_functions.writeToDos(todos)
            window['todos_list'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = value["todos_list"][0]
                new_todo = value["todo"] + '\n'
                todos = helper_functions.getToDos()
                todo_to_edit_index = todos.index(todo_to_edit)
                todos[todo_to_edit_index] = new_todo
                helper_functions.writeToDos(todos)
                window['todos_list'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 12))

        case "Complete":
            try:
                todo_to_complete = value["todos_list"][0]
                todos = helper_functions.getToDos()
                todos.remove(todo_to_complete)
                helper_functions.writeToDos(todos)
                window['todos_list'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 12))

        case "todos_list":
            window['todo'].update(value=value['todos_list'][0])

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()