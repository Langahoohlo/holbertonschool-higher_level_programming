#!/usr/bin/python3

def no_c(my_string):
    string = list(my_string)

    while 'c' in string or 'C' in string:
        if 'c' in string:
            string.remove('c')

        if 'C' in string:
            string.remove('C')

    return ''.join(string)
