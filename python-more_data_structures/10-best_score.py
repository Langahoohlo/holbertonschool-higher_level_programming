#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    items = {k: v for k, v in a_dictionary.items() if v is not None}
    if not items:
        return None
    best = max(items, key=items.get)
    return best
