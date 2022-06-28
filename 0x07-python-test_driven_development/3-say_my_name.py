#!/usr/bin/python3
"""
3-say_my_name module

This module contains a function that prints a message of strings supplied
"""


def say_my_name(first_name, last_name=""):
    """ Function that prints "My name is <first name> <last name>"
    Args: first_name: first name
          last_name: last name

    Raises: TypeError: If first_name or last_name is not a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
