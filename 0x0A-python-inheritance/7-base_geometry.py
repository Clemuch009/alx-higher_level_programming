#!/usr/bin/python3
"""
 an empty class BaseGeometry.
 """
 

class BaseGeometry:
    """
    an empty
    """
    def area(self):
        """
        Public instance hat raises an Exception
        """
        raise Exception("area() is not implemented")
     
    def integer_validator(self, name, value):
        self.name = name
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an interger")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
