#!/usr/bin/python3

def search_replace(my_list, search, replace):
    result = my_list[:]
    for i in range(len(result)):
        if result[i] == search:
            result[i] = replace
    return (result)
