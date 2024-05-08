#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if isinstance(i, int):
            result += i
        if ord(i) > 96 and ord(i) < 123:
            asci = ord(i) - 32
        else:
            asci = ord(i)

        char = chr(asci)
        result += char
    print(result)
