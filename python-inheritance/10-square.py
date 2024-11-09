#!/usr/bin/python3
"""Defines a class Square based on 9-rectangle.py."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a class Square."""

    def __init__(self, size):
        """Creates new instances of class Square.

        Args:
            size (int): size of 1 side of square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)  # Calls Rectangle's constructor

    def area(self):
        """Calculates the area of a square.

        Returns:
            int: the area of the square.
        """
        return self.width ** 2  # Use inherited width from Rectangle

    def __str__(self):
        """Returns string representation of the square."""
        return f"[Square] {self.width}/{self.height}"
