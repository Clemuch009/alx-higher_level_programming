#!/usr/bin/python3
"""
 class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""
from  7-base_geometry import BaseGeometry

class  Rectangle(BaseGeometry):
    """
     inherits from BaseGeometr
     """
    def __init__(self, width, height):
        """
        initializes instance's attribues
        Args:
            width: width of object
            height: height of the object
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
