#!/usr/bin/python3
"""
5-text_indentation module

This module contains a function that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """ This function prints 2 new lines after ".?:" characters
    Args: text: input string
    Raises: TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0

    for char in text:
        if i == 0:
            if char == ' ':
                continue
            else:
                i = 1

        if i == 1:
            if char == '.' or char == '?' or char == ':':
                print(char)
                print()
                i = 0
            else:
                print(char, end="")
