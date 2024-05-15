#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        length, first = 0, None

    else:
        length = len(sentence)

        first = sentence[0]
    tup = (length, first)
    return tup
