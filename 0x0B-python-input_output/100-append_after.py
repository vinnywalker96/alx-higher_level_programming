#!/usr/bin/python3
"""Search and update"""
import os


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string 
    Args:
        search_string (str)
        new_string (str)
    """
    with open(filename, encoding="utf-8") as f:
        if search_string in f.read():
            with open(filename, mode="a", encoding="utf-8") as f:
                f.write(new_string)
