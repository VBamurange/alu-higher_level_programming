#!/usr/bin/python3
"""square#1"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """new class square"""
    def __init__(self, size):
        """new attribute size"""
        self.__size = size
        super().__init__(self.__size, self.__size)
