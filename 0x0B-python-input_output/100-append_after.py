#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string 
    Args:
        search_string (str)
        new_string (str)
    """
    with open(filename, "a+") as f:
        file_content = f.read()
        for word in file_content:
            if word == search_string:
                continue
            f.write(new_string)
