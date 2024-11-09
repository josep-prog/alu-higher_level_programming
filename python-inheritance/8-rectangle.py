#!/usr/bin/python3
"""Defines a class Rectangle based on 7-base_geometry.py.

Attributes:
    width (int): width of the rectangle.
    height (int): height of the rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Creates a new instance of Rectangle.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        # Validate before assigning to private variables
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Now assign to the private variables after validation
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width} - {self.__height}"

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height
