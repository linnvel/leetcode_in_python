#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minPreSum = 0
        maxSum = -float('inf')
        prefixSum = 0
        for num in nums:
            prefixSum += num
            maxSum = max(maxSum, prefixSum - minPreSum)
            minPreSum = min(prefixSum, minPreSum)
        return maxSum
        
# @lc code=end

