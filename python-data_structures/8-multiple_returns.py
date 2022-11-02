#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = None
    print("Length: {:d} - First character: {}".format(len(sentence), sentence[0]))
