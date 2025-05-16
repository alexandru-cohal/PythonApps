from helper_functions import getToDos, writeToDos

while True:
    userAction = input("Type add, show, edit, complete and exit: ")
    userAction = userAction.strip()

    if userAction.startswith("add"):
        toDo = userAction[4:]
        toDos = getToDos()
        toDos.append(toDo + '\n')
        writeToDos(toDos)

    elif userAction.startswith("show"):
        toDos = getToDos()
        for indexToDo, itemToDo in enumerate(toDos):
            itemToDo = itemToDo.strip('\n')
            print(f"{indexToDo + 1} - {itemToDo}")

    elif userAction.startswith("edit"):
        try:
            indexToDo = int(userAction[5:]) - 1
            newToDo = input("Enter new ToDo: ") + '\n'
            toDos = getToDos()
            toDos[indexToDo] = newToDo
            writeToDos(toDos)
        except ValueError:
            print("Command not valid")
            continue

    elif userAction.startswith("complete"):
        try:
            indexToDo = int(userAction[9:]) - 1
            toDos = getToDos()
            toDoToRemove = toDos[indexToDo]
            toDos.pop(indexToDo)
            writeToDos(toDos)
            print(f"ToDo {toDoToRemove} was removed")
        except IndexError:
            print("No item with the introduced index")
            continue

    elif userAction.startswith("exit"):
        break

    else:
        print("Command not valid")