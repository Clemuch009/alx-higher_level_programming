#!/usr/bin/python3
""" defining the function"""
def print_square(size):
    """ print  square using # according to size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance (size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _in range(size):
        print('#' * size)
