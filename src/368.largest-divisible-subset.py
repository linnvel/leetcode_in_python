#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1] * len(nums)
        prev = [i for i in range(len(nums))]
        maxlen = 1
        maxindex = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    if dp[i] > maxlen:
                        maxlen = dp[i]
                        maxindex = i
        results = [nums[maxindex]]
        print(dp, prev)
        while prev[maxindex] != maxindex:
            maxindex = prev[maxindex]
            results.append(nums[maxindex])
        return results
        
# @lc code=end

