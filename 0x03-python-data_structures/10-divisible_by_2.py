#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for multiple in my_list:
        if multiple % 2 == 0:
            res.append(True)
        else:
            res.append(False)
    return res
