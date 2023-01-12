#!/usr/bin/python3
"""Define write_file function"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, encoding="utf-8", mode="w") as f:
        return f.write(text)
