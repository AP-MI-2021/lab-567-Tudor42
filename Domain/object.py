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
    return {
        "ID": object_id,
        "name": name,
        "description": description,
        "price": price,
        "location": location
    }


def get_ID(obj):
    return obj["ID"]


def get_name(obj):
    return obj["name"]


def get_description(obj):
    return obj["description"]


def get_price(obj):
    return obj["price"]


def get_location(obj):
    return obj["location"]


def set_name(obj, name):
    if name == "":
        raise ValueError("Numele nu poate fi string gol")
    obj["name"] = name


def set_description(obj, description):
    if description == "":
        raise ValueError("Descriptia nu poate fi string gol")
    obj["description"] = description


def set_price(obj, price):
    if not isinstance(price, (float, int)):
        raise ValueError("Pretul trebuie sa fie numar")
    obj["price"] = price


def set_location(obj, location):
    if location is not None and len(location) != 4:
        raise ValueError("Locatia poate fi formata doar din "
                         "4 caractere")
    obj["location"] = location


if __name__ == "__main__":
    try:
        obj = creaza_obiect(20, "DOAS", "d", 10, "dddd")
    except ValueError as ve:
        print(ve)
    print(obj)
