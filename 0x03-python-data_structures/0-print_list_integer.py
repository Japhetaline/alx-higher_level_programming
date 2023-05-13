#!/usr/bin/pythons
#0-print_list_integer.py

def print_list_integer(my_list=[]):
    """
    printing a lists of integers
    """

    for k in range(len(my_list)):
        print("{:d}".format(my_list[k]))
