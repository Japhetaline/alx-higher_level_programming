#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Square:
    """ Class Square that has attributes.

    Attributes:
    size (int): The size of the square
    """

    def __init__(self, size):
        """The __init__ method for Square class

        Arguments:
                size: (obj: 'int'): A private instance size
        """
        self.__size = size
