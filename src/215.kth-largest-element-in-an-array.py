#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, start, end, i):
            if start == end:
                return start
            pivot = nums[i]
            nums[i], nums[end] = nums[end], nums[i]
            left, right = start, end - 1
            while left <= right:
                while nums[left] <= pivot and left <= right:
                    left += 1
                while nums[right] >= pivot and left <= right:
                    right -= 1
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
            nums[left], nums[end] = nums[end], nums[left]
            return left
        
        pv = random.randint(0, len(nums) - 1)
        index = partition(nums, 0, len(nums) - 1, pv)
        if index == len(nums) - k:
            return nums[index]
        elif index < len(nums) - k:
            return self.findKthLargest(nums[index + 1:], k)
        else:
            return self.findKthLargest(nums[:index], k + index - len(nums))
             
# @lc code=end

