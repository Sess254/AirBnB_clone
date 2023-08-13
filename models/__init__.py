#!/usr/bin/python3

"""Importing storage variable using magic method"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class_dict = {
        'BaseModel': BaseModel,
        'User': User,
        'State': state,
        'City': City,
        'Amenity': Amenity,
        'Place': place,
        'Review': Review}

storage = FileStorage()
storage.reload()
