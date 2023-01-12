#!/usr/bin/python3
"""Define write_file function"""


def write_file(filename="", text=""):
    with open(filename, encoding="utf-8", mode="w") as f:
        return f.write(text)
