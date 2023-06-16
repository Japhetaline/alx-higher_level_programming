#!/usr/bin/python3
"""
@author: Damassoh Japhet
"""

from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class Constructor for Rectangle

        Attributes:
        width (int): Private attribute for the width of the Rectangle
        height (int): Private attribute for the height of the Rectangle
        x (int): Private attribute for x value of the Rectangle
        y (int): Private attribute for y value of the Rectangle
        id (int): Private attribute id inherits from Base
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """
            property method for width value

            Return:
            Private value width value
            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            setter method for width

            Attribute:
            value (int): value to check if is int and greater than 0
            """
            if type(value) != int:
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """
            property method for height

            Return:
            private value height value
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            setter method for height

            Attribute:
            value (int): value to check if is int and greater than 0
            """
            if type(value) != int:
                raise TypeError("height must be an integer")
            elif value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """
            property method for x

            Return:
            Private value x value
            """
            return self.__x

        @x.setter
        def x(self, value):
            """
            setter method for x

            Attribute:
            value (int): value to check if is int and greater than 0
            """
            if type(value) != int:
                raise TypeError("x must be an integer")
            elif value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """
            property method for y

            return
            Private value y value
            """
            return self.__y

        @y.setter
        def y(self, value):
            """
            setter method for y

            Attribute:
            value (int): value to check if is int and greater than 0
            """
            if type(value) != int:
                raise TypeError("y must be an integer")
            elif value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
