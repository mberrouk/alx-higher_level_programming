#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    result = 0
    x = 1
    while (x < len(sys.argv)):
        result += int(sys.argv[x])
        x += 1
    print("{}".format(result))
