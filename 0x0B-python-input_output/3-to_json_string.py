#!/usr/bin/python3
""" This module has a function that returns
   the JSON representation of an object (string) """

import json


def to_json_string(my_obj):
    """ This function returns the JSON representation of an object (string)
    Args:
        my_obj: Object to be returned in JSON
    Raises:
        Exception: when it fails to encode object
    """

    return (json.dumps(my_obj))
