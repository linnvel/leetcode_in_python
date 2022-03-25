#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # Solution 1
        # nums.sort()

        # # Solution 2: counting sort
        # colors = [0, 0, 0]
        # for num in nums:
        #     colors[num] += 1
        # i = 0
        # for color, count in enumerate(colors):
        #     while count > 0:
        #         nums[i] = color
        #         i += 1
        #         count -= 1

        # Solution 3: partition
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1

# @lc code=end

