#!/usr/bin/python3
for i in range(100):
    if i in range(0, 10):
        print("0{}".format(i), end=", ")
    else:
        print("{}".format(i), end=", ")
