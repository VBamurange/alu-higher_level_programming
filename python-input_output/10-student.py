#!/usr/bin/python3
"""student to json with filter"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json class"""

        if attrs is None or type(attrs) != list:
            return self.__dict__
        else:
            x = {}
            for y in attrs:
                if type(y) != str:
                    return self.__dict__
                if y in self.__dict__.keys():
                    x[y] = self.__dict__[elem]
            return x
