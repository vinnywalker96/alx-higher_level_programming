#!/usr/bin/python3
""""Define function lookup"""


def lookup(obj):
    """Return a list of available
    attributes and method of the object

    Args:
        obj (list): argument
    """
    return dir(obj)
