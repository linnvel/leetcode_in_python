#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # # Solution 1: DP (TLE)
        # dp = [False] * len(nums)
        # dp[0] = True
        # for i in range(1, len(nums)):
        #     for k in range(i):
        #         if nums[k] >= i - k and dp[k]:
        #             dp[i] = True
        #             break
        # return dp[len(nums) - 1]
        
        # Solution 2: greedy (Todo)
        maxStep = 0
        for i, num in enumerate(nums):
            if i > maxStep:
                return False
            maxStep = max(maxStep, i + num)
            if maxStep >= len(nums) - 1:
                return True
        return False

# @lc code=end

