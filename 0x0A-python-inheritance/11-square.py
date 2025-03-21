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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """
     def __init__(self, width, height):
            """ initializes attributes """
            self.integer_validator('width', width)
            self.integer_validator('height', height)
            self.__height = height

    def area(self):
        """ returns the area """
        return self.__height * self.__width

    def __str__(self):
        """ returns the description of the rectangle """
        return (f"[Rectangle] {self.__width}/{self.__height")

class Square(Rectangle):
    """ create square class """
    def __init__(self, size):
        """ initialize attributes """
        self.integer_validator('size' , size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ return the area of a square """
        return self.__size * self.__size

    def __str__(self):
        """returns string representation of a square """
        return f"[Square] {self.__size}/{self.__size}"
