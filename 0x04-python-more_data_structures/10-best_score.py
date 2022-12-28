#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    highest_score = ""
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        for i in my_list:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                highest_score = i
    else:
        highest_score = None
    return highest_score
