#!/usr/bin/python3
"""we are assigning a private attribute to the class square"""


class Square:
    """this is the square class"""
    def __init__(self, size):
        """this is te assigned private attribute size"""
        self.__size = size
