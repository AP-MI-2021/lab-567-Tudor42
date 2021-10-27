import Domain.inventory as di
import Domain.object as do
import Logic.CRUD as cr


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
        for key in cr.get_obj_IDs(inventory):
            if do.get_location(cr.get_obj_data(inventory, key)) is None:
                cr.modify_obj(inventory, key, location=new_location)
        return inventory
    if new_location is None:
        new_location = old_location
        old_location = None
    if old_location is not None and len(old_location) != 4:
        return inventory
    if len(new_location) != 4:
        raise ValueError("Locatia noua trebuie sa contina 4 caractere")
    if old_location is None:
        for key in cr.get_obj_IDs(inventory):
            cr.modify_obj(inventory, key, location=new_location)
    else:
        for key in cr.get_obj_IDs(inventory):
            if do.get_location(cr.get_obj_data(inventory, key)) == \
               old_location:
                cr.modify_obj(inventory, key, location=new_location)
    return inventory
