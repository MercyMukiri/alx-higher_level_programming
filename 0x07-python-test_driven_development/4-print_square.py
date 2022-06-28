#!/usr/bin/python3
"""
4-print_square module

This module contains a function that prints a square with the # character
"""


def print_square(size):
    """ This function prints a square with the character #
    Args: size: size of the square printed
    Raises: TypeError: If size is not an integer number
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print('#' * size)
