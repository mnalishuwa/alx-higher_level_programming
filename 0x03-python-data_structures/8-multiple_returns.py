#!/usr/bin/python3


def multiple_returns(sentence):

    size = len(sentence)
    if size == 0:
        return (None, )
    return (size, sentence[0])
