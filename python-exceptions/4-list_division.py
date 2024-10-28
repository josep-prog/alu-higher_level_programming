#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element of two lists.

    Args:
        my_list_1: First list of elements.
        my_list_2: Second list of elements.
        list_length: Desired length of the result list.

    Returns:
        A new list containing the results of the divisions.
    """
    new_list = []

    for i in range(list_length):
        quotient = 0  # Default value for quotient

        if i >= len(my_list_1):
            print("out of range")
        elif i >= len(my_list_2):
            print("out of range")
        else:
            try:
                if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                    quotient = my_list_1[i] / my_list_2[i]
                else:
                    raise TypeError
            except ZeroDivisionError:
                print("division by 0")
            except TypeError:
                print("wrong type")

        new_list.append(quotient)

    return new_list
