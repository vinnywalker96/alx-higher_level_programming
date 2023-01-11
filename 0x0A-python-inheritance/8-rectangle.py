#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Define class Rectangle"""


class Rectangle(BaseGeometry):
    """"Represents a Rectangle"""
    def __init__(self, width, height):
        """Initializes the object"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
