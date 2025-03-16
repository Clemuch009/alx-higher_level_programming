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

    @height.setter
    def height(self, value):
        """ set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """ returns the are of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ print the area and the perimeter """
        if self.__height or self.__width == 0:
            return ""

        return "\n".join("#" * self.__width for _ in range(self.__height))
