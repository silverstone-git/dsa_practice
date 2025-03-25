"""
    problem -
    @param arr -> array of numbers
    @param k -> int size of which subarray is to be searched
    @return the sum of subarray of k size which has maximum sum
"""


def max_sum_subarray(arr, k):
    uplim = k
    current_sum = sum(arr[uplim - k : uplim])
    maxsum = current_sum

    while uplim < len(arr) - 1:
        # running sum instead of entire sum in each iteration
        uplim += 1
        current_sum += arr[uplim] - arr[uplim - k - 1]
        maxsum = max(current_sum, maxsum)
    return maxsum


if __name__ == "__main__":
    print("expected: ", 9)
    print(max_sum_subarray([1, 2, 3, 4, 5], 2))
