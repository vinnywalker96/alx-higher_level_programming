#!/usr/bin/python3
"""Defines a class to json function"""


def class_to_json(obj):
    """Return a dictionary representation of a simple data structure"""
    return obj.__dict__
