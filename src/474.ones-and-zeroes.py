#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[j][k]: largest size of subset with at most j 0's ans k 1's
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # count1, count0 = [], []
        # for st in strs:
        #     cnt1, cnt0 = 0, 0
        #     for c in st:
        #         if c == "1":
        #             cnt1 += 1
        #         else:
        #             cnt0 += 1
        #     count1.append(cnt1)
        #     count0.append(cnt0)
        
        for i in range(len(strs)):
            cnt1, cnt0 = 0, 0
            for c in strs[i]:
                if c == "1":
                    cnt1 += 1
                else:
                    cnt0 += 1
            for j in range(m, cnt0 - 1, -1):
                for k in range(n, cnt1 - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - cnt0][k - cnt1] + 1)
            print(dp)
        return dp[m][n]
        
# @lc code=end

