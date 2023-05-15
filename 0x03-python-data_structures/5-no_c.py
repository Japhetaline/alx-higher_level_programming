#!/usr/bin/python3

def no_c(my_string):
    """ removes all character 'c' and 'C' from string"""
    japh_str = ""
    for k in my_string:
        if k not in "cC":
            japh_str += k
            return (japh_str)
