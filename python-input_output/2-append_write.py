#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """append a string at the end"""
    with open(filename, 'a+') as Q:
        return Q.write(text)
