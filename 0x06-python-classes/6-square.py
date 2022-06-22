#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize the square object.
        Args:
            size (int): This defines the size of the square.
            position (tuple): This defines the position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """This method returns the size of a square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object.
        Args:
            size (int): This defines the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Method that returns the position value"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Method that sets the position value of a square object.
        Args:
            value (tuple): This defines the position of the square.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method thatt return the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Method that prints a # square"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
