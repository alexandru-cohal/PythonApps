import os


FILEPATH_DEFAULT = "todos.txt"
if not os.path.exists(FILEPATH_DEFAULT):
    FILEPATH_DEFAULT = "ToDoListApp/todos.txt"


def getToDos(filepath=FILEPATH_DEFAULT):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, "r") as inputFileLocal:
        toDosLocal = inputFileLocal.readlines()
    return toDosLocal


def writeToDos(todosArg, filepath=FILEPATH_DEFAULT):
    """ Write the to-do items in the text file. """
    with open(filepath, "w") as outputFile:
        outputFile.writelines(todosArg)