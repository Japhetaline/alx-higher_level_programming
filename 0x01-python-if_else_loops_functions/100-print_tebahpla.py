#!/usr/bin/python3

for japh in range(0, 26):
    if japh % 2 == 0:
        print("{:c}".format(122 - japh), end="")
    else:
        print("{:c}".format(90 - japh), end="")
