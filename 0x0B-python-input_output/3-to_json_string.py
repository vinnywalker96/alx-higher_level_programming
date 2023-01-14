#!/usr/bin/python3
import json
"""
Define to_json_string function
"""


def to_json_string(my_obj):
    """returns the JSON representation of an object

    Args:
        my_obj (str): representation of an object
    """
    return json.dumps(my_obj)
