#!/usr/bin/python3
def max_integer(my_list=[]):
    maxn = 0
    if len(my_list) == 0:
        return None
    for i in range(len(my_list)):
        if my_list[i] > maxn:
            maxn = my_list[i]
    return maxn
