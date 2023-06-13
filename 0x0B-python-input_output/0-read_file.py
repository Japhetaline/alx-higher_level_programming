#!/usr/bin/python3
"""
Function that read a text file
"""


def read_file(filename=""):
    """
    Read a file and print stdout
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
