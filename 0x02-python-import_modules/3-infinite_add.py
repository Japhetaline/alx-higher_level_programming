#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

    k = 0
    output = 0
    for argument in sys.argv:
        if k != 0:
            output += int(argument)
        else:
            k += 1
            print("{:d}".format(output))
