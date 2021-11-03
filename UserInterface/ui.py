from Domain.inventory import creaza_inventoriu, get_path
from UserInterface.command import *


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
  sum_price - shows sum of prices of objects grouped by their location
  exit - to terminate the console\n""")


def loop():
    inventory = creaza_inventoriu()
    while True:
        command = input('$').split()
        if len(command) == 0:
            continue
        if command[0] == 'cd':
            cd_c(command, inventory)
        elif command[0] == "pwd":
            print(get_path(inventory))
        elif command[0] == "help":
            print_menu()
        elif command[0] == "save":
            save_c(command, inventory)
        elif command[0] == "open":
            open_c(command, inventory)
        elif command[0] == "showall":
            showall_c(command, inventory)
        elif command[0] == "add_obj":
            add_obj_c(command, inventory)
        elif command[0] == "delete_obj":
            delete_obj_c(command, inventory)
        elif command[0] == "modify_obj":
            modify_obj_c(command, inventory)
        elif command[0] == "mutare_objs":
            mutare_objs_c(command, inventory)
        elif command[0] == "add_description":
            add_description_c(command, inventory)
        elif command[0] == "max_price_per_location":
            max_price_per_location_c(command, inventory)
        elif command[0] == "sort_by_price":
            inventory = sort_by_price_c(command, inventory)
        elif command[0] == "sum_price":
            sum_price_c(command, inventory)
        elif command[0] == "exit":
            break
        else:
            print("Command not found")


def run():
    print("For commands list type help")
    loop()


if __name__ == "__main__":
    run()
