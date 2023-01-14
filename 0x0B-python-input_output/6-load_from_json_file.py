#!/usr/bin/python3
"""define load_from_file function"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file"

    Args:
       filename (str): input to load the json file
    """
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)

    return data
