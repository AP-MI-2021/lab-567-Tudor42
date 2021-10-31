"""
Obiect:
    ID - id obiect
    name - nume obiect
    description - descriptie obiect
    price - pret obiect
    location - locatie obiect
"""


def creaza_obiect(object_id: int, name: str, description: str, price=None,
                  location=None):
    if object_id <= 0 or name == "" or description == "":
        raise ValueError("ID, nume si descriptia obiectului trebui sa fie"
                         " nenule, si ID nu trebuie sa fie negativ")
    if location is not None and len(location) != 4:
        raise ValueError("Locatia poate fi formata doar din "
                         "4 caractere")
    if price is not None and not isinstance(price, (float, int)):
        raise ValueError("Pretul trebuie sa fie numar")
    if price is None:
        price = 0
    if price < 0:
        raise ValueError("Pretul nu poate fi negativ")
    return [
        object_id,  # ID
        name,  # Name
        description,  # Description
        price,  # price
        location  # location
    ]


def get_ID(obj):
    return obj[0]


def get_name(obj):
    return obj[1]


def get_description(obj):
    return obj[2]


def get_price(obj):
    return obj[3]


def get_location(obj):
    return obj[4]


def set_name(obj, name):
    if name == "":
        raise ValueError("Numele nu poate fi string gol")
    obj[1] = name


def set_description(obj, description):
    if description == "":
        raise ValueError("Descriptia nu poate fi string gol")
    obj[2] = description


def set_price(obj, price):
    if not isinstance(price, (float, int)):
        raise ValueError("Pretul trebuie sa fie numar")
    obj[3] = price


def set_location(obj, location):
    if location is not None and len(location) != 4:
        raise ValueError("Locatia poate fi formata doar din "
                         "4 caractere")
    obj[4] = location


if __name__ == "__main__":
    try:
        obj = creaza_obiect(20, "DOAS", "d", 10, "dddd")
    except ValueError as ve:
        print(ve)
    print(obj)
