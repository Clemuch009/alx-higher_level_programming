#!/usr/bin/python3
"""
class Square that inherits from Rectangle
"""


Rectangle = __import__('rectangle').Rectangle

class Square(Rectangle):
    """
    Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes a new instance with these attributes

        Args:
            size: dimenision of the object
            x: x-coordinate
            y: y-coordinate
            id: indetification of the instance

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
         return b description of the square
        """
        return f" [Square] ({self.id}) {x}/{y} - {self.__height}"

    @property
    def size(self):
        return self.__height

    @size.setter
    def size(self, value):
        self.__width = valufe
        self.__height = height
    
    def update(self, *args, **kwargs):
        """
        assigns attributes

        Args:
            args: tuple of values to set
            kwargs: key-value pair to add
        """
        if args not None:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                if hasattr(self, size) and i == 1:
                    self.width = value
                    self.height = value
                else:
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        return self.__dict__
