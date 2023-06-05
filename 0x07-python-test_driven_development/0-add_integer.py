#!/usr/bin/python3
"""
module that write a function
which adds 2 integer
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
    a (int): The first integer to be added.
    b (int): The second integer to be added.(default: 98)

    Raises:
    TypeError: Raised if the input is not an integer.
    """
    if type(a) is not int:
        if type(a) is float and a == a and abs(a) <= 1.7976931348623158e+308:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
        if type(b) is not int:
            if type(b) is float and b == b and abs(b) <= 1.7976931348623158e+308:
                b = int(b)
            else:
                raise TypeError("b must be an integer")
            return a + b
