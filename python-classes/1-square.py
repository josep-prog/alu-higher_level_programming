#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """Class that defines properties of a square."""

    def __init__(self, size=0):
        """Creates new instances of square."""
        self.__size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
