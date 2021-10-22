from Domain.inventory import creaza_inventoriu, set_folder, save_data, \
                             get_data, get_obj_data, get_obj_IDs, add_obj, \
                             delete_obj


def print_menu():
    pass


def loop():
    inventory = creaza_inventoriu()
    while True:
        command = input('$').split()
        if command[0] == 'cwd':
            if len(command) < 2:
                print("Path isnt specified")
                continue
            set_folder(inventory, command[1])
        elif command[0] == "help":
            print_menu()
        elif command[0] == "save":
            if len(command) < 2:
                save_data(inventory)
            else:
                save_data(inventory, command[1])
        elif command[0] == "open":
            if len(command) >= 2:
                get_data(command[1], inventory)
            else:
                get_data(inventory=inventory)
        elif command[0] == "showall":
            keys = get_obj_IDs(inventory)
            for key in keys:
                print(get_obj_data(inventory, key))
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
            add_obj(inventory, ID, name, description, price, location)
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
        elif command[0] == "exit":
            break
        else:
            print("Command not found")


def run():
    print("For commands list type help")
    loop()


if __name__ == "__main__":
    run()
