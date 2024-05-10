#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg = sys.argv
    add = 0

    for i in arg[1:]:
        add += int(i)
    print(add)
