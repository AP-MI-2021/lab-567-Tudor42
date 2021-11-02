from Domain.inventory import creaza_inventoriu, set_folder, save_data, \
                             get_data, get_path
from Logic.CRUD import add_obj, delete_obj, modify_obj, \
                       get_obj_data_str, get_obj_IDs, \
                       get_obj_data
from Logic.functionalities import mutare_obiecte, add_description, \
                                  get_max_price_per_location, \
                                  sort_invetory_by_price
from Domain.object import get_ID, get_name, get_price


def print_menu():
    print("""  help - prints the menu
  cd [path] - change the folder for opening and saving files
  pwd - print working directory
  save [file] - saves inventory in file if no argument is given
    it get saved in swap.json
  open [file] - get inventory data from the file if no argument is
    given it gets data form swap.json
  showall - shows all objects in inventory
  add_obj - adds an object
  delete_obj [ID] - deletes an object by its ID
  modify_obj [ID] - modifies an object by its ID
  mutare_objs [old location] [new location] - if only one param is given then
    all objects' locations will be set to this param
  add_description - concatenate a string to every description of objects
    with price bigger than a given number
  max_price_per_location - shows the biggest price of objects in every location
  sort_by_price - sorts objects by their price
  exit - to terminate the console\n""")


def loop():
    inventory = creaza_inventoriu()
    while True:
        command = input('$').split()
        if len(command) == 0:
            continue
        if command[0] == 'cd':
            if len(command) < 2:
                print("Path isnt specified")
                continue
            if not set_folder(inventory, command[1]):
                print(get_path(inventory))
        elif command[0] == "pwd":
            print(get_path(inventory))
        elif command[0] == "help":
            print_menu()
        elif command[0] == "save":
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
        elif command[0] == "open":
            if len(command) >= 2:
                get_data(command[1], inventory)
            else:
                get_data(inventory=inventory)
        elif command[0] == "showall":
            keys = get_obj_IDs(inventory)
            for key in keys:
                print(get_obj_data_str(inventory, key))
        elif command[0] == "add_obj":
            try:
                ID = int(input("  ID: "))
            except ValueError:
                print("ID is a number")
                continue
            name = input("  Name: ").strip()
            description = input("  Description: ").strip()
            try:
                price = int(input("  Price: "))
            except ValueError:
                print("  Price should be a number")
                continue
            location = input("  Location: ").strip()
            flag = add_obj(inventory, ID, name, description, price, location)
            if flag == 0:
                print("Object was added successfully")
            elif flag == -2:
                print("ID dublicate")
        elif command[0] == "delete_obj":
            if len(command) < 2:
                try:
                    ID = int(input("  ID: "))
                except ValueError:
                    print("ID is a number")
                    continue
                delete_obj(inventory, ID)
            else:
                for i in command[1:]:
                    try:
                        delete_obj(inventory, int(i))
                    except ValueError:
                        print(i, " is not a number")
        elif command[0] == "modify_obj":
            if len(command) < 2:
                print("ID missing")
                continue
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
                continue
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
        elif command[0] == "mutare_objs":
            if len(command) == 2:
                inventory = mutare_obiecte(inventory, command[1])
            elif len(command) == 3:
                inventory = mutare_obiecte(inventory, command[1], command[2])
            else:
                print("Wrong number of arguments")
        elif command[0] == "add_description":
            try:
                n = int(input("Lower bound price: "))
            except ValueError:
                print("Lower bound must be an integer")
                continue
            str = input("Description: ")
            inventory = add_description(inventory, n, str)
        elif command[0] == "max_price_per_location":
            res = get_max_price_per_location(inventory)
            for loc in res:
                print(loc + ":", res[loc])
        elif command[0] == "sort_by_price":
            inventory = sort_invetory_by_price(inventory)
            for id in get_obj_IDs(inventory):
                obj = get_obj_data(inventory, id)
                print("ID:", get_ID(obj), " Nume:", get_name(obj),
                      " Pret:", get_price(obj))
        elif command[0] == "exit":
            break
        else:
            print("Command not found")


def run():
    print("For commands list type help")
    loop()


if __name__ == "__main__":
    run()
