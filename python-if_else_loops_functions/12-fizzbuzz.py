#!/usr/bin/python3

def fizzbuzz():
    num = range(0, 101)
    for i in num:
        if i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        elif i % 3 == 0 and i % 5 == 0:
            print(f"{i}", end=' ')
        else:
            print(f"{i}", end=' ')
