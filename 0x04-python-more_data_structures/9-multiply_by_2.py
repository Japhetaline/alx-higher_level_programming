#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    return a new dictionary vlaues multiplied by 2
    """
    return {
            pointer: worth*2 for (pointer, worth) in a_dictionary.items()
            }
