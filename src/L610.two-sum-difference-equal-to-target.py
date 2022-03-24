# @lintcode
#
# 610. Two Sum - difference equals to target
#
# https://www.lintcode.com/problem/610/
#

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        # write your code here
        # # Solution 1: two pointer
        # if len(nums) < 2:
        #     return []
        # nums.sort()
        # first, second = 0, 1
        # target = abs(target)
        # while second < len(nums):
        #     if first == second:
        #         second += 1
        #         continue
        #     curDiff = nums[second] - nums[first]
        #     if curDiff == target:
        #         return [nums[first], nums[second]]
        #     elif curDiff < target:
        #         second += 1
        #     else:
        #         first += 1
        # return []

        # Solution2: hash set
        seen = set()
        for num in nums:
            smaller, larger = num - target, num + target
            if smaller in seen:
                return [min(num, smaller), max(num, smaller)]
            if larger in seen:
                return [min(num, larger), max(num, larger)]
            seen.add(num)
        return []