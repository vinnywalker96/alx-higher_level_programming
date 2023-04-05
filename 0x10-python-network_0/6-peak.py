#!/bin/bash/python3
def find_peak(list_of_integers):
    """
    Finds a peak in a unsorted list of integers
    
    Args:
        list_of_integers (list[int])
    """
    if len(list_of_integers) == 0:
        return None

    low, high = 0, len(list_of_integers) - 1
    while low < high:
        peak = (low + high) // 2

        if list_of_integers[peak] > list_of_integers[peak + 1]:
            high = peak
        else:
            low = peak + 1
    return list_of_integers[low]
