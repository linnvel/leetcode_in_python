#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        # # Solution 1: recursion
        # Time: O(2^n), Space: O(n)
        # if n <= 1:
        #     return n
        # return self.fib(n - 1) + self.fib(n - 2)

        # # Solution 2: DP
        # Time: O(n), Space: O(n)
        # # dp[i]: the ith Fibonacci number
        # # dp[i] = dp[i - 1] + dp[i - 2]
        # # dp[0] = 0, dp[1] = 1
        # # answer: dp[n]
        # if n <= 1:
        #     return n
        # dp = [0] * (n + 1)
        # dp[0] = 0
        # dp[1] = 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]
        
        # Solution 3: DP memory optimization
        # Time: O(n), Space: O(1)
        if n <= 1:
            return n
        dp = [0, 1]
        for i in range(2, n + 1):
            dp[i % 2] = dp[0] + dp[1]
        return dp[n % 2]
# @lc code=end

