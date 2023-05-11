#!/usr/bin/python3
import sys

if __name__ == "__main__":

    output = 0
    for k in range(len(sys.argv) - 1):
        output += int(sys.argv[k + 1])
        print("{:d}".format(output))
