#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for j in range(target + 1):
            for i in range(len(nums)):
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]
        return dp[target]
        
# @lc code=end

