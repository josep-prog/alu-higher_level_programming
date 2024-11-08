#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
It adds a method to print the list sorted in ascending order.
"""

class MyList(list):
    """
    MyList is a subclass of the built-in list class.
    This class adds a method `print_sorted` to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        
        The sorted() function is used to return a new sorted list, which is then printed.
        """
        print(sorted(self))
