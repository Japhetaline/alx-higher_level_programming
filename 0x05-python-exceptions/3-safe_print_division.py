#!/usr/bin/python3

def safe_print_division(a, b):
    """
    divides two integers and prints the result
    divide by zero exception
    """

    try:
        count = a / b
    except Exception:
        count = None
    finally:
        print("Inside result: {}".format(count))
        return count
