#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    aLength = len(tuple_a)
    bLength = len(tuple_b)
    a0 = 0
    a1 = 0
    b0 = 0
    b1 = 0

    if aLength == bLength and aLength >= 2:
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    if aLength == 1:
        a0 = tuple_a[0]
    if aLength == 2:
        a0 = tuple_a[0]
        a1 = tuple_a[1]
    if bLength == 1:
        b0 = tuple_b[0]
    if bLength == 2:
        b0 = tuple_b[0]
        b1 = tuple_b[1]

    return (a0 + b0, a1 + b1)
