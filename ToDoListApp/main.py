def getToDos(filepath):
    with open(filepath, "r") as inputFileLocal:
        toDosLocal = inputFileLocal.readlines()
    return toDosLocal


def writeToDos(filepath, todosArg):
    with open(filepath, "w") as outputFile:
        outputFile.writelines(todosArg)


while True:
    userAction = input("Type add, show, edit, complete and exit: ")
    userAction = userAction.strip()

    if userAction.startswith("add"):
        toDo = userAction[4:]
        toDos = getToDos("todos.txt")
        toDos.append(toDo + '\n')
        writeToDos("todos.txt", toDos)

    elif userAction.startswith("show"):
        toDos = getToDos("todos.txt")
        for indexToDo, itemToDo in enumerate(toDos):
            itemToDo = itemToDo.strip('\n')
            print(f"{indexToDo + 1} - {itemToDo}")

    elif userAction.startswith("edit"):
        try:
            indexToDo = int(userAction[5:]) - 1
            newToDo = input("Enter new ToDo: ") + '\n'
            toDos = getToDos("todos.txt")
            toDos[indexToDo] = newToDo
            writeToDos("todos.txt", toDos)
        except ValueError:
            print("Command not valid")
            continue

    elif userAction.startswith("complete"):
        try:
            indexToDo = int(userAction[9:]) - 1
            toDos = getToDos("todos.txt")
            toDoToRemove = toDos[indexToDo]
            toDos.pop(indexToDo)
            writeToDos("todos.txt", toDos)
            print(f"ToDo {toDoToRemove} was removed")
        except IndexError:
            print("No item with the introduced index")
            continue

    elif userAction.startswith("exit"):
        break

    else:
        print("Command not valid")