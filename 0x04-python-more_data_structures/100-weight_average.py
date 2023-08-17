#!/usr/bin/python3


def weight_average(my_list=[]):

    total = 0
    weights = 0
    if (not my_list) or (len(my_list) == 0):
        return 0
    for score_weight in my_list:
        total += score_weight[0] * score_weight[1]
        weights += score_weight[1]
    return total / weights
