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

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """"return area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """get area"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

   def __str__(self):
       """represent the string again"""
       if self.__width == 0 or self.__height == 0:
           return ("")

       rect = []
       for i in range(self.__height):
           [rect.append('#') for j in range(self.__width)]
           if i != self.__height - 1:
               rect.append("\n")
      return ("".join(rect))
