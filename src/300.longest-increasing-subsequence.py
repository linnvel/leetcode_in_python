#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # # Solution 1: DFS (TLE)
        # def dfs(nums, lastValue, curLen, curIndex):
        #     if curIndex == len(nums):
        #         return curLen
        #     nextLen = curLen + 1 if nums[curIndex] > lastValue else 1
        #     len1 = dfs(nums, nums[curIndex], nextLen, curIndex + 1)
        #     len2 = dfs(nums, lastValue, curLen, curIndex + 1)
        #     return max(len1, len2)
        
        # return dfs(nums, -float('inf'), 0, 0)
        
        # # Solution 2: DFS with memorization
        # def dfs(nums, lastValue, curLen, curIndex):
        #     if index == len(nums):
        #         return curLen
        #     if (lastValue, index) not in memo:
        #         nextLen = curLen + 1 if nums[index] > curLast else 1
        #         len1 = dfs(nums, nums[index], nextLen, index + 1)
        #         len2 = dfs(nums, curLast, curLen, index + 1)
        #         memo[(lastValue, index)] = max(len1, len2)
        #     return memo[(lastValue, index)]
        
        # global memo
        # memo = {}  # key: startIndex, curIndex; value: ???
        # return dfs(nums, -float('inf'), 0, 0)

        # Solution 3: DP
        # dp[i][j] = max length of increasing subsequence when lastIndex = i, curIndex = j
        # dp[j] = max length of increasing subsequence of nums[0:j+1]
        # dp = [1 for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] > nums[i]:
        #             dp[j] = max(dp[j], dp[i] + 1)
        # return max(dp)

        # Another idea of DP
        # dp[i] = max LIS ended by nums[i]
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):  # optimization: binary search
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i]) 
            print(dp)
        return max(dp)

# @lc code=end

