import FreeSimpleGUI as sg
from zip_creator import make_archive

# Frontend
sg.theme("DarkGrey10")

label_select_source = sg.Text("Select files to compress:",
                              font=("Helvetica", 12, "bold"),
                              size=(19,1))
input_source = sg.Input()
button_choose_source = sg.FilesBrowse("Choose",
                                      key="source_files")

label_select_dest = sg.Text("Select destination folder:",
                            font=("Helvetica", 12, "bold"),
                            size=(19,1))
input_dest = sg.Input()
button_choose_dest = sg.FolderBrowse("Choose",
                                     key="dest_folder")

button_compress = sg.Button("Compress")
label_compress_output = sg.Text("",
                                key="compress_output",
                                font=("Helvetica", 12, "bold"))

window = sg.Window("FileZipperApp",
                   layout=[[label_select_source, input_source, button_choose_source],
                           [label_select_dest, input_dest, button_choose_dest],
                           [button_compress, label_compress_output]],
                   font=('Helvetica', 12))

# Backend
while True:
    event, values = window.read()

    filepaths = values["source_files"].split(";")
    folder = values["dest_folder"]

    match event:
        case "Compress":
            try:
                make_archive(filepaths, folder)
            except ValueError:
                window["compress_output"].update(value="Compression failed!", text_color="red")
            else:
                window["compress_output"].update(value="Compression completed!", text_color="green")

        case sg.WIN_CLOSED:
            break

window.close()