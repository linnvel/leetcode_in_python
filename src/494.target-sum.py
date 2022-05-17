#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Return # of subsets sum up to targetSum
        # targetSum = (sum(nums) + target) // 2
        
        if (sum(nums) + target) % 2 != 0:
            return 0
        targetSum = (sum(nums) + target) // 2
        # # Solution 0: DFS
        # def dfs(nums, index, remainSum):
        #     if remainSum < 0:
        #         return 0
        #     if index == len(nums):
        #         return 1 if remainSum == 0 else 0
        #     return dfs(nums, index + 1, remainSum - nums[index]) + dfs(nums, index + 1, remainSum)

        # # return dfs(nums, 0, targetSum)  

        # # Solution 1: DFS + memorization
        # # key: index & remainSum, value: # of expression
        # global cache
        # cache = [{} for _ in range(len(nums))]
        # def dfs(nums, index, remainSum):
        #     if remainSum < 0:
        #         return 0
        #     if index == len(nums):
        #         return 1 if remainSum == 0 else 0
        #     if remainSum not in cache[index]:
        #         cache[index][remainSum] = dfs(nums, index + 1, remainSum - nums[index]) + dfs(nums, index + 1, remainSum)
        #     return cache[index][remainSum]
        
        # return dfs(nums, 0, targetSum)  

        # Solution 2: DP 0-1 knapsack
        # dp[j] = # of expressions with positive nums sum up to j

        if targetSum < 0:
            return 0
        dp = [1] + [0 for _ in range(targetSum)]
        for i in range(len(nums)):
            for j in range(targetSum, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[targetSum]

        
# @lc code=end

