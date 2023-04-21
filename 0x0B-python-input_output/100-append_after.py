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
    temp = filename + '.tmp'
    with open(filename, encoding="utf-8") as f:
        with open(temp, mode="w", encoding="utf-8") as tmp_f:
            for line in f:
                tmp_f.write(line)
                if search_string in line:
                    tmp_f.write(new_string)
    os.replace(temp, filename)
    if os.path.isfile(temp):
        os.remove(temp)
