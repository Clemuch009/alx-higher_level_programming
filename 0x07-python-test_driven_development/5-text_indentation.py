#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for( '.' , ',', '?' ':' ) in text:
        print("\n")
        print("\n")
