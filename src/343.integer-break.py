#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        # Solution 1: DP
        # dp[i]: maximum product of intergers whith sum of i
        # dp[i] = max(i - k, k * dp[i - k]), k = 1, ..., i // 2
        # answer: dp[n]
        # Time: O(n^2), Space: O(n)

        if n == 2:
            return 1
        dp = [1] * (n + 1)
        for i in range(3, n + 1):
            for k in range(1, i // 2 + 1):
                dp[i] = max(dp[i], k * (i - k), k * dp[i - k])
        return dp[n]

        # Solution 2: Greedy
        # todo

# @lc code=end

