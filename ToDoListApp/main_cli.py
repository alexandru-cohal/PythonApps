import helper_functions
import time

DESCRIPTION_COMMANDS = ("\n Possible commands: \n"
                        "\t show \n"
                        "\t add + ToDo \n"
                        "\t edit + index of ToDo \n"
                        "\t complete + index of ToDo \n"
                        "\t exit")

print("Current date and time: ", time.strftime("%d %b %Y, %H:%M:%S"))

while True:
    # Get user command
    print(DESCRIPTION_COMMANDS)
    user_action = input("Command: ")
    user_action = user_action.strip()

    # React based on the user command
    if user_action.startswith("add"):
        todo = user_action[4:]
        list_todo = helper_functions.getToDos()
        list_todo.append(todo + '\n')
        helper_functions.writeToDos(list_todo)

    elif user_action.startswith("show"):
        list_todo = helper_functions.getToDos()
        for index_todo, todo in enumerate(list_todo):
            todo = todo.strip('\n')
            print(f"{index_todo + 1} - {todo}")

    elif user_action.startswith("edit"):
        try:
            index_todo = int(user_action[5:]) - 1
            new_todo = input("Enter new ToDo: ") + '\n'
            list_todo = helper_functions.getToDos()
            list_todo[index_todo] = new_todo
            helper_functions.writeToDos(list_todo)
        except ValueError:
            print("Command not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            index_todo = int(user_action[9:]) - 1
            list_todo = helper_functions.getToDos()
            remove_todo = list_todo[index_todo]
            list_todo.pop(index_todo)
            helper_functions.writeToDos(list_todo)
            print(f"ToDo {remove_todo} was removed")
        except IndexError:
            print("No item with the introduced index")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command not valid")