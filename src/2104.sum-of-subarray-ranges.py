#
# @lc app=leetcode id=2104 lang=python3
#
# [2104] Sum of Subarray Ranges
#

# @lc code=start
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # def findMaxSum(nums):
        #     n = len(nums)
        #     stack, left, right = [], [1] * n, [1] * n
        #     for i in range(n):
        #         while stack and nums[i] > stack[-1][0]:
        #             left[i] += stack.pop()[1]
        #         stack.append((nums[i], left[i]))
        #     stack = []
        #     for i in range(n - 1, -1, -1):
        #         while stack and nums[i] >= stack[-1][0]:
        #             right[i] += stack.pop()[1]
        #         stack.append((nums[i], right[i]))
        #     return sum( a * l * r for a, l, r in zip(nums, left, right))
        
        # Better implementation
        # calculate while pop to only use one loop 
        def findMaxSum(nums):
            n = len(nums)
            res = 0
            stack = []
            for i in range(n + 1):
                while stack and (i == n or nums[i] > nums[stack[-1]]):
                    right_boundary = i
                    mid = stack.pop()
                    left_boundary = stack[-1] if stack else -1
                    res += nums[mid] * (mid - left_boundary) * (right_boundary - mid)
                stack.append(i)
            return res
        return findMaxSum(nums) + findMaxSum([-a for a in nums])
# @lc code=end

