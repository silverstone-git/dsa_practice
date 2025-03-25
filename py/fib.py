#!/usr/bin/python
from sys import argv


def fib(n, memo={}):
    if n == 2:
        return 1
    if n == 1:
        return 0
    # print("current: ", n)
    if n in memo:
        # print("cache hit: ", memo)
        return memo[n]
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        # print("cache miss")
        print(memo[n], ",", end=" ", sep="")
        return memo[n]


# expected: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
fib(int(argv[1]))
print()
