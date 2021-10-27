import Domain.object as do


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
