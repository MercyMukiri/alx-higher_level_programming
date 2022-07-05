#!/usr/bin/python3
""" This module returns the dictionary description with a simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
"""


def class_to_json(obj):
    """ This function retuns the dictionary description
    for JSON serialization of an object
    Args:
        obj: Object whose dictionary description is returned
    """

    return obj.__dict__
