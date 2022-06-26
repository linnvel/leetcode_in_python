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
        # dp = [1 for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     for j in range(i):  # optimization: binary search
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[j] + 1, dp[i]) 
        #     print(i, dp)
        # return max(dp)

        # Solution 4: DP + Greedy + Binary Search
        # dp[i] = smallest ending number for LIS with length of i
        # dp[j + 1] = nums[i], j = argmax(dp[j] < nums[i])
        dp = [-float('inf')] 
        for num in nums:
            # binary search: find last j so that dp[j] < num
            l, r = 0, len(dp) - 1
            while l < r - 1:
                mid = (l + r) // 2
                if dp[mid] < num:
                    l = mid
                else:
                    r = mid
            index = r if dp[r] < num else l
            if index <= len(dp) - 2:
                dp[index + 1] = num
            else:
                dp.append(num)
        return len(dp) - 1

# @lc code=end

