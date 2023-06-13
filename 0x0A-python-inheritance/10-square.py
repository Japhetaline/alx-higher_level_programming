#!/usr/bin/python3
"""
@author: Damassoh Japhet
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square class shape, inherits from Rectangle and
    BaseGeometry
    """
    def __init__(self, size):
        """
        Init function for square

        Attributes:
        size (int): The size of the square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
