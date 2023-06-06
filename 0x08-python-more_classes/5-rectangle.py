#!/usr/bin/python3

class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """init for Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Rectangle width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Rectangle height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Rectangle height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns a string representation of the rectangle"""
        rectangle_str = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle_str
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str[:-1]
    def __repr__(self):
        """returns an object representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
    def __del__(self):
        """kill the rectangle"""
        print("Bye rectangle...")