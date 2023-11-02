"""
File: homework/h2/tests/test_reduce_adjacent.py
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
        expected = [1, 2, 3]
        result = linear_efficiency.reduce_adjacent([1, 2, 2, 3])
        self.assertEqual(expected, result)

    def test_two(self):
        expected = [5, 4, 1]
        result = linear_efficiency.reduce_adjacent([5, 5, 5, 4, 1])
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()

