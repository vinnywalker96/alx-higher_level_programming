#!/usr/bin/python3

"""Defines class Rectangles"""


class Rectangle:
    """Representation of a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing a new rectangle
            Args:
                width (int): Width of rectangle
                height (int): Height of rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get/set width of rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns current area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns current perimeter of rectangle"""
        res = 0
        if self.__width == 0 or self.__height == 0:
            res = 0
        else:
            res = ((self.__width + self.__height) * 2)

        return res
    	
    def __str__(self):
        """Print represetation of a rectangle object"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        for row in range(self.__height):
            for col in range(self.__width):
                str += "#"
            if row != self.__height -1:
                str += "\n"
        return str
