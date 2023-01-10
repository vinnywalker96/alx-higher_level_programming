#!/usr/bin/python3
"""
Define a class BaseGeometry
"""


class BaseGeometry:
    """Representation of a  BaseGeometry"""

    def area(self):
        """Not Implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integers"""
        if type(obj) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))
