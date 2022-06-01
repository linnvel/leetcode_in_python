#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x:x[0])
        dp = [1] * (len(envelopes) + 1)
        for i in range(len(envelopes)):
            for j in range(i + 1, len(envelopes)):
                if envelopes[j][0] > envelopes[i][0] and envelopes[j][1] > envelopes[i][1]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)
        
# @lc code=end

