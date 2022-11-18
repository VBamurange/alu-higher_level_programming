#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """function"""
    with open(filename) as Q:
        glass = Q.read()
        print(glass, end="")
