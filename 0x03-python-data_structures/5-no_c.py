#!/usr/bin/python3

def no_c(my_string):

    """
    removes all character 'c' and 'C' from string
    """

    rem_str = [k for k in my_string if k != 'c' and k != 'C']
    return ("".join(rem_str))
