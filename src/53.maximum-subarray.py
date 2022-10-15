#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Solution 1: prefix sum
        minPreSum = 0
        maxSum = -float('inf')
        prefixSum = 0
        for num in nums:
            prefixSum += num
            maxSum = max(maxSum, prefixSum - minPreSum)
            minPreSum = min(prefixSum, minPreSum)
        return maxSum

        # # Solution 2: DP
        # # dp[i]: max sum of subarray ended by nums[i]
        # # dp[i] = dp[i - 1] + nums[i] if dp[i - 1] > 0 else nums[i]
        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i - 1] > 0:
        #         nums[i] += nums[i - 1]
        # return max(nums)
        
# @lc code=end

