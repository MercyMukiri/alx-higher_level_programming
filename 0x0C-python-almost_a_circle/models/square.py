#!/usr/bin/python3

""" This module defines a Square class that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class defines a Square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization of the Square instance

            Args:
                size (int): size
                x (int): position
                y (int): position
                id (int): id
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns a strong representation of the Square """

        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

    @property
    def size(self):
        """ getter function for size """

        return self.width

    @size.setter
    def size(self, value):
        """ setter function for size

            Args:
                value (int): value to be set
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns key/value arguments to attributes of an instance.

            Args:
                *args: variable number of no-keyword args
                *kwargs: variable number of keyword args
        """

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """

        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
