#!/usr/bin/python3
"""
@author: Damassoh Japhet
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of text
    and the return number of character
    """
    with open(filename, "a", encoding='utf-8') as file:
        file.write(text)
        return len(text)
