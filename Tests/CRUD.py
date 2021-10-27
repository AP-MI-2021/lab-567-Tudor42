import Logic.CRUD as di
import Domain.inventory as iv


def test_inventory():
    inventory = iv.creaza_inventoriu()
    assert iv.get_obj_data_str(inventory, 10) == ""

    di.add_obj(inventory, 10, "p", "x", 2, "aaaa")
    assert iv.get_obj_data_list(inventory, 10) == [10, "p", "x", 2,
                                                   "aaaa"]

    di.modify_obj(inventory, 10, description="K")
    assert iv.get_obj_data_list(inventory, 10) == [10, "p", "K", 2,
                                                   "aaaa"]

    di.delete_obj(inventory, 10)
    assert iv.get_obj_data_str(inventory, 10) == ""

    di.add_obj(inventory, 14, "p", "x", 2, "aaaa")
    di.add_obj(inventory, 21, "p", "x", 2, "aaaa")
    di.add_obj(inventory, 32, "p", "x", 2, "aaaa")
    assert iv.get_obj_IDs(inventory) == [14, 21, 32]
