#!/usr/bin/python3
"""
 class Square that inherits from Rectangle (9-rectangle.py):
"""

Rectangle = __import__('9-rectangle.py').Rectangle

class Square(rectangle):
    """
    Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        initializes size of object after validation
        """
        self.integer_validator("size", size)
        self.__size = size
    
    def area(self):
        """
        returns area of square
        """
        return self.__size ** 2

    def __str__(self):
        """
        return, the square description
        """
        return f"[square] {width}/{height}"

