#!/usr/bin/python3
"""full rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle inherited base geometry"""
    def __init__(self, width, height):
        """new attributes"""
        BaseGeometry.integer_validator(self, 'width', self.__width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', self.__height)
        self.__height = height

    def area(self):
        """get area"""
        return (self.__width * self.__height)

    def __str__(self):
        """new function for rectangle definition"""
        return ("[Rectangle]" + str(self.__width) + "/" + str(self.__height))
