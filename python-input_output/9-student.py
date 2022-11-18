#!/usr/bin/python3
"""student to JSON"""


class Student:
    """new class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """json class"""

        return self.__dict__
