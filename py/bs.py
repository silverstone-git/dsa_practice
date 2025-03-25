import random


def binary_search(el, arr, rightlim=None, leftlim=0):

    if rightlim is None:
        rightlim = len(arr)

    while leftlim < rightlim:
        mpt = int((rightlim + leftlim) / 2)

        if arr[mpt] == el:
            return mpt
        elif el < arr[mpt]:
            # left window
            rightlim = mpt
        else:
            # right window
            leftlim = mpt

        # print(f"bs leftlim is: {leftlim}")
        # print(f"bs rightlim is: {rightlim}")
    return -1


def binary_search_recursive(el, arr, rightlim=None, leftlim=0):
    if rightlim is None:
        rightlim = len(arr)

    if leftlim > rightlim:
        return -1

    mpt = int((rightlim + leftlim) / 2)

    if arr[mpt] == el:
        return mpt
    elif el < arr[mpt]:
        # left window
        return binary_search_recursive(el, arr, rightlim=mpt, leftlim=leftlim)
    else:
        # right window
        return binary_search_recursive(el, arr, rightlim=rightlim, leftlim=mpt)

        # print(f"bs leftlim is: {leftlim}")
        # print(f"bs rightlim is: {rightlim}")


if __name__ == "__main__":
    n = 100
    r = 20
    arr1 = sorted(random.sample(range(n), r))
    print("arr: ", arr1)
    ind = random.randint(0, 20)
    print("finding: ", arr1[ind])
    print("expected: ", ind)
    print(binary_search_recursive(arr1[ind], arr1))
