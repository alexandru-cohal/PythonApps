import helper_functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a ToDo")
input_box = sg.InputText(tooltip="Enter ToDo")
add_button = sg.Button("Add")
window = sg.Window("My ToDoList App", layout=[[label, input_box, add_button]])

window.read()
window.close()