#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    if not tuple_a and not tuple_b:
        sum1, sum2 = 0, 0

    sum1 = tuple_a[0] if tuple_a else 0
    sum2 = tuple_a[1] if len(tuple_a) > 1 else 0
    sum1 += tuple_b[0] if tuple_b else 0
    sum2 += tuple_b[1] if len(tuple_b) > 1 else 0

    total = (sum1, sum2)

    return total
