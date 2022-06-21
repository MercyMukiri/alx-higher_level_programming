#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """This class has a private size attribute"""

    def __init__(self, size=0):
        """ Method to initialize the square object
        Args:
             size (int): This defines size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = int(size)
