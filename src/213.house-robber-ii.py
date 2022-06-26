#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)    

        # def rob1(nums):
        #     dp0, dp1 = nums[0], max(nums[:2])
        #     for i in range(2, len(nums)):
        #         dp0, dp1 = dp1, max(dp0 + nums[i], dp1)
        #     return max(dp0, dp1)

        # return max(rob1(nums[:-1]), rob1(nums[1:]))


        # Space optimization:
        # Slicing a list is actually O(n) space in Python. In our case, nums[1:], nums[:-1] create copies, 
        # to avoid this, we can pass indices into the rob1 function instead of sliced lists.
        def rob1(nums, start, end):
            dp0, dp1 = nums[start], max(nums[start : start + 2])
            for i in range(start + 2, end):
                dp0, dp1 = dp1, max(dp0 + nums[i], dp1)
            return max(dp0, dp1)

        return max(rob1(nums, 0, len(nums) - 1), rob1(nums, 1, len(nums)))
# @lc code=end

