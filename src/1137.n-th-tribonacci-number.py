#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n <= 2:
            return dp[n]
        for i in range(3, n + 1):
            val = sum(dp)
            dp = [dp[1], dp[2], val]
        return dp[2]

# @lc code=end

