#!/usr/bin/python3

def uppercase(str):
    for c in str:
        japh = ord(c)
        if japh >= 97 and japh <=122:
            japh -= 32
            print("{:c}".format(japh), end='')
            print()
