#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Solution 1: DP
        # Time: O(m * n)
        # Space: O(m * n)
        # dp = [[1 for _ in range(n)] for _ in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # return dp[m - 1][n - 1] 

        # memory optimization
        # Time: O(m * n)
        # Space: O(n)
        # dp = [1] * n
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[j] += dp[j - 1]
        # return dp[n - 1]

        # Solution 2: Math
        # Total: (m + n - 2) steps = (m - 1) down + (n - 1) right
        # C(m + n - 2)(m - 1) = (m + n - 2)! / ((m - 1)! * (n - 1)!)
        import math
        if m <= 1 or n <= 1:
            return 1
        return math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))
        
        # Todo: avoid overflow
# @lc code=end

