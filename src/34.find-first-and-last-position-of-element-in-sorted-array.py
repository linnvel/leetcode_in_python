#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            first = left
        elif nums[right] == target:
            first = right
        else:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            last = right
        else:
            last = left
        return [first, last]
        
        
        

        
# @lc code=end

