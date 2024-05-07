#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit

if last_digit == 0:
    result = "and is 0"
elif last_digit < 5:
    result = "and is less than 6 and not 0"
else:
    result = "and is greater than 5"

print(f'Last digit of {number} is {last_digit} {result}')
