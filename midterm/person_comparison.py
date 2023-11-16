"""
Create a Python class Person with attributes for a person's name and age.
Implement a method to compare the ages of two people, returning a message that
indicates who is older. For example, if person1 is 30 years old and person2 is
25 years old, calling person1.compare_age(person2) should return
"person1 is older."

- Use appropriate function docstrings.
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.
"""

class Person:
    """
    A class to represent a person with a name and age, and to compare ages between two people.

    attributes:
    name (str): The name of the person.
    age (int): The age of the person.

    Time complexity: O(1)
    """

    def __init__(self, name, age):
        """
        constructs all the necessary attributes for the person object

        args:
        name (str): The name of the person.
        age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def compare_age(self, other):
        """
        Compares the age of this person with another person's age and returns a message indicating who is older

        args:
        other (Person): Another person object to compare age with.

        returns: str: A message indicating which person is older or if they are the same age.
        """
        if self.age > other.age:
            return f"{self.name} is older."
        elif self.age < other.age:
            return f"{other.name} is older."
        else:
            return f"{self.name} and {other.name} are the same age."

person1 = Person("person1", 30)
person2 = Person("person2", 25)
result = person1.compare_age(person2)
print(result)

