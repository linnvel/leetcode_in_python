#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from sys import prefix


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Solution 1: Brute force (TLE)
        # count = 0
        # for i in range(len(nums)):
        #     prefix = 0
        #     for j in range(i, len(nums)):
        #         prefix += nums[j]
        #         if prefix == k:
        #             count += 1
        # return count

        # Solution 2: prefixsum + dict (two sum/diff)
        # how many paris (a, b) in prefixsum so that a - b = k
        # dict[prefixsum] = count
        prefixSum = 0
        preDict = {0:1}
        count = 0
        for num in nums:
            prefixSum += num
            if prefixSum - k in preDict:
                count += preDict[prefixSum - k]
            if prefixSum in preDict:
                preDict[prefixSum] += 1
            else:
                preDict[prefixSum] = 1
        return count

        
# @lc code=end

