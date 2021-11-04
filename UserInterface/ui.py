from Domain.inventory import creaza_inventoriu, add_undo_list_and_clear_redo, \
                             add_undo_list, add_redo_list, get_undo_list, \
                             get_data_objs, set_data
from UserInterface.handler import handle_command, multiple_commands_handle
from Logic.functionalities import undo, redo
from copy import deepcopy


def loop():
    inventory = creaza_inventoriu()
    undo_instance = {
        "index": -1,
        "cmds": []
    }
    while True:
        command = input('$').split()
        if len(command) == 0:
            continue
        if command[0] == "redo":
            redo(inventory)
            continue
        if command[0] == "undo":
            undo(inventory)
            continue
        add_undo_list(inventory)
        if '&' not in command:
            flag, inventory = handle_command(command, inventory)
        else:
            flag, inventory = multiple_commands_handle(command, inventory)
        if flag == 0 and (command[0] == "add_obj" or command[0] == "delete_obj"
           or command[0] == "modify_obj" or command[0] == "mutare_objs"
           or command[0] == "add_description" or
           command[0] == "open"):
            lst = deepcopy(get_data_objs(inventory))
            set_data(inventory, get_undo_list(inventory))
            add_undo_list_and_clear_redo(inventory)
            set_data(inventory, lst)
        else:
            get_undo_list(inventory)
        if flag == 4:
            break


def run():
    print("For commands list type help")
    print("Separator &")
    loop()


if __name__ == "__main__":
    run()
