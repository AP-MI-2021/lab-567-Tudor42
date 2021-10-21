from object import Object, ObjectExceptions
from json import loads, dumps
from os import getcwd, chdir


class Inventory:
    def __init__(self, file=None):
        while True:
            try:
                self.__file_folder = getcwd()  # path to the folder where
                # files are saved
                self.__file_folder += "/DataFiles"
                chdir(self.__file_folder)
                break
            except NotADirectoryError or OSError:
                chdir("..")
        if file is not None:
            self.__data = self.get_data(file)
        else:
            self.__data = dict()

    def save_data(self, file=None):
        """
        Save invetory data in a file for later use
        """
        if file is None:
            file = self.__file_folder + "/swap.json"
        if file[-5:] != ".json":
            file += ".json"
        d = dict()  # dictionary for serialization
        n = 1
        for obj in self.__data.values():
            d[n] = obj.serialize()
            n += 1
        with open(file, "w") as fout:
            fout.write(dumps(d))

    def get_data(self, file=None):
        """
        Get inventory data from file
        param:
            file - name of the file
        return:
            A dictionary of objects
        """
        file = self.__file_folder + "/" + file
        d = dict()
        for value in loads(open(file, "r").read()).values():
            d[value["ID"]] = Object(0, "", "", serialization=value)
        return d

    def add_obj(self, ID, name, description, price=None, location=None):
        """
        Adds a new instance of an object in inventory
        param:
            ID - object id
            name - object name
            description - object description
            price
            location - object location
        return:
            1 - object added successfully
            -2 - ID dublicate
            -1 - Invalid object params
        """
        if ID in self.__data.keys():
            return -2
        try:
            self.__data[ID] = Object(ID, name, description, price, location)
        except ObjectExceptions:
            return -1
        return 1

    def delete_obj(self, ID):
        """
        Deletes an object
        param:
            ID - object id
        return:
            1 - successful operation
            -1 - delete error
            -2 - object with such ID doesnt exist
        """
        if ID not in self.__data.keys():
            return -2
        self.__data.pop(ID)
        return 1


if __name__ == "__main__":
    d = Inventory("swap.json")
    d.add_obj(190, "oat", "pat")
    print(d.delete_obj(190))
    d.save_data("gg")
