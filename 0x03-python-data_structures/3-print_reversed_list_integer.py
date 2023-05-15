#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    """
    Print reverse of a given list
    """

    if isinstance(my_list, list):
        my_list.reverse()
        for k in my_list:
            print("{:d}".format(k))
