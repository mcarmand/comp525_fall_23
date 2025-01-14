"""
test_parse_season.py
Mihaela
Created March 20, 2019. Updated October 15, 2019, November 2, 2023
"""

import unittest
from practice_dictionaries import Practice


class TestParseSeasons(unittest.TestCase):
    """
    Tests for parse_seasons() method
    """
    def setUp(self):
        """
        Define attribute p to hold object of type Problems
        """
        self.p = Practice()

    def test_brief_descriptions(self):
        """
        Test case with short season descriptions
        """
        input1 = {
            'spring': 'warm',
            'summer': 'hot',
            'fall': 'justright',
            'winter': 'cold'
        }
        actual_result = self.p.parse_seasons(input1)
        expected_result = 'springwarmsummerhotfalljustrightwintercold'
        self.assertEqual(actual_result, expected_result)

    def test_update_inventory(self):
        input1 = {
            'milk' : 50,
            'bread' : 20,
            'soda' : 5
        }
        input2 = 5
        actual_result = self.p.update_inventory(input1, input2)
        expected_result = {'milk' : 55, 'bread' : 25, 'soda' : 10}
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
