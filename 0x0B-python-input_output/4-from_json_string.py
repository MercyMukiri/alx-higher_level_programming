#!/usr/bin/python3
""" This module has a function that returns an object
   (Python data structure) represented by a JSON string """

import json


def from_json_string(my_str):
    """ This function returns an object represented by a JSON string
    Args:
        my_str: JSON string representation of an object
    Raises:
        Exception: when it fails to encode object
    """

    return (json.loads(my_str))
