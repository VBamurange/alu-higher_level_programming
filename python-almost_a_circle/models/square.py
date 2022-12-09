#!/usr/bin/python3
"""The square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """
    Initialize the new variables
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size function for the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
    set size of the square
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        string representation
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
        the update function for the square
        """
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

        elif len(kwargs) != 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            else:
                self.id

            if "size" in kwargs:
                self.size = kwargs["size"]
            else:
                self.size

            if "x" in kwargs:
                self.x = kwargs["x"]
            else:
                self.x

            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        dictionary representation of the square
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
