while True:
    userAction = input("Type add, show, edit, complete and exit: ")
    userAction = userAction.strip()

    match userAction:

        case 'add':
            toDo = input("Enter a ToDo: ") + '\n'

            with open("todos.txt", "r") as inputFile:
                toDos = inputFile.readlines()

            toDos.append(toDo)

            with open("todos.txt", "w") as outputFile:
                outputFile.writelines(toDos)

        case 'show':
            with open("todos.txt", "r") as inputFile:
                toDos = inputFile.readlines()

            for indexToDo, itemToDo in enumerate(toDos):
                itemToDo = itemToDo.strip('\n')
                print(f"{indexToDo + 1} - {itemToDo}")

        case 'edit':
            indexToDo = int(input("Index of ToDo to edit: ")) - 1
            newToDo = input("Enter new ToDo: ") + '\n'

            with open("todos.txt", "r") as inputFile:
                toDos = inputFile.readlines()

            toDos[indexToDo] = newToDo

            with open("todos.txt", "w") as outputFile:
                outputFile.writelines(toDos)

        case 'complete':
            indexToDo = int(input("Index of ToDo to complete: ")) - 1

            with open("todos.txt", "r") as inputFile:
                toDos = inputFile.readlines()

            toDos.pop(indexToDo)

            with open("todos.txt", "w") as outputFile:
                outputFile.writelines(toDos)

        case 'exit':
            break