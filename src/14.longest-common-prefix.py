#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Solution 0: horizontal scanning
        # LCP(strs) = LCP(LCP(LCP(strs[0], strs[1]), strs[2]), ... ) 
        # Time: worst case: all strs are the same
        # O(S): S - # of all characters

        # Solution 1: vertical scanning
        # Time: worst case: O(s) (all strs have equal length)
        #       best case: O(minlen * n)
        # Space: O(1)
        # i = 0
        # while 1:
        #     c = ""
        #     for s in strs:
        #         if i >= len(s):
        #             return s[:i]
        #         cur = list(s)[i]
        #         if not c:
        #             c = cur
        #         elif c != cur:
        #             return s[:i]
        #     i += 1
        # return s[:i]

        # Solution 2: min and max / sort
        # Time: min/max - worst: O(S), best: O(minlen * n)
        # s0 = min(strs)
        # s1 = max(strs)

        for i, c in enumerate(s0):
            if c != s1[i]:
                return s0[:i]
        return s0

# @lc code=end

