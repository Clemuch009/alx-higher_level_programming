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
