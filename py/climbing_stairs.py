def no_of_ways(n, memo = {}):
    # no of ways to climb stairs, we'll count
    ## assuming we can either walk up one or two steps at max (dont try with jeans)
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    ways = no_of_ways(n-1, memo) + no_of_ways(n-2, memo)
    memo[n] = ways
    return ways

if __name__ == "__main__":
    print(no_of_ways(2))
    print(no_of_ways(3))
    print(no_of_ways(5))
