#!/usr/bin/python3


def max_integer(my_list=[]):
    """Function that returns the biggest integer in a list.

    If the list is empty, return None.
    You can assume that the list only contains integers.
    You are not allowed to import any module.
    You are not allowed to use the builtin max().
    """

    if not my_list:
        return None

    max_value = my_list[0]  # Start with the first element

    for num in my_list:
        if num > max_value:
            max_value = num  # Update max_value if a larger number is found

    return max_value
