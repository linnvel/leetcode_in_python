#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        # while i < len(nums) and nums[i] != val:
        #     i += 1
        # j = i + 1
        # while j < len(nums):
        #     if nums[j] != val:
        #         nums[i] = nums[j]
        #         i += 1
        #     j += 1
        # return i

        # faster implementation
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i
        
# @lc code=end

