#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums) and nums[i] != 0:
            i += 1
        j = i + 1
        # Solution 1 (faster if most are zero)
        # while j < len(nums):
        #     if nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i] # three steps
        #         i += 1
        #     j += 1

        # Solution 2 (faster if most are non-zero)
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j] # one step
                i += 1
            j += 1
        while i < len(nums):
            nums[i] = 0 # one step
            i += 1


        
# @lc code=end

