from Domain.object import *

"""
Inventory:
    data - list of objects
"""


def creaza_inventoriu():
    """
    Creaza un inventoriu
    return:
        O variabila de tip inventory
    """
    return list()


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
    if ID in get_obj_IDs(inventory):
        return -2
    try:
        inventory.append(creaza_obiect(ID, name,
                                       description, price, location))
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
        Modified inventory on succes
        -2 - object with such ID doesnt exist
    """
    if ID not in get_obj_IDs(inventory):
        return -2
    m = -1
    for i in range(len(inventory)):
        if ID == get_ID(inventory[i]):
            m = i
            break
    del inventory[m]
    return inventory


def modify_obj(inventory, ID, name=None, description=None, price=None,
               location=None):
    """
    Modify an object
    param:
    return:
        Modified inventory - successful operation
        -2 - object with such ID doesnt exist
        -1 - invalid input
    """
    if ID not in get_obj_IDs(inventory):
        return -2
    m = 0
    for i in range(len(inventory)):
        if ID == get_ID(inventory[i]):
            m = i
            break
    try:
        if name is not None:
            set_name(inventory[m], name)
        if description is not None:
            set_description(inventory[m], description)
        if price is not None:
            set_price(inventory[m], price)
        if location is not None:
            set_location(inventory[m], location)
    except ValueError as ve:
        print(ve)
        return -1
    return inventory


def get_obj_IDs(inventory):
    """
    Returns the list of objects IDs
    param:
        inventory instance
    return:
        A list
    """
    res_lst = []
    for obj in inventory:
        res_lst.append(get_ID(obj))
    return res_lst


def get_obj_data(inventory, ID):
    """
    Get object data as object instance
    param:
        inventory instance
        object's ID
    return:
        Object instance
        Empty dictionary if object doesnt exist
    """
    if ID not in get_obj_IDs(inventory):
        return {}
    m = 0
    for i in range(len(inventory)):
        if ID == get_ID(inventory[i]):
            m = i
            break
    return inventory[m]


def get_obj_data_str(inventory, ID):
    """
    Get object data as string
    param:
        inventory instance
        ID - object's ID
    return:
        A string of data on succes
        If object with this ID doesnt exist
        it returns an empty string
    """
    if ID not in get_obj_IDs(inventory):
        return ""
    for i in range(len(inventory)):
        if ID == get_ID(inventory[i]):
            m = i
            break
    obj = inventory[m]
    str = """-------------
    ID: {}
    Nume: {}
    Descriptie: {}
    Pret: {}
    Locatie: {}""".format(ID, obj["name"], obj["description"],
                          obj["price"], obj["location"])
    return str
