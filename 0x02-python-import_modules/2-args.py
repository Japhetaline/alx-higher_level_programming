#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Print number and list of arguments."""

    argcount = len(sys.argv) - 1
    if argcount == 0:
        print("0 arguments.")
    elif argcount == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argcount))

        for k in range(argcount):
            print("{}: {}".format(k + 1, sys.argv[k + 1]))
