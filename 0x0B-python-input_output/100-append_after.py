#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string 
    Args:
        search_string (str)
        new_string (str)
    """
    temp = filename + '.tmp'
    with open(filename, mode="a+", encoding="utf-8") as f:
        for line in f:
            if search_string in line:
                f.write(new_string)

