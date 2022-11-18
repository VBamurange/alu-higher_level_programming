#!/usr/bin/python3
"""save object to file"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an object to text file"""
    with open(filename, 'w+') as Q:
        return json.dump(my_obj, Q)
