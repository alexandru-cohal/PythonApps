while True:
    userAction = input("Type add, show, edit, complete and exit: ")
    userAction = userAction.strip()

    if userAction.startswith("add"):
        toDo = userAction[4:]

        with open("todos.txt", "r") as inputFile:
            toDos = inputFile.readlines()

        toDos.append(toDo + '\n')

        with open("todos.txt", "w") as outputFile:
            outputFile.writelines(toDos)

    elif userAction.startswith("show"):
        with open("todos.txt", "r") as inputFile:
            toDos = inputFile.readlines()

        for indexToDo, itemToDo in enumerate(toDos):
            itemToDo = itemToDo.strip('\n')
            print(f"{indexToDo + 1} - {itemToDo}")

    elif userAction.startswith("edit"):
        indexToDo = int(userAction[5:]) - 1
        newToDo = input("Enter new ToDo: ") + '\n'

        with open("todos.txt", "r") as inputFile:
            toDos = inputFile.readlines()

        toDos[indexToDo] = newToDo

        with open("todos.txt", "w") as outputFile:
            outputFile.writelines(toDos)

    elif userAction.startswith("complete"):
        indexToDo = int(userAction[9:]) - 1

        with open("todos.txt", "r") as inputFile:
            toDos = inputFile.readlines()

        toDoToRemove = toDos[indexToDo]
        toDos.pop(indexToDo)

        with open("todos.txt", "w") as outputFile:
            outputFile.writelines(toDos)

        print(f"ToDo {toDoToRemove} was removed")

    elif userAction.startswith("exit"):
        break

    else:
        print("Command not valid")