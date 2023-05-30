#!/usr/bin/python3

def safe_function(fct, *args):
    """
    executes a function safely and return the result of the
    function
    """
    try:
        outcome = fct(*args)
        return outcome
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return None
