#!/usr/bin/python3

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
        self.__height = height
        self.__width = width

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
            return self.__height

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
            return self.__width

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
                self.__width = value

        def area(self):
            """
            Calculate the area of rectanglr

            Returns:
            The area of the rectanglr
            """
            return self.__width * self.__height

        def perimeter(self):
            """
            Calculate the perimeter of the rectangle

            Returns:
            The perimeter of the rectangle
            """
            if self.__width == 0 or self.__height == 0:
                return 0
            return 2 * (self.__width + self.__height)
