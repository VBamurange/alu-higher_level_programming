#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as NF:
        glass = NF.read()
        print (glass)
