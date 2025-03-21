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
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
