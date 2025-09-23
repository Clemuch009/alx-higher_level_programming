#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    return (set_1 ^ set_2)
import dis
print(dis.dis(only_diff_elements))
