#!/usr/bin/python3
"""handle file storage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review


class FileStorage:
    """also handles serialisation and deserialisation
    Attributes: __file_path: storage file
                __objects: dictionary
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns a dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects with key"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serialises __objects to json file"""
        obj = self.__objects
        objdict = {value: obj[value].to_dict() for value in obj.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserialise the json file into a python object"""
        try:
            with open(self.__file_path) as f:
                objdict = json.load(f)
                for val in objdict.values():
                    name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(name)(**val))
        except FileNotFoundError:
            return
