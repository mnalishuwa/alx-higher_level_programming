#!/usr/bin/python3


def best_score(a_dictionary):

    if not a_dictionary:
        return None
    top_key = next(iter(a_dictionary.keys()))
    best_score = a_dictionary[top_key]
    for key in a_dictionary:
        if a_dictionary[key] > best_score:
            top_key = key
    return top_key
