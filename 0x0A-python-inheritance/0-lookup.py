#!/usr/bin/python3


""" look for methods and attributes that can be access by object"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return dir(obj)
