#!/usr/bin/python3
"""
defines a class Base
"""


class Base:
    """
    create a blueprint
    """
     __nb_objects = 0

     def __init__(self, id=None):
         """
         initializes new instances

         Args:
             id: unique indentification of an instance

        """
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
