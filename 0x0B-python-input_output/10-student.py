#!/usr/bin/python3
"""
 class Student that defines a student
"""
import json
class Student:
    """ 
    defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        initialize an instance

        Args:
            first_name: the first name
            last_name: the last name
            age: age of the object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method  that retrieves a dictionary representation of a Student
        """
        return self.__dict__
