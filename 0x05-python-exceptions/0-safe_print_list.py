#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            n += 1
            print("{}".format(my_list[i]), end="")
        except:
            break
    print("")
    return (n)
