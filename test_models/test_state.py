#!/usr/bin/python3
"""
Unittests for models/state.py
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class
    """

    def test_state_name(self):
        """
        Test the name attribute of the State class
        """
        state = State(name="California")
        self.assertEqual(state.name, "California")


if __name__ == "__main__":
    unittest.main()
