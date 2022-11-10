#!/usr/bin/python3

"""size validation"""


class Square:
    """we are going to initialize the size attribute"""
    def __init__(self, size=0):

        """attribute size is equating to 0"""

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        elif size < 0:

            raise ValueError("size must be >= 0")

        self.__size = size
    def area(self):
        """to return the area of the square"""
        return(self.__size * self.__size)
