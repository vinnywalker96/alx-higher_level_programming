#!/usr/bin/python3
"""
Define class Square that inherits from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set ths size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size,
                                      self.x, self.y)
                    else:
                        self.id = arg

                elif a == 1:
                    self.size = arg

                elif a == 2:
                    self.x = arg

                elif a == 3:
                    self.y = arg
                a += 1

        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.size,
                                      self.x, self.y)
                    else:
                        self.id = value
                elif key == 'size':
                    self.size = value

                elif key == 'x':
                    self.x = value

                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns Dictionary Representation of a Square"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.size)
