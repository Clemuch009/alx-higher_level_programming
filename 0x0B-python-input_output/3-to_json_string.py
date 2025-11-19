#!/usr/bin/python3
"""
a function that returns the JSON representation of an object (string)
"""

import json

def to_json_string(my_obj):
    """
     returns the JSON representation of an object (string)

     Args:
         my_obj: object to turn to json representation.

    Return: the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
