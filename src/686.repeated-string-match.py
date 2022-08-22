#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#

# @lc code=start
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # # Solution 1: Two pointers (TLE)
        # m, n = len(a), len(b)
        # repeat = 1
        # i, j = 0, 0
        # find = 0
        # start = 0
        # while j < n:
        #     if i >= m:
        #         repeat += 1
        #         i = i % m
        #     if repeat > 1 and j == 0:
        #         return -1
        #     if a[i] == b[j]:
        #         j += 1
        #         if find == 0:
        #             start = i
        #             find = 1
        #     else:
        #         if find == 1:
        #             j = 0
        #             if start + 1 > i:
        #                 repeat -= 1
        #             i = start + 1
        #             find = 0
        #             continue
        #     i += 1
        # return repeat

        # Solution 2: 
        times = -(-len(b) // len(a))
        if b in a * times:
            return times
        elif b in a * (times + 1):
            return times + 1
        else:
            return -1
        
# @lc code=end

