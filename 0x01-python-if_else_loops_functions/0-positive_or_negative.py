#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print (f"the {number} is positive")

elif number == 0:
    print("the {}is zero".format(number))

else:
          print("the {} is negative".format(number))
