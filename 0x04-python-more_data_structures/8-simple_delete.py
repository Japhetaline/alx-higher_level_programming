#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Delete an element based on the key from dictionary
    """
    if key in a_dictionary:
        a_dictionary.pop(key)
        return (a_dictionary.copy())
