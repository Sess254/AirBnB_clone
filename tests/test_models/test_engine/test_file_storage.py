#!/usr/bin/python3
""" module containts unittests for class BaseModel """


import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class testFileStorage(unittest.TestCase):
    """ unittests for File Storage """

    def test_created_at_storage(self):
        """ Datetime at creation of an object when stored """

    def test_updated_at_storage(self):
        """ Datetime at update of an object when stored """

    def test_from_dict(self):
        """ Test that keys/values are saving correctly """

    def test_save(self):
        """ Tests that instance attributes are saved and updated
        correctly with the proper updated datetime """


if __name__ == "__main__":
    testFileStorage()
