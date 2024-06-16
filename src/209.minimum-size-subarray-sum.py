#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Solution 1: sliding window
        # time: O(n) -> two tranverse
        # space: O(1)
        # l, r = 0, 0
        # ans = float('inf')
        # cur = 0
        # while r < len(nums):
        #     cur += nums[r]
        #     while cur >= target:  # l <= r is not necessary
        #         ans = min(ans, r + 1 - l)
        #         cur -= nums[l]
        #         l += 1
        #     r += 1
        # return ans if ans < float('inf') else 0

        # Solution 2: cumulative sum + binary search
        # time: O(nlogn)
        # space: O(1)
        def search(start, target):
            l, r = start, len(nums) - 1
            while l < r - 1:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid
                else:
                    r = mid
            if nums[l] >= target:
                return l
            elif nums[r] >= target:
                return r
            else:
                return -1
        
        nums.insert(0, 0)
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        ans = float('inf')
        for i in range(len(nums) - 1):
            j = search(i + 1, nums[i] + target)
            if j > 0:
                ans = min(ans, j - i)
        
        return ans if ans < float('inf') else 0

# @lc code=end

