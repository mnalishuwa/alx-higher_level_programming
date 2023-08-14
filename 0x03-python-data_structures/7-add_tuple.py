#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    size_a = len(tuple_a)
    size_b = len(tuple_b)
    if size_a == 0:
        ta = (0, 0)
    if size_b == 0:
        tb = (0, 0)
    if size_a == 1:
        ta = (tuple_a[0], 0)
    if size_b == 1:
        tb = (tuple_b[0], 0)
    if size_a >= 2 and size_b >= 2:
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    if size_a >= 2 and size_b < 2:
        return (tuple_a[0] + tb[0], tuple_a[1] + tb[1])
    if size_a < 2 and size_b >= 2:
        return (ta[0] + tuple_b[0], ta[1] + tuple_b[1])
    if size_a < 2 and size_b < 2:
        return (ta[0] + tb[0], ta[1] + tb[1])
