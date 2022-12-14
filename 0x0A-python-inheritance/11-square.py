#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square using a rectangle"""

    def __init__(self, size):
        """Initializes a new Square
        Args:
            size (int): The size of the Square
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns area of Square"""
        return self.__size * self.__size

    def __str__(self):
        """Return a str representation of a square"""
        return "[{}] {}/{}".format(self.__class__.__name__, self.__size,
                                   self.__size)
