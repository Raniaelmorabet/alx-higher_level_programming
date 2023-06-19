#!/usr/bin/python3
"""class of the square"""
from models.rectangle import Rectangle
"""superclass Rectangle"""

class Square(Rectangle):
    """a class square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """intiliaze instance attributes """
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size
    def __str__(self):
        """returns string"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size of this square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """Internal method that updates instance attributes via */**args"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
