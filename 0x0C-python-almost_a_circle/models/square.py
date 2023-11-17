#!/usr/bin/python3
"""Define class Square inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size property."""
        return self.width

    @size.setter
    def size(self, value):
        """The size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update Square attributes"""
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Representative string of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
