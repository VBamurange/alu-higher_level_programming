#!/usr/bin/python3
"""my list"""


class list:
    """parent class"""

    def print_sorted(self):
        """sorted in ascending order"""
        return (sorted(self))
class MyList(list):
    """child class"""
    pass
