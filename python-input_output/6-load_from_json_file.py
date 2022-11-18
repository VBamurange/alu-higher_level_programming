#!/usr/bin/python3
"""create object from JSON file"""


import json


def load_from_json_file(filename):
    """function taht create objects from json file"""
    with open(filename, 'r') as Q:
        return json.load(Q)
