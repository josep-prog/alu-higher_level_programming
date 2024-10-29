#!/usr/bin/python3


"""Defines a class Square"""


class Square:
    """Class that defines properties of a square."""

    def __init__(self, size=0):
        """Creates new instances of square."""
        self.size = size  # Use the setter

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2