#!/usr/bin/python3

def multiple_returns(sentence):

    """
    Returns the length of a string and its first character
    """

    str_len = len(sentence)
    if str_len == 0:
        role = None
    else:
        role = sentence[0]
        return ((str_len, role))
