#!/usr/bin/python3
""" Class Square that defines a square"""


class Square:
    """This class has a private size attribute"""
    def __init__(self, size):
        """Initialize method that stores the size of the square
        Args:
             size (int): Defines size of square
        """
        self.__size = size
