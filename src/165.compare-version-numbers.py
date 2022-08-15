#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        l1, l2 = len(v1), len(v2)
        i = 0
        while i < min(l1, l2):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1
            i += 1
        while i < l1:
            if int(v1[i]) != 0:
                return 1
            i += 1
        while i < l2:
            if int(v2[i]) != 0:
                return -1
            i += 1
        return 0        
        
# @lc code=end

