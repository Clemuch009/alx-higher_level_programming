#!usr/bin/python3
"""
defines class Rectangle that inherits from Base
"""


Base = __import__('base').Base

class Rectangle(Base):
    """
    class Rectangle that inherits from Base

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes the instance of Recatngle

        Args:
            width: dimension of width
            height: dimmension of rectangle
            x : location in coordinate
            y: location in coordinate
            id: inditification

        """
        super().__init__(id)
        self.__width = width
        self.__height = heigth
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an ineger")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

   @ height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an int")
        if value <= 0:
            raise ValueError("height must > 0")

        self.__height = value
    
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height
    def display(self):
        for _ in range(self.__height):
            print('#' * self.__width)
    def __str__(self):
        return f"[rectangle] ({self.id} {self.__x}/{self.__height} - {self.__width]/{self.__height")

    def update(self, *args):
        """
        updating the public method by changing the prototype

        Args:
            args: a tuple that takes variable number of argument

        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        for i, value in enumerate(args):
            setattr(self, attrs[i], value)
    
    def to_dictionary(self):
        """
        returns dictionary representation of the instance
        """
        return {
                "id": self.id,
                "height": self.width,
                "width": self.height,
                "x": self.x,
                "y": self.y
                }
