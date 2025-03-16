#!/usr/bin/python3


""" create a rectangle class """


class Rectangle:
    """
    initializes rectangle class
    args:
       width : the dimension of the longer side
       height: the dimension of the smaller side
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ retrive the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """ retrive the height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """ set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return self.__width

    @height.setter
    def height(self, value):
        """ set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("eight must be >= 0")
        self.__height = value
        return self.__height

    def area(self):
        """ returns the are of the rectangle """
        return widht * height

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if width or height == 0:
            return 0
        return 2 * (width * height)
