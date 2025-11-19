#!/usr/bin/python3
"""
 function that writes an Object to a text file, using a JSON representation
"""

import json

def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation

    Args:
        my_obj: the object to the file
        filename: the file to write to

    """
    with open(filename, 'w', encoding='UTF8')  as f:
        json.dump(my_obj, f)
