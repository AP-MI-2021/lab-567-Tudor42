from Domain.inventory import set_folder, save_data, \
                             get_data, get_path
from Logic.CRUD import add_obj, delete_obj, modify_obj, \
                       get_obj_data_str, get_obj_IDs, \
                       get_obj_data
from Logic.functionalities import mutare_obiecte, add_description, \
                                  get_max_price_per_location, \
                                  sort_invetory_by_price, \
                                  get_price_sum_per_location
from Domain.object import get_ID, get_name, get_price

"""
Each function returns 0 on success and -1 on fail
Excption sort_by_price_c delete_obj_c which returns modified inventory
"""


def cd_c(command, inventory):
    if len(command) < 2:
        print("Path isnt specified")
        return -1
    if not set_folder(inventory, command[1]):
        print(get_path(inventory))
        return 0


def save_c(command, inventory):
    if len(command) < 2:
        save_data(inventory)
        print("Saved in folder: " + get_path(inventory))
        print("File: swap.json")
    else:
        save_data(inventory, command[1])
        print("Saved in folder: " + get_path(inventory))
        if command[1][-5:] != ".json":
            command[1] += ".json"
        print("File: " + command[1])
    return 0


def open_c(command, inventory):
    if len(command) >= 2:
        get_data(command[1], inventory)
    else:
        get_data(inventory=inventory)
    return 0


def showall_c(command, inventory):
    keys = get_obj_IDs(inventory)
    for key in keys:
        print(get_obj_data_str(inventory, key))
    return 0


def add_obj_c(command, inventory):
    if len(command) == 1:
        try:
            ID = int(input("  ID: "))
        except ValueError:
            print("ID is a number")
            return -1
        name = input("  Name: ").strip()
        description = input("  Description: ").strip()
        try:
            price = int(input("  Price: "))
        except ValueError:
            print("  Price should be a number")
            return -1
        location = input("  Location: ").strip()
        flag = add_obj(inventory, ID, name, description, price, location)
        if flag == 0:
            print("Object was added successfully")
        elif flag == -2:
            print("ID duplicate")
            return -2
    elif len(command) == 6:
        try:
            ID = int(command[1])
        except ValueError:
            print("ID is a number")
            return -1
        try:
            price = int(command[4])
        except ValueError:
            print("  Price should be a number")
            return -1
        flag = add_obj(inventory, ID, command[2], command[3],
                       price, command[5])
        if flag == 0:
            print("Object was added successfully")
        elif flag == -2:
            print("ID duplicate")
            return -2
    elif len(command) > 6:
        if command[3][0] != '"':
            print("Descriptions with more than 1 word should be written "
                  "between quotation marks")
            return -1
        i = 3
        while i < len(command) and command[i][-1] != '"':
            i += 1
        if i == len(command):
            print("Closing quotation mark missing")
            return -1
        command[3] = ' '.join(command[3:i+1])
        if len(command[i+1:]) != 2:
            print("Wrong number of arguments")
            print("add_obj use:")
            print('  add_obj [ID] [name] "[description]" [price] [location]')
            return -1
        try:
            ID = int(command[1])
        except ValueError:
            print("ID is a number")
            return -1
        try:
            price = int(command[i+1])
        except ValueError:
            print("  Price should be a number")
            return -1
        flag = add_obj(inventory, ID, command[2], command[3][1:-1],
                       price, command[i+2])
        if flag == 0:
            print("Object was added successfully")
        elif flag == -2:
            print("ID duplicate")
            return -2
    else:
        print("Wrong number of arguments")
        print("add_obj use:")
        print('  add_obj [ID] [name] "[description]" [price] [location]')
        return -1
    return flag


def delete_obj_c(command, inventory):
    if len(command) < 2:
        try:
            ID = int(input("  ID: "))
        except ValueError:
            print("ID is a number")
            return -1
        delete_obj(inventory, ID)
        print(f"Object {ID} deleted")
    else:
        for i in command[1:]:
            try:
                delete_obj(inventory, int(i))
                print(f"Object {i} deleted")
            except ValueError:
                print(i, "is not a number")
    return inventory


def modify_obj_c(command, inventory):
    if len(command) < 2:
        print("ID missing")
        return -1
    str = "1. Name"
    str += "    2. Description"
    str += "    3. Price"
    str += "    4. Location\n"
    str += "Your option: "
    x = input(str)
    try:
        command[1] = int(command[1])
    except ValueError:
        print("ID should be a number")
        return -1
    if x == "1":
        option = input("Name: ")
        n = modify_obj(inventory, command[1], name=option)
    elif x == "2":
        option = input("Description: ")
        n = modify_obj(inventory, command[1], description=option)
    elif x == "3":
        try:
            option = int(input("Price: "))
        except ValueError:
            option = ""
        n = modify_obj(inventory, command[1], price=option)
    elif x == "4":
        option = input("Location: ")
        n = modify_obj(inventory, command[1], location=option)
    else:
        print("No such option")
        return -1
    if n == -2:
        print("An object with this ID doesnt exist")
    return n


def mutare_objs_c(command, inventory):
    if len(command) == 2:
        inventory = mutare_obiecte(inventory, command[1])
    elif len(command) == 3:
        inventory = mutare_obiecte(inventory, command[1], command[2])
    else:
        print("Wrong number of arguments")
        return -1
    return 0


def add_description_c(command, inventory):
    if len(command) == 1:
        try:
            n = int(input("Lower bound price: "))
        except ValueError:
            print("Lower bound must be an integer")
            return -1
        str = input("Description: ")
        inventory = add_description(inventory, n, str)
    elif len(command) >= 3:
        try:
            n = int(command[1])
        except ValueError:
            print("Lower bound must be an integer")
            return -1
        for c in command[3:]:
            command[2] += (" " + c)
        inventory = add_description(inventory, n, command[2])
    else:
        print("Wrong number of arguments")
        print("add_description use:")
        print("  add_description [lower_bound_price] [description]")
        return -1
    return 0


def max_price_per_location_c(command, inventory):
    res = get_max_price_per_location(inventory)
    for loc in res:
        print(loc + ":", res[loc])
    return 0


def sort_by_price_c(command, inventory):
    inventory = sort_invetory_by_price(inventory)
    for id in get_obj_IDs(inventory):
        obj = get_obj_data(inventory, id)
        print("ID:", get_ID(obj), " Nume:", get_name(obj),
              " Pret:", get_price(obj))
    return inventory


def sum_price_c(command, inventory):
    res = get_price_sum_per_location(inventory)
    for loc in res:
        print(loc + ":", res[loc])
    return 0


def print_menu():
    print("""  help - prints the menu
  cd [path] - change the folder for opening and saving files
  pwd - print working directory
  save [file] - saves inventory in file if no argument is given
    it get saved in swap.json
  open [file] - get inventory data from the file if no argument is
    given it gets data form swap.json
  showall - shows all objects in inventory
  add_obj [ID] [name] "[description]" [price] [location] - adds an object
  delete_obj [ID, ...] - deletes an object by its ID
  modify_obj [ID] - modifies an object by its ID
  mutare_objs [old location] [new location] - if only one param is given then
    all objects' locations will be set to this param
  add_description [lower_bound_price] [description] - concatenate a string to
    every description of objects with price bigger than a given number
  max_price_per_location - shows the biggest price of objects in every location
  sort_by_price - sorts objects by their price
  sum_price - shows sum of prices of objects grouped by their location
  exit - to terminate the console\n""")
