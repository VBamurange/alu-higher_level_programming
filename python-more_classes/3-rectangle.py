#!/usr/bin/python3
"""string representation"""


class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """initialize new variables width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """"return area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """get area"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """using # in printing"""
        if self.__width == 0 or self.___height == 0:
            return ''
        else:
            rect = ''
            for i in range(self.__height):
                for x in range(self.__width):
                    rect = rect + '#'

                rect += '\n'
            return rect[:-1]
