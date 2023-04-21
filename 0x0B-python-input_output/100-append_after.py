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
    with open(filename, "r") as f, open(temp, "w") as data:
        for line in f:
            data.write(line)
            if search_string in line:
                data.write(new_string)
    with open(temp, 'r') as f, open(filename, 'w') as data:
        for line in f:
            data.write(line)
