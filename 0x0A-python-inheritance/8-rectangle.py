#!/usr/bin/python3
""" creates BaseGeometry class """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ return exception if area is none"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """  validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ creates rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
