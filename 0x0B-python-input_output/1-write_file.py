#!/usr/bin/python3
"""
@Author: Damassoh Japhet
"""


def write_file(filename="", text=""):
    """
    Function that write a string to a text file
    and return number of characteristics written
    """
    with open(filename, "w", encoding='utf-8') as file:
        file.write(text)
        return len(text)
