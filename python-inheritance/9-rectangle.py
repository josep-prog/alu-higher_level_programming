#!/usr/bin/python3
"""Defines a class Rectangle based on 8-base_geometry.py."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Creates new instances of Rectangle.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calculates area of a rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
