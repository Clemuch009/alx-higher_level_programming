#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry:
    """ BaseGeometry class"""

    def area(self):
        """ raise an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value argument """
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if value < 0:
            raise ValueError(f"{value} must be greater than 0")

class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """
     def __init__(self, width, height):
            """ initializes attributes """
            integer_validator('width', width)
            integer_validator('height', height)
            self.__height = height

    def area(self):
        """ returns the area """
        return self.__height * self.__width
    
    def __str__(self):
        """ returns the description of the rectangle """
        return (f" [Rectangle] {self.__height}/{self.__height")
