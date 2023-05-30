#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints list of anyting
    Returns the amount of integers printed
    """

    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
