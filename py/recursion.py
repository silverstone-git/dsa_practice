# the idea is to solve some of the problem and call the function with
# the rest of the problem
# recursion ends at base case: a case for which we already know the
# solution


# if it can be solved using recursion, it can be
# solved by loops as well
# recursion is more intuitive but loops are more efficient

# print numbers from n to 1


def printn(n):
    if n < 1:
        return
    print(n, end=" ")
    printn(n - 1)


printn(4)
print()


def factorial(res):
    if res < 1:
        return 1
    return res * factorial(res - 1)


print(factorial(5))


# can find time complexity using -
# -> recurrence relation
# -> total no. of recursive calls * work done in each

# can find space complexity using -
# recurison depth * space occupied in each stack


