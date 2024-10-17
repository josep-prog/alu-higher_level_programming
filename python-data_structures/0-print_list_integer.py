#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Print integers from a list, one per line.
    
    Assume the list only contains integers.
    Use str.format() to print.
    """
    for integer in my_list:
        print("{:d}".format(integer))
