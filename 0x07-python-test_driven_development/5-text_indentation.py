#!/usr/bin/python3

"""Defines function at that indent text"""


def text_indentation(text):
    """Prints a text with 2 new lines 
       after each of these characters:

    Args:
        text (str): argument as form of a string

    Raises:
        TypeError: if text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    string_len = 0

    while string_len < len(text) and text[string_len] == " ":
        string_len += 1
    while string_len < len(text):
        print(text[string_len], end="")
        if text[string_len] in ".?:":
            print("\n")
        string_len += 1
        while string_len < len(text) and text[string_len] == " ":
            string_len += 1
        continue
    string_len += 1
