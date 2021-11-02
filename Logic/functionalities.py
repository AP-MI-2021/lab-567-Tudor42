from Domain.object import *
from Logic.CRUD import *


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
    try:
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
    except ValueError as ve:
        print(ve)
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


def get_price_sum_per_location(inventory):
    """
    Gets the sum of prices per location
    param inventory: inventory instance
    return: A dictionary with key representing
      the location and value represents the sum
    """
    res = dict()
    for i in get_obj_IDs(inventory):
        obj = get_obj_data(inventory, i)
        if get_location(obj) not in res.keys():
            res[get_location(obj)] = get_price(obj)
        else:
            res[get_location(obj)] += get_price(obj)
    return res
