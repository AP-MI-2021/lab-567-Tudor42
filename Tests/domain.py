import Domain.object as do
import Domain.inventory as di


def test_obiect():
    obiect = do.creaza_obiect(10, "obj1", "X", 20, "AAAA")

    assert do.get_ID(obiect) == 10
    assert do.get_name(obiect) == "obj1"
    assert do.get_description(obiect) == "X"
    assert do.get_price(obiect) == 20
    assert do.get_location(obiect) == "AAAA"

    do.set_name(obiect, "obj2")
    assert do.get_name(obiect) == "obj2"

    do.set_description(obiect, "Y")
    assert do.get_description(obiect) == "Y"

    do.set_price(obiect, 10)
    assert do.get_price(obiect) == 10

    do.set_location(obiect, "BBBB")
    assert do.get_location(obiect) == "BBBB"


def test_inventory():
    inventory = di.creaza_inventoriu()
    assert di.get_obj_data_str(inventory, 10) == ""

    di.add_obj(inventory, 10, "p", "x", 2, "aaaa")
    assert list(di.get_obj_data(inventory, 10).values()) == [10, "p", "x", 2,
                                                             "aaaa"]

    di.modify_obj(inventory, 10, description="K")
    assert list(di.get_obj_data(inventory, 10).values()) == [10, "p", "K", 2,
                                                             "aaaa"]

    di.delete_obj(inventory, 10)
    assert di.get_obj_data_str(inventory, 10) == ""

    di.add_obj(inventory, 14, "p", "x", 2, "aaaa")
    di.add_obj(inventory, 21, "p", "x", 2, "aaaa")
    di.add_obj(inventory, 32, "p", "x", 2, "aaaa")
    assert di.get_obj_IDs(inventory) == [14, 21, 32]
