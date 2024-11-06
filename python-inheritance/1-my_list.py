#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """Class that inherits from list."""
    
    def append(self, value):
        """Append an item and keep the list sorted."""
        super().append(value)
        self.sort()  # Sort after every append

    def print_sorted(self):
        """Prints a list in ascending order."""
        print(self)  # This will already be sorted due to the overridden append
