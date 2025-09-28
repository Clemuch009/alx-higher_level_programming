#!/usr/bin/ python3

class Square:
    def __init__(self, size = 0, position = (0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position
    
    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError(" size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()

        else:
            for h in range(self.__size):
                print("#" * self.__size)
    @pro`perty
    def position(self):
        return self.__position

    @position.setter
    def postion(self, value):
        if (
                len(value) != 2
                or not isinstance(value, tuple) 
                or not all(x >= 0 in value)
                or not all(isinstance(x, int)for x in value)
                ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
