#!/usr/bin/python3
""" creates def class_to_json """


class Myclass:
    """ creates Myclass class """
    def __init__(self, name):
        """ initializes attributes """
        self.name = name
        self.number = 0

    @staticmethod
    def class_to_json(obj):
        """ convert obj to json """
        if isinstance(obj, Myclass):
            return obj.__dict__
