#!/usr/bin/python3
"""
This module defines the lookup function, which returns a list of all attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of all available attributes and methods of an object.
    
    Args:
        obj: The object whose attributes and methods are to be listed.
        
    Returns:
        list: A list of attributes and methods of the object.
    """
    return dir(obj)
