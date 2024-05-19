#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i, elements_printed = 0, 0
    for j in my_list:
        elements_printed += 1

    try:
        while i < x:
            print("{}" .format(my_list[i]), end="")
            i += 1
        print()
        return i
    except IndexError:
        print()
        return elements_printed
