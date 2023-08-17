#!/usr/bin/python3

def uniq_add(my_list=[]):
    tmp = my_list[:]
    i = 0
    j = 0
    num = 0
    while (i < len(tmp)):
        j = i + 1
        while (j < len(tmp)):
            if tmp[i] < tmp[j]:
                num = tmp[i]
                tmp[i] = tmp[j]
                tmp[j] = num
            j += 1
        i += 1
    num = 0
    i = 0
    while (i < len(tmp)):
        if tmp[i] != tmp[i - 1]:
            num += tmp[i]
        i += 1
    return num
