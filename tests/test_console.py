#!/usr/bin/python3
"""
Unittests for console.py
"""
import unittest
import MySQLdb
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Test cases for the HBNBCommand class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up for the test class
        """
        cls.db = MySQLdb.connect(
            host="localhost",
            user="hbnb_test",
            passwd="hbnb_test_pwd",
            db="hbnb_test_db"
        )
        cls.cursor = cls.db.cursor()
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """
        Clean up after tests
        """
        cls.db.close()

    def test_create_state(self):
        """
        Test creating a new state
        """
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        self.console.onecmd('create State name="California"')

        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]

        self.assertEqual(final_count, initial_count + 1)


if __name__ == "__main__":
    unittest.main()
