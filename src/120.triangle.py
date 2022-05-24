#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m, n = len(triangle), len(triangle[-1]) 
        # Solution 1: Top-down
        # dp = triangle[0] * n
        # for i in range(1, m):
        #     curArray = triangle[i]
        #     for j in range(len(curArray) - 1, -1, -1):
        #         if j == 0:
        #             dp[j] += curArray[0]
        #         elif j == len(curArray) - 1:
        #             dp[j] = dp[j - 1] + curArray[-1]
        #         else:
        #             dp[j] = min(dp[j - 1], dp[j]) + curArray[j]
        # return min(dp)

        # Solution 2: Bottom-up
        dp = triangle[-1]
        for i in range(m - 2, -1, -1):
            curArray = triangle[i]
            for j in range(len(curArray)):
                dp[j] = min(dp[j], dp[j + 1]) + curArray[j]
        return dp[0]

        
# @lc code=end

