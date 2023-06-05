#!/usr/bin/python3
"""
Module that prints a text with 2 lines after each character
.,? and :.
"""


def text_indentation(text):
    """
    prints str with two new lines after '.', '?' and ':'

    Parameters:
    text(int): text to print

    Raises:
    TypeError: "text must be a string"
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    link = text.replace('.', '.\n\n').replace(
            ':', ':\n\n').replace('?', '?\n\n')
    for k in range(len(text)):
        link = link.replace('\n', '\n')

        print(link, end='')
