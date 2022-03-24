#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Solution 1: hash set
        # hashset = {}
        # for i, num in enumerate(nums):
        #     if target - num in hashset:
        #         return [hashset[target - num], i]
        #     else:
        #         hashset[num] = i
        # return []

        # Solution 2: sort + two pointers
        nums = [[num, i] for i, num in enumerate(nums)]
        nums.sort(key = lambda x: x[0])
        l, r = 0, len(nums) - 1
        while l < r:
            curSum = nums[l][0] + nums[r][0]
            if curSum == target:
                return [nums[l][1], nums[r][1]]
            elif curSum < target:
                l += 1
            else:
                r -= 1
        return []

        
# @lc code=end

