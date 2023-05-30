#!/usr/bin/python3

def safe_print_integer_err(value):
    """
    Prints an integer followed by new line and Returns True if
    value is correct otherwise fail if value is not correct
    """

    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return False
    else:
        return True
