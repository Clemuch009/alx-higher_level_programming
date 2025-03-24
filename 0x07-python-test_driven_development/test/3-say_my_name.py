#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """ prints the name of a person

    args:
         first_name : it is the first name of a person
         last_name : last name of a person

    exceptions:
              TypeError:first_name must be a string
              TypeError:last_name must be a string

     >>> say_my_name("john","kamau")
     My name is john kamau
     >>> say_my_name(2,"kamau")
     traceback(most recent call last)
     
     ...
      

      TypeError:first_name must be a string

       >>> say_my_name("kamau", 2)
     traceback(most recent call last)

     ...

     TypeError:last_name must be a string

     """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
