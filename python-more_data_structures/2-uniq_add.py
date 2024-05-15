#!/usr/bin/python3

def uniq_add(my_list=[]):
    add_list = []

    not_duplicates = set()

    for i in my_list:
        if i not in not_duplicates:
            if my_list.count(i) > 1:
                not_duplicates.add(i)
            add_list.append(i)
        
    return sum(add_list)
