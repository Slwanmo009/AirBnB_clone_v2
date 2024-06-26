#!/usr/bin/python3
"""
This module contains unittests for database operations.
"""
import unittest
import MySQLdb
from console import HBNBCommand  # Import the console command

class TestDBOperations(unittest.TestCase):
    """
    This class contains unittests for database operations.
    """

    def setUp(self):
        """
        Set up the database connection and initialize the console.
        """
        self.db = MySQLdb.connect(
            host="localhost",
            user="test_user",
            passwd="test_password",
            db="test_db"
        )
        self.cursor = self.db.cursor()
        self.console = HBNBCommand()

    def tearDown(self):
        """
        Close the database connection.
        """
        self.db.close()

    def test_create_state(self):
        """
        Test creating a new state.
        """
        # Get the number of current records in the table states
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Execute the console command to create a new state
        self.console.onecmd('create State name="California"')

        # Get the number of current records in the table states
        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]

        # Validate the number of records increased by 1
        self.assertEqual(final_count, initial_count + 1)

if __name__ == "__main__":
    unittest.main()
