#!/usr/bin/python3
import random
number = random.randint(-1000,1000)
japNum = number

if number < 0:
    number = -(number)

    lastDigit = number % 10
    if japNum < 0:
        number = japNum
        lastDigit = -(lastDigit)

        if lastDigit > 5:
            thread = "and is greather than 5"
        elif lastDigit == 0:
            thread = "and is 0"
        elif lastDigit < 6:
            thread = "and is less than 6 and not 0"

            print("Last digit of {:d} is {:d}".format(number, lastDigit), thread)
