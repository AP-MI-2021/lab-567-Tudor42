import Domain.inventory as di


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
        for ID in di.get_obj_IDs(inventory):
            if di.get_obj_data(inventory, ID)['location'] is None:
                di.modify_obj(inventory, ID, location=new_location)
        return inventory
    if new_location is None:
        new_location = old_location
        old_location = None
    if old_location is not None and len(old_location) != 4:
        return inventory
    if len(new_location) != 4:
        raise ValueError("Locatia noua trebuie sa contina 4 caractere")
    if old_location is None:
        for ID in di.get_obj_IDs(inventory):
            di.modify_obj(inventory, ID, location=new_location)
        return inventory
    else:
        for ID in di.get_obj_IDs(inventory):
            if di.get_obj_data(inventory, ID)['location'] == old_location:
                di.modify_obj(inventory, ID, location=new_location)
    return inventory
