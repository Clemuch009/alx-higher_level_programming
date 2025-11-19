#!/usr/bin/python3
"""
a function that appends a string at the end of a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8) and returns the number of characters added:
     Args:
         filename: name of the file to append
         text: string to add in the file
    
    Return: number ot character added in the file
    """
    with open(filename, 'a', encoding= 'UTF8') as f:
        number = f.write(text)
    return number
