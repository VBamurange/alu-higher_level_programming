#!/usr/bin/python3
"""integer validator"""


class BaseGeometry:
    """created a class"""

    def area(self):
        """new function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """another function for validating integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
