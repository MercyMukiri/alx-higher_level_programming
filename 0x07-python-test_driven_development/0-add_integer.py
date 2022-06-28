#!/usr/bin/python3
"""
This module is made up of a function that adds two numbers
"""


def add_integer(a, b=98):
    """This functions adds two integers/float numbers
    Args: a: first number
          b: second number, the default is 98
    Returns: The sum of the two arguments
    Raises: TypeError if a or b are not integers/float numbers
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
