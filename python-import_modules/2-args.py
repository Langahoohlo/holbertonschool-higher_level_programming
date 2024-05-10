#!/usr/bin/python3
import sys

arguments = sys.argv
num_of_arg = len(arguments)

if num_of_arg > 1:
    for i in range(1, num_of_arg):
        print("{}: {}" .format(str(i), arguments[i]))

else:
    print("{} arguments." .format(num_of_arg - 1))
