#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys
    """
    [print("{}: {}".format(
        dict_key, a_dictionary[dict_key]))for dict_key in sorted(
            a_dictionary)]
