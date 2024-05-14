#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    if not tuple_a and not tuple_b:
        sum1, sum2 = 0, 0

    max_length = max(len(tuple_a), len(tuple_b))
    padded_tuple_a = tuple_a + (0,) * (max_length - len(tuple_a))
    padded_tuple_b = tuple_b + (0,) * (max_length - len(tuple_b))

    total = tuple(a + b for a, b in zip(padded_tuple_a, padded_tuple_b))

    return total
