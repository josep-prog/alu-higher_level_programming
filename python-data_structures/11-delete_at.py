#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Function that deletes the item at a specific position in a list.

    If idx is negative or out of range, return the same list.
    You are not allowed to use pop().
    You are not allowed to import any module.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Create a new list excluding the element at the specified index
    new_list = my_list[:idx] + my_list[idx + 1:]

    return new_list
