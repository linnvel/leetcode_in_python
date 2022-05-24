#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n
        maxi = int(sqrt(n))
        for i in range(1, maxi + 1):
            for j in range(i * i, n + 1):
                dp[j] = min(dp[j], dp[j - i * i] + 1)
        return dp[n]
        
        # i = 1
        # while(i * i <= n):
        #     for j in range(i * i, n + 1):
        #         dp[j] = min(dp[j], dp[j - i * i] + 1)
        #     i += 1
        # return dp[n]

        
# @lc code=end

