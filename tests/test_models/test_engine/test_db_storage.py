#!/usr/bin/python3
"""
Unittests for models/engine/db_storage.py
"""
import unittest
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """
    Test cases for the DBStorage class
    """

    def test_instance(self):
        """
        Test if storage is an instance of DBStorage
        """
        storage = DBStorage()
        self.assertIsInstance(storage, DBStorage)


if __name__ == "__main__":
    unittest.main()
