#!/usr/bin/python3

class Square:
    """Define a square shape."""

    def __init__(self, size=0):
        """Initialize the square with a given size (default is 0)."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size  # Private attribute

    def get_size(self):
        """Retrieve the size."""
        return self.__size

    def set_size(self, value):
        """Set a new value for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value  # Update size

    size = property(get_size, set_size)  # Define property for size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the `#` character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
