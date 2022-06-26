#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # # dfs
        # def dfs(s1, s2, s3):
        #     if not s1 and not s2 and not s3:
        #         return True
        #     elif (not s1 and not s2) or not s3:
        #         return False
        #     if s1 and s1[0] == s3[0] and (not s2 or s2[0] != s3[0]):
        #         return dfs(s1[1:], s2, s3[1:])
        #     elif (not s1 or s1[0] != s3[0]) and s2 and s2[0] == s3[0]:
        #         return dfs(s1, s2[1:], s3[1:])
        #     elif s1 and s2 and s1[0] == s3[0] and s2[0] == s3[0]:
        #         return dfs(s1[1:], s2, s3[1:]) or dfs(s1, s2[1:], s3[1:])
        #     else:
        #         return False

        # return dfs(list(s1), list(s2), list(s3))
        
        # # dfs with memorization
        # global memo
        # memo = {}
        # def dfs(s1, s2, s3, i1, i2, i3):
        #     global memo
        #     if i1 == len(s1) and i2 == len(s2) and i3 == len(s3):
        #         return True
        #     elif i1 == len(s1) and i2 == len(s2) or i3 == len(s3):
        #         return False
        #     if (i1, i2, i3) not in memo:
        #         if i1 < len(s1) and s1[i1] == s3[i3] and (i2 == len(s2) or s2[i2] != s3[i3]):
        #             memo[(i1, i2, i3)] = dfs(s1, s2, s3, i1 + 1, i2, i3 + 1)
        #         elif (i1 == len(s1) or s1[i1] != s3[i3]) and i2 < len(s2) and s2[i2] == s3[i3]:
        #             memo[(i1, i2, i3)] = dfs(s1, s2, s3, i1, i2 + 1, i3 + 1)
        #         elif i1 < len(s1) and i2 < len(s2) and s1[i1] == s2[i2] == s3[i3]:
        #             memo[(i1, i2, i3)] = dfs(s1, s2, s3, i1 + 1, i2, i3 + 1) or dfs(s1, s2, s3, i1, i2 + 1, i3 + 1)
        #         else: 
        #             memo[(i1, i2, i3)] = False
        #     return memo[(i1, i2, i3)]
        # return dfs(s1, s2, s3, 0, 0, 0)

        # DP

# @lc code=end

