#!/usr/bin/python3
"""
101-locked_class module

This module contains a locked class
"""


class LockedClass:
    """LockedClass defines a class that pevents the user from
    dynamically creating new instance attributes
    except if the new instance variable is called first_name"""
    __slots__ = ['first_name']
