#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    result = [result*weight for (result, weight) in my_list]
    return sum(result) / sum([weight for (result, weight) in my_list])
