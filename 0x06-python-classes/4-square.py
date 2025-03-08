#!/usr/bin/python3
class Square:
    """ define square shape"""
    def __init__ (self, size=0):
        """ initiate size"""
        if not isinstance(size, int):

            raise TypeError("size must be an integer")


        if size < 0 :
            raise ValueError ("size must be >= 0")

        self.__size = size
        """ assign size"""

    def area (self):
        """ return the area of a square"""
        return self.__size * self.__size
    
    def get_size(self):
        """ get the value of size"""
        return self.__size
    
    def set_size(self, value):
        """ set a new value of size"""
          """Set a new value for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
