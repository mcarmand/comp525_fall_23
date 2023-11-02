"""
File: homework/h2/tests/test_hide.py
Initial contributor: Mihaela
Contributor: Mason Armand
Date: Oct 26, 2023
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from src import linear_efficiency

class TestHide(unittest.TestCase):

    def test_one(self):
        expected = "ba**le"
        result = linear_efficiency.hide("babble")
        self.assertEqual(expected, result)

    def test_two(self):
        expected = "more is*l***"
        result = linear_efficiency.hide("more is less")
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()

