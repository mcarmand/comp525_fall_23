"""
node.py
Jon Shallow
Mason Armand
Nov 8, 2023
"""

class Node:
    """
    Class representation of Node
    """

    def __init__(self, data):
        """
        Constructor

        :param data: the data for the node
        :type data: any
        """
        self.data = data
        self.next = None
        self.previous = None

    def get_data(self):
        """
        Gets the data from the node

        :return: the data in the node
        :rtype: any
        """
        return self.data

    def set_data(self, new_data):
        """
        Set the new_data in the node

        :param new_data: the new data to set
        :type new_data: any
        """
        self.data = new_data

    def get_next(self):
        """
        gets the Next property

        :return: the next property
        :rtype: Node | None
        """
        return self.next

    def set_next(self, new_next):
        """
        Sets a new node the be the next property

        :param new_next: The next Node
        :type new_next: Node | None
        """
        self.next = new_next

    def get_previous(self):
        """
        gets the previous property

        :return: the previous property
        :rtype: Node | None
        """
        return self.previous

    def set_previous(self, new_previous):
        """
        Sets a new node the be the previous property

        :param new_previous: The previous Node
        :type new_previous: Node | None
        """
        self.previous = new_previous

    def __str__(self):
        node_str = ""
        if self.previous:
            node_str += f"({self.previous.data})<-"

        node_str += f"[{self.data}]"

        if self.next:
            node_str += f"->({self.next.data})"

        return node_str
