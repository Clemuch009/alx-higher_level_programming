#!/usr/bin/python3
""" creates write_file function """


def write_file(filename="", text=""):
    """ writes a string to a text file  """
    with open(filename, "w" encoding="UTF-8") as f:
        return f.write(text)
