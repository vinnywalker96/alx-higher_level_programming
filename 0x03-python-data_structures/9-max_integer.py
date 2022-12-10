#!/usr/bin/python3
def max_integer(my_list=[]):
    sum = 0
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            sum += i
        return sum
