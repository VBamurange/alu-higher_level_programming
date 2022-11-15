#!/usr/bin/python3
"""my list"""


class MyList(list):
    """parent class"""

    def print_sorted(self):
        """sorted in ascending order"""
        return (sorted(self))
