#!/usr/bin/python3

def safe_print_division(a, b):
    div = None
    try:
        div = int(a) / int(b)
    except (ZeroDivisionError, TypeError):
        div = None
    finally:
        print("inside result: {}".format(div))
    return div
