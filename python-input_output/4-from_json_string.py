#!/usr/bin/python3
"""JSON string to object"""


import json


def from_json_string(my_str):
    """from string to object"""
    return json.loads(my_str)
