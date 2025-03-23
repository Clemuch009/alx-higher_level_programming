#!/usr/bin/python3
""" creates write_file function """


def write_file(filename="", text=""):
    """ writes a string to a text file and returns the number of characters written """
    with open(filename, "w" encoding="UTF-8") as f:
        return f.write(text)
