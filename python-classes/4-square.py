#!/usr/bin/python3


"""Defines a class Square"""


class Square:
    """Class that defines properties of a square."""

    def __init__(self, size=0):
        """Creates new instances of square."""
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square."""
        return f"Square(size={self.__size})"
