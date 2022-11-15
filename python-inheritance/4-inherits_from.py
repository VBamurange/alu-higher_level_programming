#!/usr/bin/python3
"""only sub class of"""


def inherits_from(obj, a_class):
    """same object inherited directly or indirectly"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
