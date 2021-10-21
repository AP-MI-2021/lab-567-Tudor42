
class Object:
    def __init__(self, object_id: int, name: str, description: str, price=None,
                 location=None, serialization=None):
        if serialization is not None:
            self.deserialize(serialization)
            return
        if object_id == 0 or name == "" or description == "":
            raise ObjectExceptions
        self.__ID = object_id
        self.__name = name
        self.__description = description
        self.set_price(price)
        self.set_location(location)

# getteri

    def get_ID(self):
        return self.__ID

    def get_nume(self):
        return self.__name

    def get_descriere(self):
        return self.__description

    def get_pret(self):
        return self.__price

    def get_locatie(self):
        return self.__location

# setteri

    def set_description(self, description):
        self.__description = description

    def set_price(self, price):
        if price is not None and not isinstance(price, (float, int)):
            raise ObjectExceptions
        self.__price = price

    def set_location(self, location):
        if location is not None and len(location) != 4:
            raise ObjectExceptions
        self.__location = location

# serialization and deserialization

    def serialize(self):
        return {
            "ID": self.__ID,
            "name": self.__name,
            "description": self.__description,
            "price": self.__price,
            "location": self.__location
        }

    def deserialize(self, dict):
        self.__ID = dict["ID"]
        self.__name = dict["name"]
        self.__description = dict["description"]
        self.__price = dict["price"]
        self.__location = dict["location"]


class ObjectExceptions(Exception):
    """Raised when object is created
    with object_id 0 or name and description
    are empty strings. Invalid data can also
    raise this exception
    """
    pass


if __name__ == "__main__":
    try:
        obj = Object(0, "", "")
    except ObjectExceptions:
        print(False)
    print(True)
