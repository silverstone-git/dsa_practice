# search for the element in a sorted array of infinite size
# no len() use allowed, ofc

import random

from bs import binary_search


def inf_search(el, arr):

    if el == arr[0]:
        return 0
    if el == arr[1]:
        return 1

    # to find the ballpark rightlimit, ie, a number between el's
    # position and length of array
    def find_ballpark(el, arr, rightlim=2):
        # print(f"ballpark lim {rightlim}")

        try:
            if arr[rightlim] > el:
                # print("ballpark found")
                return rightlim
        except IndexError:
            # we decrease right pointer to get near the valid range index
            # q -> why not decrease exponentially instead of -1 ing ?
            # ans -> you go even before element sometimes and then double that
            #  to continue, you then go into even more invalid
            #  range, which then oscillates back and forth
            #  more-than-recursion-depth times, especially if the element
            #  is near the end of the array

            # print("we gone out of range")
            rightlim = (rightlim - 1) / 2

        return find_ballpark(el, arr, rightlim=int(rightlim * 2))

    rightlim = find_ballpark(el, arr)
    leftlim = int(rightlim / 2)

    # print(f"leftlim is: {leftlim}")
    # print(f"rightlim is: {rightlim}")

    # now element is in the middle of both the pointers

    return binary_search(el, arr, rightlim=rightlim, leftlim=leftlim)


if __name__ == "__main__":
    test1 = sorted(random.sample(range(10**5), 10**3))

    # Expected Output : 998 duh
    print(inf_search(test1[998], test1))
