#!/usr/bin/python3
def max_integer(my_list=[]):
     biggest = my_list[0]
     
     if my_list == None:
         return None

      for i in my_list:
          if i > biggest:
              return biggest
