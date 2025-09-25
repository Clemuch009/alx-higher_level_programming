#!/usr/bin/python3
"""Adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Take two parameters and return their sum as integers.
    a and b must be integers or floats, otherwise raise a TypeError.
    Floats are cast to integers before the addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

