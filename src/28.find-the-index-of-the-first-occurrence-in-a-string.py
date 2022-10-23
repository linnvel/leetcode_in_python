#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Solution 1: O(mn)
        l, k = 0, 0
        while l <= len(haystack) - len(needle):
            while k < len(needle) and haystack[l + k] == needle[k]:
                if k == len(needle) - 1:
                    return l
                k += 1
            l += 1
            k = 0
        return -1   

        # Solution 2: KMP pattern matching - O(m+n)  
# @lc code=end

