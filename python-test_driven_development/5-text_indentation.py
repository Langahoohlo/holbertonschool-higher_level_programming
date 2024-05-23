#!/usr/bin/python3
"""
    Function divides all elements of a matrix

    Example:
       first_name = "Langa"
       last_name = "Hoohlo"

       say_my_name(first_name, last_name)

       Langa Hoohlo
"""


def text_indentation(text):

    """
        Args:
            first_name: first name
            last_name: second name

        Returns:
            A string with the first and last name
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    full_names = 0
    while full_names < len(text) and text[full_names] == ' ':
        full_names += 1

    while full_names < len(text):
        print(text[full_names], end="")
        if text[full_names] == "\n" or text[full_names] in ".?:":
            if text[full_names] in ".?:":
                print("\n")
            full_names += 1
            while full_names < len(text) and text[full_names] == ' ':
                full_names += 1
            continue
        full_names += 1
