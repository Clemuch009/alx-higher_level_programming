#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [i % 2 == 0 for i in my_list]
print(divisible_by_2([1,2,3,4,5,6,]))
