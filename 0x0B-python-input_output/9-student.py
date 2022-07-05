#!/usr/bin/python3
""" This module writes a class that defines a student """


class Student:
    """ This class defines student instances """

    def __init__(self, first_name, last_name, age):
        """ This method initializes a student instance
        Args:
             first_name (string): student's first name
             last_name (string): student's last name
             age (int): student's age
        Raises:
             None
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ This method returns a dictionary representation
        of a student instance """
        return self.__dict__
