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
            y = {}
            for w in attrs:
                if type(w) != str:
                    return self.__dict__
                if w in self.__dict__.keys():
                    y[w] = self.__dict__[w]
                return y
