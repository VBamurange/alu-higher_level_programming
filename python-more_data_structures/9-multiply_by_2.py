#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    x = a_dictionary.copy()
    y = list(x.keys())
    for i in y:
        x[i] *= 2
    return (x)
