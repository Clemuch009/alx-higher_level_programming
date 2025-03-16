#!/usr/bin/python3
""" create a square"""
class Square:
    """ define square shape"""
    def __init__ (self, size=0):
        """ a constructor tha initializes  size of a square"""
        if not isinstance(size, int):
            
            raise TypeError("size must be an integer")
        

        if size < 0 :
            raise ValueError ("size must be >= 0")

        self.__size = size       
