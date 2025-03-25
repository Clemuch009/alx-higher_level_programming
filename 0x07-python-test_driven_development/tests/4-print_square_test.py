#!/usr/bin/python3
def print_square(size):
    """ print square using # according to the size
    
    args:
        size : an integer the determine the number of #s to be printed

    Exceptions:
           TypeError
           ValueError:

    >>>print_square(4)
    ####
    ####
    ####
    ####

    >>>print_square(-1)
    traceback(most recent call last)

    ...
    ValueError:size must be >= 0



    >>>print_square("hello")

    traceback(most recent call last)
    ...
    TypeError:size must be an integer



    >>>print_square(0.1)
    traceback(most recent call last)

    ...

    TypeError:size must be an integer

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance (size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _in range(size):
        print('#' * size)                                               ~                                                                       ~                                                                       ~                                       
