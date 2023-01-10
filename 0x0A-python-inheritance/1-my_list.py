#!/usr/bin/python3
"""
Defines class MyList
"""


class MyList(list):
    """Creates a subclass of List"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
