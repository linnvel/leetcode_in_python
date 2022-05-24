#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for j in range(n):
            if j == 0:
                dp[j] = grid[0][j]
            else:
                dp[j] = dp[j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[n - 1]

        
# @lc code=end

