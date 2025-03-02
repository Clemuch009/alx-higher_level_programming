#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_1, a_2 = ( tuple_a() + (0,0)[:2])
    b_1 ,b_2 = ( tuple_b() + (0,0)[:2])
    
    return ( a_1 + b_1, a_2 + b_2)


