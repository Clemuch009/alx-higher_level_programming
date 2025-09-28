#!/usr/bin/python3
""" class Rectangle that defines a rectangle 
"""


class Rectangle:
    """"
    defines a rectangle 
    """

    def __init__(self, width=0, height=0):
        """
        initializes atrributes, hight and widht to each instance
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        to retrieve width
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        set width 
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """
        retrieves instance's height
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """changes or set height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height + self.__width) * 2)
    
    def __str__(self):
        if self.__height == 0 or self.width == 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            rect_str += '#' *self.__width
        return rect_str

    def __repr__(self):
        return f"Rectangle{self.__height}, {self.__width}"
