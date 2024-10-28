#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.
    my_list can contain any type (integer, string, etc.)
    You have to use try: / except:
    You are not allowed to import any module.
    All integers have to be printed on the same line followed by a new line,
    - other type of value in the list must be skipped (in silence).
    You are not allowed to use len().

    Args:
        my_list: List of elements.
        x: Number of elements to access in my_list.

    Returns: 
        The real number of integers printed.
    """
    count = 0
    index = 0

    while index < x:
        try:
            if isinstance(my_list[index], int):
                print("{:d}".format(my_list[index]), end="")
                count += 1
            index += 1
        except IndexError:
            break

    print()
    return count
