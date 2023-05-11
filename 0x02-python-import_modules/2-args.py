#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

    argstring = "{:d} argument"
    argcount = len(sys.argv) - 1
    if argcount == 0:
        argstring += 's.'
    elif argcount == 1:
        argstring += ':'
    else:
        argstring += 's:'
        print(argstring.format(argcount))

        k = 0
        for argument in sys.argv:
            if k != 0:
                print("{:d}: {:s}".format(k, argument))
                k += 1
