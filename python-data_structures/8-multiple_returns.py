#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_len = len(sentence)
    if sentence_len == 0:
        new_tuple = (sentence_len, None)
    else:
        new_tuple = (sentence_len, sentence[0])
    return new_tuple
