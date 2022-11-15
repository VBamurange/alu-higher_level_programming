#!/usr/bin/python3
"""square2"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherited class rectangle"""
    def __init__(self, size):
        """attribute size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """get area"""
        return self.__size ** 2

    def __str__(self):
        """str"""
        return("[Square]" + str(self.__size) + "/" + str(self.__size))
