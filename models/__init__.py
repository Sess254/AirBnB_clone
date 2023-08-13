#!/usr/bin/python3

"""Importing storage variable using magic method"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class_dict = {'BaseModel': BaseModel}

storage = FileStorage()
storage.reload()
