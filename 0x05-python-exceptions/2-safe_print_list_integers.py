#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range (my_list):

            try:
                print ("{:d}".format(my_list=[i]), end="")
                count +=1
            except (ValueError, TypeError):
                pass

    except IndexError:
        pass

    print()
    return count


