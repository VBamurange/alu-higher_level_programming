#!/usr/bin/python3


"""size validation"""
class Square:
    """we are going to initialize the size attribute"""

    def __init__(self, size=0):
        """attribute size is equating to 0"""
        self.size = size

    @property
    def size(self):
        """get size of the square"""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """to return the area of the square"""
        return(self.__size * self.__size)
