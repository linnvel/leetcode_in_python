#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # # Solution 1: recursion
        # if not p:
        #     return not s
        # firstmatch = s and (p[0] in [s[0], "."])
        # if len(p) >= 2 and p[1] == "*":
        #     return self.isMatch(s, p[2:]) or (firstmatch and self.isMatch(s[1:], p))
        # else:
        #     return firstmatch and self.isMatch(s[1:], p[1:])
        
        # Solution 2: DP
        memo = {}
        s = list(s)
        p = list(p)
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j >= len(p):
                return (i >= len(s))
            firstmatch = i < len(s) and p[j] in [s[i], "."]
            if j + 1 < len(p) and p[j + 1] == "*":
                memo[(i, j)] = helper(i, j + 2) or (firstmatch and helper(i + 1, j))
            else:
                memo[(i, j)] = firstmatch and helper(i + 1, j + 1)
            return memo[(i, j)]
        return helper(0, 0)
# @lc code=end

