#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right - 1:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid - 1]:
                left = mid
            else:
                right = mid
        if arr[left] > arr[right]:
            return left
        else:
            return right
        
# @lc code=end

