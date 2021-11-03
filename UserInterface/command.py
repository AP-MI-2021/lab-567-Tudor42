from Domain.inventory import creaza_inventoriu, set_folder, save_data, \
                             get_data, get_path
from Logic.CRUD import add_obj, delete_obj, modify_obj, \
                       get_obj_data_str, get_obj_IDs, \
                       get_obj_data
from Logic.functionalities import mutare_obiecte, add_description, \
                                  get_max_price_per_location, \
                                  sort_invetory_by_price, \
                                  get_price_sum_per_location
from Domain.object import get_ID, get_name, get_price


def cd_c(command, inventory):
    if len(command) < 2:
        print("Path isnt specified")
    if not set_folder(inventory, command[1]):
        print(get_path(inventory))


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


def open_c(command, inventory):
    if len(command) >= 2:
        get_data(command[1], inventory)
    else:
        get_data(inventory=inventory)


def showall_c(command, inventory):
    keys = get_obj_IDs(inventory)
    for key in keys:
        print(get_obj_data_str(inventory, key))


def add_obj_c(command, inventory):
    try:
        ID = int(input("  ID: "))
    except ValueError:
        print("ID is a number")
        return
    name = input("  Name: ").strip()
    description = input("  Description: ").strip()
    try:
        price = int(input("  Price: "))
    except ValueError:
        print("  Price should be a number")
        return
    location = input("  Location: ").strip()
    flag = add_obj(inventory, ID, name, description, price, location)
    if flag == 0:
        print("Object was added successfully")
    elif flag == -2:
        print("ID dublicate")


def delete_obj_c(command, inventory):
    if len(command) < 2:
        try:
            ID = int(input("  ID: "))
        except ValueError:
            print("ID is a number")
            return
        delete_obj(inventory, ID)
    else:
        for i in command[1:]:
            try:
                delete_obj(inventory, int(i))
            except ValueError:
                print(i, " is not a number")


def modify_obj_c(command, inventory):
    if len(command) < 2:
        print("ID missing")
        return
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
        return
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
    if n == -2:
        print("An object with this ID doesnt exist")


def mutare_objs_c(command, inventory):
    if len(command) == 2:
        inventory = mutare_obiecte(inventory, command[1])
    elif len(command) == 3:
        inventory = mutare_obiecte(inventory, command[1], command[2])
    else:
        print("Wrong number of arguments")


def add_description_c(command, inventory):
    try:
        n = int(input("Lower bound price: "))
    except ValueError:
        print("Lower bound must be an integer")
        return
    str = input("Description: ")
    inventory = add_description(inventory, n, str)


def max_price_per_location_c(command, inventory):
    res = get_max_price_per_location(inventory)
    for loc in res:
        print(loc + ":", res[loc])


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
