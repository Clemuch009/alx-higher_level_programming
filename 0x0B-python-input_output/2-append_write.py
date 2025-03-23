#!/usr/bin/python3
""" creates a append_write function """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file and returns the number of characters added """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
