#!/usr/bin/python3

def islower(c):
    if isinstance(c, int):
        traceback.print_exc()
    asci = ord(f"{c}")
    if asci > 96 and asci < 123:
        return True
    else:
        return False
