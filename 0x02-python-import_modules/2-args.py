#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    ac = len(sys.argv) - 1
    if ac == 0:
        print("0 arguments.")
    elif ac == 1:
        print("1 argument:")
    else:
        print("{} argumets:".format(ac))
    x = 1
    while (x < ac + 1):
        print("{}: {}".format(x, sys.argv[x]))
        x += 1
