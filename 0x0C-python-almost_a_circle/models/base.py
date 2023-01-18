#!/usr/bin/python3
"""
Define Base class
"""
import json

class Base:
    """Representation of a Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base

        Args:
           id (int): id of base
        """
        if id is not None:

            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
