#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # dp[i]: maximum money from 0 to i
        # dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        # dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
        # could further optimize memory
        dp0 = nums[0]
        dp1 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp0, dp1 = dp1, max(nums[i] + dp0, dp1)
        return max(dp0, dp1)

        
# @lc code=end

