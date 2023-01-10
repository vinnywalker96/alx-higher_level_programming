#!/usr/bin/python3
"""returns True if the object is exactly an instance 
of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """"Checks if object is an instance of a class

    Args:
        obj (object): object argument
        a_class (class): class argument

    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
