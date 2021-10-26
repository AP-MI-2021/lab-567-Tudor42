import Logic.inventory_logic as invl
import Domain.inventory as inv


def test_mutare():
    inventory = inv.creaza_inventoriu()

    inv.add_obj(inventory, 19, "L", "L", 12, "LLLL")
    inv.add_obj(inventory, 20, "L", "L", 12, "llll")
    inv.add_obj(inventory, 21, "L", "L", 12, "LLLL")
    inv.add_obj(inventory, 22, "L", "L", 12, "llll")

    inventory = invl.mutare_obiecte(inventory, "LLLL", "aaaa")
    assert list(inv.get_obj_data(inventory, 19).values()) == [19, "L", "L", 12,
                                                              "aaaa"]
    assert list(inv.get_obj_data(inventory, 21).values()) == [21, "L", "L", 12,
                                                              "aaaa"]

    inventory = invl.mutare_obiecte(inventory, "dddd")

    for id in inv.get_obj_IDs(inventory):
        assert list(inv.get_obj_data(inventory, id).values()) == [id, "L", "L",
                                                                  12, "dddd"]

    for id in range(1, 12):
        inv.add_obj(inventory, id, "a", "a", 0)
    inventory = invl.mutare_obiecte(inventory, new_location="OPPP")

    for id in range(1, 12):
        assert list(inv.get_obj_data(inventory, id).values()) == [id, "a", "a",
                                                                  0, "OPPP"]
