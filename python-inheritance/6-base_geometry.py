#!/usr/bin/python3
"""Defines a class BaseGeometry based on 5-base_geometry.py"""


class AreaNotImplementedError(Exception):
    """Custom exception for unimplemented area method."""
    pass


class BaseGeometry:
    """Class BaseGeometry."""
    def area(self):
        """Area function.

        Raises:
            AreaNotImplementedError: if area is not implemented.
        """
        raise AreaNotImplementedError("area() is not implemented")
