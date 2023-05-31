#!/usr/bin/python3
"""
@author: Japhetaline
"""


class Square:
    """Class Square that has attributes.

    Attributes:
    size (int): The weight of square
    """

    def __init__(self, size=0):
        """This __init__ method for square class

        Arguments:
        size: (:obj: 'int', optional): Private instance size

        Raises:
        TypeError: Exception if size is not an integer
        ValueError: Execption if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size

            def area(self):
                """Calculating area of the square

                Returns:
                The square area
                """
                return self.__size ** 2
