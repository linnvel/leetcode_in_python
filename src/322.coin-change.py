#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[j] = fewest number of coins to make up j
        # The order of i and j CAN be changed!!!
        # Because output is # of coins, either combination or permutation would get the same result.
        dp = [0] + [float('inf')] * amount
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
        
# @lc code=end

