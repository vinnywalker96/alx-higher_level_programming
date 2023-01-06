#!/usr/bin/python3

"""Defines class Rectangles"""


class Rectangle:
    """Representation of a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing a new rectangle
            Args:
                width (int): Width of rectangle
                height (int): Height of rectangle
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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
        symbol = ""
        if self.__width == 0 or self.__height == 0:
            return symbol

        for row in range(self.__height):
            for col in range(self.__width):
                symbol += str(self.print_symbol)
            if row != self.__height - 1:
                symbol += "\n"
        return symbol

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.
        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.
            Args:
             size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __repr__(self):
        """Return a string representation
        of the rectangle to be able to
        recreate a new instance
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
