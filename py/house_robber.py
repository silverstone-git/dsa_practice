def rob(houses):
    # get the maximum money which can be stolen in houses list
    # @params :
    #    houses[] --> money of each house

    if len(houses) == 0:
        return 0
    if len(houses) == 1:
        return houses[0]

    print(houses)
    return max(houses[0] + rob(houses[2:]), rob(houses[1:]))

def rob_dp(houses, dp: dict | None = None):
    # get the maximum money which can be stolen in houses list
    # @params :
    #    houses[] --> money of each house

    print(houses)
    if dp is None:
        dp = {}

    if len(houses) == 0:
        return 0
    if len(houses) == 1:
        return houses[0]

    strhouses = str(houses)

    if strhouses in dp:
        return dp[strhouses]

    ans = max(houses[0] + rob_dp(houses[2:], dp), rob_dp(houses[1:], dp))
    dp[strhouses] = ans
    return ans
    
if __name__ == "__main__":
    print(rob_dp([1, 2, 3, 1]))
    print(rob_dp([2, 7, 9, 3, 1]))
    # print(rob([1, 2, 3, 1]))
    # print(rob([2, 7, 9, 3, 1]))
