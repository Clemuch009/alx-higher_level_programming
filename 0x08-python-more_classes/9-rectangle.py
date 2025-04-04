#!/usr/bin/python3

"""Define a rectangle class with instance tracking."""


class Rectangle:
    """
    Defines a rectangle with width and height.
    Tracks the number of active instances.
    """

    # Public class attribute
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the rectangle and increment instance count."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment count

    @property
    def width(self):
        """Retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ print the area and the perimeter """
        if self.__height or self.__width == 0:
            return ""
        row = str(self.print_symbol) * self.width
        return "\n".join(row for _ in range(self.height))

    def __repr__(self):
        """Return a string representation that can recreate the instance"""
        return (f"Rectangle({self.__width}, {self.__height}")

    def __del__(self):
        """Print a message when an instance is deleted and decrement count."""
        Rectangle.number_of_instances -= 1  # Decrement count
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compares the areas of two rectangles and return the biggest one"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance where width == height == size."""
        return cls(size, size)
