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


def test_mutare():
    inventory = iv.creaza_inventoriu()

    cr.add_obj(inventory, 19, "L", "L", 12, "LLLL")
    cr.add_obj(inventory, 20, "L", "L", 12, "llll")
    cr.add_obj(inventory, 21, "L", "L", 12, "LLLL")
    cr.add_obj(inventory, 22, "L", "L", 12, "llll")

    inventory = cr.mutare_obiecte(inventory, "LLLL", "aaaa")
    assert cr.get_obj_data_list(inventory, 19) == [19, "L", "L", 12,
                                                   "aaaa"]
    assert cr.get_obj_data_list(inventory, 21) == [21, "L", "L", 12,
                                                   "aaaa"]

    inventory = cr.mutare_obiecte(inventory, "dddd")

    for id in cr.get_obj_IDs(inventory):
        assert cr.get_obj_data_list(inventory, id) == [id, "L", "L",
                                                       12, "dddd"]

    for id in range(1, 12):
        cr.add_obj(inventory, id, "a", "a", 0)
    inventory = cr.mutare_obiecte(inventory, new_location="OPPP")

    for id in range(1, 12):
        assert cr.get_obj_data_list(inventory, id) == [id, "a", "a",
                                                       0, "OPPP"]


def test_add_description():
    inventory = iv.creaza_inventoriu()

    cr.add_obj(inventory, 19, "L", "L", 8, "LLLL")
    cr.add_obj(inventory, 20, "L", "l", 16, "llll")
    cr.add_obj(inventory, 21, "L", "L", 10, "LLLL")
    cr.add_obj(inventory, 22, "L", "l", 123, "llll")

    cr.add_description(inventory, 10, "JKRLNG")

    for obj in cr.get_obj_IDs(inventory):
        if obj == 20 or obj == 22:
            assert cr.get_description(cr.get_obj_data(inventory, obj)) == \
                "lJKRLNG"
        else:
            assert cr.get_description(cr.get_obj_data(inventory, obj)) == \
                "L"
