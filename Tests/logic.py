import Logic.inventory_logic as invl
import Domain.inventory as inv
import Logic.CRUD as cr


def test_mutare():
    inventory = inv.creaza_inventoriu()

    cr.add_obj(inventory, 19, "L", "L", 12, "LLLL")
    cr.add_obj(inventory, 20, "L", "L", 12, "llll")
    cr.add_obj(inventory, 21, "L", "L", 12, "LLLL")
    cr.add_obj(inventory, 22, "L", "L", 12, "llll")

    inventory = invl.mutare_obiecte(inventory, "LLLL", "aaaa")
    assert inv.get_obj_data_list(inventory, 19) == [19, "L", "L", 12,
                                                    "aaaa"]
    assert inv.get_obj_data_list(inventory, 21) == [21, "L", "L", 12,
                                                    "aaaa"]

    inventory = invl.mutare_obiecte(inventory, "dddd")

    for id in inv.get_obj_IDs(inventory):
        assert inv.get_obj_data_list(inventory, id) == [id, "L", "L",
                                                        12, "dddd"]

    for id in range(1, 12):
        cr.add_obj(inventory, id, "a", "a", 0)
    inventory = invl.mutare_obiecte(inventory, new_location="OPPP")

    for id in range(1, 12):
        assert inv.get_obj_data_list(inventory, id) == [id, "a", "a",
                                                        0, "OPPP"]
