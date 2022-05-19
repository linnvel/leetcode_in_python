#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[j] = number of combinations make up the amount j
        dp = [1] + [0] * amount
        # The order of i and j CANNOT be changed!!!
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = dp[j] + dp[j - coins[i]]
        return dp[amount]

        # This is not correct
        # for j in range(amount + 1):
        #     for i in range(len(coins)):
        #         if j >= coins[i]:
        #             dp[j] = dp[j] + dp[j - coins[i]]
        #     print(dp)
        return dp[amount]
# @lc code=end

