from Domain.object import *


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


def get_obj_IDs(inventory):
    """
    Returns the list of objects IDs
    param:
        inventory instance
    return:
        A list
    """
    return list(inventory['data'].keys())


def get_obj_data_list(inventory, ID):
    """
    Get object data as object instance
    param:
        inventory instance
        object's ID
    return:
        Return obj as a list
        Empty list if object doesnt exist
    """
    if ID not in inventory['data'].keys():
        return []
    return list(get_obj_data(inventory, ID))


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
    if ID not in inventory['data'].keys():
        return {}
    return inventory['data'][ID]


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
    if ID not in inventory['data'].keys():
        return ""
    obj = inventory['data'][ID]
    str = """-------------
    ID: {}
    Nume: {}
    Descriptie: {}
    Pret: {}
    Locatie: {}""".format(ID, get_name(obj), get_description(obj),
                          get_price(obj), get_location(obj))
    return str
