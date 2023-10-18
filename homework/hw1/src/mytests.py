from my_list import ( count, extend, remove, index )

def count_test():
    """
    Test count function
    """
    test_input = [5, 10, 15, 20, 67, 12, 3]
    test_value = 5
    expected = 1
    result = count(test_input, test_value)

    print(f"Expected {expected}, result was {result}")


def extend_test():
    """
    Test extend function
    """
    list_one = [1, 2, 3]
    list_two = [5, 4, 1]
    expected = [1, 2, 3, 5, 4, 1]
    result = extend(list_one, list_two)

    print(f"Expected {expected}, result was {result}")


def remove_test():
    """
    Test remove function
    """
    test_input = [12, 50, 3, 1]
    test_value = 50
    expected = [12, 3, 1]
    result = remove(test_input, test_value)

    print(f"Expected {expected}, result was {result}")


def index_test():
    """
    Test index function
    """
    test_input = [12, 50, 3, 1]
    test_value = 50
    expected = 1
    result = index(test_input, test_value)

    print(f"Expected {expected}, result was {result}")


if __name__ == "__main__":
    count_test()
    extend_test()
    remove_test()
    index_test()
