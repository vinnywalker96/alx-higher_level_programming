#!/usr/bin/python
"""
Define function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
