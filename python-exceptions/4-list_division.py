#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    ret = []
    
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            result = a / b

        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            ret.append(result)
    return ret
