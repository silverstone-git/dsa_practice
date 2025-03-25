from math import comb


def combination(num, base):
    # finds the combination
    return comb(num, base)


def k_diff(arr: list[int], k: int):
    if k < 0:
        return 0

    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # print("freq is: ", freq)

    count = 0
    for unique_num in freq:
        # print("iteration for unique: ", unique_num)
        if k > 0 and unique_num + k in freq:
            # unique - k wala case handle hi nahi kar rahe kyunki
            # agar pehle kabhi aya hoga iska complement to uske iteration me +k
            # wala number same hi ho gaya hoga, therefore, double counting

            # and the multiply sign is just to accommodate for all combinations
            # in duplicate cases like [2, 2, 4, 4, 4] at k = 2 should give 6
            count += freq[unique_num] * freq.get(unique_num + k, 0)
            # print("count updated to: ", count)
        elif k == 0 and freq[unique_num] > 1:
            # we only want same number case to count if they occur more
            # than once (thats when its actually a 'pair') and thus must use
            # combination_2 formula to find the number of pairs that can be
            # (not permutation because the elements are same in k = 0 case)
            # (and thus, order in pair doesnt matter)
            count += combination(freq[unique_num], 2)
            # print("count updated to: ", count)

    return count


if __name__ == "__main__":
    print("expected: ", 1)
    print(k_diff([1, 2, 2, 4], 0))

    print("expected: ", 6)
    print(k_diff([2, 2, 4, 4, 4], 2))

    print("expected: ", 3)
    print(k_diff([5, 3, 3, 4], 1))

    print("expected: ", 6)
    print(k_diff([1, 1, 1, 1], 0))

    print("expected: ", 6)
    print(k_diff([3, 6, 6, 9, 12, 5, 2], 3))
