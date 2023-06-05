#!/usr/bin/python3
"""
Define rectanglr by figure
"""


class Rectangle:
    """
    class rectangle that defines a rectangle figure

    Parameters:
    empty
    """

    def __init__(self, width=0, height=0):
        """
        An Init method for Rectangle

        Parameters:
        width (int, optional): the width of rectangle
        height (int, optional): The height of rectangl
        self.width = width
        self.height = height
        """
        self._height = height
        self._width = width

        @property
        def height(self):
            """
            Property height to retrieve it

            Returns:
            height (int): The height of thr rectangle

            Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
            """
            return self._height

        @height.setter
        def height(self, value):
            """
            Setter height of the rectangle

            Parameters:
            height (int): The height of the rectangle

            Raises:
            TypeError: If height is not an integer
            ValueEror: If height is less than 0
            """
            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.height = value

        @property
        def width(self):
            """
            Property width to retrieve it

            Returns:
            width (int): The width of the rectangle
            """
            return self._width

        @width.setter
        def width(self, value):
            """
            Setter idth of the rectangle

            Parameters:
            width (int): The width of the rectangle

            Raises:
            TypeError: If width is not an integer
            ValueError: if width is less than 0
            """
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self._width = value
