from UserInterface.command import *


def handle_command(command, inventory):
    if command[0] == 'cd':
        flag = cd_c(command, inventory)
    elif command[0] == "pwd":
        print(get_path(inventory))
        flag = 0
    elif command[0] == "help":
        print_menu()
        flag = 0
    elif command[0] == "save":
        flag = save_c(command, inventory)
    elif command[0] == "open":
        flag = open_c(command, inventory)
    elif command[0] == "showall":
        flag = showall_c(command, inventory)
    elif command[0] == "add_obj":
        flag = add_obj_c(command, inventory)
    elif command[0] == "delete_obj":
        inventory = delete_obj_c(command, inventory)
        flag = 0
    elif command[0] == "modify_obj":
        flag = modify_obj_c(command, inventory)
    elif command[0] == "mutare_objs":
        flag = mutare_objs_c(command, inventory)
    elif command[0] == "add_description":
        flag = add_description_c(command, inventory)
    elif command[0] == "max_price_per_location":
        flag = max_price_per_location_c(command, inventory)
    elif command[0] == "sort_by_price":
        sort_by_price_c(command, inventory)
        flag = 0
    elif command[0] == "sum_price":
        flag = sum_price_c(command, inventory)
    elif command[0] == "exit":
        flag = 4
    else:
        print("Command not found")
        flag = -1
    return flag, inventory


def multiple_commands_handle(command, inventory):
    i = 0
    sub_command = []
    while i < len(command):
        if command[i] != "&":
            sub_command.append(command[i])
        else:
            if len(sub_command) > 0:
                n, inventory = handle_command(sub_command, inventory)
                if n == 4:
                    return n, inventory
                if n != 0 and n != -2:
                    print(f"Error with command {sub_command[0]}")
                    break
                elif n == -2:
                    break
            sub_command = []
        i += 1
    if n == 0:
        if len(sub_command) > 0:
            n, inventory = handle_command(sub_command, inventory)
            if n == 4:
                return n, inventory
            if n != 0 and n != -2:
                print(f"Error with command {sub_command[0]}")
    return n, inventory
