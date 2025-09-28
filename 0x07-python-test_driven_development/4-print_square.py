#!/usr/bin/python3
"""
Prints a square with the character #.
"""


def print_square(size):
    """
    Prints a square with the character #

    Args:
       size (int): size of square to print

    >>> print_square(4)
    ####
    ####
    ####
    ####

    >>> print_square("h")
    Traceback (most recent call last):
    ...
    TypeError: size must be an integer

    >>> print_square(-1)
    Traceback (most recent call last):
    ...
    ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
