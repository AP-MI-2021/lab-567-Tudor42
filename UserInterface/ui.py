from Domain.inventory import creaza_inventoriu, add_undo_list_and_clear_redo, \
                             get_data_objs, set_data
from UserInterface.handler import handle_command, multiple_commands_handle
from Logic.functionalities import undo, redo
from copy import deepcopy


def loop():
    inventory = creaza_inventoriu()
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
        previous_inv_data = deepcopy(get_data_objs(inventory))  # Saves
        # inventory data before executing the command
        if '&' not in command:
            flag, inventory = handle_command(command, inventory)
        else:
            flag, inventory = multiple_commands_handle(command, inventory)
        act_inv_data = get_data_objs(inventory)
        if act_inv_data != previous_inv_data:  # If data before and after the
            # execution of the command is different then we change undo and
            # redo list
            lst = deepcopy(act_inv_data)
            set_data(inventory, previous_inv_data)
            add_undo_list_and_clear_redo(inventory)
            # add_undo_list_... adds the data of the inventory
            # into the list, so before the function call, inventory's
            # data should be changed to the previous data
            set_data(inventory, lst)
            # after this the inventory's data is set back to normal
        if flag == 4:
            break


def run():
    print("For commands list type help")
    print("Separator &")
    loop()


if __name__ == "__main__":
    run()
