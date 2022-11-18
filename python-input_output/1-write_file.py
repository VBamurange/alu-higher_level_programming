#!/usr/bin/python3
""""write to a file"""


def write_file(filename="", text=""):
    """function to write file"""
    with open(filename, 'w+') as Q:
        return Q.write(text)
