#!/usr/bin/python3
""" cerates module """


class Student:
    """ create a student class """
    def __init__(self, first_name, last_name, age):
        """ initialize attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ converts obj to json initialable """
        if isinstance(obj, Student):
            return obj.__dict__
