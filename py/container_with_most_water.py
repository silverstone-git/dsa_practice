def container_with_most_water(arr: list[int]):
    rightlimit = len(arr) - 1
    leftlimit = 0
    maxvol = float("-inf")
    while leftlimit < rightlimit:
        inter_wall_distance = 1
        lowerwall = min(arr[leftlimit], arr[rightlimit])
        vol = (rightlimit - leftlimit) * inter_wall_distance * lowerwall
        maxvol = max(vol, maxvol)
        if arr[leftlimit] == lowerwall:
            # right wall bigger, search bigger left wall
            leftlimit += 1
        else:
            rightlimit -= 1
        print(
            f"limits: {leftlimit}, {rightlimit}, vol: {vol}, maxvol: {maxvol}"
        )
    return maxvol


if __name__ == "__main__":
    # Expected output: 15
    print(container_with_most_water([3, 4, 6, 8, 0, 3]))

    # Expected output: 49
    print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
