def lcs(text1: str, text2: str, i: int = 0, j: int = 0, dp: dict | None = None):
    # recursively calls itself  for matching further indices

    if dp is None:
        dp = {}

    if i >= len(text1) or j >= len(text2):
        return 0
    
    if (i, j) in dp:
        return dp[(i, j)]

    if text1[i] == text2[j]:
        # mark a match by adding 1, and then 'iterating' further
        ans = 1 + lcs(text1, text2, i + 1, j + 1, dp)
    else:
        ans = max(lcs(text1, text2, i + 1, j, dp), lcs(text1, text2, i, j + 1, dp))

    dp[(i, j)] = ans
    return ans

if __name__ == "__main__":
    print(lcs("abc", "def"))
