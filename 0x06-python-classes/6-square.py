#!/usr/bin/python3
class Square:
    def __init__(self, size=0 ,position=(0, 0)):
        if  not isinstance(size , int):
            raise TypeError ("size must be an integer")
         
        if size < 0:
            raise ValueError  ("size must be >= 0")

        self.__size = size

    @property
    def size(self):
            return self.__size

    @size.setter
    def size(self, value):
            if  not isinstance(value , int):
                raise TypeError ("value must be an integer")

            if value < 0:
                raise ValueError  ("value must be >= 0")

            self.__size = value
            return self.__size

    def position(self):
          """Retrieve the position of the square."""
          return self.__position

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position


    @position.setter
    def position(self, value):
        if(
                not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(num , int) and num>= 0 for num in value)

          ):
            raise TypeError ("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size
    def my_print(self):
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")

        for _ in range (self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
