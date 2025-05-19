import helper_functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a ToDo")
input_box = sg.InputText(tooltip="Enter ToDo",
                         key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=helper_functions.getToDos(),
                      key="todos_list",
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("My ToDoList App",
                   layout=[[label, input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 12))

while True:
    event, value = window.read()

    match event:
        case "Add":
            todos = helper_functions.getToDos()
            todos.append(value['todo'] + '\n')
            helper_functions.writeToDos(todos)
            window['todos_list'].update(values=todos)

        case "Edit":
            todo_to_edit = value["todos_list"][0]
            new_todo = value["todo"] + '\n'
            todos = helper_functions.getToDos()
            todo_to_edit_index = todos.index(todo_to_edit)
            todos[todo_to_edit_index] = new_todo
            helper_functions.writeToDos(todos)
            window['todos_list'].update(values=todos)

        case 'todos_list':
            window['todo'].update(value=value['todos_list'][0])

        case sg.WIN_CLOSED:
            break

window.close()