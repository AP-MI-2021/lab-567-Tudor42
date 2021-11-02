import Logic.CRUD as cr
import Domain.inventory as iv


def test_get_obj_data_list():
    inventory = iv.creaza_inventoriu()
    cr.add_obj(inventory, 14, "p", "x", 2, "aaaa")
    cr.add_obj(inventory, 21, "d", "x", 2, "aaaa")
    cr.add_obj(inventory, 32, "s", "x", 2, "aaaa")
    assert cr.get_obj_data(inventory, 14) == [14, "p", "x", 2,
                                              "aaaa"]
    assert cr.get_obj_data(inventory, 21) == [21, "d", "x", 2,
                                              "aaaa"]
    assert cr.get_obj_data(inventory, 32) == [32, "s", "x", 2,
                                              "aaaa"]


def test_get_obj_IDs():
    inventory = iv.creaza_inventoriu()
    cr.add_obj(inventory, 15, "p", "x", 2, "aaaa")
    cr.add_obj(inventory, 16, "p", "x", 2, "aaaa")
    cr.add_obj(inventory, 17, "p", "x", 2, "aaaa")
    assert cr.get_obj_IDs(inventory) == [15, 16, 17]


def test_modify_obj():
    inventory = iv.creaza_inventoriu()
    cr.add_obj(inventory, 10, "p", "x", 2, "aaaa")
    cr.modify_obj(inventory, 10, description="K")
    assert cr.get_obj_data_list(inventory, 10) == [10, "p", "K", 2,
                                                   "aaaa"]
    cr.modify_obj(inventory, 10, price=100)
    assert cr.get_obj_data_list(inventory, 10) == [10, "p", "K", 100,
                                                   "aaaa"]
    cr.modify_obj(inventory, 10, location="dddd")
    assert cr.get_obj_data_list(inventory, 10) == [10, "p", "K", 100,
                                                   "dddd"]


def test_delete_obj():
    inventory = iv.creaza_inventoriu()
    assert cr.get_obj_data_str(inventory, 10) == ""
    cr.add_obj(inventory, 10, "p", "x", 2, "aaaa")
    cr.add_obj(inventory, 100, "p", "x", 2, "aaaa")

    cr.delete_obj(inventory, 10)
    cr.delete_obj(inventory, 100)
    assert cr.get_obj_data_str(inventory, 10) == ""


def test_add_obj():
    inventory = iv.creaza_inventoriu()
    cr.add_obj(inventory, 14, "p", "x", 2, "aaaa")
    cr.add_obj(inventory, 21, "p", "x", 2, "aaaa")
    cr.add_obj(inventory, 32, "p", "x", 2, "aaaa")
    assert cr.get_obj_IDs(inventory) == [14, 21, 32]
