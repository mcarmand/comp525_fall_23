"""
File: src/main.py
Author: Mihaela
Date: 3/21/2023
Developer:
Date:
"""

from unorderedlist import UnorderedList
import unittest

class TestHide(unittest.TestCase):

    def test_prepend(self):
        """
        Call prepend() to create the list with items 6, 3, 7
        """
        lst = UnorderedList()
        lst.prepend(7)
        lst.prepend(3)
        lst.prepend(6)

        expected = "(6)->(3)->(7)"
        result = str(lst)

        self.assertEqual(expected, result)


    def test_size(self):
        """
        Use code in test_prepend() to create the list 6, 3, 7.
        Call size() to test the method.
        """
        lst = UnorderedList()

        lst.prepend(7)
        lst.prepend(3)
        lst.prepend(6)
        lst.pop()
        lst.remove(3)

        expected = 1
        result = lst.get_size()
        self.assertEqual(expected, result)

    def test_search(self):
        """
        Use code in test_prepend() to create the list 6, 3, 7.
        Call search(7) and search(10) to test the full behavior of the method.
        """
        lst = UnorderedList()

        lst.prepend(7)
        lst.prepend(3)
        lst.prepend(6)

        expected = True
        result = lst.search(7)
        self.assertEqual(expected, result)

        expected = False
        result = lst.search(10)
        self.assertEqual(expected, result)


    def test_print(self):
        """
        Use code in test_prepend() to create the list 6, 3, 7.
        Call print() to test __str__() method.
        """
        lst = UnorderedList()
        lst.prepend(7)
        lst.prepend(3)
        lst.prepend(6)

        expected = "(6)->(3)->(7)"
        result = str(lst)
        self.assertEqual(expected, result)



    def test_append(self):
        """
        Create an empty unordered list object.
        Call append(7) and append(3) to test the method.
        """
        lst = UnorderedList()
        lst.append(7)
        lst.append(3)

        expected = "(7)->(3)"
        result = str(lst)
        self.assertEqual(expected, result)


    def test_pop(self):
        """
        Use code in test_append() to create the list 7, 3
        Call pop(7) and pop(10) to test the full behavior of the method.
        """
        lst = UnorderedList()
        lst.append(7)
        lst.append(3)

        expected = 3
        result = lst.pop()
        self.assertEqual(expected, result)

        expected = "(7)"
        result = str(lst)
        self.assertEqual(expected, result)


    def test_remove(self):
        """
        Use code in test_append() to create the list 7, 3
        Call remove(7) and remove(10) to test the full behavior of the method.
        """
        lst = UnorderedList()
        lst.append(7)
        lst.append(3)
        lst.append(6)

        result = lst.remove(7)
        expected = 7
        self.assertEqual(expected, result)

        result = lst.remove(10)
        expected = None
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

