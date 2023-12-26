"""
unorderedlist.py
Jon Shallow
Mason Armand
Nov 8, 2023
"""

from node import Node

class UnorderedList:
    """
    Class representation of an UnorderedList
    """

    def __init__(self):
        """
        Constructor
        """
        self.head = None
        self.tail = None
        self.size = 0

    def prepend(self, item):
        """
        Create node that has item and make it the first element in the
        unordered list.
        :param item: integer
        """
        new_node = Node(item)
        new_node.next = self.head
        if self.head:
            self.head.previous = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def get_size(self):
        """
        Count the number of elements in the unordered list.
        :return: integer
        """
        return self.size

    def is_empty(self):
        """
        Check whether the unordered list has no nodes.
        :return: True if the unordered list object doesn't have any eleemnt.
        """
        return self.head is None

    def search(self, item):
        """
        Search for item in the unordered list.
        :param item: integer
        :return: True if item found. False otherwise.
        """
        curr_node = self.head
        while curr_node:
            if curr_node.get_data() == item:
                return True
            curr_node = curr_node.get_next()
        return False

    def get(self, index):
        """
        get the node at a specific index in the list
        :param index: The index of the node to get
        :return: The node at the specified index, or None if index is out of bounds
        """
        if index >= self.size:
            return None
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            count += 1
            current = current.get_next()
        return None

    def append(self, item):
        """
        Create node that has item and make it the last element in the
        unordered list.
        :param item: integer
        """
        new_node = Node(item)
        if self.tail:
            self.tail.set_next(new_node)
            new_node.set_previous(self.tail)
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def pop(self):
        """
        pop and return the last item from the list.
        Removes the last item from the list and returns its value.
        :return: The value of the last item
        """
        if self.is_empty():
            return None
        last_data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        self.size -= 1
        return last_data

    def remove(self, item):
        """
        Remove the first occurrence of an item from the list.
        :param item: The item to be removed.
        :return: The value of the removed item
        """
        current = self.head
        while current:
            if current.get_data() == item:
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous

                self.size -= 1
                return current.data
            current = current.get_next()

        return None

    def __str__(self):
        """
        Create string representation of the unordered list object. The string
        shows the data items, separated by ','. If the list is empty, the
        string is empty string.
        :return: string
        """
        current = self.head
        list_str = ""
        while current:
            list_str += f'({current.get_data()})'
            if current.get_next():
                list_str += "->"
            current = current.get_next()
        return list_str

