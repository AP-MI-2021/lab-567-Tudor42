from Domain.inventory import get_path
from Domain.object import *


def get_objs(invetory):
    """
    param inventory: inventory instance
    return: inventory objects
    """
    return invetory["data"]


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


def mutare_obiecte(inventory, old_location=None, new_location=None):
    """
    Modify objects location
    param inventory:
        Inventory instance
    param old_location:
        From where objects are moved.
        If new_location is None old_location will be new location.
    param new_location:
        Where objects are moved.
    return:
        Modified inventory instance.
    """
    if old_location is None and new_location is None:
        return inventory
    if new_location is not None and old_location is None:
        for key in get_obj_IDs(inventory):
            if get_location(get_obj_data(inventory, key)) is None:
                modify_obj(inventory, key, location=new_location)
        return inventory
    if new_location is None:
        new_location = old_location
        old_location = None
    if old_location is not None and len(old_location) != 4:
        return inventory
    if len(new_location) != 4:
        raise ValueError("Locatia noua trebuie sa contina 4 caractere")
    if old_location is None:
        for key in get_obj_IDs(inventory):
            modify_obj(inventory, key, location=new_location)
    else:
        for key in get_obj_IDs(inventory):
            if get_location(get_obj_data(inventory, key)) == \
               old_location:
                modify_obj(inventory, key, location=new_location)
    return inventory


def add_description(inventory, n, text):
    """
    Concatenates text to every description of objects with price bigger than n
    param inventory: inventory instance
    param n: minimum price
    param text: string
    return: modified inventory
    """
    if text == "":
        return inventory
    for obj in get_obj_IDs(inventory):
        o = get_obj_data(inventory, obj)
        if get_price(o) > n:
            s = get_description(o) + text
            modify_obj(inventory, obj, description=s)
    return inventory


def get_max_price_per_location(inventory):
    """
    Gets the max price per location
    param inventory: inventory instance
    return: A dictionary with key representing
      the location and value represents the max price
    """
    res = dict()
    for i in get_obj_IDs(inventory):
        obj = get_obj_data(inventory, i)
        if get_location(obj) not in res.keys():
            res[get_location(obj)] = get_price(obj)
        else:
            if res[get_location(obj)] < get_price(obj):
                res[get_location(obj)] = get_price(obj)
    return res


def sort_invetory_by_price(inventory):
    """
    Sorts objects in inventory by their price
    param inventory: inventory instance
    return: sorted inventory
    """
    return {
        'data': dict(sorted(get_objs(inventory).items(),
                            key=lambda x: get_price(x[1]))),
        'folder': get_path(inventory)
    }
