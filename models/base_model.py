#!/usr/bin/python3
"""Defines the BaseModel"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """This the base class for all other classes in this project """
    id = 0

    def __init__(self, *args, **kwargs):
        """ initializes base class with a unique id """
        if (kwargs):
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.\
                                      strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    continue
                if key == 'updated_at':
                    self.updated_at = datetime.\
                                      strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    continue
                if key == '__class__':
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ prints name, id, and dict """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """ updates the public instance attribute with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dict containing all keys/values of __dict__ """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
