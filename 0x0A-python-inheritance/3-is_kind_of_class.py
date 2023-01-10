#!/usr/bin/python
"""
Define function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """Return True or False
    if obj is an instance or subclass
    of a class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
