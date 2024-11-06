#!/usr/bin/python3
"""Returns a function lookup()"""

def lookup(obj):
    """Function that returns the list of available attributes and methods
    of an object.

    Args:
        obj (class): object

    Returns:
        list: list of available attributes and methods of an object
    """
    return list(vars(obj).keys()) + [method for method in dir(obj) if callable(getattr(obj, method))]
