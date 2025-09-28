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
         """ changes or set height value
         """
         if not isinstance(value, int):
             raise TypeError("height must be an integer")
         if value < 0:
             raise ValueError("height must be >= 0")
         self.__height = height
