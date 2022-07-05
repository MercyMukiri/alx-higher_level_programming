#!/usr/bin/python3
""" Module that has a function which writes a string file """


def append_write(filename="", text=""):
    """ This function appends a string to the end of a file
    Args:
        filename (string): Name of input file
        text (string): Output text
    Raises:
        Exception: When file fails to open
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
