#!/usr/bin/python3

"""Define print_square function"""

def print_square(size):
    """Prints a square withe the character #

    Args:
        size (int): The size of the square

    Raises:
        TypeError: if size not an integer
        ValueError: if size < 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        [print("#", end="") for col in range(size)]
        print("")
    

