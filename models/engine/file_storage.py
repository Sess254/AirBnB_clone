#!/usr/bin/python3

"""serializes instances to a JSON file/deserialize JSON file to instances"""

import models
import os.path
import json
from models.base_model import BaseModel


class FileStorage:
    """File storage class that serializes and deserializes to and from  JSON
       Class Attributes with file_path - path to JSON file
       and objects - dictionary used to store objects by ID
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Instantation method"""
        pass

    def all(self):
        """Returns dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """sets object into __objects with id key"""
        FileStorage.__objects['{}.{}'.format(obj.__class__.__name__, obj.id)]\
            = obj

    def save(self):
        """Serialize objects to JSON file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserialize from JSON file"""
        if os.path.isfile(self.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                temp = json.load(file)
                for key, value in temp.items():
                    clas_rel = temp[key]["__class__"]
                    g_class = models.class_dict[clas_rel]
                    self.__objects[key] = g_class(**value)
