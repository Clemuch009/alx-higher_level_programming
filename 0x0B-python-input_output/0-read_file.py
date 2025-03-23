#!/usr/bin/python3
""" creates a read_file function """


def read_file(filename=""):
    """ reads a text file and prints it to stdout """
    with open(filename, encoding="UTF-8") as f:
        file_data = f.read()
        print(file_data)
