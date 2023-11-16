"""
Create a Python function that calculates the factorial of a given non-negative
 integer using recursion. The function should take an integer as input and
 return its factorial. For example, factorial(5) should return 120.

- Use appropriate function docstrings.
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.
"""

def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Time complexity: O(n)

    args:
    n (int): A non-negative integer whose factorial will be calculated.

    returns: int: The factorial of the input number.
    """

    if n in (0, 1):
        return 1

    return n * factorial(n-1)


factorial_value = factorial(5)
print(f"the factorial of 5 is {factorial_value}")

