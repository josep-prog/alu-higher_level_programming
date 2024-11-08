#!/usr/bin/python3
"""
This module defines the MyList class, which inherits from the built-in list class and adds
a method to print the list in sorted order.
"""

class MyList(list):
    """
    A subclass of the built-in list class with a method to print the list sorted.
    """
    
    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
