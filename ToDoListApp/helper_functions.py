def getToDos(filepath="todos.txt"):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, "r") as inputFileLocal:
        toDosLocal = inputFileLocal.readlines()
    return toDosLocal


def writeToDos(todosArg, filepath="todos.txt"):
    """ Write the to-do items in the text file. """
    with open(filepath, "w") as outputFile:
        outputFile.writelines(todosArg)