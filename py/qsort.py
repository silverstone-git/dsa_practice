def qsort(arr):
    if len(arr) < 2:
        return arr
    # could also use:  pivot = arr[randint(0, len(arr) - 1)]
    pivot = arr[len(arr) // 2]
    lesser_arr = list(filter(lambda num: num < pivot, arr))
    greater_arr = list(filter(lambda num: num > pivot, arr))
    equal_nums = list(filter(lambda num: num == pivot, arr))
    return qsort(lesser_arr) + equal_nums + qsort(greater_arr)


test1 = [5, 1, 7, 3, 5, 7, 2, 3]
print(test1)
print(qsort(test1))
