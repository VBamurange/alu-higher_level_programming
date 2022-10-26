#!/usr/bin/python3
def uppercase(str):
    for y in str:
        if 123 > ord(y) > 96:
            y = chr(ord(y) - 32)
            print('{}'.format(y), end="")
            print('')
