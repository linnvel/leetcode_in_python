#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        # left, right = 0, len(nums) - 1
        # while left + 1 < right:
        #     mid = left + (right - left) // 2
        #     if nums[mid - 1] < nums[mid] > nums[mid + 1]:
        #         return mid
        #     elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
        #         left = mid
        #     else:
        #         right = mid
        # return left if nums[left] > nums[right] else right

        # Faster solution
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
# @lc code=end

