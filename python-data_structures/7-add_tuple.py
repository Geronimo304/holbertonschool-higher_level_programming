#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    r1 = tuple_a[0]
    r2 = tuple_a[1]
    r3 = tuple_b[0]
    r4 = tuple_b[1]

    return (r1 + r3, r2 + r4)
