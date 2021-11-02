import Logic.CRUD as cr
import Domain.inventory as iv
import Logic.functionalities as fn


def test_mutare():
    inventory = iv.creaza_inventoriu()

    cr.add_obj(inventory, 19, "L", "L", 12, "LLLL")
    cr.add_obj(inventory, 20, "L", "L", 12, "llll")
    cr.add_obj(inventory, 21, "L", "L", 12, "LLLL")
    cr.add_obj(inventory, 22, "L", "L", 12, "llll")

    inventory = fn.mutare_obiecte(inventory, "LLLL", "aaaa")
    assert cr.get_obj_data_list(inventory, 19) == [19, "L", "L", 12,
                                                   "aaaa"]
    assert cr.get_obj_data_list(inventory, 21) == [21, "L", "L", 12,
                                                   "aaaa"]

    inventory = fn.mutare_obiecte(inventory, "dddd")

    for id in cr.get_obj_IDs(inventory):
        assert cr.get_obj_data_list(inventory, id) == [id, "L", "L",
                                                       12, "dddd"]

    for id in range(1, 12):
        cr.add_obj(inventory, id, "a", "a", 0)
    inventory = fn.mutare_obiecte(inventory, new_location="OPPP")

    for id in range(1, 12):
        assert cr.get_obj_data_list(inventory, id) == [id, "a", "a",
                                                       0, "OPPP"]


def test_add_description():
    inventory = iv.creaza_inventoriu()

    cr.add_obj(inventory, 19, "L", "L", 8, "LLLL")
    cr.add_obj(inventory, 20, "L", "l", 16, "llll")
    cr.add_obj(inventory, 21, "L", "L", 10, "LLLL")
    cr.add_obj(inventory, 22, "L", "l", 123, "llll")

    fn.add_description(inventory, 10, "JKRLNG")

    for obj in cr.get_obj_IDs(inventory):
        if obj == 20 or obj == 22:
            assert cr.get_description(cr.get_obj_data(inventory, obj)) == \
                "lJKRLNG"
        else:
            assert cr.get_description(cr.get_obj_data(inventory, obj)) == \
                "L"


def test_get_max_price_per_location():
    inventory = iv.creaza_inventoriu()

    cr.add_obj(inventory, 19, "L", "L", 8, "aaaa")
    cr.add_obj(inventory, 20, "L", "l", 16, "bbbb")
    cr.add_obj(inventory, 21, "L", "L", 10, "cccc")
    cr.add_obj(inventory, 22, "L", "l", 123, "dddd")

    d = {"aaaa": 8, "bbbb": 16, "cccc": 10, "dddd": 123}

    assert fn.get_max_price_per_location(inventory) == d

    cr.add_obj(inventory, 23, "L", "L", 10, "aaaa")
    cr.add_obj(inventory, 24, "L", "l", 14, "bbbb")
    cr.add_obj(inventory, 25, "L", "L", 18, "cccc")
    cr.add_obj(inventory, 26, "L", "l", 2, "dddd")

    d = {"aaaa": 10, "bbbb": 16, "cccc": 18, "dddd": 123}

    assert fn.get_max_price_per_location(inventory) == d


def test_sort_invetory_by_price():
    inventory_unsorted = iv.creaza_inventoriu()
    inventory_sorted = iv.creaza_inventoriu()

    cr.add_obj(inventory_unsorted, 19, "L", "L", 8, "aaaa")
    cr.add_obj(inventory_unsorted, 20, "L", "l", 16, "bbbb")
    cr.add_obj(inventory_unsorted, 21, "L", "L", 10, "cccc")
    cr.add_obj(inventory_unsorted, 22, "L", "l", 1, "dddd")

    cr.add_obj(inventory_sorted, 22, "L", "l", 1, "dddd")
    cr.add_obj(inventory_sorted, 19, "L", "L", 8, "aaaa")
    cr.add_obj(inventory_sorted, 21, "L", "L", 10, "cccc")
    cr.add_obj(inventory_sorted, 20, "L", "l", 16, "bbbb")

    inventory_unsorted = fn.sort_invetory_by_price(inventory_unsorted)
    assert inventory_sorted == inventory_unsorted
