#!/usr/bin/python3

i = 0

while (i < 9):
    j = i + 1
    while (j <= 9):
        print("{}{}".format(i, j), end=", " if i < 8 else "\n")
        j += 1
    i += 1
