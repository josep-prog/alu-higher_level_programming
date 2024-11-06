#!/usr/bin/python3
"""Defines a class Square based on 9-rectangle.py."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a class Square that inherits from Rectangle.

    Args:
        Rectangle (Rectangle): rectangle class to inherit from.
    """

    def __init__(self, size):
        """Creates a new instance of class Square.

        Args:
            size (int): size of one side of the square.
        """
        self.integer_validator("size", size)  # Validate size
        self.__size = size  # Private attribute for size
        super().__init__(size, size)  # Initialize the Rectangle with width and height equal to size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2  # Area of the square is size squared
