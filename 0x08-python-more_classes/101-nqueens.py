#!/usr/bin/python3
"""
Module: The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard. Write a program that solves the N queens problem.

    Usage: nqueens N
        - If the user called the program with the wrong number of arguments,
        print Usage: nqueens N, followed by a new line, and exit with the
        status 1
    Where N must be an integer greater or equal to 4:
        - If N is not an integer, print N must be a number, followed by a
        new line, and exit with the status 1
        - If N is smaller than 4, print N must be at least 4, followed by
        a new line, and exit with the status 1
    The program should print every possible solution to the problem:
        - One solution per line
"""


def check(aqueen, n_queen):
    """ check if queens can kill each other """
    for x in range(n_queen):
        if aqueen[x] == aqueen[n_queen]:
            return False
        if abs(aqueen[x] - aqueen[n_queen]) == abs(x - n_queen):
            return False
    return True


def printer(aqueen, n_queen):
    """print"""
    results = []

    for x in range(n_queen):
        results.append([x, aqueen[x]])
    print(results)


def Queen(aqueen, n_queen):
    """ Recursion """
    if n_queen == len(aqueen):
        printer(aqueen, n_queen)
        return
    aqueen[n_queen] = -1
    while(aqueen[n_queen] < len(aqueen) - 1):
        aqueen[n_queen] += 1
        if check(aqueen, n_queen) is True:
            if n_queen < len(aqueen):
                Queen(aqueen, n_queen + 1)


def init_backtracker(n):
    """ initial algorithem"""
    queen = [-1 for x in range(n)]
    Queen(queen, 0)


if __name__ == "__main__":
    """ first step """
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    init_backtracker(n)
