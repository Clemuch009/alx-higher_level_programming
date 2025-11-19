#!/usr/bin/python3
"""
 a function that writes a string to a text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
     writes a string to a text file (UTF8) and returns the number of characters written
     Args:
         filename: name of the file to write
         text: string to write to the file

    Return: number of character written in the file
    """
    with open(filename, 'w', encoding='UTF8') as f:
        number = f.write(text)
    return number
