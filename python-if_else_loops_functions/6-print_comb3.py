#!/usr/bin/python3

for i in range(0, 10):
    for j in range(i + 1, 10):
        if i == j:
            continue
        if i == 8 and j == 9:
            print("{}""{}".format(i, j))
            continue
        print("{}""{}" .format(i,j), end=', ')
