def get_longest_substr_without_repeating(s):
    maxsub = ''
    cur_sub = ''
    right = 0
    left = 0
    has_occured = {}

    while right < len(s):


        if s[right] in has_occured:
            #refresh the current window

            # print(f"{s[right]} has occured: cur sub, left, right and maxsub", cur_sub, left, right, maxsub)
            # left = right
            left = has_occured[s[right]] + 1
            right = left
            has_occured.clear()
            # print("has occured, flushing window: cur sub, left, right and maxsub", cur_sub, left, right, maxsub)
        cur_sub  = s[left:right + 1]
        # print("hasnt occured: cur sub is: ", cur_sub, left, right)
        has_occured[s[right]] = right

        # checkif maxsub
        if len(cur_sub) > len(maxsub):
            maxsub = cur_sub
        right += 1

    # extra check for the last lingering cur_sub
    if len(cur_sub) > 0:
        if len(cur_sub) > len(maxsub):
            maxsub = cur_sub
    return maxsub


if __name__ == "__main__":
    s = "abcabcbb"
    print(get_longest_substr_without_repeating(s))
    s = "bbbbb"
    print(get_longest_substr_without_repeating(s))
    s = "pwwkew"
    print(get_longest_substr_without_repeating(s))
    s = "dvdf"
    print(get_longest_substr_without_repeating(s))

