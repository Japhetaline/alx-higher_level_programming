#!/usr/bin/python3

def print_last_digit(number):
    card = abs(number) % 10
    print("{:d}".format(card), end='')
    return card
