#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        None

    else:
        length = len(sentence)

        first = sentence[0]

    return length, first

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
