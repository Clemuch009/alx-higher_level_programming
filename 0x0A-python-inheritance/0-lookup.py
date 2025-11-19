#!/usr/bin/python3
"""
function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    
    Args:
        obj: object to look for attributes and methods.
    """
    return (dir(obj))
