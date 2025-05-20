import helper_functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")

label_time = sg.Text("", key="time")

label = sg.Text("Type in a ToDo")
input_box = sg.InputText(tooltip="Enter ToDo",
                         key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=helper_functions.getToDos(),
                      key="todos_list",
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window("My ToDoList App",
                   layout=[[label_time],
                           [label, input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 12))

while True:
    event, value = window.read(timeout=500)

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