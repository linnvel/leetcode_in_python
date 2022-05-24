#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # # Solution 1: DFS (TLE)                   
        # #              start           
        # #            /      \
        # #           1        2       
        # #         ...       ...
        # #       /      \
        # #      1        2
        # #     /  \     / \
        # #    1    2   1   2
        # #   / \   /  /
        # #  1   2 1  1
        # # / 
        # #1
        # global numofways
        # numofways = 0
        # def dfs(remainStep):
        #     global numofways
        #     if remainStep == 0:
        #         numofways += 1
        #         return
        #     for i in range(1, 3):
        #         if remainStep >= i:
        #             dfs(remainStep - i)
        # dfs(n)
        # return numofways
        """
        dfs(5) -> dfs(4) -> dfs(3) -> dfs(2) -> dfs(1) -> dfs(0)
                                            ->dfs(0)
                                -> dfs(1) -> dfs(0) (duplicate)
                         -> dfs(2) ... (duplicate)
               -> dfs(3) ... (duplicate)
        """

        # Solution 2: DP
        # dp[i]: # of solutions when remainStep = i (climb to ith level)
        # state transition: dp[i] = dp[i - 1] + dp[i - 2] (one step or two step)
        # initialize: dp[0] = 1, dp[1] = 1
        # answer: dp[n]
        # dp => Fibonacci number
        # memory optimization: dp[i] => dp[i%2]
        
        # if n <= 1:
        #     return 1
        # dp = [1, 1]
        # for i in range(2, n + 1):
        #     dp[i%2] = dp[0] + dp[1]
        # return dp[n%2]

        # faster implementation
        if n <= 1:
            return 1
        dp = [1, 1]
        for i in range(2, n + 1):
            # dp[i%2] = dp[0] + dp[1]
            sum = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = sum
        return dp[1]
    
    # Follow up: 1, 2, ... or m steps for each climb => how many distinct ways to the top?
    # <=> Combination Sum IV
    # Solution: Unbounded knapsack
    # dp[0] = 1, dp[1...n] = 0
    # dp[j] += dp[j - i] for i in range(1, m + 1) for j in range(n + 1)

# @lc code=end

