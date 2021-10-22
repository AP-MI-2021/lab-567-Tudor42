from object import *
from json import loads, dumps
from os import getcwd, chdir


def creaza_inventoriu(file_name=None, file_path=None):
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
    """
    if file_name[-5:] != ".json":
        file_name += ".json"
    file_name = inventory['folder'] + "/" + file_name
    d = dict()  # dictionary for serialization
    n = 1
    for obj in inventory['data'].values():
        d[n] = obj
        n += 1
    with open(file_name, "w") as fout:
        fout.write(dumps(d))


def get_data(file_name):
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
    for value in loads(open(file_name, "r").read()).values():
        d[value["ID"]] = value
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
        -1 - object with such ID doesnt exist
    """
    if ID not in inventory['data'].keys():
        return -1
    if name is not None:
        set_name(inventory['data'][ID], name)
    if description is not None:
        set_description(inventory['data'][ID], description)
    if price is not None:
        set_price(inventory['data'][ID], price)
    if location is not None:
        set_location(inventory['data'][ID], location)
    return 1


if __name__ == "__main__":
    d = creaza_inventoriu('gg')
    add_obj(d, 19, "oat", "pat", 120, "ddas")
    modify_obj(d, 19, price=300)
    save_data(d, "gg")
