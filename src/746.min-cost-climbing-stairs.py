#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # if n <= 1:
        #     return 0
        # cost = [0] + cost + [0]
        # dp = cost[:2]
        # for i in range(2, n + 2):
        #     val = min(dp) + cost[i]
        #     dp[0] = dp[1]
        #     dp[1] = val
        # return dp[1]

        # cleaner code
        dp = cost[:2]
        n = len(cost)
        for i in range(2, n):
            val = min(dp) + cost[i]
            dp = dp[1], val
        return min(dp)
        
# @lc code=end

