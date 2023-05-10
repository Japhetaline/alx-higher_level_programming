#!/usr/bin/python3
for numb1 in range(0, 9):
    for numb2 in range(numb1 + 1, 10):
        if numb1 == 8:
            print("{:d}{:d}".format(numb1, numb2))
            break
        print("{:d}{:d}".format(numb1, numb2), end=', ')
