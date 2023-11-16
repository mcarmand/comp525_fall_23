"""
Create a Python function that reverses a string using a Stack. For example,
string_reverse("I really love data structures") should return
"serutcurts atad evol yllaer I".

- Use appropriate function docstrings.
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.
"""

def string_reverse(input_str):
    """
    Reverses a string using a stack data structure.

    Time complexity: O(n)

    args:
    s (str): The string to reverse.

    returns: str: The reversed string.
    """
    stack = []

    for char in input_str:
        stack.append(char)

    reversed_string = ''
    while stack:
        reversed_string += stack.pop()

    return reversed_string

reversed_string = string_reverse("I really love data structures")
print(reversed_string)

