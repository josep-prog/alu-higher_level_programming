#!/usr/bin/python3

class Rectangle:
    """Defines a class Rectangle."""
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        self.__validate_dimension(value, "width")
        self.__width = value

    @height.setter
    def height(self, value):
        self.__validate_dimension(value, "height")
        self.__height = value

    def __validate_dimension(self, value, name):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
