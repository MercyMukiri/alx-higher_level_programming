#!/usr/bin/python3
""" This module writes a class that defines a Student """


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

    def to_json(self, attrs=None):
        """ This method etrieves a dictionary representation
            of a Student instance:
            If attrs is a list of strings,
            only attribute names contained in this list must be retrieved
            Otherwise, all attributes must be retrieved
        """

        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__

        except Exception:
            return self.__dict__

        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value

        return my_dict

    def reload_from_json(self, json):
        """ This method replaces all attributes of the Student instance """

        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
