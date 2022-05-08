#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        capacity = sum(nums) // 2

        # Solution 1: DP
        # 1. dp[j] = maximum sum of values picked up from nums with capacity of j
        # dp = [0] * (capacity + 1)
        # for i in range(len(nums)):
        #     for j in range(capacity, nums[i] - 1, -1):
        #         dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        # return dp[capacity] == capacity

        # 2. dp[j] = True if can pick up from nums to sum up to value j
        dp = [True] + [False] * capacity
        for i in range(len(nums)):
            for j in range(capacity, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[capacity]

        # Solution 2: DFS with memorization (Todo)

        
# @lc code=end

