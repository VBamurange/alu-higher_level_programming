#!/usr/bin/python3
"""first rectangle"""


from models.base import Base


class Rectangle(Base):
    """new class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width function"""

        return self.__width

    @width.setter
    def width(self, value):
        """set width"""

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

        @property
        def height(self):
            """height function"""

            return self.__height

        @height.setter
        def height(self, value):
            """set height"""

            if type(value) != int:
                raise TypeError("height must be an integer")

            if value <= 0:
                raise ValueError("height must be > 0")

            self.__height = value

        @property
        def x(self):
            """function  for x"""
            return self.__x

        @x.setter
        def x(self, value):
            """set for x"""
            if type(value) !=int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """y for function"""
            return self.__y

        @y.setter
        def y(self, value):
            """set for y"""

            if type(value) != int:
                raise TypeError("y must be an integer")

            if value < 0:
                raise ValueError("y must be >= 0")

            self.__y = value
