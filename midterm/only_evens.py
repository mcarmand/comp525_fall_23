"""
Write a Python function that takes a list of integers as input and returns a
new list with only the even numbers. For example, if the input is
[1, 2, 3, 4, 5, 6], the function should return [2, 4, 6].

- Use appropriate function docstrings.
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.
"""

def filter_even_numbers(numbers_list):
    """
    Filters out all the even numbers from a list of integers and returns a new list containing only these even numbers.

    Time complexity: O(n)

    args:
    numbers_list (list of int): A list of integers to filter.

    returns: list of integers: A list containing only the even numbers from the input list.
    """

    even_numbers = []
    for num in numbers_list:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


input_list = [1, 2, 3, 4, 5, 6]
filtered_list = filter_even_numbers(input_list)
print(f"[1, 2, 3, 4, 5, 6] filtered is: {filtered_list}")

