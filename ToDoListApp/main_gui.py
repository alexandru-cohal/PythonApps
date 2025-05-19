import helper_functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a ToDo")
input_box = sg.InputText(tooltip="Enter ToDo",
                         key="todo")
add_button = sg.Button("Add")

window = sg.Window("My ToDoList App",
                   layout=[[label, input_box, add_button]],
                   font=('Helvetica', 12))

while True:
    event, value = window.read()

    match event:
        case "Add":
            todos = helper_functions.getToDos()
            todos.append(value['todo'] + '\n')
            helper_functions.writeToDos(todos)

        case sg.WIN_CLOSED:
            break

window.close()