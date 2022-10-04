#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    result = 0
    for x in my_list:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        result = result + x
    return result
