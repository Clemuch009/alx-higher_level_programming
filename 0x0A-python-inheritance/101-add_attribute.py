#!/usr/bin/python3
"""
 function that adds a new attribute to an object if it’s possible
"""

def new_attr(obj, key, value):
    """
    adds a new attribute to an object if it’s possible.
    Args:
        obj: object to add attribute
        key: key
        value: attribute to add
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute ")
    setattr(obj, key, value)

