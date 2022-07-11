#!/usr/bin/python3

""" This module defines a Rectangle class that inherits from Base """

from models.base import Base


class Rectangle(Base):
    """ This class defines a rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a Rectangle instance.

            Args:
                width (int): width
                height (int): height
                x (int): position
                y (int): position
                id (int): id
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter function for the width """

        return self.__width

    @property
    def height(self):
        """ getter function for the height """

        return self.__height

    @property
    def x(self):
        """ getter function for x """

        return self.__x

    @property
    def y(self):
        """ getter function for y """

        return self.__y

    @width.setter
    def width(self, value):
        """ setter function for the width

            Args:
                value (int): value to be set
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """ setter function for the height

            Args:
                value (int): value to be set
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """ setter function for x

            Args:
                value (int): value to be set
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """ setter function for y

            Args:
                value (int): value to be set
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ calculates the area of a rectangle """

        return self.__width * self.__height

    def display(self):
        """ prints to stdout the Rectangle instance with the # character """

        rectangle = ""

        print("\n" * self.y, end="")

        for i in range(self.height):
            rectangle += (" " * self.x) + ("#"*self.width) + "\n"

        print(rectangle, end="")

    def __str__(self):
        """ returns a string representation of the Rectangle """

        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                             self.__x, self.__y,
                                             self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ assigns key/value arguments to attributes of an instance.

            Args:
                *args: variable number of no-keyword args
                **kwargs: variable number of keyword args
        """

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """ returns the dictionary representation of a rectangle """

        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
