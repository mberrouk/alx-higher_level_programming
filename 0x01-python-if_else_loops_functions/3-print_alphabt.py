#!/usr/bin/python3


for alph in range(ord('a'), ord('z') + 1):
    if alph is not ord('q') and alph is not ord('e'):
        print("{:c}".format(alph), end="")
