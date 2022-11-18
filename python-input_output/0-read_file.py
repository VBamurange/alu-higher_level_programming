#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """function"""
    with open(filename) as NF:
        glass = NF.read()
        print(glass)
