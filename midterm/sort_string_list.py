"""
Write a Python function that takes a list of strings and sorts them based on
the length of the strings, with the shortest strings coming first.
For example, if the input is ["apple", "banana", "cherry", "date"], the
function should return ["date", "apple", "cherry", "banana"].

- Use appropriate function docstrings.
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.
"""

def sort_strings(strings_list):
    """
    Sorts a list of strings based on the length of the strings
    The shortest strings come first in the sorted list

    Time complexity: O(n^2) because of selection sort which uses nested for loops
    could use a faster sorting algorithm like merge sort, but that wasnt in the requirements

    args:
    strings_list (list of str): A list of strings to sort.

    returns: list of str: The list of strings sorted by their lengths in ascending order.
    """
    sorted_list = strings_list.copy() # copy old list so original doesnt get modified

    for i in range(len(sorted_list)):
        min_index = i
        for j in range(i+1, len(sorted_list)):
            if len(sorted_list[j]) < len(strings_list[min_index]):
                min_index = j
        sorted_list[i], strings_list[min_index] = strings_list[min_index], strings_list[i]

    return sorted_list

input_list = ["apple", "banana", "cherry", "date"]
sorted_list = sort_strings(input_list)
print(sorted_list)

