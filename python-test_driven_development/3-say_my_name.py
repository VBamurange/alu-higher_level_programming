#!/usr/bin/python3
"""say my name"""


def say_my_name(first_name, last_name=""):
    """function for printing a name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last name must be a string")
    print("My name is", first_name, last_name)
