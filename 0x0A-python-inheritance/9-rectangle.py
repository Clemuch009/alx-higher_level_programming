#!/usr/bin/python3
"""
 class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

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

    def area(self):
        """
        returns the area of an instance
        """
        return self.__width * self.__height
    
    def __str__(self):
        """
        should return, the  rectangle description
        """
        return f"[rectangle] {width}/{height}"
