#!/usr/bin/python3
import random
number = random.randint(-1000,1000)
japNum = abs(number) % 10

if number < 0:
    japNum = -(japNum)
    print("Last digit of {} is {} and is".format(number, japNum), end="")
    if japNum > 5:
        print("greather than 5")
    elif japNum == 0:
        print("0")
    else:
        print("less than 6 and not 0")
