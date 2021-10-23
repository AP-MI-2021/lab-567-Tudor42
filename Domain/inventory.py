from json.decoder import JSONDecodeError
from Domain.object import *
from json import loads, dumps
from os import getcwd, chdir

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
    if file_path is None:
        while True:
            try:
                file_path = getcwd()  # path to the folder where
                # files are saved
                file_path += "/DataFiles"
                chdir(file_path)
                break
            except NotADirectoryError or OSError:
                chdir("..")
    if file_name is not None:
        data = get_data(file_path + "/" + file_name)
    else:
        data = dict()
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
        d[n] = obj
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
            d[value["ID"]] = value
        if inventory is not None:
            inventory['data'] = d
    except JSONDecodeError:
        pass
    except FileNotFoundError:
        open(file_name, "w")
    return d


def add_obj(inventory, ID, name, description, price=None, location=None):
    """
    Adds a new instance of an object in inventory
    param:
        ID - object id
        name - object name
        description - object description
        price
        location - object location
    return:
        1 - object added successfully
        -2 - ID dublicate
        -1 - Invalid object params
    """
    if ID in inventory['data'].keys():
        return -2
    try:
        inventory['data'][ID] = creaza_obiect(ID, name,
                                              description, price, location)
    except ValueError as ve:
        print(ve)
        return -1
    return 1


def delete_obj(inventory, ID):
    """
    Deletes an object
    param:
        ID - object id
    return:
        1 - successful operation
        -1 - delete error
        -2 - object with such ID doesnt exist
    """
    if ID not in inventory['data'].keys():
        return -2
    inventory['data'].pop(ID)
    return 1


def modify_obj(inventory, ID, name=None, description=None, price=None,
               location=None):
    """
    Modify an object
    param:
    return:
        1 - successful operation
        -2 - object with such ID doesnt exist
        -1 - invalid input
    """
    if ID not in inventory['data'].keys():
        return -2
    try:
        if name is not None:
            set_name(inventory['data'][ID], name)
        if description is not None:
            set_description(inventory['data'][ID], description)
        if price is not None:
            set_price(inventory['data'][ID], price)
        if location is not None:
            set_location(inventory['data'][ID], location)
    except ValueError as ve:
        print(ve)
        return -1
    return 1


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


def get_obj_IDs(inventory):
    return inventory['data'].keys()


def get_obj_data(inventory, ID):
    obj = inventory['data'][ID]
    str = """-------------
    ID: {}
    Nume: {}
    Descriptie: {}
    Pret: {}
    Locatie: {}""".format(ID, obj["name"], obj["description"],
                          obj["price"], obj["location"])
    return str


if __name__ == "__main__":
    d = creaza_inventoriu('gg')
    add_obj(d, 19, "oat", "pat", 120, "ddas")
    modify_obj(d, 19, price=300)
    save_data(d, "gg")
