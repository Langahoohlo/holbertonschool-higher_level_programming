#!/usr/bin/python3
"""Module to append string"""


def append_write(filename="", text=""):
    '''Function to append string'''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
