#!/usr/bin/python3
"""
a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    with open(filename, 'r', encoding='UTF8') as f:
        content = f.read()
        for row in content:
            print(row, end="")
