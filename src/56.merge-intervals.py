#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # # Solution 1: recursion
        # def helper(intervals):        
        #     if len(intervals) <= 1:
        #         return intervals

        #     if intervals[0][1] >= intervals[1][0]:
        #         return helper([[intervals[0][0], max(intervals[0][1], intervals[1][1])]] + intervals[2:])
        #     else:
        #         return [intervals[0]] + helper(intervals[1:]) 
        
        # intervals.sort(key = lambda x: x[0])
        # return helper(intervals)
    
        # Solution 2: iteration
        merged = []
        intervals.sort(key = lambda x: x[0])
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
# @lc code=end

