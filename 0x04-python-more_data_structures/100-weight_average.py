#!/usr/bin/python3

def weight_average(my_list=[]):
    add = 0
    total = 0
    for tupl in my_list:
        for i in tupl:
            add += (tupl[0] * tupl[1])
            total += tupl[1]
    return (add / total)
