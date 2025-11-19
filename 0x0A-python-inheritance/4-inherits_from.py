#!/usr/bin/python3
"""
a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
"""

def inherits_from(obj, a_class):
    """
     returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

     Args:
         obj: object to check
         a_class: class to check against
     
     Return: bool
     """
     p_class = type(obj)
     return issubclass(p_class,a_class) and p_class is not a a_class
