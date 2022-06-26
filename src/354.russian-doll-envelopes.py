#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Solution 1: DP (TLE)
        # envelopes.sort(key = lambda x:x[0])
        # dp = [1] * (len(envelopes) + 1)
        # for i in range(len(envelopes)):
        #     for j in range(i + 1, len(envelopes)):
        #         if envelopes[j][1] > envelopes[i][1]:
        #             dp[j] = max(dp[j], dp[i] + 1)
        # return max(dp)

        # Solution 2: DP + Binary Search
        envelopes.sort(key = lambda x:(x[0], -x[1]))  # to handle envelopes with equal width
        dp = [-float('inf')]
        for i in range(len(envelopes)):
            l, r = 0, len(dp) - 1
            while l < r - 1:
                mid = (l + r) // 2
                if dp[mid] < envelopes[i][1]:
                    l = mid
                else:
                    r = mid
            index = r if dp[r] < envelopes[i][1] else l
            if index < len(dp) - 1:
                dp[index + 1] = envelopes[i][1]
            else:
                dp.append(envelopes[i][1])
        return len(dp) - 1
# @lc code=end

