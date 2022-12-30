#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, values in a_dictionary.fromkeys():
        if value == values:
            del a_dictionary[key]
    return a_dictionary
