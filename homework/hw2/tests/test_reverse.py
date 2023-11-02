"""
File: homework/h2/tests/test_reverse.py
Initial contributor: Mihaela
Contributor: Mason Armand
Date: Oct 26, 2023
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from src import linear_efficiency

class TestReduceAdjacent(unittest.TestCase):

    def test_one(self):
        expected = "olleh"
        result = linear_efficiency.reverse("hello")
        self.assertEqual(expected, result)

    def test_two(self):
        expected = "dlrow"
        result = linear_efficiency.reverse("world")
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()

