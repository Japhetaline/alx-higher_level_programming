#!/usr/bin/python3
"""
Module that write function which prints
My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints a full name.

    Parameters:
    first_name (str): The first part of the name to print.
    last_name (str): The second part of thr name to print.

    Raises:
    TypeError: if either parameter is not a string.

    The function concatenates the first_name and last_name parameters
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(Fist_name, last_name))
