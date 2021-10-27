from json.decoder import JSONDecodeError
from Domain.object import *
from json import loads, dumps
from os import getcwd, chdir, mkdir

"""
Inventory:
    data - dictionary of objects
    folder - path to saved files
"""


def creaza_inventoriu(file_name=None, file_path=None):
    """
    Creaza un inventoriu
    param:
        file_name - Denumirea fisierului cu obiecte
        file_path - Unde se afla fisierul
    return:
        O variabila de tip inventory
    """
    if file_path is None and getcwd()[-9:] != "DataFiles" and \
       getcwd()[-15:] == "lab-567-Tudor42":
        while True:
            try:
                chdir("./DataFiles")
                break
            except NotADirectoryError:
                mkdir("./DataFiles")
            except FileNotFoundError:
                mkdir("./DataFiles")
            except OSError:
                print("Can't set up default folder")
    if file_name is not None:
        data = get_data(file_path + "/" + file_name)
    else:
        data = dict()
    file_path = getcwd()
    return {
        'data': data,
        'folder': file_path
    }


def save_data(inventory, file_name="swap.json"):
    """
    Save invetory data in a file for later use
    param:
        inventory instance
        file_name
    return:
        -1 - if fails
        0 - if succeds
    """
    if file_name[-5:] != ".json":
        file_name += ".json"
    file_name = inventory['folder'] + "/" + file_name
    d = dict()  # dictionary for serialization
    n = 1
    for obj in inventory['data'].values():
        d[n] = {
            "ID": get_ID(obj),
            "name": get_name(obj),
            "description": get_description(obj),
            "price": get_price(obj),
            "location": get_location(obj)
        }
        n += 1
    try:
        with open(file_name, "w") as fout:
            fout.write(dumps(d))
    except FileNotFoundError as err:
        print(err)
        return -1
    return 0


def get_data(file_name="swap.json", inventory=None):
    """
    Get inventory data from file
    param:
        inventory - inventory instance
    return:
        A dictionary of objects
    """
    if file_name[-5:] != ".json":
        file_name += ".json"
    d = dict()
    try:
        for value in loads(open(file_name, "r").read()).values():
            d[value["ID"]] = creaza_obiect(value["ID"], value["name"],
                                           value["description"],
                                           value["price"],
                                           value["location"])
        if inventory is not None:
            inventory['data'] = d
    except JSONDecodeError:
        pass
    except FileNotFoundError:
        open(file_name, "w")
    return d


def set_folder(inventory, new_path):
    try:
        chdir(new_path)
    except NotADirectoryError as err:
        print(err)
        return -1
    except OSError as err:
        print(err)
        return -1
    except FileNotFoundError as err:
        print(err)
        return -1
    inventory['folder'] = getcwd()
    return 0


def get_path(inventory):
    """
    Returneaza working directory
    param:
        inventory
    return:
        String cu pathul pentru working directory
    """
    return inventory['folder']
