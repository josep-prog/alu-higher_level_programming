#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print the integers of a list in reverse order.

    One integer per line.
    You are not allowed to import any module.
    You can assume that the list only contains integers.
    You are not allowed to cast integers into strings.
    You have to use str.format() to print integers.
    """
    for element in reversed(my_list):
        print("{:d}".format(element))
